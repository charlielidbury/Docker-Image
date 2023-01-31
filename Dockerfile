FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get install curl wget git build-essential openjdk-13-jdk-headless openssh-server sudo cmake maven -y
CMD /usr/bin/bash
