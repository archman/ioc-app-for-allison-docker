TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord

# Install xxxSupport.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Build an IOC support library
LIBRARY_IOC += myexSupport

# Compile and add the code to the support library
myexSupport_SRCS += xxxRecord.c
myexSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
# This is required for Windows DLL builds.
myexSupport_SRCS += dbSubExample.c
myexSupport_SRCS += myexHello.c
myexSupport_SRCS += initTrace.c

myexSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC = myex

# myex.dbd will be created and installed
DBD += myex.dbd

# myex.dbd will include these files:
myex_DBD += base.dbd
myex_DBD += xxxSupport.dbd
myex_DBD += dbSubExample.dbd
myex_DBD += myexHello.dbd
myex_DBD += initTrace.dbd

# myex_registerRecordDeviceDriver.cpp derives from myex.dbd
myex_SRCS += myex_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
myex_SRCS_DEFAULT += myexMain.cpp
myex_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#myex_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
myex_LIBS += myexSupport

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into myexSupport
    sncExample_SNCFLAGS += +r
    myex_DBD += sncExample.dbd
    myexSupport_SRCS += sncExample.stt
    myexSupport_LIBS += seq pv
    myex_LIBS += seq pv

    # Build sncProgram as a standalone program
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Finally link IOC to the EPICS Base libraries
myex_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

