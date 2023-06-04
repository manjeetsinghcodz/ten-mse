data "aws_ecr_repository" "ten_mse_ecr_repo" {
  name = "ten-mse"
}

resource "aws_lambda_function" "ten_mse_function" {
  function_name = "ten-mse"
  image_uri = "976201004822.dkr.ecr.ap-southeast-2.amazonaws.com/ten-mse:${var.tag}"
  package_type = "Image"
  role = aws_iam_role.ten_mse_function_role.arn
}

resource "aws_iam_role" "ten_mse_function_role" {
  name = "ten-mse"

  assume_role_policy = jsonencode({
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}
