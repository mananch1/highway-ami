package com.mananc.road_helper.entity;

import jakarta.persistence.*;
import org.hibernate.annotations.CreationTimestamp;
import java.time.LocalDateTime;

@Entity
public class ChatMessage {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    private Incident incident;

    @ManyToOne
    private User sender;

    private String senderName;

    private String message;

    @CreationTimestamp
    private LocalDateTime timestamp;

    public ChatMessage() {
    }

    public ChatMessage(Long id, Incident incident, User sender, String senderName, String message, LocalDateTime timestamp) {
        this.id = id;
        this.incident = incident;
        this.sender = sender;
        this.senderName = senderName;
        this.message = message;
        this.timestamp = timestamp;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Incident getIncident() { return incident; }
    public void setIncident(Incident incident) { this.incident = incident; }
    public User getSender() { return sender; }
    public void setSender(User sender) { this.sender = sender; }
    public String getSenderName() { return senderName; }
    public void setSenderName(String senderName) { this.senderName = senderName; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
    public LocalDateTime getTimestamp() { return timestamp; }
    public void setTimestamp(LocalDateTime timestamp) { this.timestamp = timestamp; }
}
