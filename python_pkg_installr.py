import requests
from bs4 import BeautifulSoup
pkg_dict = {}
target = 'https://pypi.org/search/?q='
# target = 'https://pypi.org/search/?q=bs4'
query_entry = str(input('[?] Search for python3 packages :- '))
target = target+f'{query_entry}'
response = requests.get(target)
soup = BeautifulSoup(response.text,'lxml')
search_result = soup.find(class_='unstyled')
# search_result = soup.find_all(re.compile('^li'))
print('[No.]\tProject_Name  \t\t\t\t   Installation  \t\t\t\t  Package_Description')
print(' --- \t------------  \t\t\t\t   ------------  \t\t\t\t  ------------------- ')
#lis = search_result.findAll('ul',(re.compile('^li')))
try:
    lis = search_result.findAll('li')
    i=1
    for li in lis:
        pkg_name = li.find(class_='package-snippet__name').text
        pkg_version = li.find(class_='package-snippet__version').text
        pkg_released = li.find(class_='package-snippet__released').text.strip()
        pkg_description = li.find(class_='package-snippet__description').text.strip()
        pkg_doc_link = li.find('a')
        pkg_doc_link = pkg_doc_link['href']
        pkg_doc_link = 'https://pypi.org'+pkg_doc_link 
        pkg_dict[i] = pkg_name,pkg_version,pkg_released,pkg_description,pkg_doc_link
        i = i+1
    dict_index = 1
    for pkg in pkg_dict:
        print ("{:<5} {:<40} {:<50} {:<50}".format(f'[{pkg}]',f"{pkg_dict[pkg][0]} {pkg_dict[pkg][1]}", f'pip install {pkg_dict[pkg][0]}', pkg_dict[pkg][3]))
except AttributeError:
    print('[X] Sorry, No result Found')