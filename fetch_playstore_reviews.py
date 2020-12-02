import json

from google.oauth2 import service_account

from apiclient.discovery import build

from google.cloud import storage

#Json file path
json_file = '/Users/xxx/service_account_json_key/xxx.json'

cloud_storage_bucket = 'pubsite_prod_rev_xxxx'

report_to_download = 'reviews/reviews_com.xxx.xxxx_202007.csv'

credentials = service_account.Credentials.from_service_account_file(json_file, scopes=['https://www.googleapis.com/auth/cloud-platform'])

v1storage = build('storage', 'v1', credentials=credentials)

print (json.dumps(v1storage.objects().get(bucket=cloud_storage_bucket,object=report_to_download).execute()))

destination_file_name = "/Users/xxx/xxx/xxx.csv"

storage_client = storage.Client(project="{projectId}", credentials=credentials)

bucket = storage_client.bucket(cloud_storage_bucket)
blob = bucket.blob(report_to_download)
blob.download_to_filename(destination_file_name)

print("Blob {} downloaded to {}.".format(report_to_download, destination_file_name))



