#!/bin/bash

#PBS -q tqueue
#PBS -N hourly_clim
#PBS -j oe
#PBS -l nodes=1:ppn=1

VARNAME=qe
NOW=$(date "+%Y%m%d_%H%M%S")
RESULT_FILE="../output/result_${VARNAME}_${NOW}.txt"

cd /mnt/hail8/kosei/mim/energetics/hourly_clim/src

./EXE >& ${RESULT_FILE}


