SELECT subjects.name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = 9;