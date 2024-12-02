def add(name,phone,github):
    with open("friends.txt", 'a') as f:
        f.write(f"{name},{phone},{github}\n")
    print("friend {0} added.".format(name))

#add("sandip","1234567891","dhulo1234")

def remove(name):
    found = False
    with open("friends.txt", 'r') as f:
        a = f.readlines()
    with open("friends.txt", 'w') as f:
        for i in a:
            if not i.startswith(name + ","):
                f.write(i)
            elif i.startswith(name + ","):
                found = True

    if found == False:
        print(f"friend {name} not found.")
    else:
        print(f"friend {name} removed.")

#remove("krunal")

def updatephone(name,phone):
    update = False
    with open("friends.txt" , 'r') as f:
        a = f.readlines()
    with open("friends.txt", 'w') as f:
        for i in a:
            if i.startswith(name + ","):
                k = i.split(",")
                k[1] = phone
                f.write(",".join(k))
                update = True
            else:
                f.write(i)
    if update:
        print(f"phone number of {name} updated.")
    else:
        print(f"friend {name} not found.")

#updatephone("tushar","34455678")
                
def updategithub(name,github):
    update = False
    with open("friends.txt" , 'r') as f:
        a = f.readlines()
    with open("friends.txt", 'w') as f:
        for i in a:
            if i.startswith(name + ","):
                k = i.split(",")
                k[2] = github
                f.write(",".join(k) + "\n")
                update = True
            else:
                f.write(i)
    if update:
        print(f"github of {name} updated.")
    else:
        print(f"friend {name} not found.")
        
#updategithub("sandip","tushar97237")

def printbyname(name):
    found = False
    with open("friends.txt" , 'r') as f:
        for i in f:
            if i.startswith(name + ","):
                found = True
                print(i)
    if found:
        print("true")
    else:
        print(f"friend {name} not found.")
        
#printbyname("sandip")

def printall():
    with open("friends.txt" , 'r') as f:
        for i in f:
            print(i.strip())
        
#printall()

def readall():
    with open("friends.txt","r") as f:
        print(f.read().strip())

#readall()
