import pickle
a=open('games.pickle','wb')
c={'hacker': [3,0,0,3], 'Nitin': [40,0,0,40]}
pickle.dump(c,a)
a.close()
