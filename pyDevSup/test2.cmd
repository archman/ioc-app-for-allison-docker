#!./bin/linux-x86_64/softIocPy2.7

py "import logging"
py "logging.basicConfig(level=logging.DEBUG)"

py "import sys; sys.path.insert(0,'${PWD}/testApp')"

py "import test2"
py "test2.addDrv('AAAA')"
py "test2.addDrv('BBBB')"

dbLoadRecords("db/test2.db","P=md:")

iocInit()
