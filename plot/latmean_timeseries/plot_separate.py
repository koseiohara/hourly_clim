import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import datetime

from filein import filein as filein
from vint2gmean import vint2gmean

#vint = np.ones(145)
#gmean = vint2gmean(vint, 1.25, True, -90., 0.)
#
#print(gmean)


fname_az = '../output/JRA3Q_6hourly_clim_1970_2022_{}_VINT.dat'.format('az')
fname_kz = '../output/JRA3Q_6hourly_clim_1970_2022_{}_VINT_sub.dat'.format('kz')
fname_ae = '../output/JRA3Q_6hourly_clim_1970_2022_{}_VINT.dat'.format('ae')
fname_ke = '../output/JRA3Q_6hourly_clim_1970_2022_{}_VINT.dat'.format('ke')
shape = [145]
recl = 4*145
rec = 1
recstep = 1
kind = 4
endian = 'LITTLE'

nt = 366*4
latstep = 1.25

def get_meanclim(fname, shape, recl, rec, kind, endian, recstep, range_south, range_north):

    vint_clim = filein(fname, shape, recl, rec, kind, endian, recstep)
    vint = np.empty(shape)

    gmean = np.empty(nt)

    for t in range(nt):
        vint[:] = vint_clim.fread()

        gmean[t] = vint2gmean(vint[:], latstep, True, range_south, range_north)

    vint_clim.fclose()

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


def mkgrph(fname, title, range_south, range_north):
    date_and_time = get_datetime()
    gmean_az = get_meanclim(fname_az, shape, recl, rec, kind, endian, recstep, range_south, range_north) * 1e-6
    gmean_kz = get_meanclim(fname_kz, shape, recl, rec, kind, endian, recstep, range_south, range_north) * 1e-6
    gmean_ae = get_meanclim(fname_ae, shape, recl, rec, kind, endian, recstep, range_south, range_north) * 1e-6
    gmean_ke = get_meanclim(fname_ke, shape, recl, rec, kind, endian, recstep, range_south, range_north) * 1e-6
    gmean_w  = gmean_ae + gmean_ke

   
    figaz = plt.figure(figsize=[5,3])
    figkz = plt.figure(figsize=[5,3])
    figws = plt.figure(figsize=[5,3])
    axaz = figaz.add_subplot(111)
    axkz = figkz.add_subplot(111)
    axws = figws.add_subplot(111)

    axaz.plot(date_and_time, gmean_az, color='black', label='Az')
    axkz.plot(date_and_time, gmean_kz, color='black', label='Kz')
    axws.plot(date_and_time, gmean_ae, color='blue' , label='Ae')
    axws.plot(date_and_time, gmean_ke, color='red'  , label='Ke')
    axws.plot(date_and_time, gmean_w , color='black', label='W' )

    axaz.set_xlim(date_and_time[0], date_and_time[-1])
    axkz.set_xlim(date_and_time[0], date_and_time[-1])
    axws.set_xlim(date_and_time[0], date_and_time[-1])

    decolate(axaz, axkz, axws, title)

    figaz.savefig('{}_{}.png'.format(fname, 'az')     , dpi=350, bbox_inches='tight')
    figkz.savefig('{}_{}.png'.format(fname, 'kz')     , dpi=350, bbox_inches='tight')
    figws.savefig('{}_{}.png'.format(fname, 'ae_ke_w'), dpi=350, bbox_inches='tight')


def decolate(axaz,axkz, axws, title):

    #fig.subplots_adjust(hspace=0.15, top=0.95)

    axaz.xaxis.set_major_locator(mdates.MonthLocator(interval=2, bymonthday=1))
    axkz.xaxis.set_major_locator(mdates.MonthLocator(interval=2, bymonthday=1))
    axws.xaxis.set_major_locator(mdates.MonthLocator(interval=2, bymonthday=1))

    axaz.xaxis.set_minor_locator(mdates.MonthLocator(interval=1, bymonthday=1))
    axkz.xaxis.set_minor_locator(mdates.MonthLocator(interval=1, bymonthday=1))
    axws.xaxis.set_minor_locator(mdates.MonthLocator(interval=1, bymonthday=1))
    
    axaz.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    axkz.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    axws.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    #axaz.yaxis.set_major_locator(mticker.MultipleLocator(0.5e0))
    #axkz.yaxis.set_major_locator(mticker.MultipleLocator(0.5e0))
    #axws.yaxis.set_major_locator(mticker.MultipleLocator(0.5e0))

    #axaz.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))
    #axkz.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))
    #axws.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))

    axaz.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))
    axkz.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))
    axws.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))

    axaz.grid(axis='both', which='major', linewidth=0.3)
    axkz.grid(axis='both', which='major', linewidth=0.3)
    axws.grid(axis='both', which='major', linewidth=0.3)
    
    axaz.grid(axis='both', which='minor', linewidth=0.1)
    axkz.grid(axis='both', which='minor', linewidth=0.1)
    axws.grid(axis='both', which='minor', linewidth=0.1)

    axaz.tick_params(labelsize=10)
    axkz.tick_params(labelsize=10)
    axws.tick_params(labelsize=10)

    #fig.suptitle(title, fontsize=12)
    axaz.set_title(title, fontsize=12)
    axkz.set_title(title, fontsize=12)
    axws.set_title(title, fontsize=12)

    axaz.legend(loc='upper right', fontsize=10)
    axkz.legend(loc='upper right', fontsize=10)
    axws.legend(loc='upper right', fontsize=10)


mkgrph('./figs/gmean_1970_2022_clim', r'Global Mean Seazonal Variability ($\mathrm{10^6 \: J \: m^{-2}}$)', -90., 90.)
mkgrph('./figs/NH_1970_2022_clim'   ,     r'NH Mean Seazonal Variability ($\mathrm{10^6 \: J \: m^{-2}}$)',   0., 90.)
mkgrph('./figs/SH_1970_2022_clim'   ,     r'SH Mean Seazonal Variability ($\mathrm{10^6 \: J \: m^{-2}}$)', -90.,  0.)



