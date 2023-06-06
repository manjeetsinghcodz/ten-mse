####Official aws lambda python 3.10 image
FROM public.ecr.aws/lambda/python:3.10

## Copy app.py install /var/task
COPY ./app/app.py ${LAMBDA_TASK_ROOT}

## Copy requirement.txt
COPY requirements.txt  .

## Install all needed libraries
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

## Run handler command
CMD ["app.handler"]