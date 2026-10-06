package com.mananc.road_helper;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestParam;


@SpringBootApplication
@RestController 
public class RoadHelperApplication {

	public static void main(String[] args) {
		SpringApplication.run(RoadHelperApplication.class, args);
	}

	@GetMapping("hi")
	public String helloWorld(){
		return "Hello World";
	}

	
	

}
