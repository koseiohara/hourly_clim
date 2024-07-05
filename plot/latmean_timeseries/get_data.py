import numpy as np
import datetime

from filein import filein as filein
from vint2gmean import vint2gmean



def get_from_vint(fname, recl, rec, kind, endian, recstep, ny, nt, range_south, range_north):

    vint_clim = filein(fname, [ny], recl, rec, kind, endian, recstep)
    vint = np.empty([ny])

    gmean = np.empty(nt)

    latstep = (range_north - range_south) / np.float64(ny-1)

    for t in range(nt):
        vint[:] = vint_clim.fread()

        gmean[t] = vint2gmean(vint[:], latstep, True, range_south, range_north)

    vint_clim.fclose()

    return gmean


def get_from_gmean(fname, recl, rec, kind, endian, recstep, nt):

    gmean_clim = filein(fname, [1], recl, rec, kind, endian, recstep)
    work_gmean = np.empty([1])

    gmean = np.empty(nt)

    for t in range(nt):
        work_gmean[:] = gmean_clim.fread()

        gmean[t] = work_gmean[0]

    gmean_clim.fclose()

    return gmean


def get_datetime():
    year=2000
    hourstep = 6
    tnum = 366*4
    
    output = [0]*tnum
    output[0] = datetime.datetime(year, 1, 1)
    for t in range(1, tnum):
        output[t] = output[t-1] + datetime.timedelta(hours=hourstep)
    
    return output


