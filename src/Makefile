EXE = daily_clim
OBJS = NaNchecker.o fileio.o globals.o namelist.o leapYear.o clim_stand_norm.o main.o

FC = ifort
FLAGS = -warn all -O0 -assume byterecl -convert little_endian

%.o : %.f90
	${FC} -c $< ${FLAGS}

all : ${EXE}

${EXE} : ${OBJS}
	${FC} -o $@ $^


.PHONY : clean re

clean :
	@ rm -fv *.o *.mod ${EXE}

re : clean all

