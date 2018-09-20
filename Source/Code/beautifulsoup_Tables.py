import requests
from bs4 import BeautifulSoup

def collect_tables():
    url = "https://en.wikipedia.org/wiki/List_of_sovereign_states"
    # creating a new text file to write tables data
    file1 = open("pylab2_py3_txt1", "w+")
    # this command gives the source code of website
    source_code = requests.get(url)

    # we have to convert the source code to text format as we can't iterate through source code
    source_text = source_code.text

    # We convert the normal text into beautiful text to extract the table values
    soup_text = BeautifulSoup(source_text, 'html.parser')

    # from the below command we are getting tables from parsed data
    table = soup_text.find("table",{"class":"sortable wikitable" })

    for rows in table.findAll('td'):
    # writes the text in each row to text file
        file1.write(str(rows.text))


    file1.seek(0,0)
    string1 = file1.read()
    print(string1)
    file1.close()

if __name__ == '__main__':
    collect_tables()