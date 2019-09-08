from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.conf import settings

@login_required
def checkin(request):
    msg = None
    if request.method == "POST":
        now = datetime.now()
        t = request.POST.get("type")
        if t == "in":
            name = request.POST.get("name")
            address = request.POST.get("address")
            bed = request.POST.get("bed")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            time = request.POST.get("time")
            if request.FILES:
                image = request.FILES["image"]
            if customer.objects.filter(bed=bed,present=True):
                msg="Sorry, that bed is already occupied"
            else:
                c = customer(name=name,
                            address=address,
                            bed=bed,
                            phone=phone,
                            present=True,
                            image=image,
                            checkin_date=now.strftime("%Y-%m-%d"),
                            checkin_time=now.strftime("%H:%M:%S")
                            )
                c.save()
                msg = "Customer on bed:"+bed+" checked in!"
            context = {"msg":msg}
            return render(request,"home.html",context)

        if t == "out":
            context = {}
            bed = request.POST.get("bed")
            c = customer.objects.filter(bed=bed,present=True)
            context['checkin'] = str(c[0].checkin_date)+'||'+str(c[0].checkin_time)
            context['name'] = str(c[0].name)
            context['address'] = str(c[0].address)
            context['bed']=bed
            if c:
                manager = request.POST.get("manager")
                payment_type = request.POST.get("payment_type")
                day_price = request.POST.get("day_price")
                duration = request.POST.get("duration")
                total_price = int(day_price)*int(duration)
                
                invoice=now.strftime("%m-%d")+'-'+bed+'-'+now.strftime("%H-%M")
                print(invoice)
                
                checkout_date=now.strftime("%Y-%m-%d")
                checkout_time=now.strftime("%H:%M:%S")
                c.update(present=False, 
                        manager=manager,
                        checkout_date=checkout_date,
                        checkout_time=checkout_time,
                        invoice=invoice,
                        day_price=day_price,
                        payment_type=payment_type,
                        total_price=total_price,
                        duration=duration)


                context['checkout'] = checkout_date+'||'+checkout_time
                context['day_price'] = day_price
                context["payment_type"] = payment_type
                context['total_price'] = str(total_price)
                context['days'] = duration
                context['manager'] = manager
                context["invoice"] = invoice
                
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
        context = None
        if start_date and end_date:
            cust = customer.objects.all().filter(checkin_date__gte = start_date, checkin_date__lte = end_date)
            count = cust.count()
    
        elif start_date:
            cust = customer.objects.all().filter(checkin_date__gte=start_date)
            count = cust.count()

        elif end_date:
            cust = customer.objects.all().filter(checkin_date__lte = end_date)
            count = cust.count()
    
        else:
            cust = customer.objects.all().filter(present=True)
            count = cust.count()
        context = {"cust": cust,"count":count}
        return render(request, "index.html", context)

    else:
        cust = customer.objects.all().filter(present=True)
        count = cust.count()
        context = {"cust": cust, "count":count}
        return render(request, "index.html", context)