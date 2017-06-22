module prop

  implicit none

contains

  subroutine step(disp, model_padded, dt, dx, num_steps,   &
      nx_padded, source_len, source, num_pad)

    integer, intent (in) :: nx_padded
    integer, intent (in) :: source_len
    real, intent (in out), dimension (:, :) :: disp
    real, intent (in), dimension (:) :: model_padded
    real, intent (in) :: dt
    real, intent (in) :: dx
    real, intent (in), dimension (:)  :: source
    integer, intent (in) :: num_steps
    integer, intent (in) :: num_pad

    integer :: s
    integer :: i
    integer :: sx
    real :: f_xx

    sx = num_pad+1

    do s = 2, num_steps + 1
    do i = 9, nx_padded - 8
    f_xx = (                                                           &
      -735*disp(i-8, s)+15360*disp(i-7, s)                             &
      -156800*disp(i-6, s)+1053696*disp(i-5, s)                        & 
      -5350800*disp(i-4, s)+22830080*disp(i-3, s)                      & 
      -94174080*disp(i-2, s)+538137600*disp(i-1, s)                    & 
      -924708642*disp(i+0, s)                                          & 
      +538137600*disp(i+1, s)-94174080*disp(i+2, s)                    & 
      +22830080*disp(i+3, s)-5350800*disp(i+4, s)                      & 
      +1053696*disp(i+5, s)-156800*disp(i+6, s)                        & 
      +15360*disp(i+7, s)-735*disp(i+8, s))/(302702400*dx**2)
    disp(i, s+1) = (model_padded(i)**2 * dt**2 * f_xx + 2 * disp(i, s) - disp(i, s-1))
    end do

    if (s-1 <= source_len) then
      disp(sx, s+1) = disp(sx, s+1) + (model_padded(sx)**2 * dt**2       &
        * source(s-1))
    end if

    end do

  end subroutine step
end module prop
