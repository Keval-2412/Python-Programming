def create_array(x,y,z,value):
    return [[value for _ in range(z)] for _ in range(x)]

arr = create_array(3,4,5,7)
print(arr)