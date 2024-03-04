# from the question stem, the function of the density on the date is:
# (let the first day "date 0")  density(%)=5*(2**date)
# so we can manage it with while-loop
# input initial density and date
density=5
date=0
# set loop command
while density < 90:
    date=date+1
    density=2*density
print("on day", date+1, "the cell density goes over 90%")
date=date-1
print("I can have a holiday for at most", date, "days")