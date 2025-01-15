SELECT s.fullname, ROUND(AVG(g.grade)) as average_grade 
FROM grades g 
LEFT JOIN students s on s.id = g.student_id 
WHERE g.subject_id = 9
GROUP BY s.id 
ORDER BY average_grade DESC 
LIMIT 1
