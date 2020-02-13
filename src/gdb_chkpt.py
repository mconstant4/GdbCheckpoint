# URI Wrapper for Lapidary (https://github.com/efeslab/lapidary)
#
# TODO  Add the following command line args:
#           (1) Benchmark Suite/Name
#           (2) Interval
#           (3) Take Checkpoint (Bool)
#
# Author:   Matt Constant (mconstant@uri.edu)
# Date:     02/05/2020

import os
import sys
import signal
import gdb
from pathlib import Path

# TODO Auto-Generate These Somehow
sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src')            # GDB Checkpoint Source
sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src/lapidary')   # Lapidary Tool
sys.path.append('/u/ugrads/mconstant/GdbCheckpoint/gdb_env/lib/python3.6/site-packages') # Python (for imports within GDB env)

from Benchmark import Benchmark
from Spec_CPU2017 import Spec_CPU2017
from checkpoint.GDBEngine import GDBEngine

def sig_handler(sig, frame):
    # FIXME Does not capture SIGINT, GDB does.
    print('User Stopped')
    sys.exit(0)

def parse_args(args):
    benchmark = args[0]
    interval = args[1]
    chkpt_dir = args[2]

    return (benchmark, interval, chkpt_dir)

def run(bmk, interval, chkpt_dir):
    """ 
    Runs the benchmark, taking checkpoints every <interval> instructions. 
    @param bmk      Benchmark to run. See GdbCheckpoint/src/Benchmark.
    @param interval Number of instructions between checkpoints.

    """
    try:
        os.mkdir(chkpt_dir)
    except FileExistsError:
        print("File Already Exists, hopefully not overwriting anything")
        
    os.chdir(bmk.cwd)

    lapidary = GDBEngine('/u/ugrads/mconstant/testdir-1', True, True)

    gdb.execute('set print elements 0')
    gdb.execute('set follow-fork-mode child')
    gdb.execute('set print elements 200')
    gdb.execute('set pagination off')
    gdb.execute('set auto-load safe-path /')
    gdb.execute('exec-file {}'.format(bmk.binary))
    gdb.execute('file {}'.format(bmk.binary))
    gdb.execute('break main')

    if bmk.inp:
        gdb.execute('run {} < {}'.format(bmk.options, bmk.inp))
    else:
        gdb.execute('run {}'.format(bmk.options))

    lapidary.fs_base = lapidary._get_fs_base()
    lapidary.run_time(interval, chkpt_dir, 100, None, False)

def start(args):
    signal.signal(signal.SIGINT, sig_handler)

    (bmk, interval, chkpt_dir) = parse_args(args)
    bmk = Spec_CPU2017.benchmarks[bmk]

    run(bmk, interval, Path(chkpt_dir))
