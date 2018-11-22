cdef extern from "precision_time.c":
    double precision_time()
    
def clock():
    return precision_time()
