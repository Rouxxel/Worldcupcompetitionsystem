#!/usr/bin/env python
# coding: utf-8

# Third and Fourth place play-off class
class Third_and_Fourth:
    """
    A class to handle the third-place play-off match in a football tournament.
    It manages goal and penalty inputs and determines third and fourth positions.
    """

    def __init__(self, c1_goals=0, c2_goals=0, c1_penalties=0, c2_penalties=0, s_final_losers=[0]*2):
        """
        Initializes the match with goals, penalties, and the two teams.

        Parameters:
        c1_goals (int): Goals scored by team 1 in normal time.
        c2_goals (int): Goals scored by team 2 in normal time.
        c1_penalties (int): Penalty goals by team 1 (if any).
        c2_penalties (int): Penalty goals by team 2 (if any).
        s_final_losers (list): List of the two semi-final losers.
        """
        self.c1_goals = c1_goals
        self.c2_goals = c2_goals
        self.c1_penalties = c1_penalties
        self.c2_penalties = c2_penalties
        self.s_final_losers = [s_final_losers[0], s_final_losers[1]]

    def third_and_fourth_round_1_result(self):
        """
        Prints the result of the third-place play-off match.
        Handles both regular-time and penalty-based outcomes.
        """
        print("Third place play-off=\n")

        # If regular goals are tied, use penalties to decide
        if self.c1_goals == self.c2_goals:
            print(self.s_final_losers[0], self.c1_goals, f"({self.c1_penalties})")
            print(self.s_final_losers[1], self.c2_goals, f"({self.c2_penalties})\n")

            # Invalid if penalties are also tied
            if self.c1_penalties == self.c2_penalties:
                print("Invalid result, please restart")  
            elif self.c1_penalties > self.c2_penalties:
                print("Third:", self.s_final_losers[0])
                print("Fourth:", self.s_final_losers[1])
            else:
                print("Third:", self.s_final_losers[1])
                print("Fourth:", self.s_final_losers[0])

        # If regular goals are not tied, decide by goals
        else:
            print(self.s_final_losers[0], self.c1_goals)
            print(self.s_final_losers[1], self.c2_goals, "\n")

            if self.c1_goals > self.c2_goals:
                print("Third:", self.s_final_losers[0])
                print("Fourth:", self.s_final_losers[1])
            else:
                print("Third:", self.s_final_losers[1])
                print("Fourth:", self.s_final_losers[0])

    def insert_scores_third_n_fourth_round(self,s_losers):
        """
        Prompts the user for input to determine the third and fourth place match result.
        Instantiates a Third_and_Fourth object and prints the match outcome.

        Parameters:
        s_losers (list): List of two teams that lost in the semi-finals.
        """
        s_final_list = [s_losers[0], s_losers[1]]

        # Input prompts
        goals_ = " FT goals (integers only):"
        penalties_ = " penalties (integers only; if there are no penalties enter 0):"

        print(s_final_list[0] + " vs " + s_final_list[1])

        # Get match data from user input
        third_n_fourth_match = Third_and_Fourth(
            int(input(s_final_list[0] + goals_)),
            int(input(s_final_list[1] + goals_)),
            int(input(s_final_list[0] + penalties_)),
            int(input(s_final_list[1] + penalties_)),
            s_final_list
        )

        # Display match result
        third_n_fourth_match.third_and_fourth_round_1_result()
