package com.example.demo.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.model.Student;
import com.example.demo.repository.StudentRepository;

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

    public Student saveStudent(Student student) {
        return studentrepository.save(student);
    }

}
