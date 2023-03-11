import azure.functions as func
import logging
import os
from google.cloud import storage

app = func.FunctionApp()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '[PATH TO YOUR CREDENTIALS JSON FILE]]'

@app.function_name(name="GCPStorageClient")
@app.route(route="readBlob")
def readBlob(req: func.HttpRequest) -> func.HttpResponse:
     logging.info('Python HTTP trigger function processed a request.')

     filename = req.params.get('filename')
     
     if not filename:
        filename="test.csv"
     
     client = storage.Client()
     bucket = client.bucket('inteltest')
     blob = bucket.blob(filename)

     content = blob.download_as_string()

     return func.HttpResponse(content)