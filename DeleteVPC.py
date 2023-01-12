import boto3

# Create a session with the user-specified region
session = boto3.Session(region_name=input('Enter your region ("us-east-1"): '))

# Create an EC2 client using the session
ec2 = session.client('ec2')

# Get the VPC Id from the user
vpc_id = input('Enter the VPC Id: ')

# Delete the specified VPC
try:
    ec2.delete_vpc(VpcId=vpc_id)
    print(f'Deleted VPC with id {vpc_id}')
except Exception as e:
    print(e)
