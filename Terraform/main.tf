module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "food-ordering-vpc"

  # The CIDR block for the VPC. This is the range of IP addresses that can be used within the VPC.
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-1a", "eu-west-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true

  tags = {
    Terraform = "true"
  }
}
