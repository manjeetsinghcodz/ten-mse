data "aws_ecr_repository" "ten_mse_ecr_repo" {
  name = "ten-mse"
}

resource "aws_lambda_function" "ten_mse_function" {
  function_name = "ten-mse"
  #image_uri = ${data.aws}:${var.img_tag}" ## Variable parsed on command line
  image_uri = "${data.aws_ecr_repository.ten_mse_ecr_repo.repository_url}:${var.img_tag}"
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
