import requests 
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"

def scrapper(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text)
    rows = soup.find('tbody').findAll('tr')[2:236]
    new_table = [["Country", "Cases", "Deaths", "Recoveries", "Death Rate", "Recovery Rate"]]
    for row in rows:
        row_header = row.findAll('th')[1]
        row_cells = row.findAll('td')[:-1]
        our_rows = []
        our_rows.append(row_header.text.strip().split('[')[0])
        for row_cell in row_cells:
            row_text = row_cell.text.strip()
            #finxing the data- NO COMMAS, NO PERIODS, ALL NUMBERS MUST BE INTEGERS
            if row_text == "No data":
                row_text = None
            else:
                row_text = int(''.join(row_text.split(',')))                
            our_rows.append(row_text)
        death_rate = str(round(our_rows[2] / our_rows[1] * 100,  2)) + "%" if our_rows[1] and our_rows[2] else None
        recovery_rate = str(round(our_rows[3] / our_rows[1] * 100,  2)) + "%" if our_rows[1] and our_rows[3] else None
        
        our_rows.append(death_rate)
        our_rows.append(recovery_rate)
        new_table.append(our_rows)
    return new_table

if __name__ == "__main__":
    app.run(debud=True)