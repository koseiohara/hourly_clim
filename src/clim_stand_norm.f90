module clim_stand_norm

    use fileio , only : fopen, fclose, fread, fwrite, reset_record
    use globals, only : kp, nx, ny, nz                              , &
                      & year_ini, year_fin, yearnum, varnum         , &
                      & input_initialRecord, input_fname, clim_fname
    use leapYear, only : isLeap

    implicit none

    private
    public ::

    contains


    subroutine mean_all()
        type(finfo) :: input_file
        type(finfo) :: clim_file

        
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


        call mean_before_leap(input_file, &  !! INOUT
                            &  clim_file  )  !! INOUT

        call mean_leap(input_file, &  !! INOUT
                     &  clim_file  )  !! INOUT

        call mean_after_leap(input_file, &  !! INOUT
                           &  clim_file  )  !! INOUT


        call fclose(input_file)  !! INOUT
        call fclose( clim_file)  !! INOUT

    end subroutine mean_all


    subroutine mean_before_leap(input_ftype, clim_file)
        type(finfo), intent(inout) :: input_ftype
        type(finfo), intent(inout) :: clim_file
        
        real(kp) :: reader(nx,ny,nz)
        real(kp) :: clim(nx,ny,nz)

        integer, parameter :: hournum_per_day = 4
        integer, parameter :: daynum_before_leap = 31+28
        integer, parameter :: hournum_before_leap = daynum_before_leap * hournum_per_day
        integer :: hourcounter
        integer :: yearcounter

        integer :: days2next
        integer :: hours2next
        integer :: record2next

        integer :: rec_ini


        do hourcounter = 1, hournum_before_leap

            rec_ini = input_file%record
            clim(1:nx,1:ny,1:nz) = 0._kp

            do yearcounter = year_ini, year_fin

                call fread(input_file          , &  !! INOUT
                         & reader(1:nx,1:ny,1:nz))  !! OUT

                clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)

                if (isLeap(yearcounter)) then
                    days2next = 366
                else
                    days2next = 365
                endif
                hours2next = days2next * hournum_per_day
                record2next = hours2next * varnum

                call reset_record(input_file       , &  !! INOUT
                                & recstep=record2next)  !! IN

            enddo

            clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) / real(yearnum, kind=kp)
            call fwrite(clim_file         , &  !! INOUT
                      & clim(1:nx,1:ny,1:nz))  !! IN

            call reset_record(input_file            , &  !! INOUT
                            & newrecord=rec_ini+varnum)  !! IN

        enddo

    end subroutine mean_before_leap


    subroutine mean_in_leap(input_ftype, clim_file)
        type(finfo), intent(inout) :: input_ftype
        type(finfo), intent(inout) :: clim_file

        real(kp) :: reader(nx,ny,nz)
        real(kp) :: clim(nx,ny,nz)

        integer, parameter :: hournum = 4
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

                if (isLeap(yearcounter) then
                    
                    call fread(input_file          , &
                             & reader(1:nx,1:ny,1:nz))

                    clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)
                    leapNum = leapNum + 1

                    days2next = 366

                else

                    days2next = 365

                endif
                hours2next = days2next * hournum
                record2next = hours2next * varnum

                call reset_record(input_file       , &  !! INOUT
                                & recstep=record2next)  !! IN

            enddo

            clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) / real(leapNum, kind=kp)
            call fwrite(clim_file         , &  !! INOUT
                      & clim(1:nx,1:ny,1:nz))  !! IN

            call reset_record(input_file            , &  !! INOUT
                            & newrecord=rec_ini+varnum)  !! IN

        enddo

    end subroutine mean_in_leap


    subroutine mean_after_leap(input_ftype, clim_file)
        type(finfo), intent(inout) :: input_ftype
        type(finfo), intent(inout) :: clim_file
        
        real(kp) :: reader(nx,ny,nz)
        real(kp) :: clim(nx,ny,nz)

        integer, parameter :: hournum_per_day = 4
                                               !! MAR  APR  MAY  JUN  JUL  AUG  SEP  OCT  NOV  DEC
        integer, parameter :: daynum_before_leap = 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        integer, parameter :: hournum_before_leap = daynum_before_leap * hournum_per_day
        integer :: hourcounter
        integer :: yearcounter

        integer :: days2next
        integer :: hours2next
        integer :: record2next

        integer :: rec_ini


        do hourcounter = 1, hournum_before_leap

            rec_ini = input_file%record
            clim(1:nx,1:ny,1:nz) = 0._kp

            do yearcounter = year_ini, year_fin

                call fread(input_file          , &  !! INOUT
                         & reader(1:nx,1:ny,1:nz))  !! OUT

                clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) + reader(1:nx,1:ny,1:nz)

                if (isLeap(yearcounter+1)) then
                    days2next = 366
                else
                    days2next = 365
                endif
                hours2next = days2next * hournum_per_day
                record2next = hours2next * varnum

                call reset_record(input_file       , &  !! INOUT
                                & recstep=record2next)  !! IN

            enddo

            clim(1:nx,1:ny,1:nz) = clim(1:nx,1:ny,1:nz) / real(yearnum, kind=kp)
            call fwrite(clim_file         , &  !! INOUT
                      & clim(1:nx,1:ny,1:nz))  !! IN

            call reset_record(input_file            , &  !! INOUT
                            & newrecord=rec_ini+varnum)  !! IN

        enddo

    end subroutine mean_after_leap


end module clim_stand_norm


