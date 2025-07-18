import boto3
import json
from datetime import datetime, timedelta

client = boto3.client('ce')

today= datetime.utcnow().date()
# start= today.replace(day=1)
start= "2025-06-01"
todayplusone= today + timedelta(days=1)

# print(f"Start date is {start}")
# print(f"End date is {todayplusone}")
# print(f"Today is {today}")

try:
    response= client.get_cost_and_usage(
        TimePeriod={
            'Start': str(start),
            'End': str(todayplusone)
        },
        Granularity= 'DAILY',
        Metrics= ['UnblendedCost']
    )
    pretty_response = json.dumps(response, indent=4)
    # print(pretty_response)
    total=0.0
    for items in response['ResultsByTime']:
        try:
            per_day_cost= items['Total']['UnblendedCost']['Amount']
            total += float(per_day_cost)
        except (KeyError, TypeError):
            pass
    if total != 0.0:
        print(f"Total AWS cost till {today} is ${total}")
    # for item in response['ResultsByTime']:
    #     if item['TimePeriod']['Start'] <= today < item['TimePeriod']['End']:
    #         todays_cost= float(item["Total"]["UnblendedCost"]["Amount"])
    #         break
    #     else:
    #         todays_cost= 0.0
except Exception as e:
    print(f"Script not executed!! Error message: ${e}")
