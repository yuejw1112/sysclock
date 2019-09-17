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

from __future__ import division
from __future__ import print_function
import ctypes

kernel32dll = ctypes.windll.kernel32
kernel32dll.SetThreadAffinityMask(kernel32dll.GetCurrentThread(),0x00000001)
freq = ctypes.c_longlong(0)
kernel32dll.QueryPerformanceFrequency(ctypes.byref(freq))
freq = freq.value

def global_clock():
    counter  = ctypes.c_longlong(0)
    kernel32dll.QueryPerformanceCounter(ctypes.byref(counter))
    return counter.value/freq

if __name__ == '__main__':
    print(global_clock())
    
    
    
    
    
    
    
    
    