import boto3

# connect to the EC2 service
ec2 = boto3.client('ec2')

# specify the ID of the EBS snapshot you want to describe
snapshot_id = 'your-snap-id-#'

# describe the EBS snapshot
response = ec2.describe_snapshots(SnapshotIds=[snapshot_id])

# print the response
print(response)

