def myfun(my_list):
    s=0
    for item in my_list:
        s=s+item
    return s
    
my_list= [1,2,3,4,5,6,7,8,9]
s= myfun(my_list)

print('la somma degli elementi della lista è: {}'.format(s))