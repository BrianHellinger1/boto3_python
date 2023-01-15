import boto3

# dynamoDB resource
dynamodb = boto3.resource('dynamodb',
    aws_access_key_id='ACCESS_KEY',
    aws_secret_access_key='SECRET_KEY',
    region_name='REGION'
)

# enter the table name
table_name = 'your-table-name'

# get the table
table = dynamodb.Table(table_name)

# delete table
table.delete()

# print the table status
print(f'Table {table_name} was deleted')
