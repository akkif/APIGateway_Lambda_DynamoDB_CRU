import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("Y O U R    T A B L E    N A M E")

def lambda_handler(event,context):
    

    #print(event)
    response = table.put_item( Item=event)
    
    return{
        'statusCode':201,
        'headers':{},
        "body":json.dumps({'messege':"order successfully created"})
    }
