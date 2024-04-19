# Data Project 3: Reassemble SQS Messages

This programming assignment makes use of your Python skills to interact with an Amazon SQS messaging queue.

You are allowed to work on this project with one other person, if you want to. But that is not required. See the "Submission & Grading" section at the bottom for instructions.

Short instructions: You have been given your own SQS queue, and some AWS credentials to use. Write python that does the following:

1. Retrieves the messages that have been published to your queue. There are 10 in total.
2. Each message contains two custom `MessageAttributes`: `order` and `word`. For instance, one message might contain an order of `3` and a word of `what`.
3. You should determine some method for storing these values as a pair. There are many options: in a Python collection object, in a text file, an SQL database, a MongoDB collection, etc.
4. Once you have picked up your messages, your python should reassemble the words by using the `order` value. This will reveal a phrase that you should then manually enter into the `phrase.txt` file. DO NOT reassemble the messages by hand.
5. Finally, your python should delete all messages after processing. This should not be done by hand.


## Setup

1. Fork this repository and open your fork in Gitpod or in your local environment. Add/commit/push your work to your own fork.
2. Make sure you use the custom AWS credentials given to you in Canvas. DO NOT USE AWS Academy for this project. It will not work. 
3. If you open this project in Gitpod, all software should be provided for you. But in case you need to reload them, simply run

    ```
    pip install -r requirements.txt
    ```
4. Reference the [`get-message.py`](get-message.py) file for a start at how to pull a single message from SQS. Read the file carefully to understand what its parts do.
5. A custom SQS queue has been created for each of you. To determine your Queue URL, simply add your UVA computing ID to the end of this URL:

    ```
    https://sqs.us-east-1.amazonaws.com/440848399208/

    # for example:
    https://sqs.us-east-1.amazonaws.com/440848399208/nem2p
    ```

## Receiving Messages

Since you are given the code to get one (1) message from the queue, you should determine a way to repeat that ten (10) times. (Without running it separately 10x.)

Messages in your queue have an `VisibilityTimeout` of 5 minutes (300 seconds). Messages in your queue will remain for 14 days unless you delete them.

## Storing Message Data

Each message contains two important attributes (extended fields that have been added). These fields are named `order` and `word`. The sample code given to you pulls those values out as variables for you to use.

However, you need to implement some means of storing them so that they can be re-ordered. Values for the `order` field are zero-indexed.

## Reassembling Message Data

Your python should take the stored data and assemble the `word` values according to their corresponding `order` values.

Here is a made-up example:

```
messages = [
    {"order":3, "word":"fox"},
    {"order":0, "word":"the"},
    {"order":2, "word":"brown"},
    {"order":1, "word":"quick"},
]
```
If put these dictionaries into order `[0,1,2,3]` you can read the phrase `The quick brown fox`.

Be sure your python outputs the correctly ordered phrase. You may then type it into `phrase.txt` by hand.

## Deleting Messages

A function has been given to you to delete a messaging using its `ReceiptHandle`. Be sure to use this for the final run of your code.

You will be penalized if any messages remain in your queue after your script runs.

## Recommendations for Testing

Your script needs to (1) retrieve all messages; (2) store message data; (3) reassemble the phrase from the message content; and (4) delete the messages in a single execution.

My advice is for you to test 1, 2, and 3 above as you like, as many times as you like. Messages that have been picked up will remain invisible for 5 minutes. After that time has elapsed they will reappear in your queue and you can test again.

Only when you are finally ready should you enable message deletion in your script.

## Submission and Grading

You should submit the URL to your fork of this repository for grading. The repository should contain your script and the reassembled phrase in the proper file.

If you completed this project with a partner, follow these steps:

1. In `phrase.txt` indicate your partner's name.
2. Only one repo should be submitted for grading. So be sure all of your collaborative work is pushed to a single repository, and both of you should submit the same repo URL.

This data project is worth 17 total points:

| Element  | Points  |
|---|---|
| Setup / proper queue  | 1  |
| Loop through messages  | 2  |
| Store message output  | 4  |
| Reassemble message logic  | 4 |
| Correct phrase | 3 |
| Delete all SQS messages  | 3  |