import os

from django.http import FileResponse

from entertainment.audio import text_to_temporary_file

# lets try this: https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/


def speak_to_me(request):
    try:
        tmp = text_to_temporary_file("Today is X")
        with open(tmp.name, 'w') as _:
            response = FileResponse(open(tmp.name, 'rb'), content_type="audio/aiff")
            return response
    finally:
        os.remove(tmp.name)
