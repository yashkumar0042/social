import base64
import json
from google.cloud import bigquery,pubsub_v1
import os,requests
from flask import Flask,request
from google.oauth2 import service_account

project_id = "docker-build-new"
cur_dir = os.getcwd()
key_path = cur_dir + '/docker-build-new-3a1a347c9783.json'
auth = service_account.Credentials.from_service_account_file(filename=key_path)

app = Flask(__name__)

class messagehandler :
    @app.route('/', methods='POST')
    def post(self):
        envelope = request.get_json()
        data = json.loads(base64.b64decode())

    def my_sub(self):
        subscriber_id = "projects/docker-build-new/subscriptions/testing_tweet"
        subscriber = pubsub_v1.SubscriberClient(credentials=auth)
        subscriber_path = subscriber.subscription_path(project=project_id,subscription=subscriber_id)
        stream_pull = subscriber.subscribe(subscription=subscriber_path,callback=process_payload)
        with subscriber :
            try:
                stream_pull.result()
            except TimeoutError:
                stream_pull.cancel()

def process_payload(message):
    print(f"Received {message}.")
    message.ack()


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))