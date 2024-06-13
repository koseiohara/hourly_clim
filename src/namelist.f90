module namelist

    use globals, only : nx, ny, nz                              , &
                      & datayear_ini, climyear_ini, climyear_fin, &
                      & yearnum, hournum                        , &
                      & varnum, input_initialRecord             , &
                      & input_fname, clim_fname                 , &
                      & mode

    implicit none

    private
    public :: read_nml, tweet_setting

    contains


    subroutine read_nml()
        integer :: hourstep

        integer :: grid_unit
        integer :: tinfo_unit
        integer :: recinfo_unit
        integer :: files_unit
        integer :: execmode_unit
        character(128), parameter :: grid_fname='../nml/grid.nml'
        character(128), parameter :: tinfo_fname='../nml/tinfo.nml'
        character(128), parameter :: recinfo_fname='../nml/recinfo.nml'
        character(128), parameter :: files_fname='../nml/files.nml'
        character(128), parameter :: execmode_fname='../nml/execmode.nml'

        namelist / grid / nx, ny, nz
        namelist / tinfo / datayear_ini, climyear_ini, climyear_fin, hourstep
        namelist / recinfo / varnum, input_initialRecord
        namelist / files / input_fname, clim_fname
        namelist / execmode / mode

        nx = 0
        ny = 0
        nz = 0

        datayear_ini = 0
        climyear_ini = 0
        climyear_fin = 0
        hourstep = 0

        varnum              = 0
        input_initialRecord = 0

        input_fname = ''
        clim_fname  = ''

        mode = ''


        call open_nml(grid_unit    , &  !! OUT
                    & grid_fname     )  !! IN
        
        call open_nml(tinfo_unit   , &  !! OUT
                    & tinfo_fname    )  !! IN
        
        call open_nml(recinfo_unit , &  !! OUT
                    & recinfo_fname  )  !! IN
        
        call open_nml(files_unit   , &  !! OUT
                    & files_fname    )  !! IN

        call open_nml(execmode_unit, &  !! OUT
                    & execmode_fname )  !! IN

        read(grid_unit    , nml=grid    )
        read(tinfo_unit   , nml=tinfo   )
        read(recinfo_unit , nml=recinfo )
        read(files_unit   , nml=files   )
        read(execmode_unit, nml=execmode)

        close(grid_unit    )
        close(tinfo_unit   )
        close(recinfo_unit )
        close(files_unit   )
        close(execmode_unit)

        call checker(hourstep)
        
        yearnum = climyear_fin - climyear_ini + 1
        hournum = 24 / hourstep

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


    subroutine checker(hourstep)
        integer, intent(in) :: hourstep
        
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

        if (datayear_ini > climyear_ini) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid datayear_ini or climyear_ini value in namelist'
            write(*,'(a)')    '|   datayear_ini must be smaller than climyear_ini'
            write(*,'(a,i0)') '|   Input : datayear_ini=', datayear_ini
            write(*,'(a,i0)') '|   Input : climyear_ini=', climyear_ini
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (climyear_ini <= 1900) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid climyear_ini value in namelist'
            write(*,'(a)')    '|   climyear_ini must be more than 1900'
            write(*,'(a,i0)') '|   Input : climyear_ini=', climyear_ini
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (climyear_fin <= 1900) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid climyear_fin value in namelist'
            write(*,'(a)')    '|   climyear_fin must be more than 1900'
            write(*,'(a,i0)') '|   Input : climyear_fin=', climyear_fin
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (climyear_fin < climyear_ini) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid climyear_fin or climyear_fin value in namelist'
            write(*,'(a)')    '|   climyear_fin must be equal or more than climyear_ini'
            write(*,'(a,i0)') '|   Input : climyear_ini=', climyear_ini
            write(*,'(a,i0)') '|   Input : climyear_fin=', climyear_fin
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

        if (hourstep <= 0 .or. hourstep > 24) then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid hourstep value in namelist'
            write(*,'(a)')    '|   hourstep must be between 1 and 24'
            write(*,'(a,i0)') '|   Input : hourstep=', hourstep
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

        if (mode /= 'DEBUG' .and. mode /= 'COMPUTE' .and. mode /= 'BOTH') then
            write(*,'(a)')    'InputError ---------------------------------------------'
            write(*,'(a)')    '|   Invalid mode value in namelist'
            write(*,'(a)')    '|   mode must be "DEBUG", "COMPUTE", or "BOTH"'
            write(*,'(a)')    '|   Input : mode=' // trim(mode)
            write(*,'(a)')    '--------------------------------------------------------'
            
            ERROR STOP
        endif

    end subroutine checker


    subroutine tweet_setting()
        
        write(*,*)
        write(*,'(a)')      '---'
        write(*,'(a)')      ' INPUT  FILE : ' // trim(input_fname)
        write(*,'(a)')      ' OUTPUT FILE : ' // trim(clim_fname)
        write(*,'(a)')      '---'
        write(*,'(a,i0)')   ' NX = ', nx
        write(*,'(a,i0)')   ' NY = ', ny
        write(*,'(a,i0)')   ' NZ = ', nz
        write(*,'(a)')      '---'
        write(*,'(a,i0,a)') ' DATA START FROM ', datayear_ini, '/01/01 00:00:00'
        write(*,'(a,i0)')   ' INITIAL YEAR TO COMPUTE CLIM. : ', climyear_ini
        write(*,'(a,i0)')   ' FINAL   YEAR TO COMPUTE CLIM. : ', climyear_fin
        write(*,'(a,i0)')   ' HOUR STEP                     : ', 24/hournum
        write(*,'(a)')      '---'
        write(*,'(a,i0)')   ' NUMBER OF VARIABLES     : ', varnum
        write(*,'(a,i0)')   ' INITIAL RECORD OF INPUT : ', input_initialRecord
        write(*,'(a)')      '---'
        write(*,*)

    end subroutine tweet_setting


end module namelist

