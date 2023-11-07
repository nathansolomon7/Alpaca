#!/usr/bin/env python3
import os
import subprocess
import sys

#Get the list of argument exes
exes = sys.argv[1:]
if not exes:
    print(f"No input files provided. Usage: {sys.argv[0]} TESTNAME.exe [TESTNAME2.exe]...", file=sys.stderr)
    sys.exit(64)

#Run all the executables
fail = False
for exe in exes:
    out_path = exe[:-4] + ".out"
    
    if os.path.exists(out_path):
        process = subprocess.run(exe, capture_output=True, text=True)
        output = process.stdout 

        with open(out_path, 'r') as f:
            expected_output = f.read()

        if output == expected_output:
            print(f"Test passed for {exe}")
        else:
            print("stdout for ", exe, "was ", output)
            print(f"Test failed for {exe} (stdout differed)")
            fail = True

    else:
        print(f"Expected output file for {exe} not found.", file=sys.stderr)
        fail = True

if fail:
    sys.exit(1)
else:
    sys.exit(0)
