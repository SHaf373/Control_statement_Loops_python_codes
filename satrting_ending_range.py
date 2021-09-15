start=int(input('enter starting number:'))
end=int(input('how far should i go:'))
print('number \t square')
for num in range(start,end+1):
    sq=num**2
    print(num ,'\t', sq)  