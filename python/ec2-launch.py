#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3

ec2 = aws.resource('ec2', region_name='my-region-1')

ec2.create_instances(
     ImageId="my-ami-image-id",
     MinCount=1,  # I want exactly 1 server
     MaxCount=1,
     KeyName='my-ssh-key',
     SecurityGroupIds=['my-security-group'],
     UserData=myStartupScript, # script that will start when server starts
     InstanceType='t2.nano',
     SubnetId="my-subnet-id",
     DisableApiTermination=True,
     PrivateIpAddress='10.0.0.1',
)
