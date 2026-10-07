package com.mananc.road_helper.service;

import com.mananc.road_helper.dto.LoginRequest;
import com.mananc.road_helper.dto.LoginResponse;
import com.mananc.road_helper.dto.RegisterRequest;
import com.mananc.road_helper.dto.UserDTO;
import com.mananc.road_helper.entity.Role;
import com.mananc.road_helper.entity.User;
import com.mananc.road_helper.exception.ResourceNotFoundException;
import com.mananc.road_helper.repository.UserRepository;
import com.mananc.road_helper.security.JwtTokenProvider;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final AuthenticationManager authenticationManager;
    private final JwtTokenProvider tokenProvider;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder, AuthenticationManager authenticationManager, JwtTokenProvider tokenProvider) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.authenticationManager = authenticationManager;
        this.tokenProvider = tokenProvider;
    }

    public LoginResponse register(RegisterRequest request) {
        if (userRepository.findByEmail(request.email()).isPresent()) {
            throw new RuntimeException("Email already exists");
        }

        User user = new User();
        user.setName(request.name());
        user.setEmail(request.email());
        user.setPassword(passwordEncoder.encode(request.password()));
        user.setRole(Role.valueOf(request.role().toUpperCase()));
        user.setIsAvailable(true);

        User savedUser = userRepository.save(user);
        String token = tokenProvider.generateToken(savedUser);

        return new LoginResponse(token, savedUser.getRole().name(), savedUser.getName(), savedUser.getId());
    }

    public LoginResponse login(LoginRequest request) {
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(request.email(), request.password())
        );

        User user = userRepository.findByEmail(request.email())
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));

        String token = tokenProvider.generateToken(user);
        return new LoginResponse(token, user.getRole().name(), user.getName(), user.getId());
    }

    public List<UserDTO> getAllTechnicians() {
        return userRepository.findAll().stream()
                .filter(u -> u.getRole() == Role.TECHNICIAN)
                .map(this::toDto)
                .collect(Collectors.toList());
    }

    public UserDTO toggleAvailability(Long userId) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        user.setIsAvailable(!user.getIsAvailable());
        return toDto(userRepository.save(user));
    }

    public User getCurrentUser(Authentication auth) {
        if (auth == null || !auth.isAuthenticated()) return null;
        return userRepository.findByEmail(auth.getName()).orElse(null);
    }

    private UserDTO toDto(User user) {
        return new UserDTO(user.getId(), user.getName(), user.getEmail(), user.getRole().name(), user.getIsAvailable());
    }
}
