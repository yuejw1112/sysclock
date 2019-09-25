#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-11-02 22:53:27
# Contact: mrtang@nudt.edu.cn 
# Github: trzp
# Last Modified by:   mr tang
# Last Modified time: 2018-11-02 22:58:51


u'''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
useage:
    from get_global_clock_rz import get_global_clock
       
这个脚本提供了跨平台(linux, windows)支持的高精度计时器，\n
返回的均是全局clock，单位为秒\n
method:
    global_clock
'''

import platform
sys = platform.system().lower()

if sys == 'linux':
    from linux_clock import clock as _clock
elif sys == 'windows':
    from win_clock import global_clock as _clock
else: raise ImportError('unrecognized system platform: %s'%sys)

def global_clock():
    return _clock()