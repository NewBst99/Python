from dataclasses import replace
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def NaverKospi(result):
    for page in range(1, 42):
        print("Processing... Page :", page)
        Kospi_URL = "https://finance.naver.com/sise/sise_market_sum.naver?&page=%d" %page
        html = urllib.request.urlopen(Kospi_URL)
        soupKospi = BeautifulSoup(html, "html.parser")
        tag_tbody = soupKospi.find("tbody")

        for stock in tag_tbody.find_all("tr"):
            if len(stock.find_all("td")) < 3:
                continue
            stock_td = stock.find_all("td")
            kospi_name = stock_td[1].find("a").string 
            # kospi_name = stock_td[1].select("a").string 
            kospi_current = stock_td[2].string
            kospi_prev = stock_td[3].find("span").string.strip()
            kospi_rate = stock_td[4].find("span").string.strip()
            kospi_face = stock_td[5].string
            kospi_capital = stock_td[6].string
            kospi_share = stock_td[7].string
            kospi_foreign = stock_td[8].string
            kospi_trade = stock_td[9].string
            kospi_PER = stock_td[10].string
            kospi_ROE = stock_td[11].string
        
            result.append([kospi_name] + [kospi_current] + [kospi_prev] + [kospi_rate]
                        + [kospi_face] + [kospi_capital] + [kospi_share] + [kospi_foreign] 
                            + [kospi_trade] + [kospi_PER] + [kospi_ROE])
    return

def main():
    result = []
    print("Naver KOSPI Crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    NaverKospi(result)
    stock_tbl = pd.DataFrame(result, columns = ("kospi_name", "kospi_current", "kospi_prev", "kospi_rate"
                                                , "kospi_face", "kospi_capital", "kospi_share", "kospi_foreign"
                                                , "kospi_trade", "kospi_PER", "kospi_ROE"))
    stock_tbl.to_csv("./data/Naver_KOSPI.csv", encoding = "cp949", mode = "w", index = True, errors = "replace")
    del result[:]

if __name__ == "__main__":
    main()