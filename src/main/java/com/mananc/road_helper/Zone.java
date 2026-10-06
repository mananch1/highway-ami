package com.mananc.road_helper;

public class Zone {
    private String zoneId;
    private double x;
    private double y;

    public Zone(String zoneId,double x, double y){
        this.zoneId = zoneId;
        this.x = x;
        this.y = y;
    }

    public String getZoneId() {
        return zoneId;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((zoneId == null) ? 0 : zoneId.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Zone other = (Zone) obj;
        if (zoneId == null) {
            if (other.zoneId != null)
                return false;
        } else if (!zoneId.equals(other.zoneId))
            return false;
        return true;
    }

    
}
