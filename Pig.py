import random

def roll():
	return random.randint(1,6)


def holdAt20Turn():
	turnTotal = 0
	pig = False
	while turnTotal < 20 and not pig:
		side = roll()
		#print("Roll:",side)
		if side == 1:
			turnTotal = 0
			pig = True 
		else:
			turnTotal += side
	#print("Turn Total:", turnTotal)
	return turnTotal
	
def holdAtXTurn(target = 20):
	turnTotal = 0
	pig = False
	while turnTotal < target and not pig:
		side = roll()
		#print("Roll:",side)
		if side == 1:
			turnTotal = 0
			pig = True 
		else:
			turnTotal += side
	#print("Turn Total:", turnTotal)
	return turnTotal
	

# part 4  
def holdAtXTurnP4(target = 20, score = 0): #set score to whatever value
	turnTotal = 0
	scoreTotal = 0
	pig = False
	while turnTotal < target and not pig and score + turnTotal < 100:
		side = roll()
		print("Roll:",side)
		if side == 1:
			turnTotal = 0
			scoreTotal = score
			pig = True 
		else:
			turnTotal += side
			scoreTotal = score + turnTotal
	#print("Turn Total:", turnTotal)
	print("New Score:", scoreTotal)
	return turnTotal 


# part 5
def holdAtXTurn(target = 20):
	score = 0
	while score < 100:
		turnTotal = 0
		pig = False
		while turnTotal < target and not pig and score + turnTotal < 100:
			side = roll()
			print("Roll:",side)
			if side == 1:
				turnTotal = 0
				pig = True 
			else:
				turnTotal += side
				user_input = input("Turn total:" + str(turnTotal) + " Roll/Hold? ")
				if	user_input != "":
					
					break
		score += turnTotal
		print("New Score:", score)


# part 7
def TwoPlayer(target = 20):
	player1S = 0
	player2S = 0
	current_player = 1
	while player1S < 100 and player2S < 100:
		turnTotal = 0
		pig = False
		print("Player 1 score:", player1S)
		print("Player 2 score:", player2S)
		print("It is player", current_player,"'s turn")
		while turnTotal < target and not pig and (player1S + turnTotal < 100 if current_player == 1 else player2S + turnTotal < 100):
			side = roll()
			print("Roll:",side)
			if side == 1:
				turnTotal = 0
				pig = True 
				
			else:
				turnTotal += side
		if current_player == 1:
			player1S += turnTotal	
			print("Turn Total:", turnTotal)
			print("New Score:", player1S)
		else:
			player2S += turnTotal
			print("Turn Total:", turnTotal)
			print("New Score:", player2S)
		current_player = 2 if current_player == 1 else 1
	
			



# part 8
def coin():
	return random.randint(1,2)
def Pig(target = 20):
    realPlayer = coin()
    print("You will be player", realPlayer)
    print("Enter nothing to roll; enter anything to hold")

    player1S = 0
    player2S = 0
    current_player = 1

    while player1S < 100 and player2S < 100:
        turnTotal = 0
        pig = False
        print("Player 1 score:", player1S)
        print("Player 2 score:", player2S)
        print("It is player", current_player, "'s turn")

        if current_player == realPlayer:
            while turnTotal < target and not pig and (player1S + turnTotal < 100 if current_player == 1 else player2S + turnTotal < 100):
                side = roll()
                print("Roll:", side)
                if side == 1:
                    turnTotal = 0
                    pig = True 
                else:
                    turnTotal += side
                    user_input = input("Turn total:" + str(turnTotal) + " Roll/Hold? ")
                    if user_input != "":
                        if realPlayer == 1:
                            player1S += turnTotal  
                        else:
                            player2S += turnTotal  
                        break
        else:
            while turnTotal < target and not pig and (player1S + turnTotal < 100 if current_player == 1 else player2S + turnTotal < 100):
                side = roll()
                print("Roll:", side)
                if side == 1:
                    turnTotal = 0
                    pig = True
                else:
                    turnTotal += side
            print("Turn total:", turnTotal)
            if current_player == 1:
                player1S += turnTotal
                print("New Score:", player1S)
            else:
                player2S += turnTotal
                print("New Score:", player2S)

        current_player = 2 if current_player == 1 else 1




def holdAt20Outcomes(trials):
	results = {}
	results[0] = 0
	# initialize possible scores
	for score in range(20,26):
		results[score] = 0 
	
	# simulate the turn "trials" times
	for _ in range(trials):
		outcome =  holdAt20Turn()
		results[outcome] += 1
	
	# print probabilities
	print("Score","\t","Estimated Prob.")

	for score in results:
		print(score,"\t",results[score]/trials)

def holdAtXOutcomes(trials, target = 20 ):
	results = {}
	results[0] = 0
	# initialize possible scores
	for score in range(target,target+6):
		results[score] = 0 
	
	# simulate the turn "trials" times
	for _ in range(trials):
		outcome =  holdAtXTurn(target)
		results[outcome] += 1
	
	# print probabilities
	print("Score","\t","Estimated Prob.")

	for score in results:
		print(score,"\t",results[score]/trials)


# Part 6
def AveragePturns(Games, target = 20 ):
	totalTurns = 0
	for _ in range(Games):
		score = 0
		turns = 0
		while score < 100:
			turnTotal = holdAtXTurnP4(target, score)
			score += turnTotal
			turns += 1
		totalTurns += turns
	Averageturns = totalTurns / Games
	print("Average turns:", Averageturns)
	return Averageturns
	
	
	

	
#trials = 100000
#Games = trials
#trials = int(input("How many Hold-at-20 turn simulations?\n"))
#score = int(input("Score?"))
#target = int(input("target?"))
#Games = int(input("Games?"))
#holdAtXOutcomes(trials,100)
#holdAtXTurnP4()
#holdAtXTurn()
#AveragePturns(Games, 20)
#TwoPlayer()

Pig()






