import numpy as np
import subprocess

class GenRand(object):
    def __init__(self, rec, link):
        x = np.linspace(0, 10, 500)
        y = np.linspace(0, 10, 500)
        self.xx, self.yy = np.meshgrid(x, y)

    def gauss2d(self, x, y, x0, y0, sx, sy):
        return np.exp(-(((x-x0)/float(sx))**2)/2.0) * np.exp(-(((y-y0)/float(sy))**2)/2.0)

    def detach(self, rec):
        pass

    def process(self, rec, reason):
        rx, ry = np.random.random()*0.5 + 0.5, np.random.random()*0.5 + 0.3
        px, py = np.random.random()*5, np.random.random()*5 + 1
        tmpdata = np.random.random()*20*self.gauss2d(self.xx, self.yy, px, py, rx, ry) + \
                np.random.random(size = 500 * 500).reshape(500, 500)
        rec.VAL = tmpdata.flatten()

class GenProf(object):
    def __init__(self, rec, link):
        R = getRecord("test:count")
        print R.field('VAL')
    def detach(self, rec):
        pass
    def process(self, rec, reason):
        #rx, ry = np.random.random()*0.5 + 0.5, np.random.random()*0.5 + 0.3
        #px, py = np.random.random()*5, np.random.random()*5 + 1
        #tmpdata = np.random.random()*20*gauss2d(xx, yy, px, py, rx, ry) + \
        #        np.random.random(size = 500 * 500).reshape(500, 500)
        
        cmdline = ' '.join(['cd linac; make soft > /dev/null'])
        subprocess.call(cmdline, shell=True)
        tmpdata = np.loadtxt('./linac/linac.h2d.asc')
        rec.VAL = tmpdata

build = GenProf
