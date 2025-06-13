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
