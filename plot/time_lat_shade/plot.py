import matplotlib.pyplot as plt
import numpy as np

from decolate import decolate
from mkdata import mkdata, mkDateTime


ny = 145

enmin = 0.
enmax = 7.
comin = -5.
comax = 5.
gemin = -2.
gemax = 2.

def mkaz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_az.dat', ny) * 1e-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, '', r'$A_Z \: (10^6 \: \mathrm{J \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_az_lat_t.png', dpi=350, bbox_inches='tight')


def mkkz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_kz.dat', ny) * 1e-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, '', r'$K_Z \: (10^6 \: \mathrm{J \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_kz_lat_t.png', dpi=350, bbox_inches='tight')


def mkw(date, lat):
    
    inputae = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ae.dat', ny) * 1e-6
    inputke = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ke.dat', ny) * 1e-6
    input = inputae + inputke

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, '', r'$W \: (10^6 \: \mathrm{J \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_w_lat_t.png', dpi=350, bbox_inches='tight')


def mkazkz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_c_az_kz.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', comin, comax, '', r'$C\left(A_Z, K_Z\right) \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_c_az_kz_lat_t.png', dpi=350, bbox_inches='tight')


def mkkzw(date, lat):
    
    inputae = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_c_kz_ae.dat', ny)
    inputke = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_c_kz_ke.dat', ny)
    input = inputae + inputke

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', comin, comax, '', r'$C\left(K_Z, W\right) \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_c_kz_w_lat_t.png', dpi=350, bbox_inches='tight')


def mkqe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', gemin, gemax, '', r'$Q_E \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mkttswr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ttswr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', gemin, gemax, '', r'TTSWR $Q_E \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_ttswr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mkttlwr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ttlwr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', gemin, gemax, '', r'TTLWR $Q_E \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_ttlwr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mklrghr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_lrghr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', gemin, gemax, '', r'LRGHR $Q_E \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_lrghr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mkcnvhr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_cnvhr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', gemin, gemax, '', r'CNVHR $Q_E \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_cnvhr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mkvdfhr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_vdfhr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', gemin, gemax, '', r'VDFHR $Q_E \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_vdfhr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def main():
    
    date = mkDateTime()
    lat = np.linspace(-90., 90., ny)

    date, lat = np.meshgrid(date, lat)

    mkaz(date, lat)
    #mkkz(date, lat)
    #mkw(date, lat)
    #mkazkz(date, lat)
    #mkkzw(date, lat)
    #mkqe(date, lat)
    #mkttswr_qe(date, lat)
    #mkttlwr_qe(date, lat)
    #mklrghr_qe(date, lat)
    #mkcnvhr_qe(date, lat)
    #mkvdfhr_qe(date, lat)


main()
