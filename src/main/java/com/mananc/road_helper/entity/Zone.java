package com.mananc.road_helper.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import java.util.Objects;

@Entity
public class Zone {

    @Id
    private String zoneId;

    private String name;

    private double x;

    private double y;

    public Zone() {
    }

    public Zone(String zoneId, String name, double x, double y) {
        this.zoneId = zoneId;
        this.name = name;
        this.x = x;
        this.y = y;
    }

    public String getZoneId() { return zoneId; }
    public void setZoneId(String zoneId) { this.zoneId = zoneId; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public double getX() { return x; }
    public void setX(double x) { this.x = x; }
    public double getY() { return y; }
    public void setY(double y) { this.y = y; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Zone zone = (Zone) o;
        return Objects.equals(zoneId, zone.zoneId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(zoneId);
    }
}
