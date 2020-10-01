from django.shortcuts import render, HttpResponse
from .forms import CountryForm
from . import services


def homepage(request):
    """ redner form to search """
    form = CountryForm()
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data['name']
            result_set = services.get_by_country(country)
            return render(request, 'app1/homepage.html', {'form': form, 'result_set': result_set})
        return render(request, 'app1/homepage.html', {'form': form})
    return render(request, 'app1/homepage.html', {'form': form})


def countries(request):
    summary_list = services.get_all_countries()
    return render(request, 'app1/all_countries.html', {'summary_list': summary_list})