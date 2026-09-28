import os

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

STORAGE_ACCOUNT = os.getenv("STORAGE_ACCOUNT")
CONATINER_NAME = os.getenv("STORAGE_CONTAINER", "reports")

credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(
    account_url=f"https://{STORAGE_ACCOUNT}.blob.core.windows.net",
    credential = credential,
)

def list_reports():
    container_client = blob_service_client.get_container_client(CONATINER_NAME)

    return [
        blob.name 
        for blob in container_client.list_blobs()
    ]