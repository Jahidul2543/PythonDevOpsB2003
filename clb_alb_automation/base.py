import boto3
import json
import logging

from botocore.exceptions import ClientError

"""

1. Get instance/s ID --> ec2
2. Start the instance
3. Register instances to CLB


"""

ec2_client = boto3.client('ec2')
elb = boto3.client('elb')
instance_id_list = []


def register_instance(instanceid_list):
    list_of_instance_id = []
    count = 0
    while count < len(instanceid_list):
        list_of_instance_id.append(
            {
                'InstanceId': instanceid_list[count]
            }
        )
        count = count + 1

    response = elb.register_instances_with_load_balancer(
        LoadBalancerName='demo-clb',
        Instances=list_of_instance_id
    )

    logging.info('Register Instance to CLB response: {}'.format(response))
    return response


def de_register_instance(instanceid_list):
    count = 0
    while count < len(instanceid_list):
        response = elb.deregister_instances_from_load_balancer(
            LoadBalancerName='demo-clb',
            Instances=[
                {
                    'InstanceId': instanceid_list[count]
                },
            ]
        )
        count = count + 1

    # logging.info('De-Resgister from CLB instances action response: {}'.format(response))
    return response


def start_instances(instanceid_list):
    # Do a dryrun first to verify permissions
    try:
        ec2_client.start_instances(InstanceIds=instanceid_list, DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            logging.error(e)
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2_client.start_instances(InstanceIds=instanceid_list, DryRun=False)
        logging.info('Instance start action response: {}'.format(response))
    except ClientError as e:
        logging.error(e)

    return response


def stop_instances(instanceid_list):
    # logging.info('***Stop instances with tag Key {} & value {}***'.format(tag_name, tag_value))
    # Do a dryrun first to verify permissions
    try:
        ec2_client.stop_instances(InstanceIds=instanceid_list, DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            logging.exception(e)
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2_client.stop_instances(InstanceIds=instanceid_list, DryRun=False)
        logging.info(response)
    except ClientError as e:
        logging.error(e)

    return response


def get_list_of_instances_by_tag(instance_state):
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    'Peak',
                ]
            },
            {
                'Name': 'instance-state-name',
                'Values': [
                    instance_state.lower(),
                ]
            },
        ]
    )
    # print(json.dumps(response, indent=4))
    print(response)
    # Process response to get instances id
    total_instances = len(response.get('Reservations')[0].get('Instances'))
    count = 0
    while count < total_instances:
        instance_id = response.get('Reservations')[0].get('Instances')[count].get('InstanceId')
        instance_id_list.append(instance_id)

        count = count + 1

    print(instance_id_list)


def lambda_handler():
    get_list_of_instances_by_tag('Running')
    response = de_register_instance(instance_id_list)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


# get_list_of_instances_by_tag('Running')
# start_instances(instance_id_list)
# register_instance(instance_id_list)
# de_register_instance(instance_id_list)
# stop_instances(instance_id_list)
