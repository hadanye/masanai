#위치인자
def get_sum(a,b):
    result = a+b
    return result
#키워드인자
def get_sum_1(a=1,b=2):
    result = a+b
    return result

def get_sum_2(b,d,a=1, c=3,):#항상 위치인자 부터 적기.

    result_1= a+b
    result_2= c-d
    return result_1, result_2

n4 = get_sum_2(5,6)
print(n4)
# n1 = get_sum(10,20)
# print('10과 20의 합 =', n1)

# n2 = get_sum(100,200)
# print('100과 200의 합=', n2)

n3= get_sum_1()
print(n3)