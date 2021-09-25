import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'level-elevator-327019-721dca179079.json'

storage_client = storage.Client()

bucket_name = 'file-share-bucket_bigredhacks'
my_bucket = storage_client.get_bucket('file-share-bucket_bigredhacks')


def upload_to_bucket(blob_name, file_path, bucket_name):
    # ask if they want to download to different folder
    try: 
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return

def download_files(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob,f)
        return True
    except Exception as e:
        print(e)
        return False

    
def create_url(bucket_name, file_name, folder_name):
    if len(folder_name)==0:
        cloud_url = 'https://storage.googleapis.com/' + bucket_name + \
            '/' + file_name
    else:
        cloud_url = 'https://storage.googleapis.com/' + bucket_name + \
            '/' + folder_name + '/' + file_name
    print('The link for your uploaded file is: ')
    print(cloud_url)