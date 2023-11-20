import requests
import arrow

'''
# Your Alpha Vantage API key
api_key = 'E0LJK4KZCX5VLHLU'
base_url = "https://www.alphavantage.co/query"
'''


# Function to find the closest Wednesday to a given date
def find_closest_wednesday(date):
    while date.format('dddd') != 'Wednesday':
        date = date.shift(days=-1)
    return date.format('YYYY-MM-DD')


'''
# Function to retrieve stock price on a specific date for a given ticker
def get_stock_price_on_date(ticker, date):
    function = "TIME_SERIES_DAILY"
    params = {
        "function": function,
        "symbol": ticker,
        "apikey": api_key,
    }
'''
# 3 Sections: 1. Get date and stock prices info, 2. Calculations 3.Output
# Input
ticker = input("Enter Stock Ticker: ")

# section 1. get date and stock prices info......................................
# dates
today = arrow.now()
datefourma = find_closest_wednesday(today.shift(months=-4))
todaycorrect = find_closest_wednesday(today)

# stock and sp prices
tickerfourma = 60
spfourma = 900
tickerrecent = 100
sprecent = 1000
tickerhigh = 150
sector = "technology"
pe = 25
marketcap = 1000000000

# Section 2. calculations.......................................................
tickerdiff = tickerrecent / tickerfourma
spdiff = sprecent / spfourma * 10
potupsideticker = tickerhigh / tickerrecent * 10
sectorrotation = 0;

if (sector == "finance", "cyclicals"):
    sectorrotation = sectorrotation + 0.5

if (sector == "technology", "industrials", "basic materials"):
    sectorrotation = sectorrotation + 1

if (sector == "staples", "energy"):
    sectorrotation = sectorrotation + 0

if (sector == "healthcare", "utilies"):
    sectorrotation = sectorrotation - 1

if spdiff < -10:
    sectorrotation = sectorrotation * -1

print(sectorrotation)

if sectorrotation > 0.5:
    sectorcorrect = "well positioned sector"
if sectorrotation < -0.5:
    sectorcorrect = "poorly positioned sector"
if -0.5 <= sectorrotation <= 0.5:
    sectorcorrect = "ok positioned sector"

risk = (abs(tickerdiff - 1)) * -1
print(risk)

bshnum = risk + potupsideticker + sectorrotation
print(bshnum)

# pe
pefinal = pe
# risk
if risk > 0.5:
    riskfinal = "low risk"
if risk < -0.5:
    riskfinal = "high risk"
if -0.5 <= risk <= 0.5:
    riskfinal = "normal risk"

if (bshnum > 1):
    bshstring = "BUY"
if (-1 <= bshnum <= 1):
    bshstring = "HOLD"
if (bshnum < -1):
    bshstring = "SELL"

# output.....................................................................

print("\n" + ticker + " is rated a " + bshstring + ", weight: ", end="")
print(bshnum, end="")

print(".\n\nFactors Calculated: \n Sector (includes current economic state): " + ticker + " is in a " + sectorcorrect,
      end="")
print(" \n Risk: " + ticker + " has " + riskfinal, end="")
print(" \n Potential Upside: " + ticker + " has a potential upside of " + str(potupsideticker) + "%")

'''
#Percentage Difference 4 Months to Now SP500
spdiff = sprecent/spfourma *10
print(spdiff)

#Price Ticker Dec 2021
tickerhigh = (get_stock_price_on_date(ticker_input, '2021-11-19'))
print(tickerhigh)

    #Percentage Upside Potential
    #State of the economy
    #Sector of Ticker
    #



ENTIRE PRIOR
import requests
import arrow

# Your Alpha Vantage API key
api_key = 'E0LJK4KZCX5VLHLU'
base_url = "https://www.alphavantage.co/query"


# Function to find the closest Wednesday to a given date
def find_closest_wednesday(date):
    while date.format('dddd') != 'Wednesday':
        date = date.shift(days=-1)
    return date.format('YYYY-MM-DD')


# Function to retrieve stock price on a specific date for a given ticker
def get_stock_price_on_date(ticker, date):
    function = "TIME_SERIES_DAILY"
    params = {
        "function": function,
        "symbol": ticker,
        "apikey": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if 'Time Series (Daily)' in data:
            daily_data = data['Time Series (Daily)']

            if date in daily_data:
                stock_price = float(daily_data[date]['4. close'])  # Convert price to float
                return stock_price
            else:
                print(f"Stock price not available for {ticker} on {date}")
                print("Available dates:")
                for available_date in daily_data:
                    print(available_date)
        else:
            print(f"No daily data found for {ticker}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


# Main program execution
if __name__ == "__main__":
    ticker_input = input("Enter Stock Ticker: ")
    IVV = 'IVV'

    # Get today's date
    today = arrow.now()

    # Find dates for 4 months ago and recent Wednesday
    datefourma = find_closest_wednesday(today.shift(months=-4))
    todaycorrect = find_closest_wednesday(today)

    # Price Ticker 4 Months Ago
    tickerfourma = get_stock_price_on_date(ticker_input, datefourma)
    print(f"Price of {ticker_input} 4 months ago: {tickerfourma}")

    # Price Ticker Recent Wednesday
    tickerrecent = get_stock_price_on_date(ticker_input, todaycorrect)
    print(f"Price of {ticker_input} on recent Wednesday: {tickerrecent}")

    # Percentage Difference 4 Months to Now Ticker
    if tickerrecent and tickerfourma:
        difftick = ((tickerrecent - tickerfourma) / tickerfourma) * 100  # Calculate percentage difference
        #print(f"Percentage difference of {ticker_input} from 4 months ago to recent: {difftick:.2f}%")


    #Price Ticker 4 Months Ago
    tickerfourma = (get_stock_price_on_date(ticker_input, datefourma))
    print(tickerfourma)

    #Price SP500 4 Months Ago
    spfourma = (get_stock_price_on_date(IVV, datefourma))
    print(spfourma)

    #Price Ticker Recent Wednesday
    tickerrecent = (get_stock_price_on_date(ticker_input, todaycorrect))
    print(tickerrecent)

    #Price SP500 Recent Wednesday
    sprecent = (get_stock_price_on_date(IVV, todaycorrect))
    print(sprecent)

    #Percentage Difference 4 Months to Now Ticker
    tickerdiff = tickerrecent/tickerfourma *10
    print(tickerdiff)

    #Percentage Difference 4 Months to Now SP500
    spdiff = sprecent/spfourma *10
    print(spdiff)

    #Price Ticker Dec 2021
    tickerhigh = (get_stock_price_on_date(ticker_input, '2021-11-19'))
    print(tickerhigh)

    #Percentage Upside Potential
    #State of the economy
    #Sector of Ticker
    #


END



api_key = 'E0LJK4KZCX5VLHLU'
base_url = "https://www.alphavantage.co/query"

# Function to retrieve stock overview data
def get_stock_overview(ticker):
    function = "OVERVIEW"

    params = {
        "function": function,
        "symbol": ticker,
        "apikey": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        stock_data = response.json()

        if 'Sector' in stock_data and 'MarketCapitalization' in stock_data and 'PERatio' in stock_data:
            company_sector = stock_data['Sector']
            market_cap = stock_data['MarketCapitalization']
            pe_ratio = stock_data['PERatio']

            print(f"Sector of {ticker}: {company_sector}")
            print(f"Market Cap of {ticker}: {market_cap}")
            print(f"P/E Ratio of {ticker}: {pe_ratio}")




            return stock_data
        else:
            print(f"Data not found for {ticker}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Main program execution
if __name__ == "__main__":
    ticker_input = input("Enter Stock Ticker: ")
    get_stock_overview(ticker_input)
# Get today's date
today = arrow.now()

def find_closest_wednesday(date):
    while date.format('dddd') != 'Wednesday':
        date = date.shift(days=-1)
    return date.format('YYYY-MM-DD')

# Get today's date
today = arrow.now()

#dates
todaycorrect = find_closest_wednesday(today)
print(todaycorrect)
todaycorrectminus = (arrow.get(todaycorrect).shift(days=-1)).format('YYYY-MM-DD')
print(todaycorrectminus)

dateonema = find_closest_wednesday(today.shift(months=-1))
datesixma = find_closest_wednesday(today.shift(months=-6))
datesixmaminus = (arrow.get(datesixma).shift(days=-1))
datetwelvema = find_closest_wednesday(today.shift(months=-12))
datetwelvemaminus = (arrow.get(todaycorrect).shift(days=-1))




#stock ticker input
tick = input("Enter Stock Ticker ")
ticker = yf.Ticker(tick)
price = ticker.history(start='2023-11-7', end='2023-11-8')['Close'].values[0]
print(price)

#variables
#time variables
def find_closest_wednesday(date):
    while date.format('dddd') != 'Wednesday':
        date = date.shift(days=-1)
    return date.format('YYYY-MM-DD')

# Get today's date
today = arrow.now()

E0LJK4KZCX5VLHLU.
#dates
todaycorrect = find_closest_wednesday(today)
print(todaycorrect)
todaycorrectminus = (arrow.get(todaycorrect).shift(days=-1)).format('YYYY-MM-DD')
print(todaycorrectminus)

dateonema = find_closest_wednesday(today.shift(months=-1))
datesixma = find_closest_wednesday(today.shift(months=-6))
datesixmaminus = (arrow.get(datesixma).shift(days=-1))
datetwelvema = find_closest_wednesday(today.shift(months=-12))
datetwelvemaminus = (arrow.get(todaycorrect).shift(days=-1))

#economy variable


HERE
E0LJK4KZCX5VLHLU
spfive = yf.Ticker('AAPL')

# Calculate the date six months ago
spfivecurrentprice = arrow.now().shift(months=-6).format('YYYY-MM-DD')

# Fetching the price for six months ago
stock_price_six_months_ago = spfive.history(start=datesixmaminus, end=datesixma)['Close'].values[0]
print(stock_price_six_months_ago)

spfive = yf.Ticker('IVV')
spfivecurrentprice = spfive.history(start=todaycorrectminus, end = todaycorrect)['Close'].values[0]
print(spfivecurrentprice)

spsixma = spfive.history(start=datesixmaminus, end = datesixma)['Close'].values[0]
print(spsixma)

econ = (spfivecurrentprice/spsixma)
print(econ)


print(ticker.history(start=datesixmaminus, end = datesixma)['holders'])

spcurrent = (yf.download('IVV', start=todaycorrectminus, end=todaycorrect)['Adj Close'])
print(spcurrent)
spsixma = (yf. download('IVV', start = datesixmaminus, end = datesixma) ['Adj Close'])
print(spsixma)
spcurrent, spsixma = spcurrent.align(spsixma, join='inner')

print (spcurrent - spsixma)


sptwelvem = (yf. download('IVV', start = datetwelvema, end = datetwelvema) ["Adj Close"])

sptwelvem = (yf. download('IVV', start = datetwelvema, end = datetwelvema) ["Adj Close"])
speighteenm = (yf. download('IVV', start = dateeighteenma, end = dateeighteenma) ["Adj Close"])
econdiff = ((sponem + spthreem + sptwelvem)/3) - speighteenm
econ= spcurrent/econdiff

print(econ)

#decision variables


adjclose = (yf. download(tick, start = datesixma, end = today) ["Adj Close"])
print(adjclose)
dif = adjclose - 1
print(dif)

E0LJK4KZCX5VLHLU
'''