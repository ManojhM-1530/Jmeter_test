print("Hi, Master Manojh, Welcome to Jenkins")
import re
import sys

with open('Filewrite/results.jtl') as f:
    data = f.read()

errors = len(re.findall('false', data))
avg_response = float(re.search('sampleTime="(\d+)"', data).group(1))

if errors > 10:  # Example threshold
    print(f"Error threshold exceeded: {errors} errors")
    sys.exit(1)
    
if avg_response > 2000:  # 2 seconds
    print(f"Response time threshold exceeded: {avg_response}ms")
    sys.exit(1)
