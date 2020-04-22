FROM tonyzhang/ioc-base:buster

WORKDIR /root

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        build-essential \
        python3 python3-dev python3-numpy \
        python3-pip python3-setuptools python3-wheel && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install cothread

COPY iocApp ./iocApp
COPY pyDevSup ./pyDevSup

RUN cd /root/pyDevSup && make
RUN cd /root/iocApp && make
COPY start-ioc.sh /usr/local/bin

CMD ["start-ioc.sh"]
