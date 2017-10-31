P = 1000
n = 12
r = .08

t = int (input('How many years will the money be compounded for ?'))
finalamount = P*(1+r/n)**(n*t)
print('The final amount is ', finalamount)