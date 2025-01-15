SELECT g2.name as name_group, subj.name as name_subject, ROUND(AVG(g.grade)) as average_grade
FROM grades g 
JOIN students s on s.id = g.id 
JOIN subjects subj on subj.id = g.subject_id 
JOIN ggroups g2 on g2.id = s.group_id 
GROUP BY g2.id 
ORDER BY average_grade DESC 