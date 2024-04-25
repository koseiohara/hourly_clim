program main

    use namelist       , only : read_nml
    use clim_stand_norm, only : mean_all

    implicit none

    call read_nml()

    call mean_all()

end program main

