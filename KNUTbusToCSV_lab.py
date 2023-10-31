from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def knut_bus_table(result):
    Knut_url = "https://www.ut.ac.kr/kor/sub06_06_01.do"
    html = urllib.request.urlopen(Knut_url)
    soupKnut = BeautifulSoup(html, "html.parser")

    tag_thead = soupKnut.find_all("thead")[1]
    bus_th = tag_thead.find_all("th")
    bus_campus_1 = bus_th[0].string.split("⇒")
    bus_campus_2 = bus_th[2].string.split("⇒")
    bus_campus_3 = bus_th[4].string.split("⇔")

    tag_tbody = soupKnut.find_all("tbody")[2]
    for bus in tag_tbody.find_all("tr"):
        if len(bus.find_all("td")) < 6:
                continue
        bus_td = bus.find_all("td")
        departure_time_1 = bus_td[0].string
        arrival_time_1 = bus_td[1].string
        bus_name_1 = bus_td[2].string
        departure_time_2 = bus_td[3].string
        arrival_time_2 = bus_td[4].string
        bus_name_2 = bus_td[5].string

        result.append([bus_campus_1[0], bus_campus_1[1], departure_time_1, arrival_time_1, bus_name_1]) 
        result.append([bus_campus_2[0], bus_campus_2[1], departure_time_2, arrival_time_2, bus_name_2])   

    bus_tr = tag_tbody.find("tr")
    departure_time_3 = bus_tr.find_all("td")[6].string
    arrival_time_3 = bus_tr.find_all("td")[7].string
    bus_name_3 = bus_tr.find_all("td")[8].string
    result.append([bus_campus_3[0], bus_campus_3[1], departure_time_3, arrival_time_3, bus_name_3])

    bus_tr = tag_tbody.find_all("tr")[2]
    departure_time_4 = bus_tr.find_all("td")[6].string
    arrival_time_4 = bus_tr.find_all("td")[7].string
    result.append([bus_campus_3[1], bus_campus_3[0], departure_time_4, arrival_time_4, bus_name_3])
    
    return



def main():
    result = []
    print("KNUT Bus Table Crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    knut_bus_table(result)
    knut_tbl = pd.DataFrame(result, columns = ("departure", "destination", "departure_time", "arrival_time", "bus_name"))
    knut_tbl.to_csv("./data/knut_bus.csv", encoding = "utf-8", mode = "w", index = True)
    del result[:]

if __name__ == "__main__":
    main()
