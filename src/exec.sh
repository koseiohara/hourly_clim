#!/bin/bash

#PBS -q tqueue
#PBS -N hourly_clim
#PBS -j oe
#PBS -l nodes=1:ppn=1

JOBNAME=c_kz_ae_clim
NOW=$(date "+%Y%m%d_%H%M%S")
RESULT_FILE="../output/result_${JOBNAME}_${NOW}.txt"

cd /mnt/hail8/kosei/mim/energetics/hourly_clim/src

./EXE >& ${RESULT_FILE}

