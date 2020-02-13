import sys

sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src')
sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src/lapidary')
sys.path.append('/u/ugrads/mconstant/GdbCheckpoint/gdb_env/lib/python3.6/site-packages')

import gdb_chkpt

bmk = "600.perlbench_s"
interval = 1.06
chkpt_dir = "/u/ugrads/mconstant/research/latency_overlap/checkpoints/spec_cpu2017/600.perlbench_s"

args = [bmk, interval, chkpt_dir]

gdb_chkpt.start(args)
