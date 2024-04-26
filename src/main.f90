program main

    use namelist   , only : read_nml
    use hourly_clim, only : compute_clim

    implicit none

    call read_nml()

    call compute_clim()

end program main

