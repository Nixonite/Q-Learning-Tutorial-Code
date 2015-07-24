import numpy as np
		
mR = np.array([[-1,-1,-1,-1,0,-1],
					[-1,-1,-1,0,-1,100],
					[-1,-1,-1,0,-1,-1],
					[-1,0,0,-1,0,-1],
					[0,-1,-1,0,-1,100],
					[-1,0,-1,-1,0,100]])
#rows are states, columns are actions
#row 1, column 1 = taking action 1 at state 1

#initialize matrix Q to zero.
mQ = np.zeros((6,6))

#set the gamma parameter.
learningRate = 0.8

#set the goal state
goalState = 5

def getPossibleActions(state):
	#state is an integer i.e. row of the rM matrix (0,...n)
	indices = []
	for i in range(len(mR[state])):
		if mR[state][i]!=-1:
			indices.append(i)
	return indices

print mR
print mQ

#for each episode:
for episode in range(10000):

	#select a random initial state
	currentState = np.random.randint(0,mR.shape[0]) #room 1
	
	while True:#do while the goal hasn't been reached
	
		#select one among all possible actions for the current state
		#using this possible action, consider going to the next state
		nextState = np.random.choice(getPossibleActions(currentState))
	
		#get all possible actions for the next state
		nextStatePossibleActions = getPossibleActions(nextState)
	
		#get maximum Q value for this next state based on all possible actions
		nextStateMaxQ = max([mQ[nextState,a] for a in nextStatePossibleActions])
	
		#compute the updated Q
		mQ[currentState,nextState] = mR[currentState,nextState]+learningRate*nextStateMaxQ
	
		#set the next state as the current state
		currentState = nextState
		
		if currentState == goalState: #if the goal is reached then end the episode
			break
	#end Do while

print mQ