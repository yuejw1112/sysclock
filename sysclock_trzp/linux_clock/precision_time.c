#include<sys/time.h>
double precision_time() 
{
    struct timeval tv;
    gettimeofday(&tv,NULL);
    return tv.tv_sec + tv.tv_usec/1000000.;
}
