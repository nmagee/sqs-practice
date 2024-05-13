import boto3
from botocore.exceptions import ClientError


def send_bulk(uid):
    sqs = boto3.client("sqs")
    url = "https://sqs.us-east-1.amazonaws.com/440848399208/" + uid
    snippets = [
        "People",
        "who",
        "know",
        "what",
        "they're",
        "talking",
        "about",
        "don't",
        "need",
        "PowerPoint.",
    ]
    for word in snippets:
        indx = str(snippets.index(word))
        try:
            response = sqs.send_message(
                QueueUrl=url,
                MessageBody="DP3 message",
                MessageAttributes={
                    "order": {"StringValue": indx, "DataType": "String"},
                    "word": {"StringValue": word, "DataType": "String"},
                },
            )
            print(response)
        except ClientError as e:
            print(e)
    print(url)
    print(uid)
    print("Bulk messages sent")


# file1 = open('students.txt', 'r')
# Lines = file1.readlines()
# for line in Lines:
#     response = send_bulk(line)

send_bulk("nem2p")
