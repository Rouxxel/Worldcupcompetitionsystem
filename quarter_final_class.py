#!/usr/bin/env python
# coding: utf-8

# QuarterFinals class to handle quarter-final stage of a knockout tournament
class QuarterFinals:
    # Note: Avoid using mutable class-level variables like this in production code.
    quarter_finals_winners = []  # Shared list to store winners moving to the semi-finals

    def __init__(self, c1_goals=0, c2_goals=0, c1_penalties=0, c2_penalties=0,
                r_16_winners=[0]*8, quarter_finals_winners=quarter_finals_winners):
        """
        Initialize a QuarterFinals match instance with goals, penalties, previous round winners, and a shared winner list.
        
        Args:
            c1_goals (int): Goals scored by team 1.
            c2_goals (int): Goals scored by team 2.
            c1_penalties (int): Penalty goals by team 1.
            c2_penalties (int): Penalty goals by team 2.
            r_16_winners (list): List of 8 winners from Round of 16.
            quarter_finals_winners (list): Shared list to store winners of each quarter-final match.
        """
        self.c1_goals = c1_goals
        self.c2_goals = c2_goals
        self.c1_penalties = c1_penalties
        self.c2_penalties = c2_penalties
        self.r_16_winners = r_16_winners.copy()
        self.quarter_finals_winners = quarter_finals_winners

    def quarter_round_1_result(self):
        """Prints the result of Quarter Final Match 1 and appends winner to the winners list."""
        print("Quarter finals=")
        print("\nMatch 1:")

        if self.c1_goals == self.c2_goals:
            # Match tied, use penalties
            print(self.r_16_winners[0], self.c1_goals, f"({self.c1_penalties})")
            print(self.r_16_winners[1], self.c2_goals, f"({self.c2_penalties})")

            if self.c1_penalties == self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties > self.c2_penalties:
                print("WINNER:", self.r_16_winners[0])
                self.quarter_finals_winners.append(self.r_16_winners[0])
            else:
                print("WINNER:", self.r_16_winners[1])
                self.quarter_finals_winners.append(self.r_16_winners[1])
        else:
            # Regular time result
            print(self.r_16_winners[0], self.c1_goals)
            print(self.r_16_winners[1], self.c2_goals)

            if self.c1_goals > self.c2_goals:
                print("WINNER:", self.r_16_winners[0])
                self.quarter_finals_winners.append(self.r_16_winners[0])
            else:
                print("WINNER:", self.r_16_winners[1])
                self.quarter_finals_winners.append(self.r_16_winners[1])

    def quarter_round_2_result(self):
        """Prints the result of Quarter Final Match 2 and appends winner to the winners list."""
        print("\nMatch 2:")
        if self.c1_goals == self.c2_goals:
            print(self.r_16_winners[2], self.c1_goals, f"({self.c1_penalties})")
            print(self.r_16_winners[3], self.c2_goals, f"({self.c2_penalties})")

            if self.c1_penalties == self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties > self.c2_penalties:
                print("WINNER:", self.r_16_winners[2])
                self.quarter_finals_winners.append(self.r_16_winners[2])
            else:
                print("WINNER:", self.r_16_winners[3])
                self.quarter_finals_winners.append(self.r_16_winners[3])
        else:
            print(self.r_16_winners[2], self.c1_goals)
            print(self.r_16_winners[3], self.c2_goals)

            if self.c1_goals > self.c2_goals:
                print("WINNER:", self.r_16_winners[2])
                self.quarter_finals_winners.append(self.r_16_winners[2])
            else:
                print("WINNER:", self.r_16_winners[3])
                self.quarter_finals_winners.append(self.r_16_winners[3])

    def quarter_round_3_result(self):
        """Prints the result of Quarter Final Match 3 and appends winner to the winners list."""
        print("\nMatch 3:")
        if self.c1_goals == self.c2_goals:
            print(self.r_16_winners[4], self.c1_goals, f"({self.c1_penalties})")
            print(self.r_16_winners[5], self.c2_goals, f"({self.c2_penalties})")

            if self.c1_penalties == self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties > self.c2_penalties:
                print("WINNER:", self.r_16_winners[4])
                self.quarter_finals_winners.append(self.r_16_winners[4])
            else:
                print("WINNER:", self.r_16_winners[5])
                self.quarter_finals_winners.append(self.r_16_winners[5])
        else:
            print(self.r_16_winners[4], self.c1_goals)
            print(self.r_16_winners[5], self.c2_goals)

            if self.c1_goals > self.c2_goals:
                print("WINNER:", self.r_16_winners[4])
                self.quarter_finals_winners.append(self.r_16_winners[4])
            else:
                print("WINNER:", self.r_16_winners[5])
                self.quarter_finals_winners.append(self.r_16_winners[5])

    def quarter_round_4_result(self):
        """Prints the result of Quarter Final Match 4 and appends winner to the winners list."""
        print("\nMatch 4:")
        if self.c1_goals == self.c2_goals:
            print(self.r_16_winners[6], self.c1_goals, f"({self.c1_penalties})")
            print(self.r_16_winners[7], self.c2_goals, f"({self.c2_penalties})")

            if self.c1_penalties == self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties > self.c2_penalties:
                print("WINNER:", self.r_16_winners[6])
                self.quarter_finals_winners.append(self.r_16_winners[6])
            else:
                print("WINNER:", self.r_16_winners[7])
                self.quarter_finals_winners.append(self.r_16_winners[7])
        else:
            print(self.r_16_winners[6], self.c1_goals)
            print(self.r_16_winners[7], self.c2_goals)

            if self.c1_goals > self.c2_goals:
                print("WINNER:", self.r_16_winners[6])
                self.quarter_finals_winners.append(self.r_16_winners[6])
            else:
                print("WINNER:", self.r_16_winners[7])
                self.quarter_finals_winners.append(self.r_16_winners[7])

    def quarter_finals_winners_list(self):
        """Returns the list of winners from all quarter-final matches."""
        return self.quarter_finals_winners

    def insert_scores_quarter_final(self, r16_list):
        """
        Gets user input for all four quarter-final matches and returns match objects and winners.
        
        Args:
            r16_list (list): List of 8 winners from Round of 16.
        
        Returns:
            tuple: (list of winners, list of match objects)
        """
        # Prompts
        goals_ = " FT goals (integers only):"
        penalties_ = " penalties (integers only; if there are no penalties enter 0):"

        # Match 1
        print(r16_list[0] + " vs " + r16_list[1])
        match1 = QuarterFinals(int(input(r16_list[0] + goals_)),
                               int(input(r16_list[1] + goals_)),
                               int(input(r16_list[0] + penalties_)),
                               int(input(r16_list[1] + penalties_)),
                               r16_list)

        # Match 2
        print("\n" + r16_list[2] + " vs " + r16_list[3])
        match2 = QuarterFinals(int(input(r16_list[2] + goals_)),
                               int(input(r16_list[3] + goals_)),
                               int(input(r16_list[2] + penalties_)),
                               int(input(r16_list[3] + penalties_)),
                               r16_list)

        # Match 3
        print("\n" + r16_list[4] + " vs " + r16_list[5])
        match3 = QuarterFinals(int(input(r16_list[4] + goals_)),
                               int(input(r16_list[5] + goals_)),
                               int(input(r16_list[4] + penalties_)),
                               int(input(r16_list[5] + penalties_)),
                               r16_list)

        # Match 4
        print("\n" + r16_list[6] + " vs " + r16_list[7])
        match4 = QuarterFinals(int(input(r16_list[6] + goals_)),
                               int(input(r16_list[7] + goals_)),
                               int(input(r16_list[6] + penalties_)),
                               int(input(r16_list[7] + penalties_)),
                               r16_list)

        quarter_finals_round_list = [match1, match2, match3, match4]

        # Return winners and list of match objects
        winner_handler = QuarterFinals()
        return [winner_handler.quarter_finals_winners_list(), quarter_finals_round_list]

    def print_quarter_final(self, quarter_finals_round_list):
        """
        Prints the results of all four quarter-final matches.
        
        Args:
            quarter_finals_round_list (list): List of QuarterFinals match objects.
        """
        quarter_finals_round_list[0].quarter_round_1_result()
        quarter_finals_round_list[1].quarter_round_2_result()
        quarter_finals_round_list[2].quarter_round_3_result()
        quarter_finals_round_list[3].quarter_round_4_result()
