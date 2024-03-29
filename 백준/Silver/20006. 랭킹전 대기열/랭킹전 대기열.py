import sys
input = sys.stdin.readline

roomNumber, roomLimit = map(int, input().split())
rooms = {0 : []}
flag = True

def mola(roomss:dict, users: list, i : int):
    if i not in roomss:
        roomss[i] = [users]
        return
    low = int(roomss[i][0][0]) - 10
    large = int(roomss[i][0][0]) + 10
    
    if low <= int(users[0]) and large >= int(users[0]) and len(roomss[i]) < roomLimit:
        roomss.get(i).append(users)
        return
    else:
        mola(roomss,users, i + 1)

for _ in range(roomNumber):
    user = list(input().split())
    if flag:
        rooms[0].append(user)
        flag = False
    
    else:
        mola(rooms, user, 0)
                
    
for i in range(len(rooms.keys())):
    rooms[i].sort(key= lambda x : x[1])
    if len(rooms[i]) == roomLimit:
        print("Started!")
        
    elif len(rooms[i]) < roomLimit:
        print("Waiting!")
    
    for c in rooms[i]:
        print(c[0], c[1])