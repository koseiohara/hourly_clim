import matplotlib.pyplot as plt
import numpy as np

from decolate import decolate
from mkdata import mkdata, mkDateTime


ny = 145

enmin = 0.
enmax = 8.
comin = -5.
comax = 5.
qemin = -3.
qemax = 3.
qzmin = -20.
qzmax = 20.

def mkaz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_az.dat', ny) * 1e-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, '', r'$A_Z \: (10^6 \: \mathrm{J \: m^{-2}})$', contour=True)
    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, title=r'$A_Z \: (10^6 \: \mathrm{J \: m^{-2}})$', contour=True)

    fig.savefig('figs/JRA3Q_1980_2023_clim_az_lat_t.png', dpi=350, bbox_inches='tight')


def mkkz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_kz.dat', ny) * 1e-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, '', r'$K_Z \: (10^6 \: \mathrm{J \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, title=r'$K_Z \: (10^6 \: \mathrm{J \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_kz_lat_t.png', dpi=350, bbox_inches='tight')


def mkw(date, lat):
    
    inputae = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ae.dat', ny) * 1e-6
    inputke = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ke.dat', ny) * 1e-6
    input = inputae + inputke

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, '', r'$W \: (10^6 \: \mathrm{J \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, title=r'$W \: (10^6 \: \mathrm{J \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_w_lat_t.png', dpi=350, bbox_inches='tight')


def mkae(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ae.dat', ny) * 1e-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, '', r'$A_E \: (10^6 \: \mathrm{J \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, title=r'$A_E \: (10^6 \: \mathrm{J \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_ae_lat_t.png', dpi=350, bbox_inches='tight')


def mkke(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ke.dat', ny) * 1e-6

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, '', r'$K_E \: (10^6 \: \mathrm{J \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'Reds', enmin, enmax, title=r'$K_E \: (10^6 \: \mathrm{J \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_ke_lat_t.png', dpi=350, bbox_inches='tight')


def mkazkz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_c_az_kz.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', comin, comax, '', r'$C\left(A_Z, K_Z\right) \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', comin, comax, title=r'$C\left(A_Z, K_Z\right) \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_c_az_kz_lat_t.png', dpi=350, bbox_inches='tight')


def mkkzw(date, lat):
    
    inputae = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_c_kz_ae.dat', ny)
    inputke = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_c_kz_ke.dat', ny)
    input = inputae + inputke

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', comin, comax, '', r'$C\left(K_Z, W\right) \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', comin, comax, title=r'$C\left(K_Z, W\right) \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_c_kz_w_lat_t.png', dpi=350, bbox_inches='tight')


def mkqe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, '', r'$Q_E \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, title=r'$Q_E \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mkttswr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ttswr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, '', r'TTSWR $Q_E \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, title=r'$Q_E$ by Short Wave Radiation $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_ttswr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mkttlwr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ttlwr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, '', r'TTLWR $Q_E \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, title=r'$Q_E$ by Long Wave Radiation $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_ttlwr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mklrghr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_lrghr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, '', r'LRGHR $Q_E \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, title=r'$Q_E$ by Large Scale Condensation $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_lrghr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mkcnvhr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_cnvhr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, '', r'CNVHR $Q_E \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, title=r'$Q_E$ by Convective Heating $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_cnvhr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mkvdfhr_qe(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_vdfhr_qe.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, '', r'VDFHR $Q_E \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qemin, qemax, title=r'$Q_E$ by Vertical Diffusion $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_vdfhr_qe_lat_t.png', dpi=350, bbox_inches='tight')


def mkqz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_qz.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, cbarform='%4.0f', title=r'$Q_Z \: (\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_qz_lat_t.png', dpi=350, bbox_inches='tight')


def mkttswr_qz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ttswr_qz.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, '', r'TTSWR $Q_Z \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, cbarform='%4.0f', title=r'$Q_Z$ by Short Wave Radiation $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_ttswr_qz_lat_t.png', dpi=350, bbox_inches='tight')


def mkttlwr_qz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_ttlwr_qz.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, '', r'TTLWR $Q_Z \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, cbarform='%4.0f', title=r'$Q_Z$ by Long Wave Radiation $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_ttlwr_qz_lat_t.png', dpi=350, bbox_inches='tight')


def mklrghr_qz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_lrghr_qz.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, '', r'LRGHR $Q_Z \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, cbarform='%4.0f', title=r'$Q_Z$ by Large Scale Condensation $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_lrghr_qz_lat_t.png', dpi=350, bbox_inches='tight')


def mkcnvhr_qz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_cnvhr_qz.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, '', r'CNVHR $Q_Z \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, cbarform='%4.0f', title=r'$Q_Z$ by Convective Heating $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_cnvhr_qz_lat_t.png', dpi=350, bbox_inches='tight')


def mkvdfhr_qz(date, lat):
    
    input = mkdata('../../output/JRA3Q_1980_2023_ALL_VINT_vdfhr_qz.dat', ny)

    fig = plt.figure(figsize=[6,3])
    ax  = fig.add_subplot(111)

    #decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, '', r'VDFHR $Q_Z \: (\mathrm{W \: m^{-2}})$')
    decolate(fig, ax, date, lat, input, 'coolwarm', qzmin, qzmax, cbarform='%4.0f', title=r'$Q_Z$ by Vertical Diffusion $(\mathrm{W \: m^{-2}})$')

    fig.savefig('figs/JRA3Q_1980_2023_clim_vdfhr_qz_lat_t.png', dpi=350, bbox_inches='tight')


def main():
    
    date = mkDateTime()
    lat = np.linspace(-90., 90., ny)

    lat[:] = lat[:] - 90.
    lat[:] = np.cos(lat[:]*np.pi/180.)

    date, lat = np.meshgrid(date, lat)

    mkaz(date, lat)
    mkkz(date, lat)
    mkw(date, lat)
    mkae(date, lat)
    mkke(date, lat)

    mkazkz(date, lat)
    mkkzw(date, lat)

    mkqe(date, lat)
    mkttswr_qe(date, lat)
    mkttlwr_qe(date, lat)
    mklrghr_qe(date, lat)
    mkcnvhr_qe(date, lat)
    mkvdfhr_qe(date, lat)

    mkqz(date, lat)
    mkttswr_qz(date, lat)
    mkttlwr_qz(date, lat)
    mklrghr_qz(date, lat)
    mkcnvhr_qz(date, lat)
    mkvdfhr_qz(date, lat)


main()
