# Mind-Game-Simulator

A suite of analytical derivations and Monte Carlo simulations for the “Mind Games” problem in MTL106: Probability and Stochastic Processes.

## Project Overview

This repository contains scripts that solve three core problems:

1. **Probability, Expectation & Variance (Problem 1)**  
   Compute closed‐form probability, expectation and variance of a sum of random variables, then output the result modulo \(10^9+7\).

2. **Greedy vs. Non-Greedy Strategies (Problem 2)**  
   Monte Carlo simulations to compare:
   - 2a: Alice’s greedy strategy  
   - 2b: Alternate non-greedy policy  
   - 2c: Estimate the expected number of rounds \(\tau\) needed for \(T\) wins.

3. **Uniform-Random Opponent Analysis (Problem 3)**  
   - 3a: Simulate Alice vs. a uniform-random Bob  
   - 3b: (Stub) Dynamic‐programming template for optimal play.

## Features

- **`ques_1.py`**  
  - Functions:  
    - `calc_prob(n, p)` – Computes the probability of event.  
    - `calc_expectation(n, p)` – Computes \(E[\sum X_i]\).  
    - `calc_variance(n, p)` – Computes \(\mathrm{Var}(\sum X_i)\).  
  - Outputs result mod \(10^9+7\).

- **`ques_2a.py`**, **`ques_2b.py`**, **`ques_2c.py`**  
  - Monte Carlo engines to simulate and compare strategies.  
  - `monte_carlo(num_trials, strategy)` – Runs trials, records average score.  
  - `estimate_tau(T, num_trials)` – Approximates expected rounds to \(T\) wins.

- **`ques_3a.py`**, **`ques_3b.py`**  
  - `ques_3a.py`: Heuristic vs. uniform-random opponent simulation.  
  - `ques_3b.py`: Placeholder for DP‐based optimal strategy (`optimal_strategy(state)`).



