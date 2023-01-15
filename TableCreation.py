import boto3

# AWS credentials for you're profile
access_key = "your-acces-key" # <-- enter your specific AWS Access key
secret_key = "your-secret-key" # <-- enter your specific AWS Secret key
region = "your-region"

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)

# connecting to DynamoDB
dynamodb = session.resource('dynamodb')

# create the table
table = dynamodb.create_table(
    TableName='Cigars_of_2022', # <-- Name the table to you're liking. 
    KeySchema=[
        {
            'AttributeName': 'brand', # <-- you can change this to whatever you want
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'price', # <-- you can change this to whatever you want
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'brand', # <-- you can change this to whatever you want
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'price', # <-- you can change this to whatever you want
            'AttributeType': 'N'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


# print message
print("Table Created!") # <-- you can add any message you would like

