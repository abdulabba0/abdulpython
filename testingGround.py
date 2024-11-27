import random
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run."""
    if n_runs == 0:
        return 0  # Handle zero runs
    
    total_profit = 0
    
    for _ in range(n_runs):
        outcome = random.choice([-1, 0, 1, 2, 3])  # Random outcome: -1, 0, 1-3
        total_profit += outcome
        
    return total_profit / n_runs
