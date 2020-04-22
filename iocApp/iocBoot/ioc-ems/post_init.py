import json
#from epics import caput
from cothread.catools import caput
from datafile import filepath


with open(filepath, 'r') as f:
    data = json.load(f)
    pos_conf = data['position']
    pos_begin = pos_conf['begin']
    pos_end = pos_conf['end']
    pos_step = pos_conf['step']
    volt_conf = data['voltage']
    volt_begin = volt_conf['begin']
    volt_end = volt_conf['end']
    volt_step = volt_conf['step']


for (pv, val) in zip(
        ('POS_BEGIN', 'POS_END', 'POS_STEP',
         'VOLT_BEGIN', 'VOLT_END', 'VOLT_STEP'),
        (pos_begin, pos_end, pos_step,
         volt_begin, volt_end, volt_step)):
    caput("EMS:" + pv, val)
