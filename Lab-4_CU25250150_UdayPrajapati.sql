-- LAB 4
-- Database Schema using DDL
-- Primary Key and Foreign Key Constraints

CREATE DATABASE CollegeDB;

USE CollegeDB;

-- Department Table
CREATE TABLE Department (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(50) NOT NULL
);

-- Student Table
CREATE TABLE Student (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Age INT CHECK (Age BETWEEN 18 AND 30),
    Department_ID INT,

    FOREIGN KEY (Department_ID)
    REFERENCES Department(Department_ID)
);

-- Insert Departments
INSERT INTO Department
VALUES
(1, 'Computer Science'),
(2, 'Electronics'),
(3, 'Mechanical');

-- Insert Students
INSERT INTO Student
VALUES
(101, 'Uday', 'uday@gmail.com', 20, 1),
(102, 'Rahul', 'rahul@gmail.com', 21, 1),
(103, 'Aman', 'aman@gmail.com', 20, 2);

-- Display Tables
SELECT * FROM Department;
SELECT * FROM Student;
