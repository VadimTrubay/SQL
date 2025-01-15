SELECT s.fullname as Name_Student, sub.name as Name_Subject, t.fullname as Teacher
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN ggroups gr on gr.id = s.group_id 
JOIN subjects sub on sub.id = g.subject_id 
JOIN teachers t on sub.teacher_id = t.id 
WHERE s.id = 43 and t.id =3
GROUP BY sub.name 