#!../../bin/linux-x86_64/prng

< envPaths

cd ${TOP}

dbLoadDatabase("dbd/prng.dbd",0,0)
prng_registerRecordDeviceDriver(pdbbase) 

dbLoadRecords("db/prng.db","P=test:prng,D=Random,S=324235")
dbLoadRecords("db/prng.db","P=test:prngasync,D=Random Async,S=324235")

cd ${TOP}/iocBoot/${IOC}
iocInit()
