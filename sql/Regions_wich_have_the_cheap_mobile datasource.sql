SELECT region
FROM jobsity_challenge.trips
WHERE datasource = "cheap_mobile"
GROUP BY 1