import subprocess
import time
import numpy as np

s = np.random.poisson(1.0,53)
print s
for x in range(len(s)):
  subprocess.call(['./launch_clients'])
  time.sleep(s[x])
