module globals

    implicit none

    integer, parameter :: kp = 4

    integer, save :: nx
    integer, save :: ny
    integer, save :: nz

    integer, save :: year_ini
    integer, save :: year_fin
    integer, save :: yearnum
    integer, save :: varnum

    integer, save :: input_initialRecord

    character(256), save :: input_fname
    character(256), save :: clim_fname

end module globals

