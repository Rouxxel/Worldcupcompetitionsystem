#!/usr/bin/env python
# coding: utf-8

# Final round class
class FinalRound:
    """
    A class to handle the final round of a football tournament, including
    goals, penalties, and determining the champion and sub-champion teams.
    """

    def __init__(self, c1_goals=0, c2_goals=0, c1_penalties=0, c2_penalties=0, s_final_wss=[0]*2):
        """
        Initializes the final round match data.

        Parameters:
        c1_goals (int): Goals scored by team 1 in normal time.
        c2_goals (int): Goals scored by team 2 in normal time.
        c1_penalties (int): Penalty goals by team 1 (if any).
        c2_penalties (int): Penalty goals by team 2 (if any).
        s_final_wss (list): List containing names of the two finalist teams.
        """
        self.c1_goals = c1_goals
        self.c2_goals = c2_goals
        self.c1_penalties = c1_penalties
        self.c2_penalties = c2_penalties
        self.s_final_wss = [s_final_wss[0], s_final_wss[1]]

    def round_1_result(self):
        """
        Prints the result of the final round, including goals, penalties (if any),
        and determines which team is the champion and which is the sub-champion.
        """
        print("Grand Final=\n")

        # If goals are tied, decide by penalties
        if self.c1_goals == self.c2_goals:
            print(self.s_final_wss[0], self.c1_goals, f"({self.c1_penalties})")
            print(self.s_final_wss[1], self.c2_goals, f"({self.c2_penalties})\n")

            # Check if penalty scores are also tied (invalid)
            if self.c1_penalties == self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties > self.c2_penalties:
                print("CHAMPION:", self.s_final_wss[0])
                print("Sub-champion:", self.s_final_wss[1])
            else:
                print("CHAMPION:", self.s_final_wss[1])
                print("Sub-champion:", self.s_final_wss[0])

        # If not tied, determine winner by regular goals
        else:
            print(self.s_final_wss[0], self.c1_goals)
            print(self.s_final_wss[1], self.c2_goals, "\n")

            if self.c1_goals > self.c2_goals:
                print("CHAMPION:", self.s_final_wss[0])
                print("Sub-champion:", self.s_final_wss[1])
            else:
                print("CHAMPION:", self.s_final_wss[1])
                print("Sub-champion:", self.s_final_wss[0])

    def insert_scores_final_round(self, s_winners):
        """
        Prompts the user to input scores and penalties for the final match based on
        the two semi-final winners. It then initializes a final round object and
        displays the match results.

        Parameters:
        s_winners (list): List of the two teams that qualified for the final.
        """
        # Assign semi-final winners to a local list
        s_final_list = [s_winners[0], s_winners[1]]

        # Prompt messages for input
        goals_ = " FT goals (integers only):"
        penalties_ = " penalties (integers only; if there are no penalties enter 0):"

        print(s_final_list[0] + " vs " + s_final_list[1])

        # Collecting user input for the final match
        final_match = FinalRound(
            int(input(s_final_list[0] + goals_)),
            int(input(s_final_list[1] + goals_)),
            int(input(s_final_list[0] + penalties_)),
            int(input(s_final_list[1] + penalties_)),
            s_final_list
        )

        # Display the final result
        final_match.round_1_result()
