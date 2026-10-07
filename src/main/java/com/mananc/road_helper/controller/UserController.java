package com.mananc.road_helper.controller;

import com.mananc.road_helper.dto.UserDTO;
import com.mananc.road_helper.service.UserService;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public ResponseEntity<List<UserDTO>> getAllTechnicians() {
        return ResponseEntity.ok(userService.getAllTechnicians());
    }

    @PatchMapping("/{id}/availability")
    public ResponseEntity<UserDTO> toggleAvailability(@PathVariable Long id) {
        return ResponseEntity.ok(userService.toggleAvailability(id));
    }
}
