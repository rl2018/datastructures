numbers=[0,0,0,0,0,0] #array setup

for i in range(0,6): #number input
    numbers[i]=int(input("number?"))

print(numbers) #normal

print(numbers[::-1]) #reverse

print("sum =",sum(numbers)) #sum

print("average =",(sum(numbers)/6)) #mean