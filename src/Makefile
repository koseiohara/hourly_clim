EXE = daily_clim
OBJS = NaNchecker.o fileio.o

FC = ifort
FLAGS = -warn all -O0 -assume byterecl -convert little_endian

%.o : %.f90
	${FC} -c $< ${FLAGS}

all : ${EXE}

${EXE} : ${OBJS}
	${FC} -o $@ $^


.PHONY : clean

clean :
	@ rm -fv *.o *.mod ${EXE}

