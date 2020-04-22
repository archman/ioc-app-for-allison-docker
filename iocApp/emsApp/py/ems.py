#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import devsup.ptable as PT
from devsup.hooks import addHook
import devsup.db as db
import json
import numpy as np
import time
from datetime import datetime
from threading import Event, Thread


class EmsSupport(PT.TableBase):
    trigger = PT.Parameter()
    status = PT.Parameter(iointr=True)
    arr = PT.Parameter(iointr=True)
    pos_now = PT.Parameter(iointr=True)

    def __init__(self, datafile, **kws):
        super(self.__class__, self).__init__(**kws)

        self._datafile = datafile
        addHook("AfterCaServerRunning", self.init_data)

    def init_data(self):
        with open(self._datafile, 'r') as fp:
            self._data = np.asarray(json.load(fp)['data']['array'])
        self.init_data0()
        #
        self.event = Event()
        self.trigger.addAction(self.event.set, lambda a, b:True)
        self.th = Thread(target=self.on_update)
        self.th.start()
        #
        pos_begin_pv = "EMS:POS_BEGIN"
        pos_end_pv = "EMS:POS_END"
        pos_step_pv = "EMS:POS_STEP"
        self.s0 = db.getRecord(pos_begin_pv)
        self.s1 = db.getRecord(pos_end_pv)
        self.ss = db.getRecord(pos_step_pv)

    def init_data0(self):
        self._data0 = np.zeros(self._data.shape)
        arr = self._data0.flatten()
        self.arr.value = arr
        self.arr.notify()
        self.status.value = 0
        self.status.notify()
        self.pos_now.value = 0
        self.pos_now.notify()

    def on_update(self):
        while self.event.wait():
            self.init_data0()

            imax = int((self.s1.VAL - self.s0.VAL) / self.ss.VAL) + 1
            i = 0
            while i < imax:
                t0 = time.time()
                self._data0[:, i] = self._data[:, i]
                arr = self._data0.flatten()
                self.arr.value = arr
                self.arr.notify()
                i += 1
                print("Pos: {0:02d}/{1:02d}".format(i, imax))
                dt = time.time() - t0
                print("-- Execution time: {0:.16f} ms".format(dt * 1000))
                time.sleep(0.1 - dt)
                t_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                print("-- Timestamp: {}".format(t_now))
                self.pos_now.value = i
                self.pos_now.notify()
            self.status.value = 12
            self.status.notify()
            self.event.clear()
            # reset status bit to 0
            time.sleep(0.5)
            self.status.value = 0
            self.status.notify()


def build(datafile, name):
    return EmsSupport(datafile, name=name)
