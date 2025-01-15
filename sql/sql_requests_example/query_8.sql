SELECT round(AVG(g.grade),2) as Average_grade , sub.name as Subject , t.fullname as Teacher
FROM grades g 
JOIN students s on s.id = g.student_id 
JOIN subjects sub on sub.id = g.subject_id 
JOIN teachers t on t.id = sub.teacher_id
WHEre t.id =3
GROUP BY sub.name 
