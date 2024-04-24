module leapYear

    implicit none

    private
    public :: isLeap

    contains


    function isLeap(year) result(output)
        integer, intent(in) :: year
        logical :: output

        if (mod(year, 4) /= 0) then
            output = .False.
            return
        else if (mod(year, 100) == 0 .and. mod(year, 400) /= 0) then
            output = .False.
            return
        else
            output = .True.
        endif
    
    end function isLeap


end module leapYear

