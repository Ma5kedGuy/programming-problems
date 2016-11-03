from __future__ import print_function

time = raw_input().strip().split(":")
hh = int(time[0])
if time[2][-2] == 'P' and hh != 12:
    hh += 12
elif time[2][-2] == 'A' and hh == 12:
    hh = 0
print('{0:02d}'.format(hh), ":", time[1], ":", time[2][:-2], sep='')
