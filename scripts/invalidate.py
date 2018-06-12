import boto3
import sys
import time
region = sys.argv[2]
profile = "michalbagrowski"
service = "flask"
cluster = "puppy"

SESSION = boto3.Session(profile_name = profile)
client = SESSION.client('cloudfront', region_name = region)


client.create_invalidation(
    DistributionId =sys.argv[1],
    InvalidationBatch = {
        'Paths': {
            "Quantity": 1,
            "Items": [
                "/*"
            ]
        },
        "CallerReference": str(time.time())
    }
)
