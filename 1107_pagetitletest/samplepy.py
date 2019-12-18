import boto3
sqs = boto3.client("sqs")
cognito_idp = boto3.client("cognito-idp")
from os import environ

def handler(event, context):
    try:
        data = cognito_idp.list_users(
            UserPoolId=environ["UserPoolId_cognitoll"],
            Limit=10
        )
    except BaseException as e:
        print(e)
        raise(e)

        try:
            data = sqs.receive_message(
                QueueUrl="https://sqs.{}.amazonaws.com/{}/ll".format(environ["AWS_REGION"], environ["SIGMA_AWS_ACC_ID"]),
                AttributeNames=['All'],
                MaxNumberOfMessages=1,
                VisibilityTimeout=30,
                WaitTimeSeconds=0
            )
        except BaseException as e:
            print(e)
            raise(e)

         
    return {"message": "Successfully executed"}
