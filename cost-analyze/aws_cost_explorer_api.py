import boto3
import json

# importing cost explorer client to query on the AWS Account
cost_client= boto3.client('ce')
ec2_client= boto3.client('ec2')

cost_response= cost_client.get_cost_and_usage(
    TimePeriod= {
        'Start': "2025-04-01",
        'End': "2025-04-26"
    },
    Granularity='MONTHLY',
    # Filter={
    #     "Tags": {
    #         "Key": "cost_management",
    #         "Values": ["ec2"]
    #     }
    # },
    Metrics= [
        'UnblendedCost'
    ],
    # GroupBy=[
    #     {
    #         'Type': 'TAG',
    #         'Key': 'cost_management'
    #     }
    # ]
)

# Get Instance ID with tag as cost_management : ec2
ec2_response= ec2_client.describe_instances()
for resevation in ec2_response['Reservations']:
    for instances in resevation['Instances']:
        tags= instances.get('Tags', [])
        if any(tag['Key'] == 'cost_management' for tag in tags):
            print("Instance ID --> ", instances['InstanceId'])


print(json.dumps(cost_response, indent=4))
