package com.example.demo.repository;

import org.springframework.stereotype.Repository;

//Repository : gère l'accès direct à la base de données
@Repository
public interface StudentRepository {
    public List<Student> findByName(String name);
    public List<Student> findByEmail(String email);
    public List<Student> findByDob(LocalDate dob);
    public List<Student> findByAge(int age);

}
