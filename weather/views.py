from django.shortcuts import render

# lets try this: https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/


def speak_to_me(request):
    return render(request, "base.html")
