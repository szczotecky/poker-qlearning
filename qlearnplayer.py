import qlearning
import GAME
import poker
import hand_dictionary
import konwerter_qlearn
import urllib
import pickle

class Q_Player():

    def __init__(self):
        self.ai = qlearning.QLearn(actions = [1,2,3], alpha = 0.1, gamma = 0.9, epsilon  = 0.1)
        self.lose = 0
        self.win = 0
        self.lastState = None
        self.lastAction = None
        self.state = None
        self.action = None

    def get_state(self,player):
        hash = konwerter_qlearn.konwertuj_q(poker.cards, player.hand)
        string = hand_dictionary.hand_dict[str(hash[0])]
        #print string
        return string

    def clean_states(self,player):
        self.lastState = None
        self.lastAction = None
        self.state = None
        self.action = None


    def aktualizuj(self, win_state, money, player,alpha,flaga):

        #win_state = -1 - porazka, 0 - brak rozstrzygniecia, 1 - wygrana
        #money - pieniadze z puli
        #flaga - czy alfa const czy nie

        state = self.get_state(player)    #aktualny stan
        r = -1                      #nagroda

        if win_state == -1:
            self.lose += 1
            r = -money

            if self.lastState is not None:
                self.ai.learn(self.lastState,self.lastAction,r,state,alpha,flaga)
            self.lastState = None

            return

        if win_state == 1:
            self.win += 1
            r = money

        if self.lastState is not None:
            self.ai.learn(self.lastState,self.lastAction,r,state,alpha,flaga)

        self.lastState = self.state
        self.lastAction = self.action

        #print 'Wins = ', self.win, '\t Loses = ', self.lose


    def select_action(self,player):
        self.state = self.get_state(player)
        self.action = self.ai.chooseAction(self.state)

        #print '\t\tSELECED ACTION: ', self.action

        return self.action

    def select_action_blef(self,player):
        self.state = self.get_state(player)
        self.action = self.ai.chooseAction_blef(self.state)

        #print '\t\tSELECED ACTION: ', self.action

        return self.action


    def import_qtable(self, name):
        self.ai.q =  pickle.load(open(name,"rb"))

    def export_qtable(self,name):
        pickle.dump(self.ai.q, open(name,"wb"))

