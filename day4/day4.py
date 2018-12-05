import re
import pandas as pd
import numpy as np

# Parse out the input with two regexpressions, one for guard number, and one for the string in general

expression1 = r".(\d+).(\d+).(\d+).(\d+).(\d+)..(.+)"
expression2 = r"Guard #(\d+)"
rx1 = re.compile(expression1)
rx2 = re.compile(expression2)
file_path = r"C:\Users\Reid\Code\adventofcode\day4\input.txt"
data = []
with open(file_path, 'r') as file:
	line = file.readline()
	while line:	
		match_object1 = rx1.search(line)
		action_string = match_object1.group(6)
		
		if "falls asleep" in action_string:
			action = 0
		else:
			action = 1
		
		match_object2 = rx2.search(action_string)
		if match_object2:
			guard_id = int(match_object2.group(1))
		else:
			guard_id = None
		
		row = {
			"year":   int(match_object1.group(1)),
			"month":  int(match_object1.group(2)),
			"day":    int(match_object1.group(3)),
			"hour":   int(match_object1.group(4)),
			"minute": int(match_object1.group(5)),
			"guard_id": guard_id,
			"action": action
		}
		data.append(row)
		line = file.readline()

data = pd.DataFrame(data)

# 1518 isnt a valid year in nanosecond precision, but year is constant so make it valid
data["year"] = data["year"] + 500 

# create sortable date time series using date-time pandas util
data["time"] = pd.to_datetime(data[["year","month","day","hour","minute"]])
data = data.sort_values(["time"])

# fill in NaN guard numbers
for index, row in data.iterrows():
	guard_id = row["guard_id"]
	if np.isnan(guard_id):
		data["guard_id"][index] = guard_id_most_recent
	else:
		guard_id_most_recent = guard_id
		
# resort 		
data = data.sort_values(["guard_id","time"])

# CALCULATE number of minutes that each guard is asleep and when they were asleep using ndarray
# setup first iteration
guard_ct = 0
guard_list = []
guard_dict = {"id":data["guard_id"][0]}
asleep = np.zeros(60)
for index, row in data.iterrows():
	# reset 
	if row["guard_id"] != guard_dict["id"]:
		guard_dict["asleep"] = asleep
		guard_dict["total_minutes_asleep"] = np.sum(asleep)
		guard_list.append(guard_dict)
		guard_dict = {"id":data["guard_id"][0]}
		asleep = np.zeros(60)
	# we only care about the sleeping guards
	if row["action"] == 0:
		next_row = data.iloc[index+1,:]
		first_minute = row["minute"]
		# check if last minute is end of hour
		if next_row["month"] > row["month"] or next_row["day"] > row["day"] or next_row["guard_id"] != row["guard_id"]:
			last_minute = 60
		else:
			last_minute = next_row["minute"]
		
		# add 1 to every index of ND array where guard is asleep
		asleep[first_minute:last_minute] += 1
	
# find the guard who is the most shleepy and his worst minute
total_minutes_asleep_max = 0
total_minutes_asleep_max_index = 0
for index, dict in enumerate(guard_list):
	if dict["total_minutes_asleep"] > total_minutes_asleep_max :
		total_minutes_asleep_max = dict["total_minutes_asleep"]
		total_minutes_asleep_max_index = index

worst_guard = guard_list[total_minutes_asleep_max_index]
worst_minute = np.argmax(worst_guard["asleep"])
print(f"Worst Guard ID: {worst_guard['id']}")
print(f"Worst Minute: {worst_minute}")
print(f"Answer: {worst_guard['id'] * worst_minute}")