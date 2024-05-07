import boto3
from botocore.exceptions import ClientError

# Set up your SQS queue URL and boto3 client
url = "https://sqs.us-east-1.amazonaws.com/440848399208/nem2p"
sqs = boto3.client('sqs')


def delete_message(handle):
    try:
        # Delete message from SQS queue
        sqs.delete_message(
            QueueUrl=url,
            ReceiptHandle=handle
        )
        print("Message deleted")
    except ClientError as e:
        print(e.response['Error']['Message'])

def get_messages():

    answer_dict = {}
    answer_list = []

    for m in range(0, 10):
        try:
            # Receive message from SQS queue. Each message has two MessageAttributes: order and word
            # You want to extract these two attributes to reassemble the secret message
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
            # Check if there is a message in the queue or not
            if "Messages" in response:
                # extract the two message attributes you want to use as variables
                order = response['Messages'][0]['MessageAttributes']['order']['StringValue']
                word = response['Messages'][0]['MessageAttributes']['word']['StringValue']
                handle = response['Messages'][0]['ReceiptHandle']

                # Print the message attributes - this is what you want to work with to reassemble the message
                # print(f"Order: {order}")
                # print(f"Word: {word}")

                # How to build if using DICT
                answer = {}
                answer[order] = word
                answer_dict.update(answer)

                # How to build if using LIST
                each_answer = [order, word]
                answer_list.append(each_answer)


                delete_message(handle)

            # If there is no message in the queue, print a message and exit    
            else:
                print("No message in the queue")
            
        # Handle any errors that may occur connecting to SQS
        except ClientError as e:
            print(e.response['Error']['Message'])

    # Sort the reassembled dict
    sorted_dict = dict(sorted(answer_dict.items()))
    answer = ""
    for key in sorted_dict:
        answer += sorted_dict[key] + " "
    print(answer)


    # Sort the reassembled list
    answer_list.sort()
    solution = ""
    for a in answer_list:
        solution += a[1] + " "

    print(solution)


# Trigger the function
if __name__ == "__main__":
    get_messages()
