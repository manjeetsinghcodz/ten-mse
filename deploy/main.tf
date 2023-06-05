
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

###AWS provider credentials are configure in runner node env variable due to security reason
provider "aws" {
  region = "ap-southeast-2"
}
