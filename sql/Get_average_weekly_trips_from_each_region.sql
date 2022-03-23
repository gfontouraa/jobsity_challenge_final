SELECT region
       ,DATE_SUB(CAST(datetime AS DATE), INTERVAL DAYOFWEEK(CAST(datetime AS DATE))-1 DAY) AS week
       ,COUNT(*)
FROM jobsity_challenge.trips
GROUP BY 1,2
ORDER BY 1