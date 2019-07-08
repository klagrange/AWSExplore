import boto3
from boto3.dynamodb.conditions import Key, Attr

class MyStorage:
    DYNAMODB = boto3.resource('dynamodb', region_name='ap-southeast-1')
    TABLE = DYNAMODB.Table('automl-api')

    def store(self, content: {}):
        response = self.TABLE.put_item(
            Item={
                'uuid': '2',
                **content
            }
        )
        return response

    def retrieve(self, uuid: str):
        results = self.TABLE.query(
            KeyConditionExpression=Key('uuid').eq(uuid)
        )
        return results['Items']

myStorage = MyStorage()

# response = myStorage.store({'a': 'a'})
# print(response)

retrieved = myStorage.retrieve('3')
print(retrieved)