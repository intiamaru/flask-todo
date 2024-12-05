# Flask Todo App Infrastructure

This directory contains the AWS CDK code to deploy the Flask Todo application infrastructure.

## Infrastructure Components

- VPC with public subnets in 2 availability zones
- EC2 instance (t2.micro) in a public subnet
- Security group allowing HTTP (80) and SSH (22) access
- IAM role for EC2 instance with SSM access
- Automatic application deployment using user data script

## Prerequisites

1. AWS CLI installed and configured with appropriate credentials
2. Python 3.9 or higher
3. AWS CDK CLI installed (`npm install -g aws-cdk`)
4. Your Flask Todo app code in a Git repository

## Deployment Steps

1. Update the Git repository URL in `app.py`:
   ```python
   git clone https://github.com/your-username/flask-todo.git
   ```

2. Install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Deploy the stack:
   ```bash
   cdk deploy
   ```

4. After deployment, you'll see the EC2 instance's public IP in the outputs.

## Useful Commands

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk destroy`     destroy the stack

## Security Considerations

- The EC2 instance is placed in a public subnet with direct internet access
- SSH access is allowed from any IP (you may want to restrict this)
- HTTP traffic is allowed from any IP
- The instance has an IAM role with SSM access for easier management

## Cost Considerations

This infrastructure uses:
- t2.micro EC2 instance (free tier eligible)
- EBS volume for the EC2 instance
- VPC networking components (minimal cost)

To minimize costs:
- Use t2.micro instance type (free tier)
- Monitor EC2 and EBS usage
- Infrastructure is optimized for cost with no NAT Gateway