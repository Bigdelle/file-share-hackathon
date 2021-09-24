import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'level-elevator-327019-721dca179079.json'

storage_client = storage.Client()

bucket_name = 'file-share-bucket_bigredhacks'
my_bucket = storage_client.get_bucket('file-share-bucket_bigredhacks')


def upload_to_bucket(blob_name, file_path, bucket_name):
    try: 
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return


upload_to_bucket('a1app.py', '/Users/bbigdelle/Documents/GitHub/file-share-hackathon/files/a1app.py', my_bucket)