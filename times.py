import datetime
import pytest
import yaml

pytest.raises

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    
    #if end_time_s < start_time_s:
        #raise ValueError("time range {},{} is invalid.".format(start_time,end_time))
    
    if end_time_s<start_time_s:
        raise ValueError("time range {},{} is invalid.".format(start_time_s,end_time_s))

    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]

def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
    return overlap_time

'''
large = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
print(compute_overlap_time(large, short))
'''
'''
large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00",2,60)
print(large,short)
'''

file=open('./fixture.yaml')
data=yaml.load(file,Loader=yaml.FullLoader)
time_range_1 = []
for i in range(len(data)):
    time_range_1.append(data[i]['time_range_1'])

print(time_range_1)