import urllib2
from bs4 import BeautifulSoup



portfolio = [
             ('cvx', 27.769),
             ('ge', 25.523),
             ('ibm', 23.797),
             ('intc', 5.062),
             ('ko', 25.636),
             ('pfe', 2.031),
             ('t', 31.999),
             ('vlo', 12.294),
             ('wmt', 4.044), 
             ('xom', 53.924) 
            ]

def get_dividend_amount(symbol):
    '''
    Return dividend amount for given symbol.
    Goes to nasdaq dividned history page, looks up given stock symbol.
    '''
    stock_url = 'http://www.nasdaq.com/symbol/%s/dividend-history' %symbol
    remote_fp = urllib2.urlopen(stock_url)

    soup = BeautifulSoup(remote_fp.read(), 'html.parser')

    amount = soup.find('table', id='quotes_content_left_dividendhistoryGrid').find('tbody').find('tr').find_all('td')[2].find('span').renderContents()
    
    print '%s: %s' %(symbol, amount)
    remote_fp.close()
    
    return amount

#================================================================
def main():
    total = 0
    for component in portfolio:
        
        total = total + (float(get_dividend_amount(component[0])) * component[1] * 4)

    print 'Total yearly income: %s' %total

if __name__ == '__main__':
    main()
