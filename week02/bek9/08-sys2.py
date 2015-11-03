# 08-sys2.py
import sys
args = sys.argv[1:]
for i in args:
	print(i.upper(), end=' ')
print()

# in CLI
# $ python3 08-sys2.py life is short
# LIFE IS SHORT