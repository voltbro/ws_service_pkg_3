#!/usr/bin/env python

import time
import tqdm
import random
import os
import string


configuration_number = "10011"

print(os.system("ls -la"))

def print_random_str(l):
    allchars = string.printable
    str_ = ''
    for i in range(0, l):
        randi = random.randint(0, len(allchars))
        # print(randi)
        symbol = allchars[randi]
        str_ = str_ + symbol
    return str_

print(print_random_str(12))

configuration_number_1 = "11101010101"
configuration_number_2 = "00000011100"
configuration_number_3 = "01111010101"
configuration_number_4 = "10001110111"
version = "2.7.0"

print("Service package 3: ver. {}".format(version))
time.sleep(0.5)
print("Service package 3: start configuration ")
time.sleep(0.5)
print("Service package 3: Search problems stage")
time.sleep(0.5)
for i in tqdm.tqdm(range(100), ascii=True, desc="Search log reports"):
    time.sleep(0.1)
print("Service package 3: search problems finished")
time.sleep(0.5)
print("Service package 3: loading log reports ")
time.sleep(1.5)



print(print_random_str(40))
print(print_random_str(40))
print(print_random_str(40))
print(print_random_str(40))
print(print_random_str(40))

for i in tqdm.tqdm(range(1000), ascii=True, desc="log checking"):
    time.sleep(0.01)

print("Service package 3: log reports checked successfully")

time.sleep(0.5)
print("Service package 3: successfully configured!")
print("Service package 3: finished")
time.sleep(0.5)
print("Service package 3: configuration checksum : {}".format(configuration_number))
