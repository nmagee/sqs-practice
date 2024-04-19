import boto3
from botocore.exceptions import ClientError
import os
import json

def purge(uid):
    sqs = boto3.client('sqs')
    url = "https://sqs.us-east-1.amazonaws.com/440848399208/" + uid
    try:
        response = sqs.purge_queue(
            QueueUrl=url
        )
        print(response)
    except ClientError as e:
        print(e)
    print("SQS purged for " + uid)

file1 = open('students.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    response = purge(line)
