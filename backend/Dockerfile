FROM python:3-alpine

ENV DBNAME link_db
ENV HOST localhost
ENV USER postgres
ENV PASSWORD postgres
ENV PORT 5432
ENV PORT_EXEC 8000

WORKDIR /app
COPY . /app

#RUN apk update && \
#    apk add -y libpq-dev gcc

#RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r /app/req.txt
RUN apk add --no-cache alpine-conf && \
    setup-timezone -z Europe/Moscow
ENTRYPOINT ["/usr/local/bin/python", "/app/main.py"]