from django.shortcuts import render,redirect
from .forms import MedicineForm
from .models import Medicine
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    med_list=Medicine.objects.all()
    return render(request,'medicine/home.html',{'med_list':med_list})

@login_required(login_url='login')
def med_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =MedicineForm()
    return render(request, 'medicine/create.html', {'form': form})

@login_required(login_url='login')
def med_update(request,id):
    med=Medicine.objects.get(pk=id)
    form=MedicineForm(request.POST,instance=med)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form=MedicineForm(instance=med)
    return render(request,'medicine/update.html',{'form':form})

@login_required(login_url='login')
def med_delete(request,pk):
    med=Medicine.objects.get(pk=pk)  
    if request.method == 'POST':
        med.delete()
        return redirect('home')
    return render(request,'medicine/delete.html',{'med':med})

@login_required(login_url='login')
def med_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        med = Medicine.objects.filter(name__istartswith=query)
        return render(request, 'medicine/search.html', {'med': med})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')


    