import boto3
import requests
import sys

# s3bucket = 'dev-lambda-alias'

def list_s3_objects(s3bucket, region):
    s3 = boto3.client('s3')

    print(f"We're echoing region: {region}")

    try:
        # List objects in the specified bucket
        response = s3.list_objects_v2(Bucket=s3bucket)
        
        if 'Contents' in response:
            print(f"Objects in bucket '{s3bucket}':")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"The bucket '{s3bucket}' is empty or does not exist.")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    s3bucket = sys.argv[1]
    region = sys.argv[2]
    print(f"Passed in bucket name: {s3bucket}. Region is {region}")
    list_s3_objects(s3bucket, region)
