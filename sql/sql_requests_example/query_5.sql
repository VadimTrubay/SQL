SELECT s.name , t.fullname 
FROM subjects s 
join teachers t on s.teacher_id = t.id 
WHERE t.id = 3
