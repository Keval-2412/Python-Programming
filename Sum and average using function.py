def sum_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg
marks = [80, 75, 90, 85, 70]
print(sum_avg(marks))