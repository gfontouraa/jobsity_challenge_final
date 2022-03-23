import pymysql
import sys
import logging
from datetime import datetime
import json
import botocore
import boto3

REGION = 'us-east-1'

rds_host = "database-2.cluster-cdkledpsjlxc.us-east-1.rds.amazonaws.com"
name = "admin"
password = "FW6A6HItyT8kvcCQrffI"
db_name = "rdslambda"
cluster_arn = 'arn:aws:rds:us-east-1:900720743795:cluster:database-2' 
secret_arn = 'arn:aws:secretsmanager:us-east-1:900720743795:secret:rds-db-credentials/cluster-3N2Q52DZD35JVSORTHCDR224MU/admin-s8Kl5G'
rds_data = boto3.client('rds-data')

logger= logging.getLogger()
logger.setLevel(logging.DEBUG)

rds_host = "database-2.cluster-cdkledpsjlxc.us-east-1.rds.amazonaws.com"
name = "admin"
password = "FW6A6HItyT8kvcCQrffI"
db_name = "rdslambda"


def lambda_handler(event, context):
    records = 0
    for record in event:
        
        records = records+1
        region = record['region']
        origin_coord = record['origin_coord']
        destination_coord = record['destination_coord']
        datetime = record['datetime']
        datasource = record['datasource']
        print(region)
        print(origin_coord)
        print(destination_coord)
        print(datetime)
        print(datasource)
        
        sql = f"INSERT INTO trips(region, origin_coord,destination_coord,datetime,datasource) VALUES('{region}','{origin_coord}','{destination_coord}','{datetime}','{datasource}')"
        print(sql)
        
        response = rds_data.execute_statement(
            resourceArn = cluster_arn, 
            secretArn = secret_arn, 
            database = 'jobsity_challenge', 
            sql = sql)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Everything went fine! You inserted {records} records!'")
    }
    
    
