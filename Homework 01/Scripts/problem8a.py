#!/usr/bin/python

oneToThirtySix = [];

for i in range(37):
	oneToThirtySix.append(i);

for i in oneToThirtySix:
	first = i % 5
	second = i % 7

	print("{0} & {1} & {2} \\\\".format(i, first, second))
