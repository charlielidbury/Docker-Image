FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get install curl wget git build-essential openjdk-13-jdk-headless openssh-server sudo cmake maven -y
RUN apt-get install openjdk-13-dbg -y
RUN apt-get install -y enscript ghostscript
COPY build-init.sh /usr/local/bin/build-init.sh
COPY generate_report.py /usr/local/bin/generate_report.py
CMD /usr/bin/bash
