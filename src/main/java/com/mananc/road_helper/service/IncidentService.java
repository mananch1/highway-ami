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
import com.mananc.road_helper.exception.InvalidStatusTransitionException;
import com.mananc.road_helper.exception.ResourceNotFoundException;
import com.mananc.road_helper.repository.IncidentRepository;
import com.mananc.road_helper.repository.UserRepository;
import com.mananc.road_helper.security.JwtTokenProvider;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class IncidentService {

    private final IncidentRepository incidentRepository;
    private final UserRepository userRepository;
    private final NotificationService notificationService;
    private final JwtTokenProvider jwtTokenProvider;

    public IncidentService(IncidentRepository incidentRepository, UserRepository userRepository, NotificationService notificationService, JwtTokenProvider jwtTokenProvider) {
        this.incidentRepository = incidentRepository;
        this.userRepository = userRepository;
        this.notificationService = notificationService;
        this.jwtTokenProvider = jwtTokenProvider;
    }

    @Transactional
    public IncidentResponse createIncident(IncidentRequest request, User customer) {
        Incident incident = new Incident();
        incident.setType(IncidentType.valueOf(request.type()));
        incident.setDescription(request.description());
        incident.setLocation(request.location());
        incident.setCustomer(customer);
        incident.setStatus(IncidentStatus.REQUESTED);
        
        Incident saved = incidentRepository.save(incident);
        autoAssignTechnician(saved);
        notificationService.notifyEmergencyServices(saved);
        return toIncidentResponse(saved);
    }

    @Transactional
    public EmergencyResponse createEmergencyIncident(EmergencyRequest request) {
        Incident incident = new Incident();
        incident.setType(IncidentType.valueOf(request.type()));
        incident.setDescription(request.description());
        incident.setLocation(request.location());
        incident.setGuestName(request.name());
        incident.setGuestPhone(request.phone());
        incident.setStatus(IncidentStatus.REQUESTED);

        Incident saved = incidentRepository.save(incident);
        String token = jwtTokenProvider.generateGuestToken(saved.getId());
        saved.setGuestToken(token);
        
        autoAssignTechnician(saved);
        notificationService.notifyEmergencyServices(saved);
        
        return new EmergencyResponse(saved.getId(), token, saved.getStatus().name(), "Emergency incident created");
    }

    private void autoAssignTechnician(Incident incident) {
        List<User> availableTechs = userRepository.findByRoleAndIsAvailableTrue(Role.TECHNICIAN);
        if (!availableTechs.isEmpty()) {
            User tech = availableTechs.get(0);
            incident.setAssignedTechnician(tech);
            incident.setStatus(IncidentStatus.AUTO_ASSIGNED);
            tech.setIsAvailable(false);
            userRepository.save(tech);
            incidentRepository.save(incident);
        }
    }

    public IncidentResponse getIncidentById(Long id) {
        return incidentRepository.findById(id).map(this::toIncidentResponse)
                .orElseThrow(() -> new ResourceNotFoundException("Incident not found"));
    }

    public IncidentResponse getIncidentByGuestToken(String token) {
        return incidentRepository.findByGuestToken(token).map(this::toIncidentResponse)
                .orElseThrow(() -> new ResourceNotFoundException("Incident not found for token"));
    }

    public List<IncidentResponse> getIncidentsByCustomer(Long customerId) {
        return incidentRepository.findByCustomerIdOrderByCreatedAtDesc(customerId).stream().map(this::toIncidentResponse).collect(Collectors.toList());
    }

    public List<IncidentResponse> getIncidentsByTechnician(Long techId) {
        return incidentRepository.findByAssignedTechnicianIdOrderByCreatedAtDesc(techId).stream().map(this::toIncidentResponse).collect(Collectors.toList());
    }

    public List<IncidentResponse> getAllIncidents() {
        return incidentRepository.findAll().stream().map(this::toIncidentResponse).collect(Collectors.toList());
    }

    public List<IncidentResponse> searchIncidents(String query) {
        return incidentRepository.findByDescriptionContainingIgnoreCaseOrLocationContainingIgnoreCase(query, query).stream().map(this::toIncidentResponse).collect(Collectors.toList());
    }

    @Transactional
    public IncidentResponse updateStatus(Long id, StatusUpdateRequest request, User currentUser) {
        Incident incident = incidentRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Incident not found"));
        
        IncidentStatus newStatus = IncidentStatus.valueOf(request.status());
        
        // Basic validation could go here
        
        incident.setStatus(newStatus);
        
        if (newStatus == IncidentStatus.RESOLVED || newStatus == IncidentStatus.CLOSED || newStatus == IncidentStatus.CANCELLED) {
            incident.setResolvedAt(LocalDateTime.now());
            if (incident.getAssignedTechnician() != null) {
                User tech = incident.getAssignedTechnician();
                tech.setIsAvailable(true);
                userRepository.save(tech);
            }
        }
        
        return toIncidentResponse(incidentRepository.save(incident));
    }

    private IncidentResponse toIncidentResponse(Incident incident) {
        return new IncidentResponse(
                incident.getId(),
                incident.getType().name(),
                incident.getDescription(),
                incident.getStatus().name(),
                incident.getLocation(),
                incident.getCustomer() != null ? incident.getCustomer().getName() : null,
                incident.getAssignedTechnician() != null ? incident.getAssignedTechnician().getName() : null,
                incident.getGuestName(),
                incident.getGuestPhone(),
                incident.getCreatedAt(),
                incident.getUpdatedAt(),
                incident.getResolvedAt()
        );
    }
}
