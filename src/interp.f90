module interp

    use globals, only : kp, nx, ny, nz
    !use, intrinsic :: IEEE_ARITHMETIC, only : IEEE_IS_NAN => IEEE_IS_NAN
    use, intrinsic :: IEEE_ARITHMETIC, only : IEEE_IS_NAN => IEEE_IS_NAN

    implicit none

    private
    public :: interp_linear_y

    contains


    subroutine interp_linear_y(array)
        real(kp), intent(inout) :: array(nx,ny,nz)
       
        integer :: i
        integer :: j
        integer :: k


        do k = 1, nz
            if (IEEE_IS_NAN(array(1,1,k))) then
                do i = 2, nx
                    if (.NOT. IEEE_IS_NAN(array(1,i,k))) then
                        array(1,1,k) = array(1,i,k)
                        exit
                    endif
                enddo
                write(*,'("NaN at i="i0", j="i0", k="i0)') 1, 1, k
            endif

            do j = 2, ny-1
                if (IEEE_IS_NAN(array(1,j,k))) then

                    if (IEEE_IS_NAN(array(1,j-1,k))) then
                        array(1,j,k) = array(1,j+1,k)
                    else if (IEEE_IS_NAN(array(1,j+1,k))) then
                        array(1,j,k) = array(1,j-1,k)
                    else
                        array(1,j,k) = (array(1,j-1,k) + array(1,j+1,k)) * 0.5_kp
                    endif

                    write(*,'("NaN at i="i0", j="i0", k="i0)') 1, j, k
                endif
            enddo

            if (IEEE_IS_NAN(array(1,ny,k))) then
                do i = 1, ny-1
                    if (.NOT. IEEE_IS_NAN(array(1,ny-i,k))) then
                        array(1,ny,k) = array(1,ny-i,k)
                    endif
                enddo
                write(*,'("NaN at i="i0", j="i0", k="i0)') 1, ny, k
            endif
        enddo

    end subroutine interp_linear_y


end module interp

