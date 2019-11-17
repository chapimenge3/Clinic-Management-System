from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Patient,PatientQueue,MedicalHistory
import traceback
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from .forms import RegisterPatient
from django.contrib import messages

from authe.models import User

@login_required
def patientreg(request):
   return render(request , 'medical/patientreg.html') 
@login_required
def patientregister(request):
   if request.method == "POST":
      patient = RegisterPatient(request.POST, request.FILES)
      if patient.is_valid():
         patient.register_date = now().date()
         post = patient.save()
         token = post.id
         patients = Patient.objects.get(id=token)
         return render(request, "medical/doctors.html", context = { 'patients': patients })
      else:
         return redirect("medical:doctors")
   else:
      return redirect("medical:patientregister")
@login_required
def searchpatient(request):
   return render(request , 'medical/search_patient.html')
@login_required
def searchresult(request):
   s = request.GET.get('search') or " none "
   p = "Your search result is this from " + s + ",skudbfg<SJkb"
   return HttpResponse(p)
@login_required
def doctors(request):
   return render(request,'medical/doctors.html')
@login_required
def doctor_p(request,pk):
   p = Patient.objects.get(id=pk)
   return render(request,'medical/doctors.html',context={"patients" : p })
@login_required
def doctor(request,pk,pid):
   try:
      doc = User.objects.get(id=pk)
      name = doc.first_name
      p = Patient.objects.get(id=pid)
      appoint = PatientQueue()
      appoint.patient = p
      appoint.doctor = doc
      appoint.is_appointment = False
      appoint.save()
      ap = PatientQueue.objects.filter(doctor=doc)
      return render(request,"medical/success.html",{ "success" : True})
   except Exception:
      return render(request,"medical/success.html",{ "success" : False})
   
@login_required
def search_p_result(requst):
   if requst.method == "POST":
      try:
         name = requst.POST.get('search').split()
         first = name[0]
         last = None
         if len(name)>1:
            last = name[1]
         p = Patient.objects.filter(first_name__icontains=first)
         patient = set()
         print("p is p" , p)
         for i in p:
            patient.add(i)
         if last:
            pp = Patient.objects.filter(last_name__icontains=last)
            if len(pp)!=0:
               for i in pp:
                  patient.add(i)
         empty = len(patient)
         return render(requst,'medical/search_p_result.html',context={'patient': patient , "empty" : empty} )
      except EOFError:
         return redirect('medical:search')
@login_required
def propic(request):
   user  = request.user
   # print(user)
   pat = PatientQueue.objects.all()
   p = set()
   l = None
   for i in pat:
      if i.doctor.id == user.id:
         p.add(i.patient)
         l = i.patient
   empty = False
   if len(p) == 0:
      empty = True
   return render (request , 'medical/propic.html' ,context={'user' : user , 'patients' : p , 'empty' : empty }  )
@login_required
def patientrecord(request,pk):
   patient = Patient.objects.get(id=pk)
   have_rec = False

   try:
      records = MedicalHistory.objects.filter(patient=patient)
      have_rec = True
      if len(records) == 0:
         have_rec = False 
      return render(request , 'medical/patientrecord.html', 
      context={
         'patient' : patient ,
         'have_rec' : have_rec ,
         'records' :records,
         'docid' : request.user.id
         } )
   except Exception:

      return render(request , 'medical/patientrecord.html',
      context={
         'patient' : patient,
         'have_rec' : have_rec,
         'docid' : request.user.id
         })
@login_required
def patientrecordadd(request,pk,dk):
   print(request.method=="POST", "slf,kjds")
   if request.method=="POST":
      try:
         precord = MedicalHistory()
         
         patient = Patient.objects.get(id=pk)
         doctor = User.objects.get(id=dk)
         precord.histroy = request.POST.get("histroy")
         precord.patient = patient
         precord.doctor = doctor
         precord.save()
         pqueue = PatientQueue.objects.filter(patient=patient,doctor=doctor)
         pqueue.delete()
         return redirect('medical:propic')
      except Exception as e:
         traceback.print_exc()
         return redirect('medical:propic')
   else:
      return redirect('authe:homepage')



   