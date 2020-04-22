#!./bin/linux-x86_64/softIocPy2.7

py "import logging"
py "logging.basicConfig(level=logging.DEBUG)"

py "import sys; sys.path.insert(0,'${PWD}/testApp')"

dbLoadRecords("db/test3.db","P=md:")

iocInit()
