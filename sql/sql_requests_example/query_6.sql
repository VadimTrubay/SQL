SELECT s.fullname , g.name 
FROM students s 
JOIN ggroups g on g.id = s.group_id 
where g.id =2