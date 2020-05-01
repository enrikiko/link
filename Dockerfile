FROM ubuntu:18.04
RUN apt-get update
RUN apt update
RUN apt-get -y install python-pip
RUN pip install --upgrade pip
RUN apt install -y chromium-browser
RUN apt-get install -y python-selenium chromium-chromedriver
RUN pip install selenium requests pick ansible
RUN mkdir scr
COPY . ./scr/
WORKDIR ./scr
ENV MACHINE docker
ARG USER_NAME
ARG USER_PASSWORD
ARG CITY
ARG JOB_TITLE
ARG BLACK_LIST
CMD python init.py
