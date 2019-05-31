from django.shortcuts import render, HttpResponse
from .models import customer


def index(request):
    f = customer.objects.all().filter(present=True)
    context = {"f":f}
    return render(request, "index.html", context)


def checkin(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        bed = request.POST.get("bed")
        phone = request.POST.get("phone")
        #date = request.POST.get("date")
        #time = request.POST.get("time")
        c = customer(name=name, address=address, bed=bed, phone=phone, present=True)
        c.save()
        return HttpResponse("Customer Created")

    else:
        return render(request, "checkin.html")


def checkout(request):
    if request.method == "POST":
        bed = request.POST.get("bed")
        c = customer.objects.filter(bed=bed, present=True).update(present=False)
        return HttpResponse("Checkout complete")
    
    else:
        return render(request, "checkout.html")
