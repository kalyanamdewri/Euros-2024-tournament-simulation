import numpy as np

# Define initial Elo ratings for teams
elo_ratings = {
    "Spain": 1850,
    "Germany": 1800,
    "Portugal": 1750,
    "France": 1750,
    "England": 1800,
    "Switzerland": 1700,
    "Netherlands": 1750,
    "Türkiye": 1700
}

# Elo probability calculation function
def elo_probability(rating1, rating2):
    return 1 / (1 + 10 ** ((rating2 - rating1) / 400))

# Define matchups for quarter-finals
quarter_finals = [
    ("Spain", "Germany"),
    ("Portugal", "France"),
    ("England", "Switzerland"),
    ("Netherlands", "Türkiye")
]

# Simulate the tournament
def simulate_tournament(elo_ratings, num_simulations=10000):
    win_counts = {team: 0 for team in elo_ratings.keys()}

    for _ in range(num_simulations):
        # Simulate quarter-finals
        semi_finalists = []
        for match in quarter_finals:
            team1, team2 = match
            prob_team1_wins = elo_probability(elo_ratings[team1], elo_ratings[team2])
            if np.random.rand() < prob_team1_wins:
                semi_finalists.append(team1)
            else:
                semi_finalists.append(team2)

        # Simulate semi-finals
        final_teams = []
        for i in range(0, len(semi_finalists), 2):
            team1 = semi_finalists[i]
            team2 = semi_finalists[i+1]
            prob_team1_wins = elo_probability(elo_ratings[team1], elo_ratings[team2])
            if np.random.rand() < prob_team1_wins:
                final_teams.append(team1)
            else:
                final_teams.append(team2)

        # Simulate final
        team1, team2 = final_teams
        prob_team1_wins = elo_probability(elo_ratings[team1], elo_ratings[team2])
        if np.random.rand() < prob_team1_wins:
            win_counts[team1] += 1
        else:
            win_counts[team2] += 1

    # Calculate probabilities
    win_probabilities = {team: win_counts[team] / num_simulations for team in elo_ratings.keys()}
    return win_probabilities

# Run the simulation
win_probabilities = simulate_tournament(elo_ratings)
print(win_probabilities)
