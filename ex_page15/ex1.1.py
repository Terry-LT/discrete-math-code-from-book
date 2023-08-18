matr = [
    [0,3,6,9,6,2,5],#A=0
    [3,0,3,6,5,5,4],#B=1
    [6,3,0,3,2,4,1],#C=2
    [9,6,3,0,5,7,4],#D=3
    [6,5,2,5,0,4,3],#E=3
    [2,5,4,7,4,0,3],#F=4
    [5,4,1,4,3,3,0],#G=5
]

def search_min_value(arr):
    min_val = 0
    for i in arr:
        if min_val == 0 and i != 0:
            min_val = i
        else:
            if min_val > i and i != 0:
                min_val = i
    return min_val

#TODO: Write Prim fuc
def prim(matr_arr,to):
    min_distance = []
    index = 0
    for i in matr:
        min_distance.append(search_min_value(i))
        if index == to:
            break
        #print(index)
        index = index + 1
    return min_distance
#3 is D
print(prim(matr,3))
