package com.mananc.road_helper.entity;

import jakarta.persistence.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;
import java.time.LocalDateTime;

@Entity
public class Incident {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Enumerated(EnumType.STRING)
    private IncidentType type;

    private String description;

    @Enumerated(EnumType.STRING)
    private IncidentStatus status;

    private String location;

    private String guestName;

    private String guestPhone;

    @Column(unique = true)
    private String guestToken;

    @ManyToOne
    @JoinColumn(name = "customer_id")
    private User customer;

    @ManyToOne
    @JoinColumn(name = "technician_id")
    private User assignedTechnician;

    @CreationTimestamp
    private LocalDateTime createdAt;

    @UpdateTimestamp
    private LocalDateTime updatedAt;

    private LocalDateTime resolvedAt;

    public Incident() {
    }

    public Incident(Long id, IncidentType type, String description, IncidentStatus status, String location, String guestName, String guestPhone, String guestToken, User customer, User assignedTechnician, LocalDateTime createdAt, LocalDateTime updatedAt, LocalDateTime resolvedAt) {
        this.id = id;
        this.type = type;
        this.description = description;
        this.status = status;
        this.location = location;
        this.guestName = guestName;
        this.guestPhone = guestPhone;
        this.guestToken = guestToken;
        this.customer = customer;
        this.assignedTechnician = assignedTechnician;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
        this.resolvedAt = resolvedAt;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public IncidentType getType() { return type; }
    public void setType(IncidentType type) { this.type = type; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public IncidentStatus getStatus() { return status; }
    public void setStatus(IncidentStatus status) { this.status = status; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public String getGuestName() { return guestName; }
    public void setGuestName(String guestName) { this.guestName = guestName; }
    public String getGuestPhone() { return guestPhone; }
    public void setGuestPhone(String guestPhone) { this.guestPhone = guestPhone; }
    public String getGuestToken() { return guestToken; }
    public void setGuestToken(String guestToken) { this.guestToken = guestToken; }
    public User getCustomer() { return customer; }
    public void setCustomer(User customer) { this.customer = customer; }
    public User getAssignedTechnician() { return assignedTechnician; }
    public void setAssignedTechnician(User assignedTechnician) { this.assignedTechnician = assignedTechnician; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
    public LocalDateTime getResolvedAt() { return resolvedAt; }
    public void setResolvedAt(LocalDateTime resolvedAt) { this.resolvedAt = resolvedAt; }
}
