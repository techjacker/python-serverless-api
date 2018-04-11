terraform {
  backend "s3" {
    bucket = "python-serverless-api-remote-state"
    key    = "terraform.tfstate"
    region = "eu-west-2"
  }
}

module "lambda_api_gateway" {
  source = "git@github.com:techjacker/terraform-aws-lambda-api-gateway"

  # tags
  project    = "${var.project}"
  service    = "${var.service}"
  owner      = "${var.owner}"
  costcenter = "${var.costcenter}"

  # vpc
  vpc_cidr             = "${var.vpc_cidr}"
  public_subnets_cidr  = "${var.public_subnets_cidr}"
  private_subnets_cidr = "${var.private_subnets_cidr}"
  nat_cidr             = "${var.nat_cidr}"
  igw_cidr             = "${var.igw_cidr}"
  azs                  = "${var.azs}"

  # lambda
  lambda_zip_path      = "${var.lambda_zip_path}"
  lambda_handler       = "${var.lambda_handler}"
  lambda_runtime       = "${var.lambda_runtime}"
  lambda_function_name = "${var.lambda_function_name}"

  # API gateway
  region     = "${var.region}"
  account_id = "${var.account_id}"
}
