import boto3
ec2_client=boto3.client("ec2")

ec2_client.create_snapshot( Description='snapshot from basevolume using python',
      VolumeId='your-volume-Id') # <-- Enter your EC2 Volume ID