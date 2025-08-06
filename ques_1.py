import time
from functools import cache
"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 1a   
def solve(wins_by_Alice , wins_by_Bob , total , Alice_need ,dp):
    if wins_by_Alice>Alice_need:
        return 0
    if wins_by_Alice+wins_by_Bob == total:
        if wins_by_Alice == Alice_need:
            return 1
        else:
            return 0
    
    if dp[wins_by_Alice][wins_by_Bob]!=-1:
        return dp[wins_by_Alice][wins_by_Bob]
    ans=0
    match=mod_add(wins_by_Alice, wins_by_Bob) # total match played till now

    #case-1: alice wins the match
    ans=mod_add(ans , mod_multiply(mod_divide(wins_by_Bob , match),solve(wins_by_Alice+1, wins_by_Bob , total , Alice_need ,dp)))

    #case-2: bob wins the match
    ans=mod_add(ans , mod_multiply(mod_divide(wins_by_Alice , match),solve(wins_by_Alice, wins_by_Bob+1 , total , Alice_need ,dp)))

    dp[wins_by_Alice][wins_by_Bob]=ans
    return ans



    #alice wins
def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    dp=[]
    total=mod_add(alice_wins, bob_wins)
    for x in range(total+1):
        row=[]
        for y in range(total+1):
            row.append(-1)
        dp.append(row)

            
    return solve(1, 1,total, alice_wins , dp)

    
# Problem 1b (Expectation)   


def dp_return(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    global dp
    dp=[]
    total=mod_add(alice_wins, bob_wins)
    for x in range(total+1):
        row=[]
        for y in range(total+1):
            row.append(-1)
        dp.append(row)

            
    a=solve(1, 1,total, alice_wins , dp)
    return dp
    

def calc_expectation(t):
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    dp=dp_return(t+1, t+1)
    total_expectations=0
    for x in range(-t, t+1):
        if (t+x)%2==0 and (t-x)%2==0:

            if dp[(t+x)//2][(t-x)//2] !=-1:
                total_expectations=mod_add(total_expectations , mod_multiply(x , dp[(t+x)//2][(t-x)//2]))
            else:
                dp[(t+x)//2][(t-x)//2]=calc_prob((t+x)//2, (t-x)//2)
                total_expectations=mod_add(total_expectations , mod_multiply(x , dp[(t+x)//2][(t-x)//2]))
    return total_expectations

# Problem 1b (Variance)
def calc_variance(t):
    
    store = [[0] * (t + 1) for _ in range(t + 1)]
    store[1][1] = 1  # Base case

    for i in range(1, t + 1):
        for j in range(1, t + 1):
            if i == 1 and j == 1:
                continue
            alice_wins_last = mod_multiply(store[i - 1][j], j)
            bob_wins_last = mod_multiply(store[i][j - 1], i)
            total_games = mod_add(i, j)
            if total_games > 1:
                store[i][j] = mod_add(
                    mod_divide(alice_wins_last, total_games - 1),
                    mod_divide(bob_wins_last, total_games - 1)
                )

    # Calculate the variance
    total_variance = 0

    # Calculate variance for the number of games
    for i in range(1, t):
        prob = store[i][t - i]  # Probability of Alice winning i games, Bob (t-i) games
        diff = 2 * i - t
        diff_squared = mod_multiply(diff, diff)  # (2*i - t)^2
        contribution = mod_multiply(diff_squared, prob)
        total_variance = mod_add(total_variance, contribution)

    return total_variance



# start=time.perf_counter()
# print(calc_prob(99 , 85))
# print(calc_expectation(85))
# print(calc_variance(102))
# end=time.perf_counter()
# print(end-start)