import sys

sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src')
sys.path.append('/u/ugrads/mconstant/research/sim/GdbCheckpoint/src/lapidary')
sys.path.append('/u/ugrads/mconstant/GdbCheckpoint/gdb_env/lib/python3.6/site-packages')

import gdb_chkpt

bmk = "620.omnetpp_s"
interval = 3.04
chkpt_dir = "/u/ugrads/mconstant/research/latency_overlap/checkpoints/spec_cpu2017/620.omnetpp_s"

args = [bmk, interval, chkpt_dir]

gdb_chkpt.start(args)
