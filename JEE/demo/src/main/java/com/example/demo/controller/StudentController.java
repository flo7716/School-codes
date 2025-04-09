package com.example.demo.controller;

import java.time.LocalDate;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.example.demo.model.Student;
import com.example.demo.service.StudentService;



@Controller
public class StudentController {
    @Autowired
    private final StudentService studentService;

    public StudentController(StudentService studentService) {
        this.studentService = studentService;
    }

    @GetMapping("/")
    public String home(Model model){
        Student s1 = new Student("Florian","florian.andre.77@gmail.com", LocalDate.of(2002, 02, 03), 23);
        studentService.saveStudent(s1);
        System.out.println(studentService.findByName("Florian"));
        return "index";
    }
    

}
