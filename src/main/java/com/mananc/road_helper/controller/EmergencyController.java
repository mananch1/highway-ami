package com.mananc.road_helper.controller;

import com.mananc.road_helper.dto.EmergencyRequest;
import com.mananc.road_helper.dto.EmergencyResponse;
import com.mananc.road_helper.dto.IncidentResponse;
import com.mananc.road_helper.service.IncidentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/emergency")
public class EmergencyController {

    private final IncidentService incidentService;

    public EmergencyController(IncidentService incidentService) {
        this.incidentService = incidentService;
    }

    @PostMapping
    public ResponseEntity<EmergencyResponse> createEmergency(@RequestBody EmergencyRequest request) {
        return ResponseEntity.ok(incidentService.createEmergencyIncident(request));
    }

    @GetMapping("/status")
    public ResponseEntity<IncidentResponse> getStatus(@RequestParam String token) {
        return ResponseEntity.ok(incidentService.getIncidentByGuestToken(token));
    }
}
