#!./bin/linux-x86_64/softIocPy2.7

py "import logging"
py "logging.basicConfig(level=logging.DEBUG)"

py "import sys; sys.path.insert(0,'${PWD}/testApp')"

py "import test6"
py "test6.SumTable(name='tsum')"

dbLoadRecords("db/test6.db","P=tst:,TNAME=tsum")

iocInit()
