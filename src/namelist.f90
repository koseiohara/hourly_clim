module namelist

    use globals, only : nx, ny, nz                 , &
                      & year_ini, year_fin, yearnum, &
                      & varnum, input_initialRecord, &
                      & input_fname, clim_fname

    implicit none

    private
    public :: read_nml

    contains


    subroutine read_nml()
        integer :: grid_unit
        integer :: yearinfo_unit
        integer :: recinfo_unit
        integer :: files_unit
        character(128), parameter :: grid_fname='../nml/grid.nml'
        character(128), parameter :: yearinfo_fname='../nml/yearinfo.nml'
        character(128), parameter :: recinfo_fname='../nml/recinfo.nml'
        character(128), parameter :: files_fname='../nml/files.nml'

        namelist / grid / nx, ny, nz
        namelist / yearinfo / year_ini, year_fin
        namelist / recinfo / varnum, input_initialRecord
        namelist / files / input_fname, clim_fname

        nx = 0
        ny = 0
        nz = 0

        year_ini = 0
        year_fin = 0

        varnum              = 0
        input_initialRecord = 0

        input_fname = ''
        clim_fname  = ''


        call open_nml(grid_unit, &  !! OUT
                    & grid_fname )  !! IN
        
        call open_nml(yearinfo_unit, &  !! OUT
                    & yearinfo_fname )  !! IN
        
        call open_nml(recinfo_unit, &  !! OUT
                    & recinfo_fname )  !! IN
        
        call open_nml(files_unit, &  !! OUT
                    & files_fname )  !! IN

        read(grid_unit    , nml=grid    )
        read(yearinfo_unit, nml=yearinfo)
        read(recinfo_unit , nml=recinfo )
        read(files_unit   , nml=files   )

        close(grid_unit    )
        close(yearinfo_unit)
        close(recinfo_unit )
        close(files_unit   )

        call checker()
        
        yearnum = year_fin - year_ini + 1

    end subroutine read_nml


    subroutine open_nml(unit, fname)
        integer, intent(out) :: unit
        character(*), intent(in) :: fname

        integer :: stat

        open(newunit=unit, file=fname, action='read', iostat=stat)
        if (stat/=0) then
            write(*,'(a)')    'OpenFileError ------------------------------------------'
            write(*,'(a)')    '|   Failed to open file'
            write(*,'(a)')    '|'
            write(*,'(a,i0)') '|   Unit     : ', unit
            write(*,'(a)')    '|   FileName : ' // trim(fname)
            write(*,'(a)')    '--------------------------------------------------------'

            ERROR STOP
        endif

    end subroutine open_nml


    subroutine checker()
        
        if (nx <= 0) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid nx value in namelist'
            write(*,'(a)')    '|   nx must be more than 0'
            write(*,'(a,i0)') '|   Input : nx=', nx
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (ny <= 0) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid ny value in namelist'
            write(*,'(a)')    '|   ny must be more than 0'
            write(*,'(a,i0)') '|   Input : ny=', ny
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (nz <= 0) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid nz value in namelist'
            write(*,'(a)')    '|   nz must be more than 0'
            write(*,'(a,i0)') '|   Input : nz=', nz
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (year_ini <= 1900) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid year_ini value in namelist'
            write(*,'(a)')    '|   year_ini must be more than 1900'
            write(*,'(a,i0)') '|   Input : year_ini=', year_ini
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (year_fin <= 1900) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid year_fin value in namelist'
            write(*,'(a)')    '|   year_fin must be more than 1900'
            write(*,'(a,i0)') '|   Input : year_fin=', year_fin
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (year_fin < year_ini) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid year_fin or year_fin value in namelist'
            write(*,'(a)')    '|   year_fin must be equal or more than year_ini'
            write(*,'(a,i0)') '|   Input : year_ini=', year_ini
            write(*,'(a,i0)') '|   Input : year_fin=', year_fin
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (varnum <= 0) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid varnum value in namelist'
            write(*,'(a)')    '|   varnum must be more than 0'
            write(*,'(a,i0)') '|   Input : varnum=', varnum
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (input_initialRecord  <= 0) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid input_initialRecord value in namelist'
            write(*,'(a)')    '|   input_initialRecord  must be more than 0'
            write(*,'(a,i0)') '|   Input : input_initialRecord =', input_initialRecord 
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (input_fname == '') then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid input_fname value in namelist'
            write(*,'(a)')    '|   input_fname is not specified'
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (clim_fname == '') then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid clim_fname value in namelist'
            write(*,'(a)')    '|   clim_fname is not specified'
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

    end subroutine checker


end module namelist

