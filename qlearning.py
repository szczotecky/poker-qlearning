import random


actual_state = None
prev_state = None

n_actions = 3
n_states = 307


class QLearn:

    def __init__(self,actions, epsilon = 0.1, alpha = 0.2, gamma = 0.9):

        self.q = {}  #zamiast tablicy 2wymiarowej, ktorej w pythonie nie ma slownik kojarzacy pare (stan,akcja) z nagroda
        # przyklad:
        # Q[(1,2)] = 333 => wynik {(1,2):333}

        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

        self.actions = actions #tablica akcji do wyboru

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0)

    def learnQ(self, state, action, reward, value, alpha):
        oldv = self.q.get((state, action), None)
        alpha = float(alpha)

        if oldv is None:
            self.q[(state, action)] = reward
        else:
            #self.q[(state, action)] = oldv + self.alpha * (value - oldv)
            self.q[(state, action)] = oldv + 1/alpha * (value - oldv)

    def learnQ_const(self, state, action, reward, value, alpha):
        oldv = self.q.get((state, action), None)
        alpha = float(alpha)

        if oldv is None:
            self.q[(state, action)] = reward
        else:
            self.q[(state, action)] = oldv + self.alpha * (value - oldv)


    def chooseAction(self, state):
        if random.random() < self.epsilon:
            action = random.choice(self.actions)
        else:
            q = [self.getQ(state, a) for a in self.actions]
            maxQ = max(q)
            count = q.count(maxQ)
            if count > 1:
                best = [i for i in range(len(self.actions)) if q[i] == maxQ]
                i = random.choice(best)
            else:
                i = q.index(maxQ)

            action = self.actions[i]
        return action

    def learn(self, state1, action1, reward, state2, alpha,flaga):

        #flaga - czy alfa const czy nie

        maxqnew = max([self.getQ(state2, a) for a in self.actions])
        if flaga == True:
            self.learnQ_const(state1, action1, reward, reward + self.gamma*maxqnew, alpha)
        elif flaga == False:
            self.learnQ(state1, action1, reward, reward + self.gamma*maxqnew, alpha)

    def chooseAction_blef(self, state):
        if random.random() < self.epsilon:
            action = random.choice(self.actions)
            #print 'random act'
        else:
            q = [self.getQ(state, a) for a in self.actions]
            p=[]
            a=[]

            #print 'WARTOSCI Q', q

            maxQ = max(q)
            minQ = min(q)

            for i in range(len(q)):
                p.append(float((q[i]-minQ+1)/(maxQ-minQ+3)))

            a=list(p)

            p.sort() #od najmniejszej do najwiekszej

            levels = []
            last_tmp = 0

            for el in p:
                if sum(p) > 0:
                    last_tmp += float(el)/float(sum(p))
                    levels.append(last_tmp)


            test = random.random()

            if len(p)>0 and sum(p)>0:
                if test < levels[0]:
                    i=a.index(p[0])
            elif len(p)>1 and sum(p)>0:
                if test < levels[1]:
                    i=a.index(p[1])
            elif len(p)>2 and sum(p)>0:
                if test < 1:
                    i=a.index(p[2])
            else:
                count = q.count(maxQ)
                if count > 1:
                    best = [i for i in range(len(self.actions)) if q[i] == maxQ]
                    i = random.choice(best)
                else:
                    i = q.index(maxQ)

            action = self.actions[i]

        #print 'selected action', action

        return action