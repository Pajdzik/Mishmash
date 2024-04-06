SELECT score, rank
FROM Scores 
JOIN (
    SELECT DISTINCT score, ROW_NUMBER() OVER (ORDER BY score DESC) as rank
    FROM Scores
    GROUP BY score
) USING(score)
ORDER BY rank