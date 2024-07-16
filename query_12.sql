SELECT students.name, grades.grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE students.group_id = 2
AND grades.subject_id = 4
AND grades.date = (
    SELECT MAX(date)
    FROM grades
    WHERE grades.subject_id = 4
);