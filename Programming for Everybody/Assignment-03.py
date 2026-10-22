
# input

hours = input('Enter Hours : ') 
hours = float(hours)
rate = input('Enter Rate : ')
rate = float(rate)

# regular pay + extra

regular_pay = 40 * rate
extra_hours = hours - 40
extra_payment = extra_hours * (rate * 1.5)
overtime_fees = regular_pay + extra_payment

if (hours<=40):
    print (hours*rate) # gross pay

else :
    print (overtime_fees)