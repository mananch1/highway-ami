package com.mananc.road_helper.repository;

import com.mananc.road_helper.entity.ChatMessage;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface ChatMessageRepository extends JpaRepository<ChatMessage, Long> {
    List<ChatMessage> findByIncidentIdOrderByTimestampAsc(Long incidentId);
}
