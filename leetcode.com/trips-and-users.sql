SELECT t.request_at AS "Day", 
        ROUND(CAST((
        CAST(COUNT(*) FILTER (WHERE status LIKE 'cancelled_by_%') AS float) 
        / CAST(COUNT(*) AS float)
        ) AS NUMERIC), 2) AS "Cancellation Rate"
FROM Trips t
JOIN Users c ON t.client_id = c.users_id
JOIN Users d ON t.driver_id = d.users_id
WHERE c.banned = 'No'
  AND d.banned = 'No'
  AND t.request_at >= '2013-10-01'
  AND t.request_at <= '2013-10-03'
GROUP BY t.request_at
