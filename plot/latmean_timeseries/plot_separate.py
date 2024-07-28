import matplotlib.pyplot as plt

from get_data import get_from_vint, get_from_gmean, get_datetime
from gmean_panels import plot_az, plot_kz, plot_w, plot_c_az_kz, plot_c_kz_w, plot_qe, plot_qz
from decolate import decolate


ny = 145
nt = 366*4

def separate():

    date = get_datetime()

    
    ### AZ
    nh = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_az.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=0, \
                       range_north=90)
    sh = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_az.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=-90., \
                       range_north=0.)
    nh = nh*1e-6
    sh = sh*1e-6
    
    figaz = plt.figure(figsize=[8,4])
    axaz = figaz.add_subplot(111)

    axaz.plot(date,    nh, color='blue' , label='NH')
    axaz.plot(date,    sh, color='red'  , label='SH')
    axaz.plot(date, nh+sh, color='black', label='Global')
    decolate(axaz, r'$A_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', '', date, 0., 4., 1, 0.5)
    axaz.legend(bbox_to_anchor=[0.5,-0.11], loc='upper center', borderaxespad=0, ncol=3)
    #plot_az(figaz, axaz, az, date, title=r'Global Mean $A_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$')
    figaz.savefig('figs/JRA3Q_1980_2023_az_NSG_clim.png', dpi=350, bbox_inches='tight')

    
    ### KZ
    nh = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_kz.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=0, \
                       range_north=90)
    sh = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_kz.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=-90, \
                       range_north=0)
    nh = nh*1e-6
    sh = sh*1e-6

    figkz = plt.figure(figsize=[8,4])
    axkz = figkz.add_subplot(111)

    axkz.plot(date,    nh, color='blue' , label='NH')
    axkz.plot(date,    sh, color='red'  , label='SH')
    axkz.plot(date, nh+sh, color='black', label='Global')
    decolate(axkz, r'$K_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', '', date, 0., 1., 1, 0.1)
    axkz.legend(bbox_to_anchor=[0.5,-0.11], loc='upper center', borderaxespad=0, ncol=3)
    #plot_kz(figkz, axkz, kz, date, title=r'Global Mean $K_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$')
    figkz.savefig('figs/JRA3Q_1980_2023_kz_NSG_clim.png', dpi=350, bbox_inches='tight')


    ### W
    nhk = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ke.dat', \
                        recl   =4*ny, \
                        rec    =1, \
                        kind   =4, \
                        endian ='LITTLE', \
                        recstep=1, \
                        ny     =ny, \
                        nt     =nt, \
                        latstep=1.25, \
                        range_south=0, \
                        range_north=90)
    shk = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ke.dat', \
                        recl   =4*ny, \
                        rec    =1, \
                        kind   =4, \
                        endian ='LITTLE', \
                        recstep=1, \
                        ny     =ny, \
                        nt     =nt, \
                        latstep=1.25, \
                        range_south=-90, \
                        range_north=0)
    nhk = nhk*1e-6
    shk = shk*1e-6

    nha = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ae.dat', \
                        recl   =4*ny, \
                        rec    =1, \
                        kind   =4, \
                        endian ='LITTLE', \
                        recstep=1, \
                        ny     =ny, \
                        nt     =nt, \
                        latstep=1.25, \
                        range_south=0, \
                        range_north=90)
    sha = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ae.dat', \
                        recl   =4*ny, \
                        rec    =1, \
                        kind   =4, \
                        endian ='LITTLE', \
                        recstep=1, \
                        ny     =ny, \
                        nt     =nt, \
                        latstep=1.25, \
                        range_south=-90, \
                        range_north=0)
    nha = nha*1e-6
    sha = sha*1e-6

    nh = nhk + nha
    sh = shk + sha

    figw = plt.figure(figsize=[8,4])
    axw = figw.add_subplot(111)

    axw.plot(date,    nh, color='blue' , label='NH')
    axw.plot(date,    sh, color='red'  , label='SH')
    axw.plot(date, nh+sh, color='black', label='Global')
    decolate(axw, r'$W \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', '', date, 0., 1.7, 1, 0.2)
    axw.legend(bbox_to_anchor=[0.5,-0.11], loc='upper center', borderaxespad=0, ncol=3)
    #plot_w(figw, axw, w, date, title=r'Global Mean $W \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$')
    figw.savefig('figs/JRA3Q_1980_2023_w_NSG_clim.png', dpi=350, bbox_inches='tight')


    ### C(AZ, KZ)
    nh = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_c_az_kz.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=0, \
                       range_north=90)
    sh = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_c_az_kz.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=-90, \
                       range_north=0)

    figazkz = plt.figure(figsize=[8,4])
    axazkz = figazkz.add_subplot(111)

    axazkz.plot(date,    nh, color='blue' , label='NH')
    axazkz.plot(date,    sh, color='red'  , label='SH')
    axazkz.plot(date, nh+sh, color='black', label='Global')
    decolate(axazkz, r'$C\left(A_Z, K_Z\right) \:\left(\mathrm{W \: m^{-2}}\right)$', '', date, 0., 2.2, 1, 0.3)
    axazkz.legend(bbox_to_anchor=[0.5,-0.11], loc='upper center', borderaxespad=0, ncol=3)
    #plot_c_az_kz(figazkz, axazkz, c_az_kz, date, title=r'Global Mean $C\left(A_Z, K_Z\right) \:\left(\mathrm{W \: m^{-2}}\right)$')
    figazkz.savefig('figs/JRA3Q_1980_2023_c_az_kz_NSG_clim.png', dpi=350, bbox_inches='tight')


    ### C(KZ, W)
    nh = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_c_kz_w.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=0, \
                       range_north=90)
    sh = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_c_kz_w.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=-90, \
                       range_north=0)

    figkzw = plt.figure(figsize=[8,4])
    axkzw = figkzw.add_subplot(111)

    axkzw.plot(date,    nh, color='blue' , label='NH')
    axkzw.plot(date,    sh, color='red'  , label='SH')
    axkzw.plot(date, nh+sh, color='black', label='Global')
    decolate(axkzw, r'$C\left(K_Z, W\right) \:\left(\mathrm{W \: m^{-2}}\right)$', '', date, -0.2, 1.2, 1, 0.2)
    axkzw.legend(bbox_to_anchor=[0.5,-0.11], loc='upper center', borderaxespad=0, ncol=3)
    #plot_c_kz_w(figkzw, axkzw, c_kz_w, date, title=r'Global Mean $C\left(K_Z, W\right) \:\left(\mathrm{W \: m^{-2}}\right)$')
    figkzw.savefig('figs/JRA3Q_1980_2023_c_kz_w_NSG_clim.png', dpi=350, bbox_inches='tight')


    ### QE
    qe = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_qe.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=0, \
                       range_north=90)

    ttswr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttswr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    ttlwr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttlwr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    lrghr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_lrghr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     = ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    cnvhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_cnvhr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    vdfhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_vdfhr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    fignhqe = plt.figure(figsize=[8,4])
    axnhqe = fignhqe.add_subplot(111)
    plot_qe(fignhqe, axnhqe, qe, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, title=r'NH Mean $Q_E \:\left(\mathrm{W \: m^{-2}}\right)$')
    fignhqe.savefig('figs/JRA3Q_1980_2023_qe_NH_clim.png', dpi=350, bbox_inches='tight')


    qe = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_qe.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=-90, \
                       range_north=0)

    ttswr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttswr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    ttlwr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttlwr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    lrghr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_lrghr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     = ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    cnvhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_cnvhr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    vdfhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_vdfhr_qe.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    figshqe = plt.figure(figsize=[8,4])
    axshqe = figshqe.add_subplot(111)
    plot_qe(figshqe, axshqe, qe, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, title=r'SH Mean $Q_E \:\left(\mathrm{W \: m^{-2}}\right)$')
    figshqe.savefig('figs/JRA3Q_1980_2023_qe_SH_clim.png', dpi=350, bbox_inches='tight')


    ### QZ
    qz = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_qz.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=0, \
                       range_north=90)

    ttswr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttswr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    ttlwr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttlwr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    lrghr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_lrghr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    cnvhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_cnvhr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    vdfhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_vdfhr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=0, \
                          range_north=90)

    fignhqz = plt.figure(figsize=[8,4])
    axnhqz = fignhqz.add_subplot(111)
    plot_qz(fignhqz, axnhqz, qz, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, title=r'NH Mean $Q_Z \:\left(\mathrm{W \: m^{-2}}\right)$')
    fignhqz.savefig('figs/JRA3Q_1980_2023_qz_NH_clim.png', dpi=350, bbox_inches='tight')


    qz = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_qz.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=1.25, \
                       range_south=-90, \
                       range_north=0)

    ttswr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttswr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    ttlwr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ttlwr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    lrghr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_lrghr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    cnvhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_cnvhr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    vdfhr = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_vdfhr_qz.dat', \
                          recl   =4*ny, \
                          rec    =1, \
                          kind   =4, \
                          endian ='LITTLE', \
                          recstep=1, \
                          ny     =ny, \
                          nt     =nt, \
                          latstep=1.25, \
                          range_south=-90, \
                          range_north=0)

    figshqz = plt.figure(figsize=[8,4])
    axshqz = figshqz.add_subplot(111)
    plot_qz(figshqz, axshqz, qz, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, title=r'SH Mean $Q_Z \:\left(\mathrm{W \: m^{-2}}\right)$')
    figshqz.savefig('figs/JRA3Q_1980_2023_qz_SH_clim.png', dpi=350, bbox_inches='tight')




separate()




