from os import name
import boto3
import time

def launchInfra():
    # Create client for EC2
    client = boto3.client("ec2")

    # Running the instance
    print("Launching EC2 Instance...")
    instance = client.run_instances(
        ImageId = "ami-0ad704c126371a549",
        InstanceType = 't2.micro',
        KeyName = 'hadoop',
        MaxCount = 1,
        MinCount = 1

    )
    # Waiting for instance to get ready for attaching volume
    print("Preparing...")
    time.sleep(30)

    # suffix for device name while attaching the volume
    var = ['f', 'g', 'h', 'i', 'j']

    # Creating and attaching the volume
    # Total 5 volumes will be created because 5 elements are there in list
    print("Creating and attaching volumes...")
    for i in var:
        # Creating the Volume
        ebsResponse = client.create_volume(
            # Fetching the AZ name same as instance
            AvailabilityZone = instance['Instances'][0]['Placement']['AvailabilityZone'],
            Size = 1,
            TagSpecifications = [
                {
                    'ResourceType' : 'volume',
                    'Tags' : [
                        {
                            'Key' : 'Name',
                            'Value' : 'python-script'
                        }
                    ]
                }
            ]
        )
        time.sleep(5)

        # Attaching the colume
        attachResponse = client.attach_volume(
            Device = '/dev/sd'+ i,
            VolumeId = ebsResponse['VolumeId'],
            InstanceId = instance['Instances'][0]['InstanceId']
        )

    print("Deployment Completed!")

