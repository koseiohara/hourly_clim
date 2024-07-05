import matplotlib.pyplot as plt

from get_data import get_from_vint, get_from_gmean, get_datetime
from gmean_panels import plot_az, plot_kz, plot_w, plot_c_az_kz, plot_c_kz_w, plot_qe, plot_qz


ny = 145
nt = 366*4

def separate():

    date = get_datetime()

    
    ### AZ
    az = get_from_gmean(fname  ='../../output/JRA3Q_1980_2023_ALL_GMEAN_az.dat', \
                        recl   =4, \
                        rec    =1, \
                        kind   =4, \
                        endian ='LITTLE', \
                        recstep=1, \
                        nt     =nt)
    az = az*1e-6
    
    figaz = plt.figure(figsize=[8,4])
    axaz = figaz.add_subplot(111)
    plot_az(figaz, axaz, az, date, r'Global Mean $A_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', '')
    figaz.savefig('figs/JRA3Q_1980_2023_GMEAN_az_clim.png', dpi=350, bbox_inches='tight')

    
    ### KZ
    kz = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_kz.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       range_south=-90, \
                       range_north=90)
    kz = kz*1e-6

    figkz = plt.figure(figsize=[8,4])
    axkz = figkz.add_subplot(111)
    plot_kz(figkz, axkz, kz, date, r'Global Mean $K_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', '')
    figkz.savefig('figs/JRA3Q_1980_2023_GMEAN_kz_clim.png', dpi=350, bbox_inches='tight')


    ### W
    ke = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ke.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       range_south=-90, \
                       range_north=90)
    ke = ke*1e-6

    ae = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ae.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       range_south=-90, \
                       range_north=90)
    ae = ae*1e-6

    w = ke + ae

    figw = plt.figure(figsize=[8,4])
    axw = figw.add_subplot(111)
    plot_w(figw, axw, w, date, r'Global Mean $W \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', '')
    figw.savefig('figs/JRA3Q_1980_2023_GMEAN_w_clim.png', dpi=350, bbox_inches='tight')


    ### C(AZ, KZ)
    c_az_kz = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_c_az_kz.dat', \
                            recl   =4*ny, \
                            rec    =1, \
                            kind   =4, \
                            endian ='LITTLE', \
                            recstep=1, \
                            ny     =ny, \
                            nt     =nt, \
                            range_south=-90, \
                            range_north=90)

    figazkz = plt.figure(figsize=[8,4])
    axazkz = figazkz.add_subplot(111)
    plot_c_az_kz(figazkz, axazkz, c_az_kz, date, r'Global Mean $C\left(A_Z, K_Z\right) \:\left(\mathrm{W \: m^{-2}}\right)$', '')
    figkz.savefig('figs/JRA3Q_1980_2023_GMEAN_c_az_kz_clim.png', dpi=350, bbox_inches='tight')


    ### C(KZ, W)
    c_kz_w = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_c_kz_w.dat', \
                           recl   =4*ny, \
                           rec    =1, \
                           kind   =4, \
                           endian ='LITTLE', \
                           recstep=1, \
                           ny     =ny, \
                           nt     =nt, \
                           range_south=-90, \
                           range_north=90)

    figkzw = plt.figure(figsize=[8,4])
    axkzw = figkzw.add_subplot(111)
    plot_c_kz_w(figkzw, axkzw, c_kz_w, date, r'Global Mean $C\left(K_Z, W\right) \:\left(\mathrm{W \: m^{-2}}\right)$', '')
    figkz.savefig('figs/JRA3Q_1980_2023_GMEAN_c_az_kz_clim.png', dpi=350, bbox_inches='tight')


    ### QE
    qe = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_qe.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       range_south=-90, \
                       range_north=90)

    ttswr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttswr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          range_south=-90, \
                          range_north=90)

    ttlwr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttlwr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          range_south=-90, \
                          range_north=90)

    lrghr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_lrghr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     = ny, \
                          nt     =nt, \
                          range_south=-90, \
                          range_north=90)

    cnvhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_cnvhr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          range_south=-90, \
                          range_north=90)

    vdfhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_vdfhr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          range_south=-90, \
                          range_north=90)

    figqe = plt.figure(figsize=[8,4])
    axqe = figqe.add_subplot(111)
    plot_qe(figqe, axqe, qe, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, r'Global Mean $Q_E \:\left(\mathrm{W \: m^{-2}}\right)$', '')
    figqe.savefig('figs/JRA3Q_1980_2023_GMEAN_qe_clim.png', dpi=350, bbox_inches='tight')


    ### QZ
    qz = get_from_gmean(fname  ='../../output/JRA3Q_1980_2023_ALL_GMEAN_qz.dat', \
                       recl   =4, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       nt     =nt)

    ttswr = get_from_gmean(fname  ='../../output/JRA3Q_1980_2023_ALL_GMEAN_ttswr_qz.dat', \
                          recl   =4, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          nt     =nt)

    ttlwr = get_from_gmean(fname  ='../../output/JRA3Q_1980_2023_ALL_GMEAN_ttlwr_qz.dat', \
                          recl   =4, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          nt     =nt)

    lrghr = get_from_gmean(fname  ='../../output/JRA3Q_1980_2023_ALL_GMEAN_lrghr_qz.dat', \
                          recl   =4, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          nt     =nt)

    cnvhr = get_from_gmean(fname  ='../../output/JRA3Q_1980_2023_ALL_GMEAN_cnvhr_qz.dat', \
                          recl   =4, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          nt     =nt)

    vdfhr = get_from_gmean(fname  ='../../output/JRA3Q_1980_2023_ALL_GMEAN_vdfhr_qz.dat', \
                          recl   =4, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          nt     =nt)

    figqz = plt.figure(figsize=[8,4])
    axqz = figqz.add_subplot(111)
    plot_qz(figqz, axqz, qz, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, r'Global Mean $Q_Z \:\left(\mathrm{W \: m^{-2}}\right)$', '')
    figqz.savefig('figs/JRA3Q_1980_2023_GMEAN_qz_clim.png', dpi=350, bbox_inches='tight')


separate()


