#!../../bin/linux-x86_64/ems

< envPaths

epicsEnvSet("PYEPICS_LIBCA", "$(EPICS_BASE)/lib/linux-x86_64/libca.so")
# epicsEnvSet("DIAGSTD_DISABLE", "YES")
epicsEnvSet("PREFIX", "EMS")

dbLoadDatabase("${TOP}/dbd/ems.dbd",0,0)
ems_registerRecordDeviceDriver(pdbbase)

py "import init"
py "import st"

dbLoadRecords("$(TOP)/db/ems.db", P=$(PREFIX))

iocInit()

py "import post_init"
