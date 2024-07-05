import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import datetime
from filein import filein as filein


hstep = 6
days = 366
hrs = int(366 * 24 / hstep)
def mkdata(fname, ny):
    inshape = [ny]
    ftype = filein(fname, inshape, 4*ny, 1, 4, 'LITTLE', 1)

    vint = np.empty([ny,hrs])

    for t in range(0, hrs):
        input_work = ftype.fread()
        vint[:,t] = input_work[::-1]

    return vint


def mkdt():
    initial_date = datetime.datetime(2000, 1, 1, 0)
    dateAndTime = [0]*hrs
    dateAndTime[0] = initial_date

    for h in range(1, hrs):
        dateAndTime[h] = dateAndTime[h-1] + datetime.timedelta(hours=hstep)

    return dateAndTime


def mkgrph_energy(ny, title):

    dateAndTime = mkdt()
    lat = np.linspace(-90., 90., ny)
    dateField, latField = np.meshgrid(dateAndTime, lat)

    viaz = mkdata('../../output/JRA3Q_6hourly_clim_1980_2022_az_VINT.dat', ny) * 1e-6
    vikz = mkdata('../../output/JRA3Q_6hourly_clim_1980_2022_kz_VINT.dat', ny) * 1e-6
    viae = mkdata('../../output/JRA3Q_6hourly_clim_1980_2022_ae_VINT.dat', ny) * 1e-6
    vike = mkdata('../../output/JRA3Q_6hourly_clim_1980_2022_ke_VINT.dat', ny) * 1e-6
    viws = viae + vike

    figaz = plt.figure(figsize=[6,3])
    figkz = plt.figure(figsize=[6,3])
    figws = plt.figure(figsize=[6,3])
    figae = plt.figure(figsize=[6,3])
    figke = plt.figure(figsize=[6,3])
    
    #axaz = figaz.add_subplot(511)
    #axkz = figkz.add_subplot(512)
    #axws = figws.add_subplot(513)
    #axae = figae.add_subplot(514)
    #axke = figke.add_subplot(515)

    axaz = figaz.add_subplot(111)
    axkz = figkz.add_subplot(111)
    axws = figws.add_subplot(111)
    axae = figae.add_subplot(111)
    axke = figke.add_subplot(111)

    #print('{:.1e}'.format(np.max(viaz)))
    #print('{:.1e}'.format(np.min(viaz)))
    #print(viaz[:,0])
    #axaz.contourf(dateField, latField, viaz, np.arange(-1.e8, 1.e8+1.e7, 1.e7), cmap='bwr', vmin=-1.e8, vmax=1.e8, extend='both')
    decolate(figaz, axaz, dateField, latField, viaz, 'seismic', -3e2, 3e2, '', r'$A_Z \: (10^6 \: \mathrm{J \: m^{-2}})$')
    decolate(figkz, axkz, dateField, latField, vikz,    'Reds',   0., 5e0, '', r'$K_Z \: (10^6 \: \mathrm{J \: m^{-2}})$')
    decolate(figws, axws, dateField, latField, viws,    'Reds',   0., 5e0, '',   r'$W \: (10^6 \: \mathrm{J \: m^{-2}})$')
    decolate(figae, axae, dateField, latField, viae,    'Reds',   0., 5e0, '', r'$A_E \: (10^6 \: \mathrm{J \: m^{-2}})$')
    decolate(figke, axke, dateField, latField, vike,    'Reds',   0., 5e0, '', r'$K_E \: (10^6 \: \mathrm{J \: m^{-2}})$')

    figaz.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('az'), dpi=400, bbox_inches='tight')
    figkz.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('kz'), dpi=400, bbox_inches='tight')
    figws.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('w') , dpi=400, bbox_inches='tight')
    figae.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('ae'), dpi=400, bbox_inches='tight')
    figke.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('ke'), dpi=400, bbox_inches='tight')


def mkgrph_conversion(ny, title):

    dateAndTime = mkdt()
    lat = np.linspace(-90., 90., ny)
    dateField, latField = np.meshgrid(dateAndTime, lat)

    viazkz = mkdata('../../output/JRA3Q_6hourly_clim_1980_2022_c_az_kz_VINT.dat', ny)
    vikzae = mkdata('../../output/JRA3Q_6hourly_clim_1980_2022_c_kz_ae_VINT.dat', ny)
    vikzke = mkdata('../../output/JRA3Q_6hourly_clim_1980_2022_c_kz_ke_VINT.dat', ny)
    viaeke = mkdata('../../output/JRA3Q_6hourly_clim_1980_2022_c_ae_ke_VINT.dat', ny)
    vikzws = vikzae + vikzke

    print(np.min(viazkz))
    print(np.max(viazkz))
    print(np.min(vikzae))
    print(np.max(vikzae))
    print(np.min(vikzke))
    print(np.max(vikzke))
    print(np.min(viaeke))
    print(np.max(viaeke))
    print(np.min(vikzws))
    print(np.max(vikzws))

    figazkz = plt.figure(figsize=[6,3])
    figkzae = plt.figure(figsize=[6,3])
    figkzke = plt.figure(figsize=[6,3])
    figaeke = plt.figure(figsize=[6,3])
    figkzws = plt.figure(figsize=[6,3])

    axazkz = figazkz.add_subplot(111)
    axkzae = figkzae.add_subplot(111)
    axkzke = figkzke.add_subplot(111)
    axaeke = figaeke.add_subplot(111)
    axkzws = figkzws.add_subplot(111)
    
    decolate(figazkz, axazkz, dateField, latField, viazkz,  'bwr',   -1e1, 1e1, '', r'$C\left(A_Z, K_Z\right) \: (\mathrm{W \: m^{-2}})$')
    decolate(figkzae, axkzae, dateField, latField, vikzae,  'bwr',   -1e1, 1e1, '', r'$C\left(K_Z, A_E\right) \: (\mathrm{W \: m^{-2}})$')
    decolate(figkzke, axkzke, dateField, latField, vikzke,  'bwr',   -1e1, 1e1, '', r'$C\left(K_Z, K_E\right) \: (\mathrm{W \: m^{-2}})$')
    decolate(figaeke, axaeke, dateField, latField, viaeke, 'bwr', -1e1,  1e1, '', r'$C\left(A_E, K_E\right) \: (\mathrm{W \: m^{-2}})$')
    decolate(figkzws, axkzws, dateField, latField, vikzws,  'bwr',   -1e1, 1e1, '', r'$C\left(K_Z, W  \right) \: (\mathrm{W \: m^{-2}})$')
    
    figazkz.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('c_az_kz'), dpi=400, bbox_inches='tight')
    figkzae.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('c_kz_ae'), dpi=400, bbox_inches='tight')
    figkzke.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('c_kz_ke'), dpi=400, bbox_inches='tight')
    figaeke.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('c_ae_ke'), dpi=400, bbox_inches='tight')
    figkzws.savefig('./figs/JRA3Q_1980_2022_clim_{}_lat_t.png'.format('c_kz_w' ), dpi=400, bbox_inches='tight')


def decolate(fig, ax, dateField, latField, shade, cmap, vmin, vmax, title, contlabel):

    levstep = (vmax - vmin) / 40.
    cont = ax.contourf(dateField, latField, shade, cmap=cmap, \
                       levels=np.arange(vmin, vmax+levstep, levstep), extend='both')
    cbar = fig.colorbar(cont, ax=ax, pad=0.01, aspect=12, \
                        ticks=np.arange(vmin, vmax+levstep, levstep*10), format='%4.0f', \
                        label=contlabel)
    #cbar = fig.colorbar(cont, ax=ax, pad=0.01, aspect=12, ticks=np.arange(vmin, vmax+levstep, levstep*5))
    #cbar.set_major_formatter(mticker.ScalarFormatter(useMathText=True))
    #cbar.ax.ticklabel_format(style='sci')

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2, bymonthday=1))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1, bymonthday=1))

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    ax.set_yticks([-90, -60, -30, 0, 30, 60,  90])
    ax.set_yticklabels(['90S', '60S', '30S', 'EQ', '30N', '60N', '90N'])

    ax.set_title(title)

#mkgrph_energy(145, '')
mkgrph_conversion(145, '')
