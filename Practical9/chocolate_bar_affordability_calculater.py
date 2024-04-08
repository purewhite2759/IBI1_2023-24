def chocolate_bar(total_money,price):
    """
    input: money you have and the price of one chocolate bar
    code: calculate how many bars you can buy and how much is left
    ouput: show the results
    """
    amount=total_money//price
    change=total_money%price
    return print("you can buy at most",amount,"chocolate bars.\nthere will be", change,"left")

#example
total_money=100 #the total money you have. the number can be changed
price=7 #the price of one chocolate bar. the number can be changed
chocolate_bar(total_money,price)