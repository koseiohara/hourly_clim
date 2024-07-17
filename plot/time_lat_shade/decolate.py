import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import datetime
from filein import filein as filein




def decolate(fig, ax, dateField, latField, shade, cmap, vmin, vmax, cbarform='%4.1f', title='', contlabel='', contour=False):

    levstep = (vmax - vmin) / 40.
    cont = ax.contourf(dateField, latField, shade, cmap=cmap, \
                       levels=np.arange(vmin, vmax+levstep, levstep), extend='both')
    if (contlabel == ''):
        cbar = fig.colorbar(cont, ax=ax, pad=0.01, aspect=12, \
                            ticks=np.arange(vmin, vmax+levstep, levstep*10), format=cbarform)
    else:
        cbar = fig.colorbar(cont, ax=ax, pad=0.01, aspect=12, \
                            ticks=np.arange(vmin, vmax+levstep, levstep*10), format=cbarform, \
                            label=contlabel)

    if (contour):
        contstep = (vmax - vmin) / 2.
        ax.contour(dateField, latField, shade, colors='white', linewidths=0.5, \
                   levels=np.arange(4*vmin, 4*(vmax+contstep), contstep))

    #cbar = fig.colorbar(cont, ax=ax, pad=0.01, aspect=12, ticks=np.arange(vmin, vmax+levstep, levstep*5))
    #cbar.set_major_formatter(mticker.ScalarFormatter(useMathText=True))
    #cbar.ax.ticklabel_format(style='sci')

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2, bymonthday=1))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1, bymonthday=1))

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    #ax.set_yscale('function', functions=(cosine_scale, arccos_scale))

    #ylabel_lat = np.array([-90, -60, -30, 0, 30, 60, 90])
    ylabel_lat = np.array([-90, -45, -20, 0, 20, 45, 90])

    #print(latField[:,0])
    #print((ylabel_lat + 90.) * np.pi / 180.)

    #ax.set_yticks(np.cos(np.array([-90., -60., -30., 0., 30., 60.,  90.])*np.pi/180.))
    ax.set_yticks(np.cos((ylabel_lat - 90.) * np.pi / 180.))
    #ax.set_yticklabels(['90S', '60S', '30S', 'EQ', '30N', '60N', '90N'])
    ax.set_yticklabels(mkylabels(ylabel_lat))

    ax.set_title(title)


def mkylabels(ylabel):
    #len = np.len(ylabel)
    len = np.size(ylabel)
    #output = np.empty(len, dtype='str')
    output = ['']*len


    for i in range(len):
        if (ylabel[i] < 0):
            output[i] = '{:2d}S'.format(-ylabel[i])
        elif (ylabel[i] > 0):
            output[i] = '{:2d}N'.format(ylabel[i])
        else:
            output[i] = 'EQ'

    return output


