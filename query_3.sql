SELECT groups.name, AVG(grades.grade) as avg_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
WHERE grades.subject_id = 3
GROUP BY groups.name;