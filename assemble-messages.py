import boto3
from botocore.exceptions import ClientError

url = "https://sqs.us-east-1.amazonaws.com/440848399208/nem2p"
sqs = boto3.client('sqs')

def delete_message(handle):
    try:
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

    for m in range(0,10):

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

                # using a dictionary
                answer = {}
                answer[order] = word
                answer_dict.update(answer)

                # using a list
                each_answer = [order, word]
                answer_list.append(each_answer)

                delete_message(handle)

            else:
                print("No message in the queue")
            
        except ClientError as e:
            print(e.response['Error']['Message'])

    # ordering the dict and extracting the answer
    sorted_dict = dict(sorted(answer_dict.items()))
    answer = ""
    for key in sorted_dict:
        answer += sorted_dict[key] + " "
    print(answer)

    # ordering the list and extracing the answer
    answer_list.sort()
    solution = ""
    for a in answer_list:
        solution += a[1] + " "
    print(solution)


# Trigger the function
if __name__ == "__main__":
    get_messages()