package com.mananc.road_helper.service;

import com.mananc.road_helper.dto.ChatMessageDTO;
import com.mananc.road_helper.entity.ChatMessage;
import com.mananc.road_helper.entity.Incident;
import com.mananc.road_helper.entity.User;
import com.mananc.road_helper.exception.ResourceNotFoundException;
import com.mananc.road_helper.repository.ChatMessageRepository;
import com.mananc.road_helper.repository.IncidentRepository;
import com.mananc.road_helper.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ChatService {

    private final ChatMessageRepository chatMessageRepository;
    private final IncidentRepository incidentRepository;
    private final UserRepository userRepository;

    public ChatService(ChatMessageRepository chatMessageRepository, IncidentRepository incidentRepository, UserRepository userRepository) {
        this.chatMessageRepository = chatMessageRepository;
        this.incidentRepository = incidentRepository;
        this.userRepository = userRepository;
    }

    public ChatMessageDTO saveMessage(ChatMessageDTO dto) {
        Incident incident = incidentRepository.findById(dto.incidentId())
                .orElseThrow(() -> new ResourceNotFoundException("Incident not found"));
        
        ChatMessage msg = new ChatMessage();
        msg.setIncident(incident);
        msg.setMessage(dto.message());
        msg.setSenderName(dto.senderName());
        
        // Sender could be null for guests, wait, we don't have senderId in DTO right now.
        // It uses senderName.
        
        ChatMessage saved = chatMessageRepository.save(msg);
        return new ChatMessageDTO(saved.getId(), incident.getId(), saved.getSenderName(), saved.getMessage(), saved.getTimestamp());
    }

    public List<ChatMessageDTO> getMessagesByIncident(Long incidentId) {
        return chatMessageRepository.findByIncidentIdOrderByTimestampAsc(incidentId).stream()
                .map(m -> new ChatMessageDTO(m.getId(), m.getIncident().getId(), m.getSenderName(), m.getMessage(), m.getTimestamp()))
                .collect(Collectors.toList());
    }
}
