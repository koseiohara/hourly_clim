module hourly_clim

    use fileio , only : finfo, fopen, fclose, fread, fwrite, reset_record
    use globals, only : kp, nx, ny, nz                                    , &
                      & year_ini, year_fin, yearnum, hournum              , &
                      & varnum, input_initialRecord, input_fname, clim_fname
    use leapYear, only : isLeap

    implicit none

    private
    public :: compute_clim


    integer :: debugUnit

    contains


    subroutine compute_clim()
        type(finfo) :: input_file
        type(finfo) :: clim_file

        call debug_open()
        
        call fopen(input_file                 , &  !! OUT
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


        call clim_before_leap(input_file, &  !! INOUT
                            &  clim_file  )  !! INOUT

        call clim_leap(       input_file, &  !! INOUT
                            &  clim_file  )  !! INOUT

        call clim_after_leap( input_file, &  !! INOUT
                            &  clim_file  )  !! INOUT


        call fclose(input_file)  !! INOUT
        call fclose( clim_file)  !! INOUT

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

            do yearcounter = year_ini, year_fin

                call debug_reclist(input_file%record)

                !call fread(input_file          , &  !! INOUT
                !         & reader(1:nx,1:ny,1:nz))  !! OUT

                clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)

                if (isLeap(yearcounter)) then
                    days2next = 366
                else
                    days2next = 365
                endif
                hours2next = days2next * hournum
                record2next = hours2next * varnum

                call reset_record(input_file       , &  !! INOUT
                                & recstep=record2next)  !! IN

            enddo

            call debug_linebreak()

            clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) / real(yearnum, kind=kp)
            !call fwrite(clim_file         , &  !! INOUT
            !          & clim(1:nx,1:ny,1:nz))  !! IN

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

            do yearcounter = year_ini, year_fin

                if (isLeap(yearcounter)) then
                    
                    call debug_reclist(input_file%record)

                    !call fread(input_file          , &
                    !         & reader(1:nx,1:ny,1:nz))

                    clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)
                    leapNum = leapNum + 1

                    days2next = 366

                else

                    call debug_reclist(0)

                    days2next = 365

                endif
                !days2next = 366

                hours2next = days2next * hournum
                record2next = hours2next * varnum

                call reset_record(input_file       , &  !! INOUT
                                & recstep=record2next)  !! IN

            enddo

            call debug_linebreak()

            clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) / real(leapNum, kind=kp)
            !call fwrite(clim_file         , &  !! INOUT
            !          & clim(1:nx,1:ny,1:nz))  !! IN

            call reset_record(input_file            , &  !! INOUT
                            & newrecord=rec_ini+varnum)  !! IN

        enddo

        if (.NOT. isLeap(year_ini)) then
            call reset_record(input_file           , &  !! INOUT
                            & recstep=-hournum*varnum)  !! IN
        endif

    end subroutine clim_leap


    subroutine clim_after_leap(input_file, clim_file)
        type(finfo), intent(inout) :: input_file
        type(finfo), intent(inout) :: clim_file
        
        real(kp) :: reader(nx,ny,nz)
        real(kp) :: clim(nx,ny,nz)

        !integer, parameter :: hournum_per_day = 4
                                               !! MAR  APR  MAY  JUN  JUL  AUG  SEP  OCT  NOV  DEC
        integer, parameter :: daynum_before_leap = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        !integer, parameter :: hournum_before_leap = daynum_before_leap * hournum_per_day
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

            do yearcounter = year_ini, year_fin

                call debug_reclist(input_file%record)

                !call fread(input_file          , &  !! INOUT
                !         & reader(1:nx,1:ny,1:nz))  !! OUT

                clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)

                if (isLeap(yearcounter+1)) then
                    days2next = 366
                else
                    days2next = 365
                endif
                hours2next = days2next * hournum
                record2next = hours2next * varnum

                call reset_record(input_file       , &  !! INOUT
                                & recstep=record2next)  !! IN

            enddo

            call debug_linebreak()

            clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) / real(yearnum, kind=kp)
            !call fwrite(clim_file         , &  !! INOUT
            !          & clim(1:nx,1:ny,1:nz))  !! IN

            call reset_record(input_file            , &  !! INOUT
                            & newrecord=rec_ini+varnum)  !! IN

        enddo

    end subroutine clim_after_leap


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


