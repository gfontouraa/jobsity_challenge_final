SELECT region
       ,datasource
FROM jobsity_challenge.trips AS principal_table
INNER JOIN (SELECT region AS region_count, count(*) FROM jobsity_challenge.trips GROUP BY 1 ORDER BY 2 DESC LIMIT 2) AS two_regions ON principal_table.region = two_regions.region_count
INNER JOIN (SELECT region AS region_date, MAX(CAST(datetime AS DATETIME)) AS last FROM jobsity_challenge.trips GROUP BY 1 ORDER BY 1 ASC) AS last_datetime ON principal_table.datetime = last_datetime.last
GROUP BY 1
ORDER BY 1


