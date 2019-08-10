# HW01_ch02_ex02
# NOTE: You do not run this script.
# #
# Practice using the Python interpreter as a calculator.
# Paste answer and calculations below

# 1. The volume of a sphere with radius r is 4/3 π r^3.
# What is the volume of a sphere with radius 5? 523.5987755982989
>>>r = 5
>>>4/3 * math.pi * r ** 3
523.5987755982989

# 2. Suppose the cover price of a book is $24.95, but bookstores get a
# 40% discount. Shipping costs $3 for the first copy and 75 cents for
# each additional copy. What is the total wholesale cost for 60 copies?
# total wholesale cost: 945.4499999999999
# 24.95 * (1 - 0.4) * 60 + 3 + (60 - 1) * 0.75
# The answer should be 945.45, but here it's not accurate because the floating point calculation error.

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace
# (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy
# pace again, what time do I get home for breakfast?
# time: 7 :  30
# [calculations here]
time_clock = 6
time_min = 52
total_time = 2 * (8 * 60 + 15) + 3 * (7 * 60 + 12)
minu = total_time // 60 # 38
# sec = total_time % 60 # 6
time_clock += (52 + minu) // 60
time_minu = (time_min + minu) % 60
print(time_clock,': ', time_minu)
