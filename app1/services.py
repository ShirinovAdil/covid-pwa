import requests


CONFIRMED = "Confirmed"
DEATH = "Deaths"
RECOVERED = "Recovered"



def get_by_country(country):
    """ returns covid statistics based on :country argument """
    try:
        response = requests.get(f'https://api.covid19api.com/country/{country}')
        country_data = response.json()
        latest_day = country_data[len(country_data)-1]
        result_queryset = {
            'confirmed': latest_day[CONFIRMED],
            'deaths': latest_day[DEATH],
            'recovered': latest_day[RECOVERED],
            'country': country
        }
        return result_queryset
    except Exception:
        return "Check if the country name is valid and try later"
