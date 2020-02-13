from Benchmark import Benchmark
class perlbench_s_base(Benchmark):
	def __init__(self):
		self.binary = 'perlbench_s_base.mytest-m64'
		self.options = '-I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/600.perlbench_s/run/run_base_refspeed_mytest-m64.0000'
class speed_bwaves_base(Benchmark):
	def __init__(self):
		self.binary = 'speed_bwaves_base.mytest-m64'
		self.options = 'bwaves_1 '
		self.inp = 'bwaves_1.in '
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/603.bwaves_s/run/run_base_refspeed_mytest-m64.0000'
class mcf_s_base(Benchmark):
	def __init__(self):
		self.binary = 'mcf_s_base.mytest-m64'
		self.options = 'inp.in '
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/605.mcf_s/run/run_base_refspeed_mytest-m64.0000'
class cactuBSSN_s_base(Benchmark):
	def __init__(self):
		self.binary = 'cactuBSSN_s_base.mytest-m64'
		self.options = 'spec_ref.par  '
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/607.cactuBSSN_s/run/run_base_refspeed_mytest-m64.0000'
class lbm_s_base(Benchmark):
	def __init__(self):
		self.binary = 'lbm_s_base.mytest-m64'
		self.options = '2000 reference.dat 0 0 200_200_260_ldc.of'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/619.lbm_s/run/run_base_refspeed_mytest-m64.0000'
class omnetpp_s_base(Benchmark):
	def __init__(self):
		self.binary = 'omnetpp_s_base.mytest-m64'
		self.options = '-c General -r 0'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/620.omnetpp_s/run/run_base_refspeed_mytest-m64.0000'
class wrf_s_base(Benchmark):
	def __init__(self):
		self.binary = 'wrf_s_base.mytest-m64'
		self.options = None
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/621.wrf_s/run/run_base_refspeed_mytest-m64.0000'
class xalancbmk_s_base(Benchmark):
	def __init__(self):
		self.binary = 'xalancbmk_s_base.mytest-m64'
		self.options = '-v t5.xml xalanc.xsl'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/623.xalancbmk_s/run/run_base_refspeed_mytest-m64.0000'
class x264_s_base(Benchmark):
	def __init__(self):
		self.binary = 'x264_s_base.mytest-m64'
		self.options = '--pass 1 --stats x264_stats.log --bitrate 1000 --frames 1000 -o BuckBunny_New.264 BuckBunny.yuv 1280x720'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/625.x264_s/run/run_base_refspeed_mytest-m64.0000'
class cam4_s_base(Benchmark):
	def __init__(self):
		self.binary = 'cam4_s_base.mytest-m64'
		self.options = None
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/627.cam4_s/run/run_base_refspeed_mytest-m64.0000'
class speed_pop2_base(Benchmark):
	def __init__(self):
		self.binary = 'speed_pop2_base.mytest-m64'
		self.options = None
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/628.pop2_s/run/run_base_refspeed_mytest-m64.0000'
class deepsjeng_s_base(Benchmark):
	def __init__(self):
		self.binary = 'deepsjeng_s_base.mytest-m64'
		self.options = 'ref.txt'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/631.deepsjeng_s/run/run_base_refspeed_mytest-m64.0000'
class imagick_s_base(Benchmark):
	def __init__(self):
		self.binary = 'imagick_s_base.mytest-m64'
		self.options = '-limit disk 0 refspeed_input.tga -resize 817% -rotate -2.76 -shave 540x375 -alpha remove -auto-level -contrast-stretch 1x1% -colorspace Lab -channel R -equalize +channel -colorspace sRGB -define histogram:unique-colors=false -adaptive-blur 0x5 -despeckle -auto-gamma -adaptive-sharpen 55 -enhance -brightness-contrast 10x10 -resize 30% refspeed_output.tga'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/638.imagick_s/run/run_base_refspeed_mytest-m64.0000'
class leela_s_base(Benchmark):
	def __init__(self):
		self.binary = 'leela_s_base.mytest-m64'
		self.options = 'ref.sgf'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/641.leela_s/run/run_base_refspeed_mytest-m64.0000'
class nab_s_base(Benchmark):
	def __init__(self):
		self.binary = 'nab_s_base.mytest-m64'
		self.options = '3j1n 20140317 220'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/644.nab_s/run/run_base_refspeed_mytest-m64.0000'
class exchange2_s_base(Benchmark):
	def __init__(self):
		self.binary = 'exchange2_s_base.mytest-m64'
		self.options = '6'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/648.exchange2_s/run/run_base_refspeed_mytest-m64.0000'
class fotonik3d_s_base(Benchmark):
	def __init__(self):
		self.binary = 'fotonik3d_s_base.mytest-m64'
		self.options = None
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/649.fotonik3d_s/run/run_base_refspeed_mytest-m64.0000'
class sroms_base(Benchmark):
	def __init__(self):
		self.binary = 'sroms_base.mytest-m64'
		self.options = ' '
		self.inp = 'ocean_benchmark3.in '
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/654.roms_s/run/run_base_refspeed_mytest-m64.0000'
class xz_s_base(Benchmark):
	def __init__(self):
		self.binary = 'xz_s_base.mytest-m64'
		self.options = 'cpu2006docs.tar.xz 6643 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1036078272 1111795472 4'
		self.inp = None
		self.cwd = '/u/ugrads/mconstant/Benchmarks/spec_cpu2017/benchspec/CPU/657.xz_s/run/run_base_refspeed_mytest-m64.0000'

class Spec_CPU2017:
    benchmarks = {
        '600.perlbench_s'   : perlbench_s_base(),
        '603.bwaves_s'      : speed_bwaves_base(),
        '605.mcf_s'         : mcf_s_base(),
        '607.cactuBSSN_s'   : cactuBSSN_s_base(),
        '619.lbm_s'         : lbm_s_base(),
        '620.omnetpp_s'     : omnetpp_s_base(),
        '621.wrf_s'         : wrf_s_base(),
        '623.xalancbmk_s'   : xalancbmk_s_base(),
        '625.x264_s'        : x264_s_base(),
        '627.cam4_s'        : cam4_s_base(),
        '628.pop2_s'        : speed_pop2_base(),
        '631.deepsjeng_s'   : deepsjeng_s_base(),
        '638.imagick_s'     : imagick_s_base(),
        '641.leela_s'       : leela_s_base(),
        '644.nab_s'         : nab_s_base(),
        '648.exchange2_s'   : exchange2_s_base(),
        '649.fotonik3d_s'   : fotonik3d_s_base(),
        '654.roms_s'        : sroms_base(),
        '657.xz_s'          : xz_s_base()
    }
