import simplejson as json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("warehouse")

def lambda_handler(event, context):
    #if event['queryStringParameters']
    body = event["queryStringParameters"]
###id processing###
    if "id" in body:
        print(True)
        id = int(event["queryStringParameters"]["id"])
        raw_response = table.query(KeyConditionExpression=Key('id').eq(id))
        response=(raw_response["Items"][0])
	

        return {
            "statusCode":200,
            "body":json.dumps(response)
            
        }
	
    elif "p1" in body and "p2" in body:
        range1=event["queryStringParameters"]['p1']
        range2=event["queryStringParameters"]['p2']
        r1=int(range1)
        r2=int(range2)
        print(r1," ",r2)
        #print(event)
        response = table.scan(FilterExpression=Attr('price').between(r1,r2))
        a = (response['Items'])
        print(a)
        #b=json.dumps(a)
        #print(b)
        return {
            'statusCode': 200,
            'body': json.dumps(a)
        }
