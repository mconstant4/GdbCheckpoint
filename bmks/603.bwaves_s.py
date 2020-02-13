import sys

sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src')
sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src/lapidary')
sys.path.append('/u/ugrads/mconstant/GdbCheckpoint/gdb_env/lib/python3.6/site-packages')

import gdb_chkpt

bmk = "603.bwaves_s"
interval = 24.83
chkpt_dir = "/u/ugrads/mconstant/research/latency_overlap/checkpoints/spec_cpu2017/603.bwaves_s"

args = [bmk, interval, chkpt_dir]

gdb_chkpt.start(args)
