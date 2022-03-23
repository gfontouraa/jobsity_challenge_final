
# Jobsity Challenge




## Brief overview
As I read the pdf for the challenge, I found myself already developing how I would do the challenge.

What I didn't realize at the time, was that I dint really have a lot of experience with how API Gateway from AWS integrate with lambda and RDS, so that was a challenge in of itself!

So the final architecture of the project is this:

AWS API Gateway > AWS Lambda > Amazon RDS (Serveless Mysql)
## API documentation

I created this api using a template from swagger, wich is creditated in the api dedication. 

As the challenge stated that the user must have access to insert records, I only created the POST method.

I also took the liberty to host the api in AWS, the host is as follows: https://5f9ckvqgig.execute-api.us-east-1.amazonaws.com/


#### Insert records

```http
  POST /Production/trips
```

As an example of request, the full url is: https://5f9ckvqgig.execute-api.us-east-1.amazonaws.com/Production/trips
and the body is:

```JSON
[
  {
    "region": "Prague",
    "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
    "destination_coord": "POINT (14.43109483523328 50.04052930943246)",
    "datetime": "2018-05-28 09:03:40",
    "datasource": "funny_car"
  }
]
```

It HAS to be an array of objetcs because of the way it's coded.

## How to Use

#### Inserting records

Following the API documentation, how to use is relatively simple, really.

Just do a POST on the endpoint mentioned above, using the body as described, can be a single record or a list of records.

If successful, it will return an 200 status code and how many records it has inserted in the database.

#### Querying the database

I debated over saving the records in S3 or inserting directly in RDS. In the end, I went with RDS as it's cost-effective.

The table is simple enough:

```sql
  	CREATE TABLE jobsity_challenge.trips 
      (`region` varchar(126) NOT NULL, 
      `origin_coord` varchar(256) NOT NULL, 
      `destination_coord` varchar(256) NOT NULL, 
      `datetime` varchar(64) NOT NULL, 
      `datasource` varchar(126) NOT NULL) 
      ENGINE=InnoDB DEFAULT CHARSET=utf8
```

The bonus queries are in the saved queries, but they are also in this repository. 

The table has the 100 records wich are in the sample csv.

