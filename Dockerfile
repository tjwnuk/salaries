FROM ubuntu:20.04

WORKDIR /usr/src/app

# installing essential packages
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install python-is-python3 -y
RUN apt-get install cron -y && cron
RUN apt-get install bash -y
RUN apt-get install nano -y
RUN apt-get install curl -y

# python packages
COPY scraper/requirements.txt ./scraper/requirements.txt
RUN pip install --no-cache-dir -r ./scraper/requirements.txt

# copy start script
COPY start.sh .
COPY wait-for-it.sh .
RUN chmod +x start.sh
RUN chmod +x wait-for-it.sh