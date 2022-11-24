
FROM debian:latest
MAINTAINER Nikolai S. Vasil'ev

RUN apt -y update && apt -y install python3-pip

ADD ./nmcrop /root/nmcrop
ADD ./run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]