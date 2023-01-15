import boto3

# AWS credentials and region for your specific account
aws_access_key_id = 'your-access-key' # <-- enter your access key id
aws_secret_access_key = 'your-secret-key' # <-- enter your secret access key
region_name = 'your-region' # <-- enter the region you are in

# connecting to dynamodb client
dynamodb = boto3.client('dynamodb',
                       aws_access_key_id=aws_access_key_id,
                       aws_secret_access_key=aws_secret_access_key,
                       region_name=region_name)

# function that will add the items to the table
def add_item(brand, price):
    table_name = 'your_table_name' #<-- enter the table name you created
    try:
        response = dynamodb.put_item(
            TableName=table_name,
            Item={
                'brand': {'S': brand},
                'price': {'N': price}
            }
        )
        print("Item added:", brand, price)
    except Exception as e:
        print("Error adding item:", e)

# Items that I am adding
add_item("Davidoff Aniversario Series", "20") # <-- you can swap out my information for whatever you want to add as in items
add_item("Padron Anniversary Series 1964", "14")
add_item("Ferio Tego Timeless Panamericana", "13")
add_item("Davidoff Aniversario Short Perfecto", "20")
add_item("Foundation Highclere Castle Churchill", "15")
add_item("Tatuaje Tattoo Series", "5")
add_item("The Texas Lancero by Alec Bradley", "10")
add_item("7-20-4 The Hustler", "6")
add_item("Ferio Tego Timeless Sterling", "11")
add_item("Ashton Estate Sun Grown", "23")
