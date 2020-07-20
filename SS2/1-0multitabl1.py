# for i in range(5):
#     for i in range(5):
#         print('','1','0', end='')
       
#     print()
    
#     for i in range(5):
#         print('', '0', '1', end='')
        
#     print()
n = int(input('Number?'))
for x in range(n):
    for i in range(n):
        if i%2 ==0:
            print('', '1', end='')
        else:
            print('', '0', end='')    
    print()
    for j in range(n):
        if j%2==0:
            print('', '0', end='')
        else:
            print('', '1', end='')
    print()