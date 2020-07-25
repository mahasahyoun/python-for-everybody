# Get inputs as string
strHrs = input("Enter Hours: ")
strRate = input("Enter Rate: ")

# Convert input from string to number
floatHrs = float(strHrs)
floatRate= float(strRate)

# Compute gross pay
grossPay = floatHrs*floatRate

print("Pay:" + " ")
print(grossPay)