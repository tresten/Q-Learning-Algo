import random

R=[
[None, 5, None, 6, None, None],
[None, None, 5, None, 7, None],
[None, None, None, None, 5, None],
[None, None, None, None, 7, None],
[None, 4, None, None, None, 100],
[None, None, None,None, None, 100]
]

#gamma variable decides how much it looks for immediate statisfaction(smaller) or future statisfaction(higher)
gamma=0.8
goal_state=15

def initalize_q(R):
	return [ len(R)*[0] for i in range(len(R)) ]

Q=initalize_q(R)

def get_random_action(current_state_row):
	#returns a random action (moving between states) that you are allowed to take
	options=[i for i in range(len(current_state_row)) if current_state_row[i]!=None]
	action=random.choice(options)
	print("Action:", action)
	return action

def display_q():
	[print (Q[i]) for i in range(len(Q))]

def update_q(current_state):
	#updates the Q matrix using the update formula and returns the next state
	action= get_random_action(R[current_state])
	Q[current_state][action] = R[current_state][action] + gamma* max( [Q[action][i] for i in range(len(R[action])) if R[action][i]!= None] )
	display_q()
	return action

def run():
	for i in range(100):
		current_state=random.choice(range(len(R)))
		while current_state != goal_state:
			current_state = update_q(current_state)

def find_path(start_state):
	path=[]
	while start_state != goal_state:
		next_state = Q[start_state].index(max(Q[start_state]))
		path.append(str(start_state)+' ->')
		start_state=next_state
	path.append(start_state)
	print(path)
