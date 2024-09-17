region = "ap-south-1"
instance_name = "k8s_master"
vm_count = 1
enable_public_ip = true
launch_template = "launch-template-rhel"  # for rhel bastion-rhel
root_volume_size = 15
vpc_name = "default"
subnet_name = "subnet-1"
spot_instance = false
instance_type = "t3a.medium"
project = "k8s_aws"
private_ip = "172.31.0.5" # Starting digit of private ip ( will increase last digit based on count value).
security_group = "default-sg"