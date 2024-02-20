s=[]

def push(input):
    global s
    s.append(input)

def pop():
    global s
    if isEmpty(s) is True:
        print("stack is empty, cannot pop")
    else:
        s.pop()

def isEmpty(stack):
    if not stack:
        return True
    else:
        return False

push("mondeo")
push("golf")
isEmpty(s)
push("fiesta")
push("punto")
pop()
push("civic")
push("porsche")
pop()
pop()
print(s)
