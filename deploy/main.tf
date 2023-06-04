
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "ap-southeast-2"
  access_key = "AKIA6GSQ5G4LKQS3C3G5"
  secret_key = "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"
}