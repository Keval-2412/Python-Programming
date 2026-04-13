day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

both_days = day1 & day2
print("Visited both days:", both_days)

one_day = day1 ^ day2
print("Visited only one day: ", one_day)

total_visitors = day1 | day2
print("Total unique visitors: ", total_visitors)