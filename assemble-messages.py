import boto3
from botocore.exceptions import ClientError


url = "https://sqs.us-east-1.amazonaws.com/440848399208/nem2p"
sqs = boto3.client('sqs')


def get_messages():

        try:
            response = sqs.receive_message(
                QueueUrl=url,
                AttributeNames=[
                    'All'
                ],
                MaxNumberOfMessages=1,
                MessageAttributeNames=[
                    'All'
                ]
            )
            if "Messages" in response:
                order = response['Messages'][0]['MessageAttributes']['order']['StringValue']
                word = response['Messages'][0]['MessageAttributes']['word']['StringValue']
                handle = response['Messages'][0]['ReceiptHandle']


            else:
                print("No message in the queue")
            
        except ClientError as e:
            print(e.response['Error']['Message'])


# Trigger the function
if __name__ == "__main__":
    get_messages()