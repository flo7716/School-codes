package com.example.demo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.repository.StudentRepository;

@Service

public class StudentService {
    @Autowired
    private final StudentRepository studentrepository;
    public StudentService(StudentRepository studentrepository) {
        this.studentrepository = studentrepository;
    }

}
