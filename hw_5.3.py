

def is_triangle(list_nums):

    list_nums.sort(reverse = True)
    if list_nums[0] < list_nums[1] + list_nums[2]:
        print(list_nums)
        print('triangle possible')
    else:
        print(list_nums)
        print('no triangle possible')
        

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

is_triangle([a,b,c])
