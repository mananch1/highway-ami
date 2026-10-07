package com.mananc.road_helper.repository;

import com.mananc.road_helper.entity.Incident;
import com.mananc.road_helper.entity.IncidentStatus;
import com.mananc.road_helper.entity.IncidentType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import java.util.List;
import java.util.Optional;

public interface IncidentRepository extends JpaRepository<Incident, Long> {
    List<Incident> findByCustomerIdOrderByCreatedAtDesc(Long customerId);
    List<Incident> findByAssignedTechnicianIdOrderByCreatedAtDesc(Long technicianId);
    Optional<Incident> findByGuestToken(String guestToken);
    List<Incident> findByDescriptionContainingIgnoreCaseOrLocationContainingIgnoreCase(String desc, String loc);
    long countByStatus(IncidentStatus status);
    long countByType(IncidentType type);
    List<Incident> findTop10ByOrderByCreatedAtDesc();
    
    List<Incident> findByResolvedAtIsNotNull();
    
    List<Incident> findByStatus(IncidentStatus status);
    List<Incident> findByType(IncidentType type);
}
