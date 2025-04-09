package com.example.demo.repository;

import java.time.LocalDate;
import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.model.Student;

//Repository : gère l'accès direct à la base de données
@Repository
public interface StudentRepository extends CrudRepository<Student, Integer>{
    public List<Student> findByName(String name);
    public List<Student> findByEmail(String email);
    public List<Student> findByDob(LocalDate dob);
    public List<Student> findByAge(int age);
    

}
