#!/usr/bin/env python3

import sys, os
import subprocess

with open(sys.argv[1]) as file:
  for line in file.readlines():
    old_name = line.strip('/data/\n')
    new_name = old_name.replace("jane", "jdoe")
    subprocess.run(["mv", os.path.expanduser('~') + "/data/" + old_name, os.path.expanduser('~') + "/data/" + new_name])
