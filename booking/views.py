from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def index(request):
    f = customer.objects.all().filter(present=True)
    context = {"f":f}
    return render(request, "index.html", context)

@login_required
def checkin(request):
    msg = None
    if request.method == "POST":
        t = request.POST.get("type")
        if t == "in":
            name = request.POST.get("name")
            address = request.POST.get("address")
            bed = request.POST.get("bed")
            phone = request.POST.get("phone")
            #date = request.POST.get("date")
            #time = request.POST.get("time")
            c = customer(name=name, address=address, bed=bed, phone=phone, present=True)
            c.save()
            return HttpResponse("Customer Created")
        
        if t == "out":
            bed = request.POST.get("bed")
            print(bed)
            c = customer.objects.filter(bed=bed, present=True).update(present=False)
            if c:
                msg = "Customer with bed number:"+bed+" checked out"
                return render(request, "home.html", {"msg":msg})
            else:
                msg = "Customer doesn't exist"
                return render(request, "home.html", {"msg":msg})
    else:
        return render(request, "home.html")