resource "aws_s3_bucket" "b" {
  bucket = "log-store-base"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Staging"
  }
}
