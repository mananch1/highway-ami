package com.mananc.road_helper.service;

import com.mananc.road_helper.entity.Incident;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

@Service
public class NotificationService {
    
    private static final Logger log = LoggerFactory.getLogger(NotificationService.class);

    public void notifyEmergencyServices(Incident incident) {
        switch (incident.getType()) {
            case FLAT_TIRE:
            case ENGINE_FAILURE:
                log.info("[MOCK] Notifying TOW_TRUCK for incident #{}", incident.getId());
                break;
            case ACCIDENT:
                log.info("[MOCK] Notifying POLICE, AMBULANCE, TOW_TRUCK for incident #{}", incident.getId());
                break;
            case LOCKOUT:
                log.info("[MOCK] Notifying LOCKSMITH for incident #{}", incident.getId());
                break;
            case FUEL_EMPTY:
                log.info("[MOCK] Notifying FUEL_DELIVERY for incident #{}", incident.getId());
                break;
        }
    }
}
