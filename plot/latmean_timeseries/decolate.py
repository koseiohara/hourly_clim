import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import datetime



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
    ax.tick_params(labelsize=13)

    #fig.suptitle(title, fontsize=12)
    ax.set_title(title, fontsize=15)
    if (label != ''):
        ax.text(0., 1.1, '[{}]'.format(label), horizontalalignment='left', verticalalignment='center', transform=ax.transAxes, fontsize=12)
    #ax.legend(loc='upper right', fontsize=10)
    #ax.legend(fontsize=10)



