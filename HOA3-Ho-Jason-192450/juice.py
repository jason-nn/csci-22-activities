# Jason L. Ho, 192450
# June 27, 2022

# I certify that this submission complies with the DISCS Academic
# Integrity Policy.

# If I have discussed my Python code with anyone other than
# my instructor(s), my groupmate(s), the teaching assistant(s),
# the extent of each discussion has been clearly noted along with a
# proper citation in the comments of my program.

# If any Python code or documentation used in my program was obtained
# from another source, either modified or unmodified, such as a textbook,
# website, or another individual, the extent of its use has been clearly
# noted along with a proper citation in the comments of my program.

# SOURCES HERE


class JuiceMachine:
    def __init__(self):
        self.remaining_juice_amt = 7.5
        self.revenue_total = 0
        self.total_cups_sold = 0
        self.cost_per_cup = 12.50
        self.volume_per_cup = 240 / 1000

    def refill_machine(self, refill_amt):
        self.remaining_juice_amt += refill_amt

    def sell_juice(self, numcups):
        self.total_cups_sold += numcups
        self.revenue_total += (numcups * self.cost_per_cup)
        self.remaining_juice_amt -= (numcups * self.volume_per_cup)

    def get_remaining_juice_amt(self):
        return "{:.2f}".format(self.remaining_juice_amt)

    def get_total_cups_sold(self):
        return self.total_cups_sold

    def get_revenue_total(self):
        return "{:.2f}".format(self.revenue_total)
