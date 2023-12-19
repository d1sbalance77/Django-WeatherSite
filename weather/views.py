from django.shortcuts import render,redirect
import requests
from .models import City
from .forms import CityForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
import weather.views
from django.contrib.auth import logout


def index(request):
    appid = '860c8927ab21ce4e124b83df6ab1f9f4'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:

        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = dict(all_info=all_cities, form=form)

    return render(request, 'weather/index.html', context)

class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_field_name = True

    def get_success_url(self):
        return reverse_lazy('WeatherMainPage')

def logout_view(request):
    logout(request)
    return redirect('WeatherMainPage')
