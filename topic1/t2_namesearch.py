studentnames=["john","james","adam","richard","reece","kieran"]

searchterm=input("name of student?")

found=False
n=0
while found is False:
    if studentnames[n]==searchterm:
        print("the index for",searchterm,"is",(n+1))
        found=True
    else:
        n=n+1

if found is False:
    print("could not find the name",searchterm,"in the array")