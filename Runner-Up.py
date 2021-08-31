n = int(input(('Number of scores: ')))
print('Enter the score: ')
A=input().split()
if len(A) > n:
    print('Number of scores is high ....!!')
    exit(0)
else:
    s=sorted(list(map(int,A)))
    print('Sorted list is: {0}'.format(s))
    s.reverse()
    print('Reverse Sorted list is: {0}'.format(s))
    for i in range(n):
        if s[i]!=s[i+1]:
            val=s[i+1]
            print("Runner Up Score is :",val)
            break




