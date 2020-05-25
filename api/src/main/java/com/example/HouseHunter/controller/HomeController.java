package com.example.HouseHunter.controller;

import com.example.HouseHunter.service.HomeService;
import com.example.HouseHunter.model.Home;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("home")
public class HomeController {

    @Autowired
    HomeService homeService;

    @PostMapping("")
    public String save(@RequestBody Home home) {
        homeService.save(home);
        return "ok";
    }

    @GetMapping("{id}")
    public Home findById(@PathVariable("id") String id) {
        return homeService.findById(id);
    }
}
