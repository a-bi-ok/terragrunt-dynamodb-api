terraform {
  source = "../../../modules/dynamodb-api"
}

locals {
  aws_region   = "us-east-1"
  table_name   = ""
  project_name = ""
  environment  = ""
  statefile_bucket = ""
  project_label    = ""
  lock_file_table  = ""
  lambda_bucket_name = ""
  
}

remote_state {
  backend = "s3"
  config = {    
    # fix terragrunt init errors "cannot unmarshal string into Go struct field"
    skip_bucket_root_access  = true
    skip_bucket_enforced_tls = true
    disable_bucket_update    = true
    
    bucket         = local.statefile_bucket
    key            = "serverless/${basename(get_terragrunt_dir())}/terraform.tfstate"
    region         = local.aws_region
    encrypt        = true
    dynamodb_table = local.lock_file_table

    s3_bucket_tags = {
      owner = "${local.project_name}"
      name  = "${local.project_name}-${local.environment}"
    }

    dynamodb_table_tags = {
      owner = "${local.project_name}"
      name  = "${local.project_name}-${local.environment}"
    }
  }
}

inputs = {
  aws_region   = local.aws_region
  table_name   = local.table_name
  project_name = local.project_name
  environment  = local.environment
  project_label = local.project_label
  lambda_bucket_name = local.lambda_bucket_name
}
