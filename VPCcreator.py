import boto3

# Get the region from the user
region = input('Enter your desired region ("us-east-1"): ')

# Create a boto3 client for Amazon VPC in the specified region
client = boto3.client('ec2', region_name=region)

# Define the VPC settings
vpc_cidr_block = '10.0.0.0/16'

# Create the VPC
try:
    response = client.create_vpc(CidrBlock=vpc_cidr_block)
    vpc_id = response['Vpc']['VpcId']
    # Enable DNS hostnames for the VPC
    client.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
    client.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})
    print(f'VPC created with ID: {vpc_id} in {region} region')
except Exception as e:
    print(e)

    

