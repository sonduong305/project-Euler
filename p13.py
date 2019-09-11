"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

number in file p13_number.txt

"""
sum_list = [0] * 50
r_sum_list = []
f = open("p13_number.txt", "r")
if f.readable():
    contents = f.readlines()
else:
    print("no file found!!")


for content in contents:
    i = 0
    content = content[:50]
    for digit in content:
        sum_list[i] += int(digit)
        i += 1

mem_temp = 0
for i in range(len(sum_list) - 1, 0, -1):
    r_sum_list.append(sum_list[i] + mem_temp)
    mem_temp = int(r_sum_list[len(sum_list) - 1 - i] / 10)
    r_sum_list[len(sum_list) - 1 - i] = int(r_sum_list[len(sum_list) - 1 - i] % mem_temp)


r_sum_list.append(sum_list[0] + mem_temp)
for digit in reversed(r_sum_list):
    print(digit, end = '')
