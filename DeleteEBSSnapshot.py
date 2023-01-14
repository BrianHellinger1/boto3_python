import boto3
ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='your-snap-Id-#') # <-- Enter your specific snapId #
