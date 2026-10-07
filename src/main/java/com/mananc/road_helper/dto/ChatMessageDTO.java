package com.mananc.road_helper.dto;

import java.time.LocalDateTime;

public class ChatMessageDTO {
    private Long id;
    private Long incidentId;
    private String senderName;
    private String message;
    private LocalDateTime timestamp;

    public ChatMessageDTO() {
    }

    public ChatMessageDTO(Long id, Long incidentId, String senderName, String message, LocalDateTime timestamp) {
        this.id = id;
        this.incidentId = incidentId;
        this.senderName = senderName;
        this.message = message;
        this.timestamp = timestamp;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Long getIncidentId() { return incidentId; }
    public void setIncidentId(Long incidentId) { this.incidentId = incidentId; }
    public String getSenderName() { return senderName; }
    public void setSenderName(String senderName) { this.senderName = senderName; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
    public LocalDateTime getTimestamp() { return timestamp; }
    public void setTimestamp(LocalDateTime timestamp) { this.timestamp = timestamp; }

    public Long id() { return id; }
    public Long incidentId() { return incidentId; }
    public String senderName() { return senderName; }
    public String message() { return message; }
    public LocalDateTime timestamp() { return timestamp; }
}
