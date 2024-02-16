# Write your code here
def cakes(eggs,butter,flour):
    cake_egg = eggs//5
    cake_butter = butter//250
    cake_flour = flour//250
    return min(cake_egg,cake_butter,cake_flour)

cakes(18,600,1000)