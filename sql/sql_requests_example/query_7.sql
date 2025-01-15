SELECT s.fullname ,g.grade ,sub.name ,gr.name 
FROM grades g 
JOIN students s on s.id = g.student_id 
JOIN ggroups gr on gr.id = s.group_id 
join subjects sub on sub.id = g.subject_id 
where gr.id = 2 and sub.id =3
ORDER BY g.grade DESC 
