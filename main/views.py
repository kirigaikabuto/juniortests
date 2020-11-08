from django.shortcuts import render
from .models import *
import random


def index(request):
    if request.method == "POST":
        fromCity = int(request.POST["from"])
        toCities = request.POST.getlist("to")
        toCities = [int(i) for i in toCities]
        toCities = [City.objects.get(pk=i) for i in toCities]
        fromCity = City.objects.get(pk=fromCity)
        directories = [fromCity]
        temp = fromCity
        for i in toCities:
            print(i)
        while True:
            if len(toCities) == 0:
                break
            distances = Distance.objects.filter(fromCity=temp, toCity__in=toCities).order_by("distance")
            temp = distances[0].toCity
            toCities.remove(temp)
            directories.append(distances[0])
        last = Distance.objects.get(fromCity=directories[len(directories)-1].toCity, toCity=fromCity)
        directories.append(last)
        print("after while")
        for i in directories:
            print(i)

    cities = City.objects.all()
    context = {
        "cities": cities,
    }
    # test_data()
    return render(request, "main/index.html", context=context)


def test_data():
    cities = City.objects.all()
    for fromCity in cities:
        for toCity in cities:
            if fromCity != toCity:
                test = Distance(fromCity=fromCity, toCity=toCity, distance=random.randint(100, 1000))
                test.save()
