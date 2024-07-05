from get_data import get_from_vint, get_from_gmean, get_datetime
from decolate import decolate


def plot_az(fig, ax, az, date, title, label):
    
    ax.plot(date, az, color='black')

    ymin = 0.
    ymax = 4.
    ydigit = 1
    yaxisstep = 0.5

    decolate(ax, title, label, date, ymin, ymax, ydigit, yaxisstep)


def plot_kz(fig, ax, kz, date, title, label):
    
    ax.plot(date, kz, color='black')

    ymin = 0.
    ymax = 1.
    ydigit = 1
    yaxisstep = 0.1

    decolate(ax, title, label, date, ymin, ymax, ydigit, yaxisstep)


def plot_w(fig, ax, w, date, title, label):
    
    ax.plot(date, w, color='black')

    ymin = 0.
    ymax = 1.7
    ydigit = 1
    yaxisstep = 0.2

    decolate(ax, title, label, date, ymin, ymax, ydigit, yaxisstep)


def plot_c_az_kz(fig, ax, c_az_kz, date, title, label):
    
    ax.plot(date, c_az_kz, color='black')

    ymin = 0.
    ymax = 2.2
    ydigit = 1
    yaxisstep = 0.3

    decolate(ax, title, label, date, ymin, ymax, ydigit, yaxisstep)


def plot_c_kz_w(fig, ax, c_kz_w, date, title, label):
    
    ax.plot(date, c_kz_w, color='black')

    ymin = 0.
    ymax = 1.2
    ydigit = 1
    yaxisstep = 0.2

    decolate(ax, title, label, date, ymin, ymax, ydigit, yaxisstep)


def plot_qe(fig, ax, qe, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, title, label):

    #colors = ['#0072B2', '#E69F00', '#009E73', '#CC79A7', '#D55E00', '#56B4E9']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    
    ax.plot(date,    qe, color=colors[0], label='Total', alpha=0.6)
    ax.plot(date, ttswr, color=colors[1], label='ttswr', alpha=0.6)
    ax.plot(date, ttlwr, color=colors[2], label='ttlwr', alpha=0.6)
    ax.plot(date, lrghr, color=colors[3], label='lrghr', alpha=0.6)
    ax.plot(date, cnvhr, color=colors[4], label='cnvhr', alpha=0.6)
    ax.plot(date, vdfhr, color=colors[5], label='vdfhr', alpha=0.6)

    ymin = -0.5
    ymax = 2.
    ydigit = 1
    yaxisstep = 0.5

    decolate(ax, title, label, date, ymin, ymax, ydigit, yaxisstep)

    ax.legend()


def plot_qz(fig, ax, qz, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, title, label):
    
    #colors = ['#0072B2', '#E69F00', '#009E73', '#CC79A7', '#D55E00', '#56B4E9']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    
    ax.plot(date,    qz, color=colors[0], label='Total', alpha=0.6)
    ax.plot(date, ttswr, color=colors[1], label='ttswr', alpha=0.6)
    ax.plot(date, ttlwr, color=colors[2], label='ttlwr', alpha=0.6)
    ax.plot(date, lrghr, color=colors[3], label='lrghr', alpha=0.6)
    ax.plot(date, cnvhr, color=colors[4], label='cnvhr', alpha=0.6)
    ax.plot(date, vdfhr, color=colors[5], label='vdfhr', alpha=0.6)

    ymin = -3.0
    ymax = 4.5
    ydigit = 1
    yaxisstep = 1.

    decolate(ax, title, label, date, ymin, ymax, ydigit, yaxisstep)

    ax.legend()


