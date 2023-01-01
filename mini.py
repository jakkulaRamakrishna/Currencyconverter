def EUR(a):
    return(a*79.82)
def USD(a):
    return(a*80.12)
def CHF(a):
    return(a*81.21)
def GBP(a):
    return(a*94.36)
def GIP(a):
    return(a*94.64)
def add():
    '''type "EUR" to convert "euro" into indian currency
       type "USD" to convert "u.s dolor" into inr
       type "CHF" to convert "swiss franic" into inr
       type "GBP" to convert "british pound" into inr
       type "GIP" to convert "gibraltar pound" into inr
       type "*" to stop converting'''
print(add.__doc__)
while True:
    ch=str(input('enter currency code :-'))
    if ch=='EUR':
        a=float(input('enter the amount to convert into indian currency :-'))
        print('RUPPES',EUR(a))
    elif ch=='USD':
        a=float(input('enter the amount to convert into indian currency :-'))
        print('RUPPES',USD(a))
    elif ch=='CHF':
        a=float(input('enter the amount to convert into indian currency :-'))
        print('RUPPES',CHF(a))
    elif ch=='GBP':
        a=float(input('enter the amount to convert into indian currency :-'))
        print('RUPPES',GBP(a))
    elif ch=='GIP':
        a=float(input('enter the amount to convert into indian currency :-'))
        print('RUPPES',GIP(a))
    elif ch=='*':
        break
    else:
        print('invalid input')
print('thanking you')
