FROM python:3.6.4-alpine3.7

RUN pip install scrapy==1.4.0

WORKDIR /workspace

RUN mkdir -p /app && chmod -R 777 /app
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

CMD ["scrapy", "crawl", "jobbole"]