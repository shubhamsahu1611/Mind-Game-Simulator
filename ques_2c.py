import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles = [1,1]  
        self.results =[1,0]    
        self.opp_play_styles =[1,1]
        self.points = 1
        self.wins=0

    def play_move(self):
        """
        Decide Alice's play style for the current round.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        na=self.points
        nb=len(self.results)-na
        last=self.results[-1]
        if last == 1:
            if ((nb)/(na+nb))>(6/11):
                return 0
            else:
                return 2
        
        if last == 0:
            return 1
        
        if last==0.5:
            return 0
        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append( own_style)  
        self.results.append( result)                      
        self.opp_play_styles.append( opp_style)   
        self.points += result 
        if result==1:
            self.wins+=1

        pass
       

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = [1,1] 
        self.results = [0,1]         
        self.opp_play_styles = [1,1]
        self.points = 1


    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append( own_style)  
        self.results.append( result)                      
        self.opp_play_styles.append( opp_style)   
        self.points += result 

 

def simulate_round(alice, bob, payoff_matrix ):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    Alice_way=alice.play_move()
    Bob_way=bob.play_move()
    win, drew, loss = payoff_matrix[Alice_way][Bob_way]

    total_prob=win+drew+loss

    random_prob=np.random.uniform(0, total_prob)
    alice_flag=False
    bob_flag=False
    drew_flag=False
    if random_prob<win:
        alice_flag=True
    elif random_prob>=win and random_prob<win+drew:
        drew_flag=True
    else: bob_flag=True
    
    na=alice.points
    nb=bob.points

    if alice_flag:
        alice.observe_result(Alice_way , Bob_way , 1)
        bob.observe_result( Bob_way, Alice_way , 0)
        payoff_matrix[0][0]=((nb)/(na+nb+1), 0, (na+1)/(na+nb+1))
    elif bob_flag:
        alice.observe_result(Alice_way , Bob_way , 0)
        bob.observe_result( Bob_way, Alice_way , 1)
        payoff_matrix[0][0]=((nb+1)/(na+nb+1), 0, (na)/(na+nb+1))
    else :
        alice.observe_result(Alice_way , Bob_way , 0.5)
        bob.observe_result( Bob_way, Alice_way , 0.5)
        payoff_matrix[0][0]=((nb+0.5)/(na+nb+1), 0, (na+0.5)/(na+nb+1))

    pass
    

def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    alice=Alice()
    bob=Bob()
    
    total_rounds=0
    x=0
    size=0
    while total_rounds<(10**5):
        cnt=0
        alice = Alice()
        bob = Bob()
        payoff_matrix=[]
        payoff_matrix.append([(0.5 ,0,  0.5) , (7/10, 0 , 3/10) , (5/11, 0, 6/11)])
        payoff_matrix.append([(3/10 ,0,  7/10) , (1/3, 1/3 , 1/3) , (3/10, 1/2, 1/5)])
        payoff_matrix.append([(6/11 ,0,  5/11) , (1/5, 1/2 , 3/10) , (1/10, 4/5, 1/10)])
        rounds = 0
        while alice.wins< T:
            simulate_round(alice, bob, payoff_matrix)
            rounds += 1
        total_rounds+=rounds
        size+=1
        rounds=0

    expectations=(total_rounds/size)
    # print(expectations)
    return expectations

# print(estimate_tau(5))
        
        
    