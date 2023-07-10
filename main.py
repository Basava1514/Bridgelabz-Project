from fastapi import FastAPI, File, UploadFile
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

connection_string="DefaultEndpointsProtocol=https;AccountName=storagetestmigrate1;AccountKey=LNDjvCqG3/pKT/DI1JZ+Jo+AQhbirIX+GwWwXW+21s6ofDbCIlZerLwqmUJ1bArk2jPmInkdVxPS+AStaaf2Fg==;EndpointSuffix=core.windows.net"

container_name="cont1"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)



@app.post("/uploadfile/")
def create_upload_file(uploadedFile: UploadFile):
    # Upload the created file
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=uploadedFile.filename)
    blob_client.upload_blob(uploadedFile.file.read())
    return {"filename": uploadedFile.filename}