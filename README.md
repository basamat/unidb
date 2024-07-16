University Management System
This project is a University Management System, which is a web-based application designed to manage student, faculty, course, schedule, and grade data. The project is built using Django, a high-level Python web framework, with HTML, CSS, and JavaScript for the frontend.

Features
Student Management: Add, edit, delete, and view student records.
Faculty Management: Add, edit, delete, and view faculty records.
Course Management: Add, edit, delete, and view course records.
Schedule Management: Manage class schedules.
Grade Management: Record and view student grades.
User Authentication: Secure login for administrators and users.
Responsive Design: Mobile-friendly web interface.
Requirements
Python 3.x
Django 3.x
MySQL 
HTML, CSS, JavaScript

ER DIAGRAM:

Students
---------
id (PK)
first_name
last_name
birth_date
address
phone
email
enrollment_date
faculty_id (FK)

Faculties
---------
id (PK)
name
department

Courses
---------
id (PK)
name
description
credits
faculty_id (FK)

Schedules
---------
id (PK)
course_id (FK)
faculty_id (FK)
day
time
location

Grades
---------
id (PK)
student_id (FK)
course_id (FK)
grade
date

