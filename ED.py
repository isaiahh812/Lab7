
S1 = "fool"
S2 = "fuel"
s1List = list(S1)
s2List = list(S2)
Table = [[0 for i in range(len(s1List)+1)] for j in range(len(s2List)+1)]
for i in range(len(s1List)+1):
    Table[0][i] = i
for i in range(len(s2List)+1):
    Table[i][0] = i
for i in range(len(s2List)):
    for j in range(len(s1List)):
            if s1List[j] == s2List[i]:
                Table[i+1][j+1] = Table[i][j]
            else: 
                Table[i+1][j+1] = min(Table[i][j], Table[i][j], Table[i+1][j])+1    
changes = Table[len(s1List)][len(s2List)]
print(changes)