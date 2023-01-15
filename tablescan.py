import boto3

# AWS credentials and region
aws_access_key_id = 'your-access-key'# <-- enter your specific information
aws_secret_access_key = 'your-secret-key' # <-- enter your specific information
region_name = 'your-region'

# connecting to DynamoDB
dynamodb = boto3.client('dynamodb',
                       aws_access_key_id=aws_access_key_id,
                       aws_secret_access_key=aws_secret_access_key,
                       region_name=region_name)

# the function to scan the table
def scan_table(table_name):
    try:
        response = dynamodb.scan(TableName=table_name)
        items = response['Items']
        print("Table scanned successfully. Items:")
        for item in items:
            print(item)
    except Exception as e:
        print("Error scanning table:", e)


scan_table('your_table_name') # <-- enter your table name 

