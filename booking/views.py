from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import customer
from django.contrib.auth.decorators import login_required
#from django.contrib import messages

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
            if customer.objects.filter(bed=bed, present=True):
                msg = "The bed is already occupied"
            else:
                c = customer(name=name, address=address, bed=bed, phone=phone, present=True)
                c.save()
                msg = "New Customer Checked In at bed:"+bed
        
        if t == "out":
            bed = request.POST.get("bed")
            c = customer.objects.filter(bed=bed, present=True).update(present=False)
            if c:
                msg = "Customer with bed number:"+bed+" checked out"
            else:
                msg = "Customer doesn't exist"
                
        context = {"msg":msg}
        return render(request, "home.html", context)
    else:
        return render(request, "home.html")

@login_required
def search(request):
    