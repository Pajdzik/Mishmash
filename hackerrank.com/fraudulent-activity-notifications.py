#!/bin/python3
#https://www.hackerrank.com/challenges/fraudulent-activity-notifications

def calculate_double_median(value_count, length):
    median_i, median_j = None, None
    
    median_index = (length // 2) + 1
    if length % 2 != 0:
        median_i, median_j = median_index, median_index
    else:
        median_i, median_j = median_index - 1, median_index

    i = 0
    median_low, median_high = None, None

    for value in range(len(value_count)):
        if median_high != None:
            break

        for _ in range(value_count[value]):
            i += 1
            if i == median_i:
                median_low = value
            if i == median_j:
                median_high = value 

    return median_low + median_high

def count_elements(arr, count_lenght):
    value_count = [0 for _ in range(count_lenght)]

    for i in arr:
        value_count[i] += 1  

    return value_count

def counting_sort(arr):
    value_count = count_elements(arr)

    output = [0 for _ in range(len(arr))]
    index = 0
    for value in range(len(value_count)):
        for _ in range(value_count[value]):
            output[index] = value
            index += 1

    return output


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    c = 0
    value_count = count_elements(expenditure[:d], max(expenditure) + 1)

    for i in range(d, len(expenditure)):
        double_median = calculate_double_median(value_count, d)

        last_element = expenditure[i]
        if last_element >= double_median:
            c += 1

        first_element = expenditure[i - d]

        value_count[first_element] -= 1
        value_count[last_element] += 1

    return c

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = "5 3".split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, "10 20 30 40 50".rstrip().split()))
    result = activityNotifications(expenditure, d)
    #fptr.write(str(result) + '\n')
    #fptr.close()
