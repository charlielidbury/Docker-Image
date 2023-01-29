FROM maven:3-adoptopenjdk-14
RUN apt-get update -y
RUN apt-get install curl wget git build-essential cmake -y
CMD /usr/bin/bash
