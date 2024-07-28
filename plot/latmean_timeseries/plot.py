import matplotlib.pyplot as plt

from get_data import get_from_vint, get_from_gmean, get_datetime
from gmean_panels import plot_az, plot_kz, plot_w, plot_c_az_kz, plot_c_kz_w, plot_qe, plot_qz


ny = 145
nt = 366*4
latstep = 1.25

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
    plot_az(figaz, axaz, az, date, title=r'Global Mean $A_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$')
    figaz.savefig('figs/JRA3Q_1980_2023_az_GMEAN_clim.png', dpi=350, bbox_inches='tight')

    
    ### KZ
    kz = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_kz.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=latstep, \
                       range_south=-90, \
                       range_north=90)
    kz = kz*1e-6

    figkz = plt.figure(figsize=[8,4])
    axkz = figkz.add_subplot(111)
    plot_kz(figkz, axkz, kz, date, title=r'Global Mean $K_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$')
    figkz.savefig('figs/JRA3Q_1980_2023_kz_GMEAN_clim.png', dpi=350, bbox_inches='tight')


    ### W
    ke = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_ke.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=latstep, \
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
                       latstep=latstep, \
                       range_south=-90, \
                       range_north=90)
    ae = ae*1e-6

    w = ke + ae

    figw = plt.figure(figsize=[8,4])
    axw = figw.add_subplot(111)
    plot_w(figw, axw, w, date, title=r'Global Mean $W \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$')
    figw.savefig('figs/JRA3Q_1980_2023_w_GMEAN_clim.png', dpi=350, bbox_inches='tight')


    ### C(AZ, KZ)
    c_az_kz = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_c_az_kz.dat', \
                            recl   =4*ny, \
                            rec    =1, \
                            kind   =4, \
                            endian ='LITTLE', \
                            recstep=1, \
                            ny     =ny, \
                            nt     =nt, \
                            latstep=latstep, \
                            range_south=-90, \
                            range_north=90)

    figazkz = plt.figure(figsize=[8,4])
    axazkz = figazkz.add_subplot(111)
    plot_c_az_kz(figazkz, axazkz, c_az_kz, date, title=r'Global Mean $C\left(A_Z, K_Z\right) \:\left(\mathrm{W \: m^{-2}}\right)$')
    figazkz.savefig('figs/JRA3Q_1980_2023_c_az_kz_GMEAN_clim.png', dpi=350, bbox_inches='tight')


    ### C(KZ, W)
    c_kz_w = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_c_kz_w.dat', \
                           recl   =4*ny, \
                           rec    =1, \
                           kind   =4, \
                           endian ='LITTLE', \
                           recstep=1, \
                           ny     =ny, \
                           nt     =nt, \
                           latstep=latstep, \
                           range_south=-90, \
                           range_north=90)

    figkzw = plt.figure(figsize=[8,4])
    axkzw = figkzw.add_subplot(111)
    plot_c_kz_w(figkzw, axkzw, c_kz_w, date, title=r'Global Mean $C\left(K_Z, W\right) \:\left(\mathrm{W \: m^{-2}}\right)$')
    figkzw.savefig('figs/JRA3Q_1980_2023_c_kz_w_GMEAN_clim.png', dpi=350, bbox_inches='tight')


    ### QE
    qe = get_from_vint(fname  ='../../output/JRA3Q_1980_2023_ALL_VINT_qe.dat', \
                       recl   =4*ny, \
                       rec    =1, \
                       kind   =4, \
                       endian ='LITTLE', \
                       recstep=1, \
                       ny     =ny, \
                       nt     =nt, \
                       latstep=latstep, \
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
                          latstep=latstep, \
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
                          latstep=latstep, \
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
                          latstep=latstep, \
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
                          latstep=latstep, \
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
                          latstep=latstep, \
                          range_south=-90, \
                          range_north=90)

    figqe = plt.figure(figsize=[8,4])
    axqe = figqe.add_subplot(111)
    plot_qe(figqe, axqe, qe, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, title=r'Global Mean $Q_E \:\left(\mathrm{W \: m^{-2}}\right)$')
    figqe.savefig('figs/JRA3Q_1980_2023_qe_GMEAN_clim.png', dpi=350, bbox_inches='tight')


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
    plot_qz(figqz, axqz, qz, ttswr, ttlwr, lrghr, cnvhr, vdfhr, date, title=r'Global Mean $Q_Z \:\left(\mathrm{W \: m^{-2}}\right)$')
    figqz.savefig('figs/JRA3Q_1980_2023_qz_GMEAN_clim.png', dpi=350, bbox_inches='tight')


def allin():

    date = get_datetime()

    figen = plt.figure(figsize=[8,4])
    axazg = figen.add_subplot(331)
    axazn = figen.add_subplot(334)
    axazs = figen.add_subplot(337)
    axkzg = figen.add_subplot(332)
    axkzn = figen.add_subplot(335)
    axkzs = figen.add_subplot(338)
    axwsg = figen.add_subplot(333)
    axwsn = figen.add_subplot(336)
    axwss = figen.add_subplot(339)

    
    ### AZ
    azn = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_az.dat', \
                        recl       =4*ny, \
                        rec        =1, \
                        kind       =4, \
                        endian     ='LITTLE', \
                        recstep    =1, \
                        ny         =ny, \
                        nt         =nt, \
                        range_south=0, \
                        range_north=90)
    azs = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_az.dat', \
                        recl       =4*ny, \
                        rec        =1, \
                        kind       =4, \
                        endian     ='LITTLE', \
                        recstep    =1, \
                        ny         =ny, \
                        nt         =nt, \
                        range_south=-90, \
                        range_north=0)
    azn = azn*1e-6
    azs = azs*1e-6
    azg = azn + azs
    
    #figaz = plt.figure(figsize=[8,4])
    #axaz = figaz.add_subplot(111)
    plot_az(figen, axazg, azg, date, title=r'$A_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', legend='Global')
    plot_az(figen, axazn, azn, date, title='', legend='NH')
    plot_az(figen, axazs, azs, date, title='', legend='SH')
    #figaz.savefig('figs/JRA3Q_1980_2023_GMEAN_az_clim.png', dpi=350, bbox_inches='tight')

    
    ### KZ
    kzn = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_kz.dat', \
                        recl       =4*ny, \
                        rec        =1, \
                        kind       =4, \
                        endian     ='LITTLE', \
                        recstep    =1, \
                        ny         =ny, \
                        nt         =nt, \
                        range_south=0, \
                        range_north=90)
    kzs = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_kz.dat', \
                        recl       =4*ny, \
                        rec        =1, \
                        kind       =4, \
                        endian     ='LITTLE', \
                        recstep    =1, \
                        ny         =ny, \
                        nt         =nt, \
                        range_south=-90, \
                        range_north=0)
    kzn = kzn*1e-6
    kzs = kzs*1e-6
    kzg = kzn + kzs

    #figkz = plt.figure(figsize=[8,4])
    #axkz = figkz.add_subplot(111)
    #plot_kz(figkz, axkz, kz, date, r'Global Mean $K_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', '')
    plot_kz(figen, axkzg, kzg, date, title=r'$K_Z \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', legend='Global')
    plot_kz(figen, axkzn, kzn, date, title='', legend='NH')
    plot_kz(figen, axkzs, kzs, date, title='', legend='SH')
    #figkz.savefig('figs/JRA3Q_1980_2023_GMEAN_kz_clim.png', dpi=350, bbox_inches='tight')


    ### W
    ken = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_ke.dat', \
                        recl       =4*ny, \
                        rec        =1, \
                        kind       =4, \
                        endian     ='LITTLE', \
                        recstep    =1, \
                        ny         =ny, \
                        nt         =nt, \
                        range_south=0, \
                        range_north=90)
    kes = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_ke.dat', \
                        recl       =4*ny, \
                        rec        =1, \
                        kind       =4, \
                        endian     ='LITTLE', \
                        recstep    =1, \
                        ny         =ny, \
                        nt         =nt, \
                        range_south=-90, \
                        range_north=0)
    ken = ken*1e-6
    kes = kes*1e-6
    keg = ken + kes

    aen = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_ae.dat', \
                        recl       =4*ny, \
                        rec        =1, \
                        kind       =4, \
                        endian     ='LITTLE', \
                        recstep    =1, \
                        ny         =ny, \
                        nt         =nt, \
                        range_south=0, \
                        range_north=90)
    aes = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_ae.dat', \
                        recl       =4*ny, \
                        rec        =1, \
                        kind       =4, \
                        endian     ='LITTLE', \
                        recstep    =1, \
                        ny         =ny, \
                        nt         =nt, \
                        range_south=-90, \
                        range_north=0)
    aen = aen*1e-6
    aes = aes*1e-6
    aeg = aen + aes

    wn = ken + aen
    ws = kes + aes
    wg = wn + ws

    #figw = plt.figure(figsize=[8,4])
    #axw = figw.add_subplot(111)
    #plot_w(figw, axw, w, date, r'Global Mean $W \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', '')
    plot_w(figen, axwsg, wg, date, title=r'$W \:\left(10^6 \: \mathrm{J \: m^{-2}}\right)$', legend='Global')
    plot_w(figen, axwsn, wn, date, title='', legend='NH')
    plot_w(figen, axwss, ws, date, title='', legend='SH')
    #figw.savefig('figs/JRA3Q_1980_2023_GMEAN_w_clim.png', dpi=350, bbox_inches='tight')

    figen.savefig('figs/GLOBAL_NH_SH_mean_Az_Kz_W_Ae_Ke_JRA3Q_1980_2022_clim.png', dpi=350, bbox_inches='tight')


    figc = plt.figure(figsize=[8,6])
    axazkzg = figc.add_subplot(331)
    axazkzn = figc.add_subplot(334)
    axazkzs = figc.add_subplot(337)
    axkzwsg = figc.add_subplot(332)
    axkzwsn = figc.add_subplot(335)
    axkzwss = figc.add_subplot(338)
    axaekeg = figc.add_subplot(333)
    axaeken = figc.add_subplot(336)
    axaekes = figc.add_subplot(339)

    ### C(AZ, KZ)
    c_az_kz_n = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_c_az_kz.dat', \
                              recl       =4*ny, \
                              rec        =1, \
                              kind       =4, \
                              endian     ='LITTLE', \
                              recstep    =1, \
                              ny         =ny, \
                              nt         =nt, \
                              range_south=0, \
                              range_north=90)
    c_az_kz_s = get_from_vint(fname      ='../../output/JRA3Q_1980_2023_ALL_VINT_c_az_kz.dat', \
                              recl       =4*ny, \
                              rec        =1, \
                              kind       =4, \
                              endian     ='LITTLE', \
                              recstep    =1, \
                              ny         =ny, \
                              nt         =nt, \
                              range_south=-90, \
                              range_north=0)
    c_az_kz_g = c_az_kz_n + c_az_kz_s

    #figazkz = plt.figure(figsize=[8,4])
    #axazkz = figazkz.add_subplot(111)
    plot_c_az_kz(figc, axazkzg, c_az_kz_g, date, title=r'$C\left(A_Z, K_Z\right) \:\left(\mathrm{W \: m^{-2}}\right)$', legend='Global Mean')
    plot_c_az_kz(figc, axazkzn, c_az_kz_n, date, legend='Global Mean')
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




