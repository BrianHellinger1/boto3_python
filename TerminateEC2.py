import boto3

# Create a session with your AWS credentials
session = boto3.Session(
    aws_access_key_id='your-access-key-id', # <-- this is your specific access key for your AWS account
    aws_secret_access_key='your-secret-key', # <-- this is your specific secret access key for your AWS account
    region_name='your-region' # <-- this is your specific region 
)

# Create an EC2 client using the session
ec2 = session.client('ec2')

# Specify the ID of the instance that you want to terminate
instance_id = 'your-ec2-instance-id' # <-- this will be your specific ec2 instance ID. You can find your ID either in the AWS console or using a script

# Terminate the instance
response = ec2.terminate_instances(InstanceIds=[instance_id])

# Print the response
print(response)

