provider "aws" {
  region = "ap-northeast-1"
}

variable "domain" {
  default = "reiwa0407"
}

data "aws_region" "current" {}

data "aws_caller_identity" "current" {}

resource "aws_elasticsearch_domain" "es" {
  domain_name = "${var.domain}"
  elasticsearch_version = "6.4"

  cluster_config {
    instance_type = "t2.small.elasticsearch"
  }

  ebs_options {
    ebs_enabled = true
    volume_size = 10
  }

  snapshot_options {
    automated_snapshot_start_hour = 23
  }

  access_policies = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "es:*",
      "Principal": "*",
      "Effect": "Allow",
      "Resource": "arn:aws:es:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:domain/${var.domain}/*",
      "Condition": {
        "IpAddress": {"aws:SourceIp": ["0.0.0.0/32"]}
      }
    }
  ]
}
POLICY
}

