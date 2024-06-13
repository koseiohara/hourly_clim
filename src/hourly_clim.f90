module hourly_clim

    use fileio , only : finfo, fopen, fclose, fread, fwrite, reset_record
    use globals, only : kp, nx, ny, nz                                            , &
                      & datayear_ini, climyear_ini, climyear_fin, yearnum, hournum, &
                      & varnum, input_initialRecord, input_fname, clim_fname      , &
                      & mode
    use leapYear, only : isLeap

    implicit none

    private
    public :: compute_clim


    integer :: debugUnit

    contains


    subroutine compute_clim()
        type(finfo) :: input_file
        type(finfo) :: clim_file

        if (mode == 'DEBUG' .or. mode == 'BOTH') then
            call debug_open()
        endif
        
        call fopen(ftype  =input_file         , &  !! OUT
                 & fname  =input_fname        , &  !! IN
                 & action ='read'             , &  !! IN
                 & recl   =kp*nx*ny*nz        , &  !! IN
                 & record =input_initialRecord, &  !! IN
                 & recstep=0                    )  !! IN

        call fopen(clim_file          , &  !! OUT
                 & fname  =clim_fname , &  !! IN
                 & action ='write'    , &  !! IN
                 & recl   =kp*nx*ny*nz, &  !! IN
                 & record =1          , &  !! IN
                 & recstep=1            )  !! IN
        
        call skip_year(input_file)  !! INOUT


        call clim_before_leap(input_file, &  !! INOUT
                            &  clim_file  )  !! INOUT

        call clim_leap(       input_file, &  !! INOUT
                            &  clim_file  )  !! INOUT

        call clim_after_leap( input_file, &  !! INOUT
                            &  clim_file  )  !! INOUT


        call fclose(input_file)  !! INOUT
        call fclose( clim_file)  !! INOUT

        if (mode == 'DEBUG' .or. mode == 'BOTH') then
            call debug_close()
        endif

    end subroutine compute_clim


    subroutine clim_before_leap(input_file, clim_file)
        type(finfo), intent(inout) :: input_file
        type(finfo), intent(inout) :: clim_file
        
        real(kp) :: reader(nx,ny,nz)
        real(kp) :: clim(nx,ny,nz)

        !integer, parameter :: hournum_per_day = 4
        integer, parameter :: daynum_before_leap = 31+28
        integer :: hournum_before_leap
        integer :: hourcounter
        integer :: yearcounter

        integer :: days2next
        integer :: hours2next
        integer :: record2next

        integer :: rec_ini


        hournum_before_leap = daynum_before_leap * hournum

        do hourcounter = 1, hournum_before_leap

            rec_ini = input_file%record
            clim(1:nx,1:ny,1:nz) = 0._kp

            do yearcounter = climyear_ini, climyear_fin

                if (mode == 'DEBUG' .or. mode == 'BOTH') then
                    call debug_reclist(input_file%record)
                endif

                if (mode == 'COMPUTE' .or. mode == 'BOTH') then
                    call fread(input_file          , &  !! INOUT
                             & reader(1:nx,1:ny,1:nz))  !! OUT

                    clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)
                endif

                !if (isLeap(yearcounter)) then
                !    days2next = 366
                !else
                !    days2next = 365
                !endif
                !hours2next = days2next * hournum
                !record2next = hours2next * varnum

                call next_record(yearcounter, &  !! IN
                               & record2next  )  !! OUT

                call reset_record(input_file       , &  !! INOUT
                                & recstep=record2next)  !! IN

            enddo

            if (mode == 'DEBUG' .or. mode == 'BOTH') then
                call debug_linebreak()
            endif

            if (mode == 'COMPUTE' .or. mode == 'BOTH') then
                clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) / real(yearnum, kind=kp)
                call fwrite(clim_file         , &  !! INOUT
                          & clim(1:nx,1:ny,1:nz))  !! IN
            endif

            call reset_record(input_file            , &  !! INOUT
                            & newrecord=rec_ini+varnum)  !! IN

        enddo

    end subroutine clim_before_leap


    subroutine clim_leap(input_file, clim_file)
        type(finfo), intent(inout) :: input_file
        type(finfo), intent(inout) :: clim_file

        real(kp) :: reader(nx,ny,nz)
        real(kp) :: clim(nx,ny,nz)

        !integer, parameter :: hournum = 4
        integer :: hourcounter
        integer :: yearcounter

        integer :: leapNum

        integer :: days2next
        integer :: hours2next
        integer :: record2next

        integer :: rec_ini


        do hourcounter = 1, hournum

            rec_ini = input_file%record
            clim(1:nx,1:ny,1:nz) = 0._kp
            leapNum = 0

            do yearcounter = climyear_ini, climyear_fin

                if (isLeap(yearcounter)) then
                    
                    if (mode == 'DEBUG' .or. mode == 'BOTH') then
                        call debug_reclist(input_file%record)
                    endif

                    if (mode == 'COMPUTE' .or. mode == 'BOTH') then
                        call fread(input_file          , &  !! INOUT
                                 & reader(1:nx,1:ny,1:nz))  !! OUT

                        clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)
                        leapNum = leapNum + 1
                    endif

                    !days2next = 366

                else

                    if (mode == 'DEBUG' .or. mode == 'BOTH') then
                        call debug_reclist(0)
                    endif

                    !days2next = 365

                endif

                !hours2next = days2next * hournum
                !record2next = hours2next * varnum

                call next_record(yearcounter, &  !! IN
                               & record2next  )  !! OUT

                call reset_record(input_file       , &  !! INOUT
                                & recstep=record2next)  !! IN

            enddo

            if (mode == 'DEBUG' .or. mode == 'BOTH') then
                call debug_linebreak()
            endif

            if (mode == 'COMPUTE' .or. mode == 'BOTH') then
                clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) / real(leapNum, kind=kp)
                call fwrite(clim_file         , &  !! INOUT
                          & clim(1:nx,1:ny,1:nz))  !! IN
            endif

            call reset_record(input_file            , &  !! INOUT
                            & newrecord=rec_ini+varnum)  !! IN

        enddo

        if (.NOT. isLeap(climyear_ini)) then
            call reset_record(input_file           , &  !! INOUT
                            & recstep=-hournum*varnum)  !! IN
        endif

    end subroutine clim_leap


    subroutine clim_after_leap(input_file, clim_file)
        type(finfo), intent(inout) :: input_file
        type(finfo), intent(inout) :: clim_file
        
        real(kp) :: reader(nx,ny,nz)
        real(kp) :: clim(nx,ny,nz)

                                               !! MAR  APR  MAY  JUN  JUL  AUG  SEP  OCT  NOV  DEC
        integer, parameter :: daynum_before_leap = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        integer :: hournum_before_leap
        integer :: hourcounter
        integer :: yearcounter

        integer :: days2next
        integer :: hours2next
        integer :: record2next

        integer :: rec_ini

        hournum_before_leap = daynum_before_leap * hournum

        do hourcounter = 1, hournum_before_leap

            rec_ini = input_file%record
            clim(1:nx,1:ny,1:nz) = 0._kp

            do yearcounter = climyear_ini, climyear_fin

                if (mode == 'DEBUG' .or. mode == 'BOTH') then
                    call debug_reclist(input_file%record)
                endif

                if (mode == 'COMPUTE' .or. mode == 'BOTH') then
                    call fread(input_file          , &  !! INOUT
                             & reader(1:nx,1:ny,1:nz))  !! OUT

                    clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)
                endif

                !if (isLeap(yearcounter+1)) then
                !    days2next = 366
                !else
                !    days2next = 365
                !endif
                !hours2next = days2next * hournum
                !record2next = hours2next * varnum

                call next_record(yearcounter+1, &  !! IN
                               & record2next    )  !! OUT

                call reset_record(input_file       , &  !! INOUT
                                & recstep=record2next)  !! IN

            enddo

            if (mode == 'DEBUG' .or. mode == 'BOTH') then
                call debug_linebreak()
            endif

            if (mode == 'COMPUTE' .or. mode == 'BOTH') then
                clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) / real(yearnum, kind=kp)
                call fwrite(clim_file         , &  !! INOUT
                          & clim(1:nx,1:ny,1:nz))  !! IN
            endif

            call reset_record(input_file            , &  !! INOUT
                            & newrecord=rec_ini+varnum)  !! IN

        enddo

    end subroutine clim_after_leap


    subroutine skip_year(input_file)
        type(finfo), intent(inout) :: input_file

        integer :: year
        integer :: record2next

        do year = datayear_ini, climyear_ini-1
            call next_record(year     , &  !! IN
                           & record2next)  !! OUT

            call reset_record(input_file       , &  !! INOUT
                            & recstep=record2next)  !! IN
        enddo

    end subroutine skip_year


    subroutine next_record(year, record2next)
        integer, intent(in)  :: year
        integer, intent(out) :: record2next

        integer :: days2next
        integer :: hours2next

        if (isLeap(year)) then
            days2next = 366
        else
            days2next = 365
        endif
        
        hours2next = days2next * hournum
        record2next = hours2next * varnum

    end subroutine next_record


    subroutine debug_open()
        character(128), parameter :: debugFile = '../output/Debugger.txt'
        integer :: stat

        open(newunit=debugUnit, file=debugFile, action='write', iostat=stat)
        if (stat/=0) then
            write(*,'(a)')    'OpenFileError --------------------------------------------------'
            write(*,'(a)')    '|   Failed to open file'
            write(*,'(a)')    '|'
            write(*,'(a,i0)') '|   Unit     : ', debugUnit
            write(*,'(a)')    '|   FileName : ' // trim(debugFile)
            write(*,'(a)')    '|   Action   : write'
            write(*,'(a)')    '----------------------------------------------------------------'

            ERROR STOP
        endif

    end subroutine debug_open


    subroutine debug_reclist(record)
        integer, intent(in) :: record

        write(debugUnit,'(i10)',advance='no') record

    end subroutine debug_reclist


    subroutine debug_linebreak()

        write(debugUnit,*)

    end subroutine debug_linebreak


    subroutine debug_close()
    
        close(debugUnit)

    end subroutine debug_close


end module hourly_clim


