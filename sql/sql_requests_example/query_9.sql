SELECT stud.fullname  , s.name 
FROM grades g 
JOIN subjects s on s.id = g.subject_id 
JOIN students stud on stud.id = g.student_id 
WHERE student_id  = 32
GROUP BY s.name 