import json
from google.oauth2 import service_account
from google.cloud import storage

project_id = "xxxx-35da0"
json_file = '/Users/xxx/service_account_json_key/xxxx-35da0-xxxxx.json'
cloud_storage_bucket = 'pubsite_prod_rev_109438xxxxxx084xxx'
credentials = service_account.Credentials.from_service_account_file(json_file, scopes=['https://www.googleapis.com/auth/cloud-platform'])
packages = ['com.xxx.xxxx', 'com.xxx.xxxxxx', 'com.xxxxx.xxxx']
years = ["2020", "2019"]
months = ["12", "11", "10", "09", "08", "07", "06", "05", "04", "03", "02", "01"]
dates = []

#downloading two years customer reviews
def get_monthly_customer_review():
  for package_name in packages:
    for date in dates:
      report_to_download = "reviews/reviews_{}_{}.csv".format(package_name, date)
      destination_file_name = "/Users/xxx/reports/review_{}_{}.csv".format(package_name, date)
      storage_client = storage.Client(project=project_id, credentials=credentials)
      bucket = storage_client.bucket(cloud_storage_bucket)
      blob = bucket.blob(report_to_download)
      try:
        blob.download_to_filename(destination_file_name)
        print("Blob {} downloaded to {}.".format(report_to_download, destination_file_name))
      except:
        print("{} file not found".format(report_to_download))

#downloading two years customer installs
def get_monthly_app_installs():
  for package_name in packages:
    for date in dates:
      report_to_download = "stats/installs/installs_{}_202011_overview.csv".format(package_name)
      destination_file_name = "/Users/xxx/reports/{}_installs.csv".format(package_name)
      storage_client = storage.Client(project=project_id, credentials=credentials)
      bucket = storage_client.bucket(cloud_storage_bucket)
      blob = bucket.blob(report_to_download)
      try:
        blob.download_to_filename(destination_file_name)
        print("Blob {} downloaded to {}.".format(report_to_download, destination_file_name))
      except:
        print("{} file not found".format(report_to_download))
      
def get_date():
  for year in years:
    for month in months:
      dates.append("{}{}".format(year, month))
  print(dates)
  
      
get_date()
get_monthly_customer_review()
get_monthly_app_installs()
