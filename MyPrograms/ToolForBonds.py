def calculate_investment():
    # Initial - at the start of each 6 months
    # Current - during the period
    initial,current = 1000,1000
    # Interst rate per month
    interestRate = 0.021/12 
    # Years till no more interest is paid
    maturity = 360 
    # Initial year
    x = 1 
    # Interst generated each month
    interest = 0 
    # Additional payments each month
    additional = 8.33334 
    
    while x <= maturity:
        print("______________________________________________________________________________________________")
        print(f"This is month {x}, with [{current} - current] and [{initial} - initial], plus ${interest} interest".format(x,current,initial,interest))
        if (x % 6) ==0:
            #Interest
            interest = round((initial*interestRate), ndigits=2)
            print("This is interest for month ", x," interest - ",interest)

            current = current + interest
            current = current + additional
            current = round(current,ndigits=2)
            initial = current 
            x += 1
            
        else:    
            interest = round((initial*interestRate), ndigits=2)
            current = current + interest
            current = current + additional
            current = round(current,ndigits=2)
            x += 1
    
    print("End balance",current)
    
        
    
calculate_investment()
