#!/usr/bin/python3
#-*- coding: utf-8 -*-

with open('s.txt',"w+") as f:
	f.write(f"{int(f.read())+f.seek(0)+1:>03}")