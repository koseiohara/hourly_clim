module globals

    implicit none

    integer, parameter :: kp = 4

    integer, save :: nx
    integer, save :: ny
    integer, save :: nz

    integer, save :: datayear_ini
    integer, save :: climyear_ini
    integer, save :: climyear_fin
    integer, save :: yearnum
    integer, save :: hournum
    
    integer, save :: varnum
    integer, save :: input_initialRecord

    character(256), save :: input_fname
    character(256), save :: clim_fname

    character(8), save :: mode

end module globals

