#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-11-02 22:33:56
# Contact: mrtang@nudt.edu.cn 
# Github: trzp
# Last Modified by:   mr tang
# Last Modified time: 2018-11-05 22:43:39


u'''
这个脚本用于提供windows系统下的全局clock，可用于时间戳记录
注意：不要随意导入该模块，因为任何导入该模块的线程都将被绑定到多核CPU的第1个核心
'''

import ctypes
import time

kernel32dll = ctypes.windll.kernel32 
DWORD = ctypes.c_uint32
HANDLE = ctypes.c_voidp
LARGE_INTEGER = ctypes.c_int64
counter = kernel32dll.QueryPerformanceCounter
kernel32dll.SetThreadAffinityMask(kernel32dll.GetCurrentThread(),0x00000001)

timebase = LARGE_INTEGER()
kernel32dll.QueryPerformanceFrequency(ctypes.addressof(timebase))
__FREQ__ = float(timebase.value)

def global_clock():
    counter  = LARGE_INTEGER()
    kernel32dll.QueryPerformanceCounter(ctypes.addressof(counter))
    return float(counter.value)/__FREQ__