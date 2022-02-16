# Import of libraries
from random import randint

'''
	- The "Stock" class represents a stock. 
	- It has the attributes "price" and "date".
	- The "price" method returns the price for the stock.
'''
class Stock:
	price = None

	def __init__(self, date):
		self.date = date

	'''
		- This function is an assumption in the statement, so the "date" is insignificant.
		- The "delta" variable sets the amount to fluctuate later on the "price" variable.
		- The "delta" variable is a random value.
		- The value of the "price" variable will be between the range: [price - delta, price + delta].
	'''
	def price(self, date, base_price, variation):
		delta = randint(variation * -1, variation)
		price = base_price + delta
		return price

'''
	- The "Portfolio" class presents a portfolio.
	- The class has a list of "Stock" objects and attributes to set the total stock and start date and end date of the portfolio.
	- The "fill_stocks" method initializes the collection of stocks with random values.
	- The "profit" method calculates the annualized return.
'''
class Portfolio:
	stocks = []

	def __init__(self, total_stocks, initial_year, final_year):
		self.total_stocks = total_stocks
		self.initial_year = initial_year
		self.final_year = final_year

	'''
		- This function will create a "total_stocks" quantity of stocks.
		- Both the price and the stock date are random values.
	'''
	def fill_stocks(self):
		for i in range(self.total_stocks):
			year = randint(self.initial_year, self.final_year)
			month = randint(1, 12)
			day = randint(1, 31)
			date = (year, month, day)
			stock = Stock(date)
			stock.price = stock.price(date, 10000, 5000)
			self.stocks.append(stock)

	'''
		- The stock collection is ordered according to the date, in increasing order.
		- Then, a filter is made to only consider the stocks that are within the previously established dates.
		- If the stock is valid, then the initial investment is stored in a variable and the final investment in another variable.
		- The "flag" variable is used to know the initial investment and differentiate it from the final investment.
		- When the above values are known, the next step is to get the annualized return.
		- The formula for the annualized return was obtained from: https://www.buyupside.com/calculators/annualizedreturn.htm
	'''
	def profit(self, start_date, final_date):
		number_years_held = final_date[0] - start_date[0] + 1
		initial_investment = 0
		ending_investment = 0
		flag = True

		self.stocks.sort(key = lambda x: x.date)

		for i in range(self.total_stocks):
			yy, mm, dd = self.stocks[i].date
			price = self.stocks[i].price
			if self.stocks[i].date >= start_date and self.stocks[i].date <= final_date:
				if flag:
					initial_investment = self.stocks[i].price
					flag = False
				else:
					ending_investment = self.stocks[i].price

		annualized_return = ((ending_investment / initial_investment) ** (1 / number_years_held)) - 1

		return annualized_return

'''
	- Execution example.
	- 20 stocks are established between 2018 and 2022.
	- Then, the collection of stocks is initialized.
	- Finally, the profit between (2018, 1, 1) and (2021, 12, 31) is printed.
'''
p = Portfolio(20, 2018, 2022)
p.fill_stocks()
print(p.profit((2018, 1, 1), (2021, 12, 31)))