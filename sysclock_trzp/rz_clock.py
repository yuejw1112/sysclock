#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-11-02 22:53:27
# Contact: mrtang@nudt.edu.cn 
# Github: trzp
# Last Modified by:   mr tang
# Last Modified time: 2018-11-02 22:58:51


import platform
sys = platform.system().lower()

if sys == 'linux':
    from linux_clock import clock as _clock
elif sys == 'windows':
    from time import clock as _clock
else: raise ImportError('unrecognized system platform: %s'%sys)

def clock():
    return _clock()