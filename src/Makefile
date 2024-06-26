EXE = EXE
OBJS = globals.o interp.o NaNchecker.o fileio.o namelist.o leapYear.o hourly_clim.o main.o

FC = ifort
FLAGS = -warn all -O0 -assume byterecl -convert little_endian

%.o : %.f90
	${FC} -c $< ${FLAGS}

all : ${EXE}

${EXE} : ${OBJS}
	${FC} -o $@ $^


.PHONY : clean re run

clean :
	@ rm -fv *.o *.mod ${EXE}

re : clean all

run :
	./${EXE}

