provider "aws"{
    region = "ap-south-1"
    profile = "default"
}

# Launching EC2 instance
resource "aws_instance""instance"{
    availability_zone = var.AZ
    instance_type = var.type
    ami = var.ami
    tags = {
        Name = var.name
    }
}

# 
output "Instance_IP" {
    value = aws_instance.instance.public_ip
 
}

#Creating volume
resource "aws_ebs_volume" "volume"{
    count = 5
    availability_zone = aws_instance.instance.availability_zone
    size = 1
    tags = {
        Name = var.name
    }
}

output "volume_Id" {
    value = aws_ebs_volume.volume.*.id
}


resource "aws_volume_attachment" "attach"{
    count = length(var.device_names)
    device_name = var.device_names[count.index]
    volume_id = aws_ebs_volume.volume[count.index].id
    instance_id = aws_instance.instance.id
}