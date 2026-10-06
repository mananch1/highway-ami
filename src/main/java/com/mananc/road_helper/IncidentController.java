package com.mananc.road_helper;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List; 

@RestController 
@RequestMapping ("api/v1/incidents")
public class IncidentController {
    @GetMapping 
    public List<Incident> getEnginners(){
        return List.of(

            new Incident(
                1,
                new Zone("AL", 0, 0),
                "Manan C"
                ),
            new Incident(
                2,
                new Zone("AR", 0, 10),
                "Arthur Morgan"
                )
            );
    }
}
