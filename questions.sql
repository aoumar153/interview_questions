SELECT name_table.Name,name_table.StudentID
FROM (name_table
INNER JOIN mark_table ON name_table.StudentID = mark_table.StudentID)
WHERE mark_table.Total_marks > (SELECT Total_marks
                               FROM mark_table
                               WHERE mark_table.StudentID = 'V002');
