variable "AZ" {
    default = "ap-south-1b"
}

variable "type" {
    default = "t2.micro"
}

variable "ami" {
    default = "ami-0ad704c126371a549"
}

variable "name" {
    default = "Terraform"
}

variable "device_names" {
    type = list(string)
    default = ["/dev/sdf","/dev/sdg","/dev/sdh","/dev/sdi","/dev/sdj",]   
}