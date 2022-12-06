# CTS MOCK SPUR API

## DATA

### Data PUT

For batching and simplificty:

Run python file in here with latest example_sanitized_data from [example_sanitized_data](https://github.com/McK-Private/cyber-cts/tree/main/example_sanitized_data) :

- `pandas/src/df_util.py`

Alternative PUT Example:

    ```python
        import requests
        import json

        url = "https://wsr20n28fh.execute-api.us-east-1.amazonaws.com/cts-serverless-lambda-stage/v1/runtimerequests"

        payload = json.dumps({
        "table": "mock-spur-database",
        "prefix": "runtimerequests",
        "id": "7a551f7558b84aabbac046b62c4e84f1",
        "data": "[{\"algorithm\":\"SHA256\",\"value\":\"xyzd78efa5960b5354e119470b2ce3bbeb18c6299ba129597618fa9fc3638da6\"},{\"algorithm\":\"SHA256\",\"value\":\"15d678efa5960b5354e119470b2ce3bbeb18c6299ba129597618fa9fc3638da6\"},{\"algorithm\":\"SHA256\",\"value\":\"f2f1f51ffda8662e76fcceb5119ed0ece97d5ccb3bfb59f3102728daad84d9c2\"}]"
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

    ```

Refer to ${specified_proxy} options to put all records

### Data GET

GET all results:

    ```python
        import requests

        url = "https://wsr20n28fh.execute-api.us-east-1.amazonaws.com/cts-serverless-lambda-stage/v1/"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    ```

GET ${specified_proxy} records:

    ```python
        import requests

        url = "https://wsr20n28fh.execute-api.us-east-1.amazonaws.com/cts-serverless-lambda-stage/v1/${specified_proxy} "

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)


    ```


    ### Data DELETE

    ```python

    import requests

    url = "https://wsr20n28fh.execute-api.us-east-1.amazonaws.com/cts-serverless-lambda-stage/v1/infrastructure/devices?id=c1d4d69c878c4facbfd7969990baa812"

    payload={}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)


    ```

${specified_proxy} options:

    ```text

        - accounts/domains
        - accounts
        - associated/domains
        - infrastructure/devices
        - infrastructure/domains/activesubdomains/ports
        - infrastructure/reputations
        - runtimerequests
        - subdomains 


    ```
