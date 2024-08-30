import requests
from bs4 import BeautifulSoup





r = requests.get('https://www.linkedin.com/jobs/search/?currentJobId=3996184002&distance=25.0&geoId=116052516&keywords=software%20engineer&origin=HISTORY')
soup = BeautifulSoup(r.text, 'lxml')
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())


div = soup.find_all('a', class_='job-card-list__title')
# job-card-list__title

print(r.status_code)
print(len(div))