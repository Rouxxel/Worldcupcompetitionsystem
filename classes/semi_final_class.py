#!/usr/bin/env python
# coding: utf-8

class SemiFinals:
    """
    A class to simulate semi-final matches in a knockout football tournament.
    It manages input, determines match winners/losers, and stores the results.
    """

    def __init__(self, c1_goals=0, c2_goals=0, c1_penalties=0, c2_penalties=0,
                 q_finals_winners=None, semi_finals_winners=None, semi_finals_losers=None):
        """
        Initializes a semi-final match with the scores and team information.

        Parameters:
        c1_goals (int): Goals scored by team 1 in normal time.
        c2_goals (int): Goals scored by team 2 in normal time.
        c1_penalties (int): Penalty goals by team 1 (if applicable).
        c2_penalties (int): Penalty goals by team 2 (if applicable).
        q_finals_winners (list): List of 4 teams that qualified from quarter-finals.
        semi_finals_winners (list): External reference list to store semi-final winners.
        semi_finals_losers (list): External reference list to store semi-final losers.
        """
        if q_finals_winners is None:
            q_finals_winners = [0]*4
        if semi_finals_winners is None:
            semi_finals_winners = []
        if semi_finals_losers is None:
            semi_finals_losers = []

        self.c1_goals = c1_goals
        self.c2_goals = c2_goals
        self.c1_penalties = c1_penalties
        self.c2_penalties = c2_penalties
        self.q_finals_winners = q_finals_winners[:4]
        self.semi_finals_winners = semi_finals_winners
        self.semi_finals_losers = semi_finals_losers

    def s_round_1_result(self):
        """
        Determines and prints the result of the first semi-final match.
        Updates the winners and losers lists accordingly.
        """
        print("Semi finals=\nMatch 1:")

        team1 = self.q_finals_winners[0]
        team2 = self.q_finals_winners[1]

        if self.c1_goals == self.c2_goals:
            print(team1, self.c1_goals, f"({self.c1_penalties})")
            print(team2, self.c2_goals, f"({self.c2_penalties})")

            if self.c1_penalties == self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties > self.c2_penalties:
                print("WINNER:", team1)
                self.semi_finals_winners.append(team1)
                self.semi_finals_losers.append(team2)
            else:
                print("WINNER:", team2)
                self.semi_finals_winners.append(team2)
                self.semi_finals_losers.append(team1)
        else:
            print(team1, self.c1_goals)
            print(team2, self.c2_goals)

            if self.c1_goals > self.c2_goals:
                print("WINNER:", team1)
                self.semi_finals_winners.append(team1)
                self.semi_finals_losers.append(team2)
            else:
                print("WINNER:", team2)
                self.semi_finals_winners.append(team2)
                self.semi_finals_losers.append(team1)

    def s_round_2_result(self):
        """
        Determines and prints the result of the second semi-final match.
        Updates the winners and losers lists accordingly.
        """
        print("\nMatch 2:")

        team3 = self.q_finals_winners[2]
        team4 = self.q_finals_winners[3]

        if self.c1_goals == self.c2_goals:
            print(team3, self.c1_goals, f"({self.c1_penalties})")
            print(team4, self.c2_goals, f"({self.c2_penalties})")

            if self.c1_penalties == self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties > self.c2_penalties:
                print("WINNER:", team3)
                self.semi_finals_winners.append(team3)
                self.semi_finals_losers.append(team4)
            else:
                print("WINNER:", team4)
                self.semi_finals_winners.append(team4)
                self.semi_finals_losers.append(team3)
        else:
            print(team3, self.c1_goals)
            print(team4, self.c2_goals)

            if self.c1_goals > self.c2_goals:
                print("WINNER:", team3)
                self.semi_finals_winners.append(team3)
                self.semi_finals_losers.append(team4)
            else:
                print("WINNER:", team4)
                self.semi_finals_winners.append(team4)
                self.semi_finals_losers.append(team3)

    def semi_finals_winners_list(self):
        """
        Returns the list of teams that won in the semi-finals.
        """
        return self.semi_finals_winners

    def semi_finals_losers_list(self):
        """
        Returns the list of teams that lost in the semi-finals.
        """
        return self.semi_finals_losers

    def insert_scores_s_final(self, quarter_final_list):
        """
        Handles user input for both semi-final matches and returns results.

        Parameters:
        quarter_final_list (list): List of 4 quarter-final winners.

        Returns:
        list: [semi-final winners list, semi-final losers list, list of match objects]
        """
        goals_ = " FT goals (integers only):"
        penalties_ = " penalties (integers only; if there are no penalties enter 0):"

        # Match 1 input
        print(quarter_final_list[0] + " vs " + quarter_final_list[1])
        semi_finals_winners = []
        semi_finals_losers = []

        semi_finals_match_1 = SemiFinals(
            int(input(quarter_final_list[0] + goals_)),
            int(input(quarter_final_list[1] + goals_)),
            int(input(quarter_final_list[0] + penalties_)),
            int(input(quarter_final_list[1] + penalties_)),
            quarter_final_list,
            semi_finals_winners,
            semi_finals_losers
        )

        # Match 2 input
        print("\n" + quarter_final_list[2] + " vs " + quarter_final_list[3])
        semi_finals_match_2 = SemiFinals(
            int(input(quarter_final_list[2] + goals_)),
            int(input(quarter_final_list[3] + goals_)),
            int(input(quarter_final_list[2] + penalties_)),
            int(input(quarter_final_list[3] + penalties_)),
            quarter_final_list,
            semi_finals_winners,
            semi_finals_losers
        )

        match_list = [semi_finals_match_1, semi_finals_match_2]
        return [semi_finals_winners, semi_finals_losers, match_list]

    def print_semi_final(self, round_semi_final_list):
        """
        Prints the results of both semi-final matches.

        Parameters:
        round_semi_final_list (list): List containing the two SemiFinals match objects.
        """
        round_semi_final_list[0].s_round_1_result()
        round_semi_final_list[1].s_round_2_result()
