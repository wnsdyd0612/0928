a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

d = a + b + c

a_index = len(a)
b_index = len(b) + a_index
c_index = len(c) + b_index
d_index = len(d)

for index_value in range (len(d)):
    if index_value < (a_index-2):
        print("{} {} {}".format(d[index_value],d[index_value+1],d[index_value+2]))
    elif index_value < (b_index-2):
        if index_value > (a_index-1):
            print("{} {} {}".format(d[index_value],d[index_value+1],d[index_value+2]))
    elif index_value < (c_index-2):
        if index_value > (b_index-1):
            print("{} {} {}".format(d[index_value],d[index_value+1],d[index_value+2]))
