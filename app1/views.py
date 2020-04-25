from django.shortcuts import render
import requests
# Create your views here.


def homepage(request):
    confirmed = "Confirmed"
    death = "Deaths"
    recover = "Recovered"
    country = "azerbaijan"
    response = requests.get(f'https://api.covid19api.com/country/{country}')
    country_data = response.json()
    latest_day = country_data[len(country_data)-1]
    return render(request, 'app1/homepage.html', {
        'confirmed': latest_day[confirmed],
    })
