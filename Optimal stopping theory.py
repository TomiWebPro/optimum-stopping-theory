# python test for optimal stopping theory
import math
import random


def compare_numbers(a, b):
    biggest_number = 0
    # print("compare number function", a, "b", b)
    if a > b:
        biggest_number = a
    else:
        biggest_number = b
    # print("biggest_number_from_def", biggest_number)
    return biggest_number


def get_list(a, b_1, b_2):
    b = []
    for i in range(a):
        b.append(random.randint(b_1, b_2))
    return(b)


e = math.e
probability_list = []
finding = 0

how_much_times = int(input("How many times do you wanna play: "))
how_much_contestant = int(input("How many slips of paper each time: "))
skill_lowest = int(input("Lowest possible number on paper: "))
skill_highest = int(input("Highest possible number on paper: "))

for i in range(how_much_times):
    a = get_list(how_much_contestant, skill_lowest, skill_highest)
    a_max_num = max(a)
    # print("a",a)
    # print("a_max", a_max_num)
    optimum = round(len(a)/e)
    sample_list = a[:optimum]
    # print("s", sample_list)
    finding_list = a[optimum:]
    # print("f",finding_list)
    length_sample_list = len(sample_list)
    # print("lel",length_sample_list)
    length_finding_list = len(finding_list)
    # print("lfl",length_finding_list)
    max_sample_list = max(sample_list)
    # print("max_sample",max_sample_list)

    for i in range(int(length_finding_list)-1):
        if compare_numbers(finding_list[i], finding_list[i+1]) > max_sample_list:
            finding = compare_numbers(finding_list[i], finding_list[i+1])
            # print("find", finding)
        # else:
            # print("nothing found")

    if a_max_num == finding:
        probability_list.append(1)
    else:
        probability_list.append(0)

# print(probability_list)
length_probability = len(probability_list)
sum_probability_list = sum(probability_list)
probability = sum_probability_list/length_probability
print("The probability of finding the biggest number is", probability)
print("e over 1 is", 1/e)
