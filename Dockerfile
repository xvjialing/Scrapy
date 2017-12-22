FROM python:3-slim-stretch

RUN pip install scrapy==1.4.0

WORKDIR /workspace

RUN mkdir -p /app && chmod -R 777 /app
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

CMD ["scrapy", "crawl", "jobbole"]