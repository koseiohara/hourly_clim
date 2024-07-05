import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import datetime
from filein import filein as filein




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

