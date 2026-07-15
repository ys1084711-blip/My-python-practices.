#check that a type cannot be changed in python

a = (78, 56, "yash")

a[2] = "larry"

#output: TypeError: 'tuple' object does not support item assignment becouse its immutable.