def legal_moves(player,li1):
	if player == 'W':
		opp = 'B'
	else:
		opp = 'W'
	li = find_position(li1,player)
	print(li)
	li2 = []
	for i in li:
		x,y = i
		if li1[x][y-1] == opp:
                        for i in range(y-1,0,-1):
                                if li1[x][i] == '_':
                                        li2.append((x+1,i+1))
                                        break
                                if li1[x][i] == player:
                                        break
                                if li1[x][i] == opp:
                                        continue
				
		if li1[x][y+1] == opp:
                	for i in range(y+2,8):
                		if li1[x][i] == '_':
                       			li2.append((x+1,i+1))
                        		break
                		if li1[x][i] == player:
                        		break
                		if li1[x][i] == opp:
                        		continue

		if li1[x-1][y] == opp:
                        for i in range(x-2,0,-1):
                                if li1[i][y] == '_':
                                        li2.append((i+1,y+1))
                                        break
                                if li1[i][y] == player:
                                        break
                                if li1[i][y] == opp:
                                        continue

		if li1[x+1][y] == opp:
                        for i in range(x+2,8):
                                if li1[i][y] == '_':
                                        li2.append((i+1,y+1))
                                        break
                                if li1[i][y] == player:
                                        break
                                if li1[i][y] == opp:
                                        continue
	print(li2)
	return li2
def find_position(li1,player):
	li2 = []
	for i in range(8):
		for j in range(8):
			if li1[i][j] == player:
				li2.append((i,j))
	return li2
games = int(input())
for i in range(games):
	input_list = []
	for j in range(8):
		x = input()
		input_list.append(x)
	player = input()
	if player == 'W' or player == 'B':
		b = legal_moves(player,input_list)
		print(b)
