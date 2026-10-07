package com.mananc.road_helper;



import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;

@Entity 
public class Incident {
    @Id 
    private Integer incidantId;
    @ManyToOne 
    private Zone incidantZone;
    private String customer;
    private String employee;
    
    public Incident(Integer incidantId, Zone incidantZone, String customer, String employee) {
        this.incidantId = incidantId;
        this.incidantZone = incidantZone;
        this.customer = customer;
        this.employee = employee;
    }

    public Incident(Integer incidantId, Zone incidantZone, String employee) {
        this.incidantId = incidantId;
        this.incidantZone = incidantZone;
        this.employee = employee;
    }

    public void setIncidantId(Integer incidantId) {
        this.incidantId = incidantId;
    }

    public void setIncidantZone(Zone incidantZone) {
        this.incidantZone = incidantZone;
    }

    public void setCustomer(String customer) {
        this.customer = customer;
    }

    public void setEmployee(String employee) {
        this.employee = employee;
    }

    public Integer getIncidantId() {
        return incidantId;
    }

    public Zone getIncidantZone() {
        return incidantZone;
    }

    public String getCustomer() {
        return customer;
    }

    public String getEmployee() {
        return employee;
    }

    
    
}
