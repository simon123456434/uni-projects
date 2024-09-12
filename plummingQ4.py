urgent = True # input true or false 
minuets = 119 #moniets
hours = 1  #hours
cost = 0 #total cost depending on control flow. 


# none urgent call out if statment
if urgent == False and minuets > 60:
     hours = minuets // 60
     if minuets % 60 == 0 and urgent == False:
         hours = minuets // 60-1
     cost = 100 + hours * 50 
     



# urgent call out if statment 
if urgent == True and minuets > 60: 
    hours = minuets // 60
    if minuets % 60 == 0 and urgent == True:
        hours = minuets // 60-1
    cost = 200 + hours * 80
        

print(cost)
