import boto3
import json
from datetime import datetime, timedelta
from datetime import date

# importing cost explorer client to query on the AWS Account
cost_client= boto3.client('ce')
ec2_client= boto3.client('ec2')

# Fetch the date on which the script is running
today = date.today()
first_of_this_month = today.replace(day=1)

# Dates for previous month
previous_month_last_day = first_of_this_month - timedelta(days=1)
previous_month_starting_date = previous_month_last_day.replace(day=1)

start_date= f"{first_of_this_month}"
end_date= f"{today}"

# Current month, at the time script is running
current_month= today.month
previous_month= previous_month_last_day.month

# Iterate this dictionary for fetching cost of current month and previous month based on start and end date
dates_array=[
    {
        "start": start_date,
        "end": end_date,
    },
    {
        "start": previous_month_starting_date,
        "end": previous_month_last_day
    }
]

for dates in dates_array:
    cost_response= cost_client.get_cost_and_usage(
        TimePeriod= {
            'Start': str(dates["start"]),
            'End': str(dates["end"])
        },
        Granularity='MONTHLY',
        Filter={
            "Tags": {
                "Key": "cost_management",
                "Values": ["ec2"]
            }
        },
        Metrics= [
            'UnblendedCost'
        ],
    )
    # Print the cost for the EC2 Service for present and previous month
    print("The cost of the EC2 Service is -->", cost_response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"])



# Get Instance ID with tag as cost_management : ec2
ec2_response= ec2_client.describe_instances()
for resevation in ec2_response['Reservations']:
    for instances in resevation['Instances']:
        tags= instances.get('Tags', [])
        if any(tag['Key'] == 'cost_management' for tag in tags):
            print("Instance ID --> ", instances['InstanceId'])


# print(json.dumps(cost_response, indent=4))
