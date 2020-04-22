import os
import json


datapath = "data"
datafile1 = "FE_LEBT_ASy_D0739_20180326_110828_RawData.json"
datafile2 = "FE_LEBT_ASx_D0739_20180323_155607_RawData.json"
datafile3 = "FE_LEBT_ASx_D0739_20180430_102209_RawData.json"
datafile4 = "FE_LEBT_ASx_D0739_20190222_123444_RawData.json"

# datafile = datafile1 # 121 x 201
# datafile = datafile2 # 121 x 101
datafile = datafile3 # 61 x 501

filepath = os.path.join(datapath, datafile)
