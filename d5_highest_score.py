student_scores = [150, 142, 185, 120, 56, 98, 9, 149, 194, 76, 90, 34, 200, 12, 21, 43, 58, 61, 143, 79, 80]
highest = 0
for score in student_scores:
    if score >= highest:
        highest = score
    else:
        continue
print(highest)