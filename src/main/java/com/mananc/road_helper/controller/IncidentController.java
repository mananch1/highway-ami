package com.mananc.road_helper.controller;

import com.mananc.road_helper.dto.IncidentRequest;
import com.mananc.road_helper.dto.IncidentResponse;
import com.mananc.road_helper.dto.StatusUpdateRequest;
import com.mananc.road_helper.entity.Role;
import com.mananc.road_helper.entity.User;
import com.mananc.road_helper.service.IncidentService;
import com.mananc.road_helper.service.UserService;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/incidents")
public class IncidentController {

    private final IncidentService incidentService;
    private final UserService userService;

    public IncidentController(IncidentService incidentService, UserService userService) {
        this.incidentService = incidentService;
        this.userService = userService;
    }

    @GetMapping
    public ResponseEntity<List<IncidentResponse>> listIncidents(Authentication authentication) {
        User user = userService.getCurrentUser(authentication);
        if (user == null) return ResponseEntity.status(401).build();

        if (user.getRole() == Role.ADMIN) {
            return ResponseEntity.ok(incidentService.getAllIncidents());
        } else if (user.getRole() == Role.TECHNICIAN) {
            return ResponseEntity.ok(incidentService.getIncidentsByTechnician(user.getId()));
        } else {
            return ResponseEntity.ok(incidentService.getIncidentsByCustomer(user.getId()));
        }
    }

    @PostMapping
    public ResponseEntity<IncidentResponse> createIncident(@RequestBody IncidentRequest request, Authentication authentication) {
        User user = userService.getCurrentUser(authentication);
        if (user == null || user.getRole() != Role.CUSTOMER) return ResponseEntity.status(403).build();
        return ResponseEntity.ok(incidentService.createIncident(request, user));
    }

    @GetMapping("/{id}")
    public ResponseEntity<IncidentResponse> getIncident(@PathVariable Long id) {
        return ResponseEntity.ok(incidentService.getIncidentById(id));
    }

    @GetMapping("/search")
    public ResponseEntity<List<IncidentResponse>> searchIncidents(@RequestParam String query) {
        return ResponseEntity.ok(incidentService.searchIncidents(query));
    }

    @PatchMapping("/{id}/status")
    public ResponseEntity<IncidentResponse> updateStatus(@PathVariable Long id, @RequestBody StatusUpdateRequest request, Authentication authentication) {
        User user = userService.getCurrentUser(authentication);
        if (user == null) return ResponseEntity.status(401).build();
        return ResponseEntity.ok(incidentService.updateStatus(id, request, user));
    }
}
