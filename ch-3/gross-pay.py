hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

# Regular hours
regularPay = r * h

# Overtime hours
if (h > 40):
    extra = h - 40
    overtimePay = extra * 0.5 * r
else:
	overtimePay = 0
    
# Gross pay
grossPay = regularPay + overtimePay

print(grossPay)