heights = input("Enter the heights with space: ")
height_list = heights.split()

# step 1: count manually
count = 0
for h in height_list:
    count = count + 1

# step 2: convert to int manually
for i in range(count):
    height_list[i] = int(height_list[i])

# step 3: assume first element is max
num = height_list[0]

# step 4: compare safely (stop at count, not count+1)
for i in range(1, count):
    if height_list[i] > num:
        num = height_list[i]
    else:
        num = num

print("the max number is", num)
