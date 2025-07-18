# List of code response
    "ResultsByTime": [
        {
            "TimePeriod": {
                "Start": "2025-07-01",
                "End": "2025-07-02"
            },
            "Total": {
                "UnblendedCost": {
                    "Amount": "4.5",
                    "Unit": "USD"
                }
            },
            "Groups": [],
            "Estimated": true
        },


```
import json
import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    client= boto3.client('ce')
    start= '2025-06-01'
    today= datetime.utcnow().date()
    todayplusone= today + timedelta(days=1)

    response= client.get_cost_and_usage(
        TimePeriod={
        'Start': str(start),
        'End': str(todayplusone)
    },
    Granularity= 'DAILY',
    Metrics= ['UnblendedCost']
    )
    total=0.0
    for items in response['ResultsByTime']:
        try:
            per_day_cost= items['Total']['UnblendedCost']['Amount']
            total += float(per_day_cost)
        except (KeyError, TypeError):
            pass
    return {
        'statusCode': 200,
        'body': json.dumps(f"Total AWS cost is ${total}")
    }
```
