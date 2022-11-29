size = 10
for i in range(size):
    if i == 0 or i == size - 1:
        print('*' * int(size - i))
    else:
        print('*' + ' ' * (size - i-2) + '*')
for j in range(size+1):
    if j == size or j==2:
        print('*' * int(j))
    elif j == 0 or j == 1:
    	pass
    else:
        print('*' + ' ' * (j-2) + '*')
        
