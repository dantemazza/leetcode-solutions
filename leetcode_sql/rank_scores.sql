# Write your MySQL query statement below


WITH RECURSIVE total as 
(
    WITH counts AS (
        SELECT Score, COUNT(Score) as Count_ FROM Scores GROUP BY (Score) ORDER BY Score DESC),

    ranks as (
        SELECT DISTINCT RANK() OVER(ORDER BY Score DESC) AS `Rank`, Score FROM (
            SELECT DISTINCT Score from Scores) AS T) 
            SELECT counts.Score, ranks.`Rank`, counts.Count_ from counts JOIN ranks on counts.Score = ranks.Score)

    ,cte AS (

        SELECT Score, `Rank`, Count_ FROM total
            UNION ALL
            SELECT Score, `Rank`, Count_-1 FROM cte WHERE Count_>1
        )
        SELECT Score, `Rank` FROM cte ORDER BY Score DESC
