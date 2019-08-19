"""
400 hot dogs brought in packages each containing
8 hot dogs
calculate how many packages are brought
"""

count = 0



total_hot_dog = 400
total_hot_dog_per_container = 8
total_container = 0

for i in range(0,total_hot_dog,total_hot_dog_per_container):
	count += 1
print(count)

while(total_hot_dog >= total_hot_dog_per_container):
	total_hot_dog -= total_hot_dog_per_container
	total_container += 1
	
	
print(total_container)
