Wrapper code for Lapidary tool (https://github.com/efeslab/lapidary)


To Run Benchmark:
	
	./run.sh <Benchmark Directory> <Benchmark Name>
		e.g. ./run.sh spec_cpu2017/benchspec/CPU/600.perlbench_s/run/run_base 600.perlbench_s

	Output is determined by chkpt_dir (set in bmks/<benchmark name>.py)

To Add Benchmarks:

	1)	create bmk python file in bmks directory. (<benchmark name>.py)
		Follow template provided by existing python file in bmks directory to create new benchmark.

	2)	create benchmark suite class in src directory (follow Spec_CPU2017.py as example)

	3)	Modify src/gdb_chkpt.py
		Currently only Spec_CPU2017 is imported.
			-> from <benchmark_suite_name> import <benchmrk_suite_name>
			-> change line 75 to search for benchmark from your benchmark suite.

