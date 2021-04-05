import boto3
import json
import os

region_name = os.getenv('Region')
source_table_name = os.getenv('Source_Table')
target_table_name = os.getenv('Target_Table')
dyndb = boto3.resource('dynamodb', region_name=region_name)


def lambda_handler(event, context):

    print("From table: " + source_table_name)
    print("To table: " + target_table_name)
    source_table_items = fetchRecords(source_table_name)
    insertRecords(source_table_items, target_table_name)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Table is copied.",
        }),
    }


def fetchRecords(source_table_name):

    try:

        source_table = dyndb.Table(source_table_name)
        response = source_table.scan()
        source_table_items = response['Items']

        while response.get('LastEvaluatedKey', False):
            response = source_table.scan(
                ExclusiveStartKey=response['LastEvaluatedKey'])
            source_table_items.extend(response['Items'])

        return source_table_items

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise e


def insertRecords(source_table_items, target_table_name):

    target_table = dyndb.Table(target_table_name)

    for item in source_table_items:
        try:
            response = target_table.put_item(
                Item=item
            )
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise e
