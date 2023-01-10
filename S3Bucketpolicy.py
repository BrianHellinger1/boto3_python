import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Set the name of the bucket for which you want to get the policy
bucket_name = 'my-bucket'

# Call the get_bucket_policy method to get the policy of the bucket
response = s3.get_bucket_policy(Bucket=bucket_name)

# Get the policy as a string
policy = response['Policy']

# Print the policy, You will need Acces to print the policy for the s3 bucket
print(policy)

