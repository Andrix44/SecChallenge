import random
import base64
import time
import uuid

with open("aws.txt", 'r') as f:
    lines = f.readlines()

with open("contracts.txt", 'w') as of:
    for line in lines:
        if(random.randrange(10) > 3): # fake objects
            fake_timestamp = int(time.time()) - random.randrange(7776000)
            fake_signature = base64.urlsafe_b64encode(bytes.fromhex("%040x" % random.randrange(16**40))).replace(b"=", b"%3d").decode()
            of.write(f"https://instant-development-company.s3.eu-central-1.amazonaws.com/{uuid.uuid4()}?AWSAccessKeyId=OKGLRFFMPMS3RROZG3MQ&Expires={fake_timestamp}&Signature={fake_signature}\n")

        fake_timestamp = int(time.time()) - random.randrange(7776000)
        fake_signature = base64.urlsafe_b64encode(bytes.fromhex("%040x" % random.randrange(16**40))).replace(b"=", b"%3d").decode()
        of.write(line.strip() + f"?AWSAccessKeyId=OKGLRFFMPMS3RROZG3MQ&Expires={fake_timestamp}&Signature={fake_signature}\n")