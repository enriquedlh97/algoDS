"""
Problem:

There is an algorithms tournament taking place in which teams of programmers compete
against each other to solve algorithmic problems as fast as possible.

Teams compete in a round robin, where each team faces off against all other teams.
Only two team compete against each other ata time, and for each competition, one team
is designated the hoe team and the other one the away team. In each competition there
is always one winner and one loser; there are no ties.  A team receives 3 points if it
wins and 0 if it loses. The winner of the tournament is the team that receives the most
amount of points.

Given an array of pairs representing the teams that have competed against each other and
an array containing the results of each competition, write a function that returns the
winner of the tournament. The input arrays are named "competitions" and "results".

The "competitions" array has elements in the form [homeTeam, awayTeam], where each team
is a string of at most 30 characters representing the name of the team. The "results" array
contains information about the winner of each competition in the "competitions" array.
"results[i]" denotes the winner of "competitions[i]", where 1 in the "results" array
means that the home team in the corresponding competition won and a 0 means that the away
team won.

It is guaranteed that exactly one team will win the tournament and that each team will
compete against all other teams exactly once. It is also guaranteed that the tournament
will always have at least two teams.

Input:
    competitions: [
                      ["HTML", "C#"],
                      ["C#", "Python"],
                      ["Python", "HTML"]
                  ]

    results: [0, 0, 1]

Output:
    "Python"
"""


HOME_TEAM_WON = 1


# Time O(n), where n is the number of competitions
# Space O(k), where k is the number of teams (because of hash table)
def tournament_winner(competitions, results):
    """ Keeps track of team with most points and replaces it when necessary.

        Keeps track of team with the most points and keeps track of the score
        of every team in a hash table. Teams are only added to the hash table
        once they win a match, otherwise it is assumed they have a score of 0.
        The value sof the hash table for the points of a player are updated every
         time it wins a match.

        Attributes:
            competitions: Non-empty multidimensional array where first dimension
                corresponds to the match number and the second one contains the
                teams that competed in that match.

            results: Non-empty array of the same size as the first dimension of the
                competitions array, corresponding to the match number. The value
                    at a particular index indicates which team won.
    """

    best_team = ""  # Contains name of team with most points

    # Contains the scores of each team that has won at least one game.
    # It is initialized with the empty best_team
    scores = {best_team: 0}

    for match_number, competitors in enumerate(competitions):

        # Gets the value indicating who won the current match
        match_winner = results[match_number]
        # decomposes competitors array into home and away team
        home_team, away_team = competitors

        # Sets the winner name to the actual winner name of the current match
        winner = home_team if match_winner == HOME_TEAM_WON else away_team

        # Updates the score for the winner of current match
        update_scores(winner, scores)

        # Check if the score of the current winner is better than the best_team score
        # and replace it in case it is
        if scores[winner] > scores[best_team]:
            best_team = winner

    return best_team


def update_scores(team, scores):
    # Check if team is already in hash table. In case it is not, then add it with a
    # score of 0
    if team not in scores:
        scores[team] = 0

    # Add points to the team
    scores[team] += 3
