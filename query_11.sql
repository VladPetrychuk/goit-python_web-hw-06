SELECT AVG(grades.grade) as avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = 5
AND subjects.teacher_id = 4;