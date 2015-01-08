__author__ = 'David'
original = [("x", "x", "x", "x"), ("_", "x", "x", "_"), ("_", "x", "x", "_"), ("x", "x", "x", "x")]
master = []
x = len(original)
print (len(original))
for i in range(x):
    for j in range(x):
        master.append(original[i][j])
print (master)

key = 0
print ("testing horizontal")
for i in range(x-1):
    key = 0
    for j in range(x-1):
        #print (str((i*x)+(j)) + " --- " + str((i*x)+(j)+1))
        if master[(i*x)+(j)] == master[(i*x)+(j+1)]:
            key += 1
            #print ("key =" + str(key))
if key >= x-1:
        print ("We have a horizontal winner: " + str(master[(i*x)+(j)]))
else:
        print ("No horizontal winner")

key = 0
print ("testing vertical")
for j in range(x):

    for i in range(x-1):
        #print ("comparing: " + str(master[j + i * x]) + " and " + str(master[j + (i+1) * x]))
        if (master[j + i*x] == "x" or master[j + i*x] == "o") and (master[j + (i+1)*x] == "x" or master[j + (i+1)*x] == "x") and master[j + i * x] == master[j + (i+1)*x]:
            key += 1
            #print ("key =" + str(key))
if key >= x-1:
    print ("We have a vertical winner:" + str(master[j + 1*x]))
else:
    print ("No vertical winner")

print ("testing right diagonal")
key = 0
for j in range(x-1):

    #print (str(j*x+j) + "...." + str(j*(x+1) + (x+1)))
    if (master[j*x+j] == "x" or master[j*x+j] == "o" ) and (master[j*(x+1) + (x+1)] == "x" or master[j*(x+1) + (x+1)] == "o") and ( master[j*x+j] == master[j*(x+1) + (x+1)]):
        key += 1
        #print (str(master[j*x+j]) + " and " + str(master[j*(x+1) + (x+1)]) + " are equal. " "key = " + str(key) + " and j=" + str(j))
if key >= x-1:
    print ("We have a right diagonal winner: " + str(master[0]))
else:
    print ("No right diagonal winner.")

print ("testing left diagonal")
key = 0
#print ("--------------------------------- x = " + str(x))
for j in range(1, x, 1):
    #print (str(j*x-j) + "...." + str((j*x-j) + (x-1)))
    if (master[j*x-j] == "x" or master[j*x-j] == "o") and (master[j*x-j + (x-1)] == "x" or master[j*x-j + (x-1)] == "o") and (master[j * x - j] == master[j*x-j + (x-1)]):
        key += 1
        #print (str(master[j*x-j]) + " and " + str(master[j*x-j + (x-1)]) + " are equal. " "key = " + str(key) + " and j=" + str(j))
if key >= x-1:
    print ("We have a left diagonal winner: " + str(master[x-1]))
else:
    print ("No left diagonal winner.")










