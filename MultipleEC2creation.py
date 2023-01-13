import boto3

# create a session with your AWS credentials
session = boto3.Session(
    aws_access_key_id='your-access-key-id', # <-- This is your specific access key for your AWS account
    aws_secret_access_key='your-secret-key', # <-- This is your specific secret access key for your AWS account
    region_name='your-region' # <-- this will be your specific region you are in 
)

# create an EC2 client using the session
ec2 = session.client('ec2')

# specify the ID of the Amazon Machine Image (AMI) that you want to use, This is the amazon linux 2 you will need to choose which AMI you want
ami_id = 'ami-0b5eea76982371e91'

# specify the instance type that you want to use, This is the free tier. We like FREE!
instance_type = 't2.micro'

# specify the key pair that you want to use to log in to the instance, This is your specific keypair
key_pair_name = 'your-keypair' # <-- this is your specific keypair

# specify the number of instances you want to launch, You can pick any specific number you would like. I only choose 2x so I can create more then 1x
instance_count = 2

# create the instances
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_pair_name,
    MinCount=instance_count,
    MaxCount=instance_count
)

# get the instance IDs of the instances that were launched
instance_ids = [instance['InstanceId'] for instance in response['Instances']]

# print the instance IDs
print('Instance IDs:', instance_ids)
