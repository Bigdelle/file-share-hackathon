import createbucket
import sharemethods
import os
from google.cloud import storage

# FILE SHARE VIRTUAL ENV CALLED file-share
"""
To Run:

Start virtual envinroment through source file-share/bin/activate
Start flask through flask run

"""


#give them the available buckets


def list_buckets():
    print()
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

#creating a bucket or not
def create_bucket_or_not():
    create_a_bucket = input('Would you like to create a new bucket? Type "True" or "False": ')
    print()
    if create_a_bucket=='True':
        name = input('What would you like to call it? ')
        try:
            createbucket.create_bucket(name)
        except Exception as e:
            print('Invalid, non-unique bucket name. Pick another and try again.')
            print()


#upload_or_download = input('Type "upload" for uploading and "download" for downloading: ')
def upload_ask():
    print()
    upload_download = input('Would you like to upload a file? y/n ')
    if upload_download=='y':
        print()
        #file must be in the toupload folder
        blob = input('What is the file name? ')
        print()
        folder = input('Would you like to upload to a specific folder? y/n ')
        if folder=='y':
            print()
            folder_name = input('What folder would you like to upload it to? ')
        else:
            folder_name = ''
        print()
        bucket = input('Which bucket? ')
        print()
        path = input('What is the path? ')
        try:
            if folder=='y':
                sharemethods.create_url(bucket, blob, folder_name)
            else:
                sharemethods.create_url(bucket, blob, '')
            sharemethods.upload_to_bucket(os.path.join(folder_name, blob), path, bucket)
        except Exception as e:
            print('Error when uploading. Make sure info is correct and try again.')
            upload_ask()

def download_ask():
    print()
    download_upload = input('Would you like to download a file? y/n ')
    print()
    if download_upload == 'y':
        bucket = input('From which bucket? ')
        print()
        #try to show the buckets and available files in each
        folder = input('Is this in another folder? y/n ')
        #define directory variable for possible subdirectory
        directory = ''
        if folder=="y":
            print()
            directory = input('What is the path to the folder? ')
        print()
        file = input('Which file would you like to download? ')
        print()
        #make sure format is right
        path = input('Which directory would you like to download the file to? ')
        print()
        sharemethods.download_files(os.path.join(directory, file), os.path.join(path, file), bucket)

upload_ask()