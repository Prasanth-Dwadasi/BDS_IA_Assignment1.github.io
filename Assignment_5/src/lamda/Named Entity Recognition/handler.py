import json
import torch
from transformers import pipeline

def serverless_pipeline():
    def predict(text):
        ner = pipeline("ner",model="./model",aggregation_strategy='simple')
        summary = ner(text)
        low = []
        for d in summary:
            low.append(d.get('word'))
        return low
    return predict

# initializes the pipeline

question_answering_pipeline = serverless_pipeline()


def handler(event, context):
    print("event started")
    try:
        print(event)
        print(context)
        # loads the incoming event into a dictonary
        body = json.loads(event['body'])
        print("body is ",body)
        # uses the pipeline to predict the answer
        answer = question_answering_pipeline(text=body['episode_narrative'])
        print("answer is",answer)
        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True

            },
            "body": json.dumps({'answer': answer})
        }
    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": repr(e)})
        }
        
        
        
