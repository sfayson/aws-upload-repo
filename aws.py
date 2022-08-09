
import data_access_s3
import boto3


def main():
    # Upload
    print(data_access_s3.upload_to_s3(upload-file-stu10.txt, 'siu-avb-bucket', object_name=None))

    # Download
    print(data_access_s3.download_from_s3('siu-avb-bucket', 'OBJECT_NAME', 'download-file.txt'))


if __name__ == '__main__':   # dunder
    main()
