#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3

ec = boto3.resource('ec2')

for instance in ec.instances.all():
    print instance.id
