dset ^JRA3Q_6hourly_clim_1980_2022_ke_VINT.dat
title MIM 366 CLIM
undef -9.99E33
options little_endian yrev

xdef 1 linear 0.0 1.25
ydef 145 linear -90. 1.25
zdef 1 linear 1 1
tdef 1464 linear 00Z01JAN2000 6hr

vars 1
ke 1 99 Ke 6hourly clim
endvars

