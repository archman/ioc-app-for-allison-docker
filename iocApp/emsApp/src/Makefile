TOP=../..

include $(TOP)/configure/CONFIG
include $(PYDEVSUP)/configure/CONFIG_SITE
include $(PYDEVSUP)/configure/CONFIG_PY

PROD_IOC = ems
DBD += ems.dbd

ems_DBD += base.dbd
ems_DBD += pyDevSup.dbd

ems_LIBS += pyDevSup$(PY_LD_VER)

ems_SRCS += ems_registerRecordDeviceDriver.cpp
ems_SRCS_DEFAULT += emsMain.cpp

ems_LIBS += $(EPICS_BASE_IOC_LIBS)

DIAGSTD ?= /usr/lib/epics
include $(TOP)/configure/RULES
include $(PYDEVSUP)/configure/RULES_PY
