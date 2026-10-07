package com.mananc.road_helper.dto;

public record LoginResponse(String token, String role, String name, Long userId) {
}
