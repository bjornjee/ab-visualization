import yfinance as yf
import os

'''
Here, you can use the functions to pull balance sheet data for tickers
'''


class Scraper:

    #path of csv files
    DATA_PATH = os.path.join('/'.join(os.getcwd().split('/')[:-1]),'data')

    def __init__(self):
        pass

    #Gets balance sheet of ticker from yahoo finance
    def get_balance_sheet(self,ticker):
        stock = yf.Ticker(ticker)
        bs = stock.balance_sheet.transpose()
        bs['year'] = bs.index
        bs.reset_index(drop=True, inplace=True)
        return bs

    #Gets and saves balance sheet of ticker from yahoo finance. The file name will be in the form <TICKER>_balance_sheet.csv
    def save_balance_sheet_csv(self,ticker):
        #check if directory exists
        if not os.path.isdir(self.DATA_PATH):
            os.mkdir(self.DATA_PATH)
        stock = yf.Ticker(ticker)
        csv_path = os.path.join(self.DATA_PATH,"{}_balance_sheet.csv".format(ticker))
        bs = stock.balance_sheet.transpose()
        bs['year'] = bs.index
        bs.reset_index(drop=True,inplace=True)
        bs.to_csv(csv_path)

if __name__ == '__main__':
    s = Scraper()
    s.save_balance_sheet_csv("MSFT")