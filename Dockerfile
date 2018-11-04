FROM python:3.4-alpine3.7

RUN apk add --no-cache --update git make gcc python3-dev musl-dev && \
    set -ex && \
    pip install --no-cache-dir pipenv==2018.10.13
# RUN pip install flask_restplus

WORKDIR /app
ADD . .

RUN set -ex && \
    pipenv install --dev --system --deploy