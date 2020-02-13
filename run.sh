#!/bin/bash

EXE="/u/ugrads/mconstant/research/sim/GdbCheckpoint/bmks"

CWD=$1
BMK=$2
CHKPT=$3
INTERVAL=$4

cd $CWD

gdb -q -x $EXE/$BMK.py
