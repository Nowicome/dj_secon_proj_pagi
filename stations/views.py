from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    land_stations = []
    with open(BUS_STATION_CSV, newline="", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            land_stations.append({
                "Name": row["Name"],
                "Street": row["Street"],
                "District": row["District"]
            })

    paginator = Paginator(land_stations, 10)
    page_number = int(request.GET.get("page", 1))
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }

    return render(request, 'stations/index.html', context)
