
def computepay(hours, rate):
    
    if hours > 40 :
        regular_pay = 40 * rate 
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        total_pay = regular_pay + overtime_pay
    
    else : total_pay = hours * rate

    return total_pay

hours = float(input('Enter Hours : '))
rate = float(input('Enter Rate : '))

print ('Pay:',computepay(hours, rate))