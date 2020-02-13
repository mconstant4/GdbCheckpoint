import sys

for bmk in sys.argv[1:]:
    f = open(bmk + '.py', 'w')
    f.write('import sys\n\n')
    f.write('sys.path.append(\'/u/ugrads/mconstant/research/sim/GdbCheckpoint/src\')\n')            # GDB Checkpoint Source
    f.write('sys.path.append(\'/u/ugrads/mconstant/research/sim/GdbCheckpoint/src/lapidary\')\n')   # Lapidary Tool
    f.write('sys.path.append(\'/u/ugrads/mconstant/GdbCheckpoint/gdb_env/lib/python3.6/site-packages\')\n') # Python (for imports within GDB env)
    f.write('\n')
    f.write('import gdb_chkpt\n\n')
    f.write('bmk = "' + bmk + '"\n')
    f.write('interval = 1\n')
    f.write('chkpt_dir = "/u/ugrads/mconstant/research/latency_overlap/checkpoints/spec_cpu2017/' + bmk + '"\n')
    f.write('\n')
    f.write('args = [bmk, interval, chkpt_dir]\n\n')
    f.write('gdb_chkpt.start(args)\n')
