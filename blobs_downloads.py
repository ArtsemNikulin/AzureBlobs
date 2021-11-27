import os
from azure.storage.blob import BlobServiceClient


class BlobsProcessing:
    def __init__(self):
        self.connection_string = "       " # ENTER
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        self.container_name = input("Enter container name. Example - my-files\n\t")
        self.all_blobs = self.blob_service_client.get_container_client(self.container_name).list_blobs()
        self.folder = self.container_name

    def download_all_blobs(self):
        for blob in self.all_blobs:
            file_path = os.path.join(self.folder, blob.name)
            blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=blob)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(os.path.join(file_path), "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())

    def download_particular_blob(self):
        def download_particular_blob(self):
            blob_name = input("Enter blob(file) name for download with full path. Example - test/test.txt\n\t")
            file_path = os.path.join(self.folder, blob_name)
            blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=blob_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(os.path.join(file_path), "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())


x = BlobsProcessing()
x.download_all_blobs()
#x.download_particular_blob()
