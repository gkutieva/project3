from django.shortcuts import render


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def teachers_index(request):
  return render(request, 'teachers/index.html', { 'teachers': teachers })