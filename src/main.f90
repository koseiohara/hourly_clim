program main

    use namelist   , only : read_nml, tweet_setting
    use hourly_clim, only : compute_clim

    implicit none

    real(4) :: begin_time
    real(4) :: end_time

    call cpu_time(begin_time)

    call read_nml()

    call tweet_setting()

    call compute_clim()

    call cpu_time(end_time)

    write(*,'(a,f0.3,a)') 'Execution Time : ', end_time - begin_time, ' s'

end program main

