import json
import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    client= boto3.client('ce')
    start= '2025-06-01'
    today= datetime.utcnow().date()
    yesterday= today - timedelta(days=1)
    todayplusone= today + timedelta(days=1)

    response= client.get_cost_and_usage(
        TimePeriod={
        'Start': str(start),
        'End': str(todayplusone)
    },
    Granularity= 'DAILY',
    Metrics= ['UnblendedCost']
    )
    latest_cost= 0.0
    for items in response['ResultsByTime']:
        if items['TimePeriod']['Start'] == yesterday:
            latest_cost= items['Total']['UnblendedCost']['Amount']
    print(f"Cost for {yesterday} is ${latest_cost}")
