import json
import torch
from transformers import pipeline

def serverless_pipeline():
    def predict(text):
        summarizer = pipeline("summarization",model="./model")
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary
    return predict

# initializes the pipeline
question_answering_pipeline = serverless_pipeline()
#print(question_answering_pipeline(text=ARTICLE)[0].get("summary_text"))
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
        
        
        
