#!/usr/bin/env python

import time
import tqdm

configuration_number = "0xFF01CA"
version = "1.1.2"

print("Service package 3: ver. {}".format(version))
time.sleep(0.5)
print("Service package 3: start configuration ")
time.sleep(0.5)
print("Service package 3: stage 1")
time.sleep(0.5)
for i in tqdm.tqdm(range(1000), ascii=True, desc="Finding dependencies"):
    time.sleep(0.01)
print("Service package 3: stage 1 finished")
time.sleep(0.5)
print("Service package 3: stage 2")
time.sleep(1.5)
print("Service package 3: configuration package 1 found")
for i in tqdm.tqdm(range(5000), ascii=True, desc="Setup in progress"):
    time.sleep(0.002)
print("Service package 3: stage 2 finished")
time.sleep(0.5)
print("Service package 3: successfully configured!")
time.sleep(0.5)
print("Service package 3: configuration checksum : {}".format(configuration_number))