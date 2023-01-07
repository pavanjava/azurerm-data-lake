import os, uuid
from azure.identity import AzureCliCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


class AzureBlobStorageOperations:

    def __init__(self):
        account_url = "https://teststorageacct99.blob.core.windows.net"
        default_credentials = AzureCliCredential()
        self.container_name = "csv-files"
        self.blob_service_client = BlobServiceClient(account_url, credential=default_credentials)
        self.container_client = self.blob_service_client.get_container_client(self.container_name)

    def upload_blob(self):
        try:
            print("Azure Blob Storage Python jumpstart example")

            local_file_name = "train.csv"
            upload_file_path = "/Volumes/BackUpDisk/DataScience_Practice/MachineLearning_Practice/house-prices-advanced-regression-techniques/train.csv"

            # Create a blob client using the local file name as the name for the blob
            blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=local_file_name)

            print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

            # Upload the created file
            with open(file=upload_file_path, mode="rb") as data:
                blob_client.upload_blob(data)

        except Exception as ex:
            print(ex)

    def list_blob_containers(self):
        print("\nListing blobs...")
        blob_list = self.container_client.list_blobs()
        for blob in blob_list:
            print("\n"+blob.name)

    def download_blob(self):
        download_file_path = os.path.join("./", str.replace("test",'.txt', 'DOWNLOAD.txt'))
        container_client = self.blob_service_client.get_container_client(container= self.container_name)
        print("\nDownloading blob to \n\t" + download_file_path)

        with open(file=download_file_path, mode="wb") as download_file:
            download_file.write(container_client.download_blob("train.csv").readall())


ops = AzureBlobStorageOperations()
# ops.upload_blob()
ops.list_blob_containers()
