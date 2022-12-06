import uuid
import pandas as pd
import boto3


dynamodb = boto3.client('dynamodb')
table = "mock-spur-database"

api_datasets = [
        "accounts-domains",
        "accounts",
        "associated-domains",
        "infrastructure-devices",
        "infrastructure-domains-activesubdomains-ports",
        "infrastructure-reputations",
        "runtime-requests",
        "subdomains"
]

for dataset in api_datasets:
    data = "resources/example_sanitized_data/raw_api_data/"+dataset+".json"
    df = pd.read_json(data)
    data_dump = df.to_json(orient="records")
    prefix = dataset.replace("-", "/");
    id = uuid.uuid4().hex
    response = dynamodb.put_item(TableName=table, Item={"id":{"S": id}, 
                                                        "table":{"S": table}, 
                                                        "prefix":{"S": prefix}, 
                                                        "data": {"S": data_dump}})
      
    '''
    >>> json_data = json.loads(data_dump)
        payload = {
                "id": id,
                "table": table,
                "prefix": prefix,
                "data": json_data
    >>>       }
    >>> data_set = JSONDataSet()
    >>> data_set.save(payload)
    >>> reloaded = data_set.load()
    >>> assert payload == reloaded

    >>> response = dynamodb.get_item(
    >>>     TableName=table,
    >>>     Key={
    >>>        'prefix': {
    >>>            'S' : 'infrastructure/reputations'           
    >>>       }
    >>>    }
    >>> )
    >>> print(response["Item"])
    
    '''
    






