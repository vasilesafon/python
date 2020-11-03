#! python
import sys
name, hours, price, prize = sys.argv
print(sys.argv)
print(float(hours) * float(price) + float(prize))
input('Press any Enter to exit')
