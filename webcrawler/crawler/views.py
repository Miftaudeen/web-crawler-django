from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def index(request, link):
    links =[
    'https://www.yellowpages.com/los-angeles-ca/plumbers',
    'https://www.yellowpages.com/los-angeles-ca/locksmiths',
    'https://www.yellowpages.com/los-angeles-ca/dentists',
    'https://www.yellowpages.com/los-angeles-ca/attorneys',
    'https://www.yellowpages.com/los-angeles-ca/doctors',
    'https://www.yellowpages.com/los-angeles-ca/veterinarians',
    'https://www.yellowpages.com/los-angeles-ca/auto%20repairs',
    'https://www.yellowpages.com/los-angeles-ca/auto%20Insurance',
    'https://www.yellowpages.com/los-angeles-ca/restaurants',
                ]
    i = 0
    req = requests.get(links[int(link)])
    soup = BeautifulSoup(req.text, 'html.parser')
    businesses = soup.find_all('div', class_= 'result flash-ad')
    bs ={}

    for business in businesses:
        bs[i]=business
        i= i+1

    return render(request, 'pages.html', {"businesses":bs})