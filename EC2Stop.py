import boto3

# create a session with your AWS credentials
session = boto3.Session(
    aws_access_key_id='your-access-key', # <-- this is your specific access key id for your AWS account
    aws_secret_access_key='your-secret-key', # <-- this is your specific secret access key for your AWS account
    region_name='your-region' # <-- this will be your specific region you are in
)

# create an EC2 client using the session
ec2 = session.client('ec2')

# specify the ID of the instance that you want to stop
instance_id = 'your-EC2-ID' # <-- you will need to get the EC2 instance id from the console inside the EC2 services or create a script that will do that for you

# stop the instance
response = ec2.stop_instances(InstanceIds=[instance_id])

# print the response
print(response)

