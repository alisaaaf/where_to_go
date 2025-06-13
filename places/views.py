from django.http import JsonResponse
from django.shortcuts import render
from .models import Place


def index(request):
    places = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in Place.objects.all():
        places["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat],
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": ""
            }
        })

    return render(request, 'mainpage.html', {'geo_json': places})


def get_place_details(request, place_id):
    place = Place.objects.get(id=place_id)

    place_details = {
        "title": place.title,
        "imgs": [

            image.image.url for image in place.images.all()

        ],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }

    }
    return JsonResponse(place_details, json_dumps_params={'ensure_ascii': False, 'indent': 4})
