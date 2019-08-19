# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:39:45 2019

@author: sande
"""



free = int(input("Enter free bytes in disk: "))
used = int(input("Enter used bytes: "))
file_deleted = int(input("Enter the size of deleting file: "))
file_created = int(input("Enter the size of created file: "))

free = free + file_deleted
used = used - file_deleted
used = used + file_created
free = free - file_created
print(free)



f = int(input("Enter Free disk size in bytes: "))
u = int(input("Enter Used disk size in bytes: "))
o = int(input("Enter old file size in bytes: "))
n = int(input("Enter new file size in bytes: "))


totalDiskSize = f+u
currentUsedDiskSize = u-o
currentUsedDiskSize = currentUsedDiskSize + n
currentFreeDiskSize = totalDiskSize - currentUsedDiskSize
print(currentFreeDiskSize)
























