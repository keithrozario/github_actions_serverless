import json

def hello(event, context):
    
    name = event.get('name', "Luke")

    body = {
        "message": f"Use the force {name}"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "name": name
    }

    return response

def goodbye(event, context):

    name = event.get('name', 'Luke')

    body = {
        "message": f"No {name}, I am your father!!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "name": name
    }

    return response

    