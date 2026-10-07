package com.mananc.road_helper.controller;

import com.mananc.road_helper.dto.ChatMessageDTO;
import com.mananc.road_helper.service.ChatService;
import org.springframework.http.ResponseEntity;
import org.springframework.messaging.handler.annotation.DestinationVariable;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
@RequestMapping("/api/v1/incidents")
public class ChatController {

    private final ChatService chatService;

    public ChatController(ChatService chatService) {
        this.chatService = chatService;
    }

    @MessageMapping("/chat/{incidentId}")
    @SendTo("/topic/chat/{incidentId}")
    public ChatMessageDTO sendMessage(@DestinationVariable("incidentId") Long incidentId, @Payload ChatMessageDTO message) {
        return chatService.saveMessage(message);
    }

    @GetMapping("/{id}/chat")
    @ResponseBody
    public ResponseEntity<List<ChatMessageDTO>> getChatHistory(@PathVariable Long id) {
        return ResponseEntity.ok(chatService.getMessagesByIncident(id));
    }
}
