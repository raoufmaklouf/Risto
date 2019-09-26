from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ReserveForm
import datetime
import dateutil.parser



#chek user input
def userdate(udate):
    user_date = dateutil.parser.parse(udate)
    today= datetime.datetime.today()
    if user_date > today:
        return True
    else:
        return False

def user_guest(guests):
    if guests > 0 and guests <= 20:
        return True
    else:
        return False    

def home(request):
    form=ReserveForm(request.POST)
    if form.is_valid():
        Udata = request.POST.get('date')
        namber_guests= request.POST.get('Guests')
        namber_guests=int(namber_guests)
        if userdate(Udata)==True and user_guest(namber_guests) == True :
            instance=form.save(commit=True or None)
            instance.save()
            messages.success(request,f'We have been  Reserved  ...')
            return redirect('home')
        else:
            
            messages.error(request,'Reservations not done !!!!!!!!! ')
            
            return redirect('home')
    return render(request,'risto/home.html',{'form':form})
