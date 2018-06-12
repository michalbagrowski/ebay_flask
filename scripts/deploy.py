import boto3

region = "eu-west-1"
profile = "michalbagrowski"
service = "flask"
cluster = "puppy"

SESSION = boto3.Session(profile_name = profile)
client = SESSION.client('ecs', region_name = region)

version = open("VERSION","r").read()

service_name = service + "-" + region
cluster_name = cluster + "-" + region
container_name = service + "-" + region

task_definition = {
    "family": service_name,
    "containerDefinitions": [
        {
            "name": container_name,
            "image": "206636293913.dkr.ecr.eu-west-1.amazonaws.com/flask-eu-west-1:"+version,

            "memory": 100,
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-region": "eu-west-1",
                    "awslogs-group": "puppy",
                    "awslogs-stream-prefix": "/aaa"
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
    "executionRoleArn": "arn:aws:iam::206636293913:role/puppy-eu-west-1-execution-role"
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
            "subnets": ["subnet-0876107e","subnet-a07fcbf8","subnet-2883e94c"],
            "securityGroups": ["sg-56889f31"],
            'assignPublicIp': "ENABLED"
        }
    },
    "loadBalancers" : [
        {
            "targetGroupArn": "arn:aws:elasticloadbalancing:eu-west-1:206636293913:targetgroup/puppy-eu-west-1/309b7584ae8f6304",
            "containerName": service_name,
            "containerPort": 80
        }
    ]
}

service_update = {
    "cluster": cluster_name,
    "service": service_name,
    "desiredCount": 1,
    "taskDefinition": task_definition["taskDefinition"]["taskDefinitionArn"],
    "networkConfiguration": {
        "awsvpcConfiguration": {
            "subnets": ["subnet-0876107e","subnet-a07fcbf8","subnet-2883e94c"],
            "securityGroups": ["sg-56889f31"],
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
