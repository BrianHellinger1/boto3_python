import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Define the name of the bucket and the file to be deleted
bucket_name = 'fake-bucke-name' # This is a fake bucket name, You will need to insert you're bucket name 
file_name = 'boto3_python/S3Search.py'

# Delete the file
s3.delete_object(Bucket=bucket_name, Key=file_name)

print(f'Successfully deleted {file_name} from {bucket_name}')
