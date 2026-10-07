package com.mananc.road_helper.dto;

import java.util.List;
import java.util.Map;

public record DashboardSummary(long totalIncidents, long todayIncidents, Map<String, Long> incidentsByStatus, Map<String, Long> incidentsByType, Double averageResolutionTimeMinutes, long availableTechnicians, long busyTechnicians, List<IncidentResponse> recentIncidents) {
}
