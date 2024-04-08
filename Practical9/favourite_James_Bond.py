#predict the one's favourite James Bond with his(or her) birthyear.
def James_Bond(birth_year):
    """
    input: the year one was born in (in the form of str)
    code: find his (or her) favourite James Bond (with the certain theory)
    output: the name of the actor
    """
    #the theory is that each person’s favourite James Bond actor is the person who played the character when they turned 18
    year=int(birth_year)+18 #transform the 'str' input to 'int', and calculate the year when he/she is 18 years old
    if year>=1973 and year<=1986:
        return print('Roger Moore')
    if year>=1986 and year<=1994:
        return print('Timothy Dalton')
    if year>=1994 and year<=2005:
        return print('Pierce Brosnan')
    if year>=2005 and year<=2021:
        return print('Daniel Craig')

#example   
birth = '1972'  #you can replace the number with other numbers(the year on was born in)
James_Bond(birth)