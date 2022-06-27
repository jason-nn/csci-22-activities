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


from juice import JuiceMachine

sunkist = JuiceMachine()
minute_maid = JuiceMachine()

sunkist.sell_juice(12)
minute_maid.sell_juice(8)

sunkist.refill_machine(5.5)
minute_maid.refill_machine(7.25)

sunkist.sell_juice(17)
minute_maid.sell_juice(9)

print('--- SUNKIST MACHINE ---')
print(f'Cups of Sunkist Sold: {sunkist.get_total_cups_sold()} cups')
print(f'Remaining Sunkist: {sunkist.get_remaining_juice_amt()} liters')
print(f'Total Revenue: PHP {sunkist.get_revenue_total()}')

print()

print('--- MINUTE MAID MACHINE ---')
print(f'Cups of Minute Maid Sold: {minute_maid.get_total_cups_sold()} cups')
print(f'Remaining Minute Maid: {minute_maid.get_remaining_juice_amt()} liters')
print(f'Total Revenue: PHP {minute_maid.get_revenue_total()}')
