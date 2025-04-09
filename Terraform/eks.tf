# Create EKS Cluster
# This module creates an Amazon EKS cluster with the specified configuration.
# It includes options for enabling public access, setting the cluster version, and configuring node pools.
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.31"

  cluster_name    = "food-ordering-cluster"
  cluster_version = "1.31"

  # Optional
  cluster_endpoint_public_access = true
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

eks_managed_node_groups = {
    default = {
      desired_capacity = 2
      max_capacity     = 3
      min_capacity     = 1

      instance_types = ["t2.large"]
    }
  }

  tags = {
    Environment = "dev"
  }
}