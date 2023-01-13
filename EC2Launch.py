import boto3

# create a session with your AWS credentials
session = boto3.Session(
    aws_access_key_id='your-access-key', # <-- this is your specific key ID for your AWS account
    aws_secret_access_key='your-secret-key', # <-- this is your specific secret key for your AWS account
    region_name='your-region' # <-- this is whatever region you are in, Not everyone is in the same region
)

# create an EC2 client using the session
ec2 = session.client('ec2')

# specify the ID of the Amazon Machine Image (AMI) that you want to use
ami_id = 'ami-0b5eea76982371e91' # <-- this is for the Amazon linux 2. You can copy and paste whatever AMI you would like

# specify the instance type that you want to use
instance_type = 't2.micro' # <-- this is the free tier instance type. We like FREE!

# specify the key pair that you want to use to log in to the instance
key_pair_name = 'your-key-pair' # <-- you will put in you're specific keypair

# create the instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_pair_name,
    MinCount=1,
    MaxCount=1
)

# get the instance ID of the instance that was launched
instance_id = response['Instances'][0]['InstanceId']

# print the instance ID
print('Instance ID:', instance_id)
