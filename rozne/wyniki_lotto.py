from bs4 import BeautifulSoup
import requests
import datetime

date = datetime.date.today()
data = str(date)
data = data[8:10]
print(data)


url = 'https://www.lotto.pl/lotto/wyniki-i-wygrane'

page = requests.get(url)
text = page.text
#print(text)
bs = BeautifulSoup(page.content, 'html.parser')

#print(bs)

for i in bs.find_all(class_="scoreline-item circle"):
    if
        print(i)
#for number in bs.find_all(class_="result-item__balls-box"):
 #   for footer in bs.find_all(class_="scoreline-item circle"):
  #      print("test", footer)

    #for footer in bs.find_all(class_="scoreline-item circle"):
        #print(len(footer))
        #footer.strip()
        #numbers.append(footer)

        #print(number)



#print(numbers)
#print(len(numbers[0]))