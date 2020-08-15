'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all
hours worked above 40 hours. Put the logic to do the computation of pay in a function called
computepay() and use the function to do the computation. The function should return a value.
'''

# h : total hours
# r : rate per hour
def computepay(h, r):
    totalPay = 0
    overtime = 0
    extraHours = 0.

    # convert string to float
    hrs = float(h)
    rate = float(r)

    if hrs <= 40:
    	totalPay = hrs * rate
    else:
        extraHours = hrs - 40
        totalPay = (40 * rate) + (extraHours * rate * 1.5)

	return totalPay

hInput = input("Enter Hours:")
rInput = input("Enter Rate:")

p = computepay(hInput, rInput)

print("Pay", p)
