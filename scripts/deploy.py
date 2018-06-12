import boto3
import sys

region = sys.argv[1]
profile = "michalbagrowski"
service = "flask"
cluster = "puppy"
aws_account ="206636293913"
SESSION = boto3.Session(profile_name = profile)
client = SESSION.client('ecs', region_name = region)

version = open("VERSION","r").read()

service_name = service + "-" + region
cluster_name = cluster + "-" + region
container_name = service + "-" + region
config = {
    "us-east-1": {
        "subnets": [
            "subnet-6432eb2d",
            "subnet-9062db9c",
            "subnet-8678e9e3",
            "subnet-5b806d67",
            "subnet-7ce20b51",
            "subnet-2bcf2070"
        ],
        "securityGroups": [
            "sg-d3f492a9"
        ],
        "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:206636293913:targetgroup/puppy-us-east-1/f7f51f7050177ad2"

    },
    "eu-west-1": {
        "subnets": [
            "subnet-0876107e",
            "subnet-a07fcbf8",
            "subnet-2883e94c"
        ],
        "securityGroups": [
            "sg-56889f31"
        ],
        "targetGroupArn": "arn:aws:elasticloadbalancing:eu-west-1:206636293913:targetgroup/puppy-eu-west-1/309b7584ae8f6304"
    }
}

task_definition = {
    "family": service_name,
    "containerDefinitions": [
        {
            "name": container_name,
            "image": aws_account+".dkr.ecr."+region+".amazonaws.com/flask-"+region+":"+version,
            "memory": 100,
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-region": region,
                    "awslogs-group": "puppy-"+region,
                    "awslogs-stream-prefix": "fargate"
                }
            },
            "portMappings": [{
                "containerPort": 80,
                "hostPort": 80,
                "protocol": "tcp"
            }]
        }
    ],
    "requiresCompatibilities": ["FARGATE"],
    "networkMode": "awsvpc",
    "cpu": "256",
    "memory": "512",
    "executionRoleArn": "arn:aws:iam::"+aws_account+":role/puppy-"+region+"-execution-role"
}

task_definition = client.register_task_definition(**task_definition)

service = {
    "cluster": cluster_name,
    "serviceName": service_name,
    "desiredCount": 1,
    "taskDefinition": task_definition["taskDefinition"]["taskDefinitionArn"],
    "launchType": "FARGATE",
    "networkConfiguration": {
        "awsvpcConfiguration": {
            "subnets": config[region]["subnets"],
            "securityGroups": config[region]["securityGroups"],
            'assignPublicIp': "ENABLED"
        }
    },
    "loadBalancers" : [
        {
            "targetGroupArn": config[region]["targetGroupArn"],
            "containerName": service_name,
            "containerPort": 80
        }
    ]
}
print(service)
service_update = {
    "cluster": cluster_name,
    "service": service_name,
    "desiredCount": 1,
    "taskDefinition": task_definition["taskDefinition"]["taskDefinitionArn"],
    "networkConfiguration": {
        "awsvpcConfiguration": {
            "subnets": config[region]["subnets"],
            "securityGroups": config[region]["securityGroups"],
            'assignPublicIp': "ENABLED"
        }

    }
}

cluster_services = client.describe_services(
    cluster = cluster_name,
    services = [service_name]
)
print(cluster_services)
if cluster_services["failures"] or cluster_services["services"][0]["status"] == "INACTIVE":
    client.create_service(**service)
else:
    client.update_service(**service_update)
