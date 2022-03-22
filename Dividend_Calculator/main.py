from time import gmtime, strftime
import json
import math

# Ticker   - The ticker of the stock you want to investigate (will be used to automate gather data at a later point)
# Price    - The current price of the stock
# Shares   - The amount of shares you own or want to calculate dividends for holding
# Dividend - The dividend amount you earn per share in decimal form
# Quarters - The amount of quarters the stock pays in every year (normally 4)
# MaxYears - The amount of years to project calculations for holding dividends
# CurrYear - The current year now

# These are your input parameters
Ticker = input("Enter the stock ticker you'd like to investigate: ")
Price = float(input("Enter the current price of the stock: "))
Shares = int(input("Enter the amount of shares you would like to calculate holdings: "))
Dividend = float(input("Enter the div/yield: "))
Quarters = 4
MaxYears = int(input("Enter the amount of years you want to hold the stock: "))
CurrYear = int(strftime("%Y"))

# In each year are 4 Quarters, Annual Income, and Annual Shares
# In each quarter there are Profit,
#   Profit/Price
#       ReInvest of the stock and
#           Current Stock holding
#       P/P is used to find how many additional stocks you can buy if reinvested
#           based on the profit earned from dividends
#       ReInvest is rounded down from P/P to estimate the exact amount of additional stocks to buy
#       Cur is the current amount of stocks in that quarter



years = {}

for yr in range(0, MaxYears + 1):
    years[CurrYear + yr] = {}
    AI = 0  # Annual Income

    for q in range(1, Quarters + 1):
        Q = {}
        Q["Profit"] = round(Shares * Dividend, 3)  # rounded down to cents
        AI += Q["Profit"]
        Q["P/P"] = round(Q["Profit"] / Price, 3)  # rounded down to 3 decs
        Q["ReInvest"] = math.floor(Q["P/P"])
        Q["Cur"] = Shares
        #         AS = {}
        #         AS.Q["Cur"])
        Shares += Q["ReInvest"]  # update the current shares for next quarter
        years[CurrYear + yr]["Q" + str(q)] = Q

    years[CurrYear + yr]["Annual Income"] = round(AI, 3)
    years[CurrYear + yr]["Annual Shares"] = years[CurrYear + yr]["Q" + ((str)(Quarters))]["Cur"]

print(json.dumps(years, indent=4))
