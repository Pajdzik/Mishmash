SELECT ROUND(CAST(SUM(tiv_2016) AS NUMERIC), 2) as "tiv_2016"
FROM Insurance
WHERE pid IN (
    SELECT DISTINCT i1.pid
    FROM Insurance i1
    JOIN Insurance i2 on i1.tiv_2015 = i2.tiv_2015
    WHERE i1.pid != i2.pid
    AND i1.lat != i2.lat
    AND i1.lon != i2.lon
) AND CONCAT(lat, lon) NOT IN (
    SELECT CONCAT(lat, lon)
    FROM Insurance
    GROUP BY CONCAT(lat, lon)
    HAVING COUNT(CONCAT(lat, lon)) > 1
);