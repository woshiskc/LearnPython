def create_list(list_num):
    list1 = []
    for i in range(0,int(list_num)):
        list1.append(i)
        i+=1
    
    return list1
#==================================

number = raw_input("input list number (must>2)")
list2 = create_list(number)

print "this is new list: ",list2

print "this is index2 element: %d " % list2[1]

