package com.mananc.road_helper.service;

import com.mananc.road_helper.dto.EmergencyRequest;
import com.mananc.road_helper.dto.EmergencyResponse;
import com.mananc.road_helper.dto.IncidentRequest;
import com.mananc.road_helper.dto.IncidentResponse;
import com.mananc.road_helper.dto.StatusUpdateRequest;
import com.mananc.road_helper.entity.Incident;
import com.mananc.road_helper.entity.IncidentStatus;
import com.mananc.road_helper.entity.IncidentType;
import com.mananc.road_helper.entity.Role;
import com.mananc.road_helper.entity.User;
import com.mananc.road_helper.repository.IncidentRepository;
import com.mananc.road_helper.repository.UserRepository;
import com.mananc.road_helper.security.JwtTokenProvider;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Collections;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class IncidentServiceTest {

    @Mock
    private IncidentRepository incidentRepository;

    @Mock
    private UserRepository userRepository;

    @Mock
    private NotificationService notificationService;

    @Mock
    private JwtTokenProvider jwtTokenProvider;

    @InjectMocks
    private IncidentService incidentService;

    private User customer;
    private User technician;

    @BeforeEach
    void setUp() {
        customer = new User(1L, "Test Customer", "customer@example.com", "pass", Role.CUSTOMER, true, null);
        technician = new User(2L, "Tech Mike", "mike@example.com", "pass", Role.TECHNICIAN, true, null);
    }

    @Test
    @DisplayName("Create Incident with auto-assignment when technician is available")
    void testCreateIncidentWithAutoAssignment() {
        IncidentRequest req = new IncidentRequest("FLAT_TIRE", "Flat tire on highway", "Mile marker 42");

        Incident savedIncident = new Incident();
        savedIncident.setId(100L);
        savedIncident.setType(IncidentType.FLAT_TIRE);
        savedIncident.setDescription("Flat tire on highway");
        savedIncident.setLocation("Mile marker 42");
        savedIncident.setStatus(IncidentStatus.REQUESTED);
        savedIncident.setCustomer(customer);

        when(incidentRepository.save(any(Incident.class))).thenReturn(savedIncident);
        when(userRepository.findByRoleAndIsAvailableTrue(Role.TECHNICIAN)).thenReturn(List.of(technician));

        IncidentResponse response = incidentService.createIncident(req, customer);

        assertNotNull(response);
        assertEquals("FLAT_TIRE", response.type());
        assertEquals("Mile marker 42", response.location());
        assertEquals(IncidentStatus.AUTO_ASSIGNED.name(), savedIncident.getStatus().name());
        assertFalse(technician.getIsAvailable());

        verify(notificationService).notifyEmergencyServices(savedIncident);
        verify(userRepository).save(technician);
    }

    @Test
    @DisplayName("Create Emergency Incident generates guest token and initiates auto-assignment")
    void testCreateEmergencyIncident() {
        EmergencyRequest req = new EmergencyRequest("Guest Jane", "9876543210", "Highway 66", "ACCIDENT", "Car collided with barrier");

        Incident savedIncident = new Incident();
        savedIncident.setId(200L);
        savedIncident.setType(IncidentType.ACCIDENT);
        savedIncident.setDescription("Car collided with barrier");
        savedIncident.setLocation("Highway 66");
        savedIncident.setGuestName("Guest Jane");
        savedIncident.setGuestPhone("9876543210");
        savedIncident.setStatus(IncidentStatus.REQUESTED);

        when(incidentRepository.save(any(Incident.class))).thenReturn(savedIncident);
        when(jwtTokenProvider.generateGuestToken(200L)).thenReturn("mock-guest-token-xyz");
        when(userRepository.findByRoleAndIsAvailableTrue(Role.TECHNICIAN)).thenReturn(List.of(technician));

        EmergencyResponse resp = incidentService.createEmergencyIncident(req);

        assertNotNull(resp);
        assertEquals(200L, resp.incidentId());
        assertEquals("mock-guest-token-xyz", resp.guestToken());
        assertEquals("mock-guest-token-xyz", savedIncident.getGuestToken());
        verify(notificationService).notifyEmergencyServices(savedIncident);
    }

    @Test
    @DisplayName("Update status to RESOLVED marks technician as available again")
    void testUpdateStatusToResolvedFreesTechnician() {
        Incident incident = new Incident();
        incident.setId(300L);
        incident.setType(IncidentType.LOCKOUT);
        incident.setStatus(IncidentStatus.IN_PROGRESS);
        incident.setAssignedTechnician(technician);
        technician.setIsAvailable(false);

        when(incidentRepository.findById(300L)).thenReturn(Optional.of(incident));
        when(incidentRepository.save(any(Incident.class))).thenReturn(incident);

        StatusUpdateRequest updateReq = new StatusUpdateRequest("RESOLVED");
        IncidentResponse resp = incidentService.updateStatus(300L, updateReq, technician);

        assertNotNull(resp);
        assertEquals("RESOLVED", resp.status());
        assertNotNull(incident.getResolvedAt());
        assertTrue(technician.getIsAvailable());
        verify(userRepository).save(technician);
    }
}
