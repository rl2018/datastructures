numbers=[0,0,0,0,0,0] #array numbers[6]

for i in range(0,6): # for i = 0 to 5 do
    numbers[i]=int(input("number?"))
    # next i

print(numbers) #normal

print(numbers[::-1]) #reverse

print("sum =",sum(numbers)) #sum

print("average =",(sum(numbers)/6)) #mean