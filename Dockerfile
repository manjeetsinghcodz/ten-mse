FROM alpine:latest

RUN apk update && \
    apk add python3 py3-pip --no-cache

WORKDIR /flask
COPY ./requirements.txt /flask/requirements.txt
COPY ./app /flask
RUN pip install -r requirements.txt
EXPOSE 8080

CMD [ "python", "app.py" ]
