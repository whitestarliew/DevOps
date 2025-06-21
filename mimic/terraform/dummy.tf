provider "aws" {
  region = "ap-southeast-3"
}

module "vpc" {
  source = "./modules/vpc"
  vpc_name = "dummy-vpc"
}

module "ec2" {
  source = "./modules/ec2"
  instance_name = "dummy-ec2"
  vpc_id = module.vpc.vpc_id
  subnet_id = module.vpc.public_subnet_id
  security_group_id = module.vpc.sg_id
}
