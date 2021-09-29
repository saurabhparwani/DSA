# Problem Statement : https://www.geeksforgeeks.org/buy-maximum-stocks-stocks-can-bought-th-day/

class Stock(object):
    def __init__(self,price,day):
        self.price = price
        self.day = day

def maximumStock(price,k):
    stock_price = []
    total_stocks =0

    for i in range(0,len(price)):
        stock_price.append(Stock(price[i],i+1))

    stock_price = sorted(stock_price,key= lambda x : x.price)

    for stock in stock_price:

        # Calculate the Units we can purchase on a particular day
        unites = min(stock.day,(k//stock.price))
        total_stocks = total_stocks + unites
        k = k - (unites*stock.price)

    return total_stocks



# Driver Code
price = [7, 10, 4]
k = 100

print('Maximum Number of stock that  person can buy {}'.format(maximumStock(price,k)))
