import boto3

# dynamoDB client
client = boto3.client('dynamodb',
    aws_access_key_id='your-access-id',
    aws_secret_access_key='your-secret-key',
    region_name='REGION'
)

# enter the table name
table_name = 'your-table-name'

# enter the item key
key = {'primary_key': {'S': 'value'}}

# delete the item
response = client.delete_item(TableName=table_name, Key=key)

# print a message to verify that the item was deleted
print(f'Item with key {key} was deleted from table {table_name}')

