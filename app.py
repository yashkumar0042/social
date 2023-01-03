import tornado
from google.cloud import pubsub_v1,bigquery
import os, requests, json
from google.oauth2 import service_account
from tornado.web import HTTPServer,RequestHandler

class pubsubrequesthandler(RequestHandler):
    # project_id = "docker-build-new"
    # s_path = os.getcwd() + '/docker-build-new-3a1a347c9783.json'
    # auth = service_account.Credentials.from_service_account_file(filename=s_path)

    def post(self):
        envelope = None
        try:
            envelope = tornado.web.escape.json_decode(self.request.body)
            print(envelope)

        except Exception as envelope_error:
            print(f"error while decoding the message {envelope_error.__str__()}")
            self.set_status(status_code=200)



if __name__ == '__main__':
    application = tornado.web.Application([("/",pubsubrequesthandler)])
    application.listen(port=8080,address='0.0.0.0')
    server = HTTPServer(application)
    server.start(num_processes=3)