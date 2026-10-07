package com.mananc.road_helper.dto;

import java.time.LocalDateTime;

public record IncidentResponse(Long id, String type, String description, String status, String location, String customerName, String technicianName, String guestName, String guestPhone, LocalDateTime createdAt, LocalDateTime updatedAt, LocalDateTime resolvedAt) {
}
