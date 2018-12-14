#Isaiah Hernandez
#80591211
#date modified 12/14/18
#cs2302
S1 = "fool"
S2 = "fuel"
s1List = list(S1)#seperates both strings into list
s2List = list(S2)#seperates both strings into list
Table = [[0 for i in range(len(s1List)+1)] for j in range(len(s2List)+1)]
for i in range(len(s1List)+1):#set the first row
    Table[0][i] = i
for i in range(len(s2List)+1):#sets the first coloumn 
    Table[i][0] = i
for i in range(len(s2List)):#
    for j in range(len(s1List)):#checks if the characters are the same
            if s1List[j] == s2List[i]:#if so uses the diagonal vaule
                Table[i+1][j+1] = Table[i][j]
            else(): 
                Table[i+1][j+1] = min(Table[i][j], Table[i][j], Table[i+1][j])+1#checks for the lowest number    
changes = Table[len(s1List)][len(s2List)]
print(changes)
file = open("results_for_lab_7.txt","w")
file.write("The number of changes for the the two words is " + str(changes))
