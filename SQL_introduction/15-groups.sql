-- Lists the number of records
SELECT score, COUNT(score) as number FROM second_table ORDER BY score, number desc GROUP BY score, number;