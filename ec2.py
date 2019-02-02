import boto3
try:
    ec2 = boto3.resource('ec2', region_name='ap-south-1') #here we have to give region name not availability-zone 
    subnet = ec2.Subnet('subnet-01f9b969')
    instances = subnet.create_instances(ImageId='ami-5b673c34', InstanceType='t2.micro', MaxCount=1, MinCount=1, KeyName='first', SecurityGroups=[], SecurityGroupIds=['sg-0520185bc4a3343922'])
   
    print(instances)


except BaseException as exe:
	print(exe) 


