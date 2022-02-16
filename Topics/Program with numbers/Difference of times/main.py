hours_a = int(input())
minutes_a = int(input())
seconds_a = int(input())
hours_b = int(input())
minutes_b = int(input())
seconds_b = int(input())
sum_a = seconds_a + minutes_a * 60 + hours_a * 3600
sum_b = seconds_b + minutes_b * 60 + hours_b * 3600
print(sum_b-sum_a)
