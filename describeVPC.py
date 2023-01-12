import boto3

# Create a session with the user-specified region
session = boto3.Session(region_name=input('Enter your region ("us-east-1"): '))

# Create an EC2 client using the session
ec2 = session.client('ec2')

# Describe the specified VPC and store the response
vpc = ec2.describe_vpcs(VpcIds=[input('Enter the VPC Id: ')])['Vpcs'][0]

# Print the details of the VPC
print(f'VPC ID: {vpc["VpcId"]}')
print(f'VPC CIDR: {vpc["CidrBlock"]}')
print(f'VPC Is Default: {vpc["IsDefault"]}')
print(f'VPC State: {vpc["State"]}')
print(f'VPC DHCP options ID: {vpc["DhcpOptionsId"]}')

