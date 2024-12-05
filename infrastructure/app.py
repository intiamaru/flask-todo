#!/usr/bin/env python3
from aws_cdk import App, Stack, aws_ec2 as ec2, aws_iam as iam, CfnOutput
from constructs import Construct

class TodoAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC with only public subnets
        vpc = ec2.Vpc(self, "TodoAppVPC",
            max_azs=2,
            nat_gateways=0,  # Remove NAT Gateway
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                )
            ]
        )

        # Create security group for EC2 instance
        security_group = ec2.SecurityGroup(self, "TodoAppSecurityGroup",
            vpc=vpc,
            description="Security group for Todo App EC2 instance",
            allow_all_outbound=True
        )

        security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP traffic"
        )

        security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH traffic"
        )

        # Create IAM role for EC2 instance
        role = iam.Role(self, "TodoAppInstanceRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore")
        )

        # Import the public key
        with open("todo-app-key.pub", "r") as key_file:
            public_key = key_file.read().strip()

        # Create key pair
        key_pair = ec2.CfnKeyPair(self, "TodoAppKeyPair",
            key_name="todo-app-key",
            public_key_material=public_key
        )

        # Create EC2 instance
        instance = ec2.Instance(self, "TodoAppInstance",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=security_group,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.generic_linux({
                "us-east-1": "ami-0c7217cdde317cfec"  # Ubuntu 22.04 LTS in us-east-1
            }),
            role=role,
            key_name="todo-app-key",
            user_data=ec2.UserData.custom('''#!/bin/bash
# Clone the repository
git clone https://github.com/intiamaru/flask-todo.git /home/ubuntu/flask-todo
chown -R ubuntu:ubuntu /home/ubuntu/flask-todo

# Run the setup script
cd /home/ubuntu/flask-todo
chmod +x deploy/setup.sh
./deploy/setup.sh
''')
        )

        # Output the instance public IP
        CfnOutput(self, "InstancePublicIP",
            value=instance.instance_public_ip,
            description="Public IP address of the EC2 instance"
        )

app = App()
TodoAppStack(app, "TodoAppStack")
app.synth() 