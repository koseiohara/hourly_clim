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


def mkgrph_energy(fname):
    date_and_time = get_datetime()
    gmean_az = get_meanclim(fname_az, shape, recl, rec, kind, endian, recstep, -90., 90.) * 1e-6
    gmean_kz = get_meanclim(fname_kz, shape, recl, rec, kind, endian, recstep, -90., 90.) * 1e-6
    gmean_ae = get_meanclim(fname_ae, shape, recl, rec, kind, endian, recstep, -90., 90.) * 1e-6
    gmean_ke = get_meanclim(fname_ke, shape, recl, rec, kind, endian, recstep, -90., 90.) * 1e-6
    gmean_w  = gmean_ae + gmean_ke

    nmean_az = get_meanclim(fname_az, shape, recl, rec, kind, endian, recstep, 0., 90.) * 1e-6
    nmean_kz = get_meanclim(fname_kz, shape, recl, rec, kind, endian, recstep, 0., 90.) * 1e-6
    nmean_ae = get_meanclim(fname_ae, shape, recl, rec, kind, endian, recstep, 0., 90.) * 1e-6
    nmean_ke = get_meanclim(fname_ke, shape, recl, rec, kind, endian, recstep, 0., 90.) * 1e-6
    nmean_w  = nmean_ae + nmean_ke

    smean_az = get_meanclim(fname_az, shape, recl, rec, kind, endian, recstep, -90., 0.) * 1e-6
    smean_kz = get_meanclim(fname_kz, shape, recl, rec, kind, endian, recstep, -90., 0.) * 1e-6
    smean_ae = get_meanclim(fname_ae, shape, recl, rec, kind, endian, recstep, -90., 0.) * 1e-6
    smean_ke = get_meanclim(fname_ke, shape, recl, rec, kind, endian, recstep, -90., 0.) * 1e-6
    smean_w  = smean_ae + smean_ke

    fig = plt.figure(figsize=[12,7])
    axga = fig.add_subplot(331)
    axgk = fig.add_subplot(332)
    axgw = fig.add_subplot(333)
    axna = fig.add_subplot(334)
    axnk = fig.add_subplot(335)
    axnw = fig.add_subplot(336)
    axsa = fig.add_subplot(337)
    axsk = fig.add_subplot(338)
    axsw = fig.add_subplot(339)

    fig.subplots_adjust(wspace=0.17, hspace=0.4)

    axga.plot(date_and_time, gmean_az, color='black', label=r'$A_Z$')
    axgk.plot(date_and_time, gmean_kz, color='black', label=r'$K_Z$')
    axgw.plot(date_and_time, gmean_ae, color='blue' , label=r'$A_E$')
    axgw.plot(date_and_time, gmean_ke, color='red'  , label=r'$K_E$')
    axgw.plot(date_and_time, gmean_w , color='black', label=r'$W$'  )

    axna.plot(date_and_time, nmean_az, color='black', label=r'$A_Z$')
    axnk.plot(date_and_time, nmean_kz, color='black', label=r'$K_Z$')
    axnw.plot(date_and_time, nmean_ae, color='blue' , label=r'$A_E$')
    axnw.plot(date_and_time, nmean_ke, color='red'  , label=r'$K_E$')
    axnw.plot(date_and_time, nmean_w , color='black', label=r'$W$'  )

    axsa.plot(date_and_time, smean_az, color='black', label=r'$A_Z$')
    axsk.plot(date_and_time, smean_kz, color='black', label=r'$K_Z$')
    axsw.plot(date_and_time, smean_ae, color='blue' , label=r'$A_E$')
    axsw.plot(date_and_time, smean_ke, color='red'  , label=r'$K_E$')
    axsw.plot(date_and_time, smean_w , color='black', label=r'$W$'  )

    decolate(axga, r'Global $A_Z$ ($\mathrm{10^6 \: J \: m^{-2}}$)', 'a', date_and_time,   0., 4.0, 1, 5e-1)
    decolate(axgk, r'Global $K_Z$ ($\mathrm{10^6 \: J \: m^{-2}}$)', 'b', date_and_time,   0., 1.0, 1, 1e-1)
    decolate(axgw, r'Global $W$ ($\mathrm{10^6 \: J \: m^{-2}}$)', 'c', date_and_time,   0., 1.6, 1, 2e-1)

    decolate(axna, r'NH $A_Z$ ($\mathrm{10^6 \: J \: m^{-2}}$)'    , 'd', date_and_time, -25., 25., 0, 5e0 )
    decolate(axnk, r'NH $K_Z$ ($\mathrm{10^6 \: J \: m^{-2}}$)'    , 'e', date_and_time,   0., 1.0, 1, 1e-1)
    decolate(axnw, r'NH $W$ ($\mathrm{10^6 \: J \: m^{-2}}$)'    , 'f', date_and_time,   0., 1.6, 1, 2e-1)

    decolate(axsa, r'SH $A_Z$ ($\mathrm{10^6 \: J \: m^{-2}}$)'    , 'g', date_and_time, -25., 25., 0, 5e0 )
    decolate(axsk, r'SH $K_Z$ ($\mathrm{10^6 \: J \: m^{-2}}$)'    , 'h', date_and_time,   0., 1.0, 1, 1e-1)
    decolate(axsw, r'SH $W$  ($\mathrm{10^6 \: J \: m^{-2}}$)'    , 'i', date_and_time,   0., 1.6, 1, 2e-1)

    fig.savefig(fname, dpi=350, bbox_inches='tight')


def mkgrph_conversion(fname):
    date_and_time = get_datetime()
    gmean_azkz = get_meanclim(fname_azkz, shape, recl, rec, kind, endian, recstep, -90., 90.)
    gmean_kzae = get_meanclim(fname_kzae, shape, recl, rec, kind, endian, recstep, -90., 90.)
    gmean_kzke = get_meanclim(fname_kzke, shape, recl, rec, kind, endian, recstep, -90., 90.)
    gmean_aeke = get_meanclim(fname_aeke, shape, recl, rec, kind, endian, recstep, -90., 90.)
    gmean_kzw  = gmean_kzae + gmean_kzke

    nmean_azkz = get_meanclim(fname_azkz, shape, recl, rec, kind, endian, recstep,   0., 90.)
    nmean_kzae = get_meanclim(fname_kzae, shape, recl, rec, kind, endian, recstep,   0., 90.)
    nmean_kzke = get_meanclim(fname_kzke, shape, recl, rec, kind, endian, recstep,   0., 90.)
    nmean_aeke = get_meanclim(fname_aeke, shape, recl, rec, kind, endian, recstep,   0., 90.)
    nmean_kzw  = nmean_kzae + nmean_kzke

    smean_azkz = get_meanclim(fname_azkz, shape, recl, rec, kind, endian, recstep, -90.,  0.)
    smean_kzae = get_meanclim(fname_kzae, shape, recl, rec, kind, endian, recstep, -90.,  0.)
    smean_kzke = get_meanclim(fname_kzke, shape, recl, rec, kind, endian, recstep, -90.,  0.)
    smean_aeke = get_meanclim(fname_aeke, shape, recl, rec, kind, endian, recstep, -90.,  0.)
    smean_kzw  = smean_kzae + smean_kzke

    fig = plt.figure(figsize=[12,7])
    axgak = fig.add_subplot(331)
    axgkw = fig.add_subplot(332)
    axgee = fig.add_subplot(333)
    axnak = fig.add_subplot(334)
    axnkw = fig.add_subplot(335)
    axnee = fig.add_subplot(336)
    axsak = fig.add_subplot(337)
    axskw = fig.add_subplot(338)
    axsee = fig.add_subplot(339)

    fig.subplots_adjust(wspace=0.17, hspace=0.4)

    axgak.plot(date_and_time, gmean_azkz, color='black', label=r'$C(A_Z, K_Z)$')
    axgkw.plot(date_and_time, gmean_kzae, color='blue' , label=r'$C(K_Z, A_E)$')
    axgkw.plot(date_and_time, gmean_kzke, color='red'  , label=r'$C(K_Z, K_E)$')
    axgkw.plot(date_and_time, gmean_kzw , color='black', label=r'$C(K_Z, W)$')
    axgee.plot(date_and_time, gmean_aeke, color='black', label=r'$C(A_E, K_E)$')

    axnak.plot(date_and_time, nmean_azkz, color='black', label=r'$C(A_Z, K_Z)$')
    axnkw.plot(date_and_time, nmean_kzae, color='blue' , label=r'$C(K_Z, A_E)$')
    axnkw.plot(date_and_time, nmean_kzke, color='red'  , label=r'$C(K_Z, K_E)$')
    axnkw.plot(date_and_time, nmean_kzw , color='black', label=r'$C(K_Z, W)$')
    axnee.plot(date_and_time, nmean_aeke, color='black', label=r'$C(A_E, K_E)$')

    axsak.plot(date_and_time, smean_azkz, color='black', label=r'$C(A_Z, K_Z)$')
    axskw.plot(date_and_time, smean_kzae, color='blue' , label=r'$C(K_Z, A_E)$')
    axskw.plot(date_and_time, smean_kzke, color='red'  , label=r'$C(K_Z, K_E)$')
    axskw.plot(date_and_time, smean_kzw , color='black', label=r'$C(K_Z, W)$')
    axsee.plot(date_and_time, smean_aeke, color='black', label=r'$C(A_E, K_E)$')

    decolate(axgak, r'Global $C(A_Z, K_Z)$ ($\mathrm{W \: m^{-2}}$)', 'a', date_and_time,   0., 2.1, 1, 3e-1)
    decolate(axgkw, r'Global $C(K_Z, W)$ ($\mathrm{W \: m^{-2}}$)', 'b', date_and_time, -2.3, 2.3, 1, 5e-1)
    decolate(axgee, r'Global $C(A_E, K_E)$ ($\mathrm{W \: m^{-2}}$)', 'c', date_and_time,   0., 3.3, 1, 5e-1)

    decolate(axnak, r'NH $C(A_Z, K_Z)$ ($\mathrm{W \: m^{-2}}$)'    , 'd', date_and_time,   0., 2.1, 1, 3e-1)
    decolate(axnkw, r'NH $C(K_Z, W)$ ($\mathrm{W \: m^{-2}}$)'    , 'e', date_and_time, -2.3, 2.3, 1, 5e-1)
    decolate(axnee, r'NH $C(A_E, K_E)$ ($\mathrm{W \: m^{-2}}$)'    , 'f', date_and_time,   0., 3.3, 1, 5e-1)

    decolate(axsak, r'SH $C(A_Z, K_Z)$ ($\mathrm{W \: m^{-2}}$)'    , 'g', date_and_time,   0., 2.1, 1, 3e-1)
    decolate(axskw, r'SH $C(K_Z, W)$ ($\mathrm{W \: m^{-2}}$)'    , 'h', date_and_time, -2.3, 2.3, 1, 5e-1)
    decolate(axsee, r'SH $C(A_E, K_E)$ ($\mathrm{W \: m^{-2}}$)'    , 'i', date_and_time,   0., 3.3, 1, 5e-1)

    fig.savefig(fname, dpi=350, bbox_inches='tight')


def decolate(ax, title, label, date_and_time, ymin, ymax, ydigit, yaxisstep):

    ax.set_xlim(date_and_time[0], date_and_time[-1])
    ax.set_ylim(ymin, ymax)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2, bymonthday=1))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1, bymonthday=1))
    
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.yaxis.set_major_locator(mticker.MultipleLocator(yaxisstep))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.{}f'.format(ydigit)))
    ax.yaxis.set_minor_locator(mticker.AutoMinorLocator(5))

    ax.grid(axis='both', which='major', linewidth=0.3)
    ax.grid(axis='both', which='minor', linewidth=0.1)
    ax.tick_params(labelsize=10)

    #fig.suptitle(title, fontsize=12)
    ax.set_title(title, fontsize=12)
    ax.text(0., 1.1, '[{}]'.format(label), horizontalalignment='left', verticalalignment='center', transform=ax.transAxes,
    fontsize=12)
    #ax.legend(loc='upper right', fontsize=10)
    #ax.legend(fontsize=10)


fname_az   = '../../output/JRA3Q_6hourly_clim_1980_2022_{}_VINT.dat'.format('az')
fname_kz   = '../../output/JRA3Q_6hourly_clim_1980_2022_{}_VINT.dat'.format('kz')
fname_ae   = '../../output/JRA3Q_6hourly_clim_1980_2022_{}_VINT.dat'.format('ae')
fname_ke   = '../../output/JRA3Q_6hourly_clim_1980_2022_{}_VINT.dat'.format('ke')
fname_azkz = '../../output/JRA3Q_6hourly_clim_1980_2022_{}_VINT.dat'.format('c_az_kz')
fname_kzae = '../../output/JRA3Q_6hourly_clim_1980_2022_{}_VINT.dat'.format('c_kz_ae')
fname_kzke = '../../output/JRA3Q_6hourly_clim_1980_2022_{}_VINT.dat'.format('c_kz_ke')
fname_aeke = '../../output/JRA3Q_6hourly_clim_1980_2022_{}_VINT.dat'.format('c_ae_ke')

mkgrph_energy('./figs/GLOBAL_NH_SH_mean_Az_Kz_W_Ae_Ke_JRA3Q_1980_2022_clim.png')
mkgrph_conversion('./figs/GLOBAL_NH_SH_mean_cazkz_ckzae_ckzke_ckzw_JRA3Q_1980_2022_clim.png')

