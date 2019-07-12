from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime



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
            manager = request.POST.get("manager")
            date = request.POST.get("date")
            time = request.POST.get("time")
            image = request.POST.get("image")
            c = customer(name=name,
                         address=address,
                         bed=bed,
                         phone=phone,
                         present=True,
                         manager=manager,
                         image=image,
                         checkin_date=datetime.datetime.now(),
                         checkin_time=datetime.datetime.now()
                         )
            c.save()
            return HttpResponse("Customer Created")

        if t == "out":
            context = {}
            bed = request.POST.get("bed")
            c = customer.objects.filter(bed=bed,
                                        present=True)
            context['det'] = customer.objects.filter(bed=bed,
                                                     checkin_date=c[0].checkin_date)
            c = c.update(present=False,
                         checkout_date=datetime.datetime.now(),
                         checkout_time=datetime.datetime.now()
                         )
            if c:
                context['msg'] = "Customer with bed number:"+bed+" checked out"
                return render(request, "bill.html", context)
            else:
                msg = "Customer doesn't exist"
                return render(request, "home.html", {"msg": msg})
    else:
        return render(request, "home.html")

@login_required
def dashboard(request):
    if request.method == "POST":
        start_date = request.POST.get("startdate")
        end_date = request.POST.get("enddate")
        if start_date and end_date:
            cust = customer.objects.all().filter(checkin_date__gte = start_date, checkin_date__lte = end_date)
            count = cust.count()
    
        elif start_date:
            cust = customer.objects.all().filter(checkin_date__gte=start_date)
            count = cust.count()
            context = {"cust": cust, "count":count}

        elif end_date:
            cust = customer.objects.all().filter(checkin_date__lte = end_date)
            count = cust.count()
            context = {"cust": cust, "count":count}
    
        else:
            cust = customer.objects.all().filter(present=True)
            count = cust.count()
            context = {"cust": cust}
        return render(request, "index.html", context)

    else:
        cust = customer.objects.all().filter(present=True)
        count = cust.count()
        context = {"cust": cust, "count":count}
        return render(request, "index.html", context)