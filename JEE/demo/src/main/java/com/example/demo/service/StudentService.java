package com.example.demo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.repository.StudentRepository;
import java.util.List;

@Service

public class StudentService {
    @Autowired
    private final StudentRepository studentrepository;
    public StudentService(StudentRepository studentrepository) {
        this.studentrepository = studentrepository;
    }

    public List<Student> findByName(String name) {
        return studentrepository.findByName(name);
    }

}
