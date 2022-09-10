#  https://docs.python-guide.org/
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

BASE_URL = "http://robocontest.uz/"
USERS_URL = "http://robocontest.uz/users"
PROBLEMS_URL = "http://robocontest.uz/tasks"
OLYMPIADS_URL = "https://robocontest.uz/olympiads"
QUIZ_URl = "https://robocontest.uz/quizzes"
NEWS_URL = "https://robocontest.uz/news"
SYSTEM_URL = "https://robocontest.uz/system"
TEAM_URL = "https://robocontest.uz/team"
ONLINE_USERS_URL = "https://robocontest.uz/users?"
SUBMIT_PROBLEM_URL = "https://robocontest.uz/tasks/0001"

class Problems():
    def __init__(self):
        self.id = int
        self.title = str()
        self.difficulty = str()
        self.toifasi = str()
        self.iwlanganlar_soni = int()
        self.acceptedlar_soni = int()
        self.total_soni = int()
        self.parcentage_soni = int()

class Users():
    def __init__(self):
        self.name = str()
        self.adres = str()
        self.orni  = str()

class Olympiads():
    def __init__(self):
        self.name = str()
        self.masalaalr_soni = int()
        self.qatnashuvchilar_soni = int()
        self.boshlanish_vaqti = str()
        self.holati = str()

class Quiz():
    def __init__(self):
        self.name = str()
        self.masalalar_soni = int()
        self.qatnawuvchilar_soni = int()
        self.bowlaniw_vaqti = str()
        self.holati = str()

class System():
    def __init__(self):
        self.id = int()
        self.holati = str()
        self.hodisa = str()
        self.sabab = str()
        self.dasturlash_tillari = str()

class Online_users():
    def __init__(self):
        self.name = str()

class Team():
    def __init__(self):
        self.name = str()
        self.job = str()
        self.place_of_study = str()
        self.course = str()

def post_html(url,data=None):
    response = requests.post(url,data=data)
    if response.ok:
        return response.status_code


def submit_problem():
    data = {"_token":"GcUALbFd97gxo5gTvrm2RUeNeJMF0eXDZYnTgDqO","language_id":2,"code":'''A,B=map(int,input().split())
    print(A+B)'''}
    html = post_html(SUBMIT_PROBLEM_URL,data=data)
    return html

def Team_members():
    #Team_members_1 = Team_members()
    html = get_html(TEAM_URL)
    soup = BeautifulSoup(html,'lxml')
    members = soup.find('div',class_="form-row").find_all('div',class_="col-12 col-md-6 mb-5")
    for member in members:
        nimadir = member.find('div',class_= "profileinfo")
        print(nimadir.find('h1').text.strip(),'  ',nimadir.find('h3').text.strip())
        print()

def Online_users_name():
    #online_users_name_1 = Online_users()
    html = get_html(ONLINE_USERS_URL)
    soup = BeautifulSoup(html,'lxml')
    online_users = soup.find_all('span',class_="badge badge-success")
    for user in online_users:
        print(user.text.strip())


def Authorization(username,password):
    driver = webdriver.Chrome(executable_path=r"D:\CPython\project_parse\chromedriver.exe")
    driver.get('https://robocontest.uz/login')
    driver.find_element_by_id("email").send_keys(f"{username}")
    driver.find_element_by_id('password').send_keys(f'{password}')
    driver.find_element_by_xpath('//button[@type="submit"]').submit()
    driver.get("https://robocontest.uz/tasks/0001")


def get_html(url,params=None):
    responce = requests.get(url,params=params)
    if responce.ok:
        return responce.text

def page_count_problems():
    html = get_html(PROBLEMS_URL)
    soup = BeautifulSoup(html,'lxml')
    page_count = soup.find('ul',class_="pagination").find_all('li')[-2].text.strip()
    return page_count

def parser_problems_title():
    problem = Problems()
    page_count = 5 # page_count_problems()
    for page in range(1,int(page_count)):
        params = {"page":page}
        html = get_html(PROBLEMS_URL,params=params)
        soup = BeautifulSoup(html,'lxml')
        table = soup.find('table',class_="table table-hover m-0 table-borderless table-striped text-left slim-table").find_all('tr')
        table.pop(0)
        for i in table:
            for index,td_tag in enumerate(i.find_all('td')):
                if index == 0:
                     problem.id = td_tag.text.strip()
                elif index ==1:
                    problem.title =  td_tag.text.strip()
                elif index == 2:
                    problem.difficulty = td_tag.text.strip()
                elif index == 3:
                    problem.toifasi = td_tag.text.strip()
                elif index == 4:
                    problem.iwlanganlar_soni = td_tag.text.strip()
                elif index == 5:
                    problem.acceptedlar_soni = td_tag.text.strip()
                elif index == 6:
                    problem.total_soni = td_tag.text.strip()
                elif index == 7 :
                    problem.parcentage_soni = td_tag.text.strip()
            print(problem.id,problem.title,problem.difficulty,problem.toifasi,
            problem.iwlanganlar_soni,problem.acceptedlar_soni,problem.total_soni,problem.parcentage_soni)
    
def page_count_users():
    html = get_html(USERS_URL)
    soup = BeautifulSoup(html,'lxml')
    page_count = soup.find('div',class_="mx-auto").find_all('li')[-2].text.strip()
    return int(page_count)

def parser_users():
    users = Users()
    page_count = page_count_users
    for page in range(1,5):
        params = {'page':page}
        html = get_html(USERS_URL,params=params)
        soup = BeautifulSoup(html,'lxml')
        table = soup.find('table',class_="table table-hover m-0 table-borderless table-striped text-left slim-table").find_all('tr')
        table.pop(0)
        for i in table:
            for index, td_tag in enumerate(i.find_all('td')):
                if index == 1:
                    users.name = td_tag.find('a').text.strip()
                elif index == 2 :
                    users.adres =td_tag.text.strip()
                elif index == 3:
                    users.orni = td_tag.text.strip()

            print(users.orni,users.name,users.adres)

def page_count_olympiads():
    html = get_html(OLYMPIADS_URL)
    soup =BeautifulSoup(html,'lxml')
    page_count = soup.find('div',class_="mx-auto").find('ul',class_="pagination").find_all('li')[-2].text.strip()
    return int(page_count)

def parser_olympiads():
    olympiads = Olympiads()
    page_count = page_count_olympiads()
    for page in range(1,page_count):
        params = {'page':page}
        html = get_html(OLYMPIADS_URL,params=params)
        soup = BeautifulSoup(html,'lxml')
        table = soup.find('table',class_="table table-hover table-borderless m-0 table-striped text-left slim-table").find_all('tr')
        for i in table:
            for index,td_tag in enumerate(i.find_all('td')):
                if index == 0:
                    olympiads.name = td_tag.text.strip()
                elif index == 1 :
                    olympiads.masalaalr_soni = td_tag.text.strip()
                elif index == 2:
                    olympiads.qatnashuvchilar_soni = td_tag.text.strip()
                elif index == 3:
                    olympiads.boshlanish_vaqti = td_tag.text.strip()
                elif index == 4:
                    olympiads.holati = td_tag.text.strip()
            print(olympiads.name,olympiads.masalaalr_soni,olympiads.qatnashuvchilar_soni
            ,olympiads.boshlanish_vaqti,olympiads.holati)              

def parser_testlar():
    quiz = Quiz()
    html = get_html(QUIZ_URl)
    soup = BeautifulSoup(html,'lxml')
    table = soup.find('table',class_="table m-0 table-hover table-borderless table-striped text-left").find_all('tr')
    table.pop(0)
    for i in table:
        for index,td_tag in enumerate(i.find_all('td')):
            if index ==0:
                quiz.name = td_tag.text.strip()
            elif index == 1:
                quiz.masalalar_soni = td_tag.text.strip()
            elif index == 2:
                quiz.qatnawuvchilar_soni = td_tag.text.strip()
            elif index == 3:
                quiz.bowlaniw_vaqti = td_tag.text.strip()
            elif index == 4:
                quiz.holati = td_tag.text.strip()

        print(quiz.name,quiz.masalalar_soni,quiz.qatnawuvchilar_soni,
        quiz.bowlaniw_vaqti,quiz.holati)

def parser_system():
    system = System()
    html = get_html(SYSTEM_URL)
    soup = BeautifulSoup(html,'lxml')
    ul_tag = soup.find('ul',attrs={"class":"nav nav-pills mb-3","id":"langs-tab","role":"tablist"}).find_all('li')
    for li_tag in ul_tag:
        system.dasturlash_tillari = li_tag.text.strip()
        print(system.dasturlash_tillari)
    table = soup.find('table',class_="table m-0 table-hover table-borderless table-striped text-left").find_all('tr')
    table.pop(0)
    for i in table:
        for index,td_tag in enumerate(i.find_all('td')):
            if index == 0:
                system.id = td_tag.text.strip()
            elif index == 1:
                system.holati = td_tag.text.strip()
            elif index == 2:
                system.hodisa = td_tag.text.strip()
            elif index == 3:
                system.sabab = td_tag.text.strip()
        print(system.id,system.holati,system.hodisa,system.sabab)
        
def parser_team():
    html = get_html(NEWS_URL)
    soup = BeautifulSoup(html,'lxml')

def main():
    #print(page_count_problems())
    #print(page_count_users())
    #parser_users()
    # print(page_count_olympiads())
    #parser_olympiads()
    # parser_testlar()
    #parser_system()
    #Authorization('Zohidbek_Ollayorov','Zohid_1340')
    # Online_users_name()
    #pass
    #Team_members()
    #parser_problems_title()
    # print(322)
    pass

if __name__ == "__main__":
    main()
