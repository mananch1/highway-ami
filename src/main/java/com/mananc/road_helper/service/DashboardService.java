package com.mananc.road_helper.service;

import com.mananc.road_helper.dto.DashboardSummary;
import com.mananc.road_helper.entity.IncidentStatus;
import com.mananc.road_helper.entity.IncidentType;
import com.mananc.road_helper.entity.Role;
import com.mananc.road_helper.repository.IncidentRepository;
import com.mananc.road_helper.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import com.mananc.road_helper.entity.Incident;

@Service
public class DashboardService {

    private final IncidentRepository incidentRepository;
    private final UserRepository userRepository;
    private final IncidentService incidentService;

    public DashboardService(IncidentRepository incidentRepository, UserRepository userRepository, IncidentService incidentService) {
        this.incidentRepository = incidentRepository;
        this.userRepository = userRepository;
        this.incidentService = incidentService;
    }

    public DashboardSummary getSummary() {
        long totalIncidents = incidentRepository.count();
        
        LocalDate today = LocalDate.now();
        long todayIncidents = incidentRepository.findAll().stream()
                .filter(i -> i.getCreatedAt().toLocalDate().equals(today))
                .count();

        Map<String, Long> statusMap = new HashMap<>();
        for (IncidentStatus status : IncidentStatus.values()) {
            statusMap.put(status.name(), incidentRepository.countByStatus(status));
        }

        Map<String, Long> typeMap = new HashMap<>();
        for (IncidentType type : IncidentType.values()) {
            typeMap.put(type.name(), incidentRepository.countByType(type));
        }

        List<Incident> resolvedIncidents = incidentRepository.findByResolvedAtIsNotNull();
        double avgTimeMin = resolvedIncidents.isEmpty() ? 0.0 :
                resolvedIncidents.stream()
                        .filter(i -> i.getCreatedAt() != null && i.getResolvedAt() != null)
                        .mapToLong(i -> java.time.Duration.between(i.getCreatedAt(), i.getResolvedAt()).toMinutes())
                        .average()
                        .orElse(0.0);

        long availableTechs = userRepository.countByRoleAndIsAvailableTrue(Role.TECHNICIAN);
        long busyTechs = userRepository.countByRoleAndIsAvailableFalse(Role.TECHNICIAN);

        var recent = incidentRepository.findTop10ByOrderByCreatedAtDesc().stream()
                .map(i -> incidentService.getIncidentById(i.getId()))
                .collect(Collectors.toList());

        return new DashboardSummary(
                totalIncidents, todayIncidents, statusMap, typeMap, avgTimeMin, availableTechs, busyTechs, recent
        );
    }
}
