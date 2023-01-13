import boto3

# create a session with your AWS credentials
session = boto3.Session(
    aws_access_key_id='your-access-key', # <-- this will be your specific access key ID for your AWS account
    aws_secret_access_key='your-secret-key', # <-- this is your specific secret key for your AWS account
    region_name='your-region' # <-- Enter your specific region as not everyones is the same
)

# create an EC2 client using the session
ec2 = session.client('ec2')

# get all instances
response = ec2.describe_instances()

# get the instance ID of all instances
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        print("Instance ID:", instance_id)
