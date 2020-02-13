import sys

sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src')
sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src/lapidary')
sys.path.append('/u/ugrads/mconstant/GdbCheckpoint/gdb_env/lib/python3.6/site-packages')

import gdb_chkpt

bmk = "607.cactuBSSN_s"
interval = 16.90
chkpt_dir = "/u/ugrads/mconstant/research/latency_overlap/checkpoints/spec_cpu2017/607.cactuBSSN_s"

args = [bmk, interval, chkpt_dir]

gdb_chkpt.start(args)
