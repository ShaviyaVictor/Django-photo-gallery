from django.shortcuts import render


memories = [

  {
    'source':'Victor Shaviya',
    'title':'Rugby adventure.',
    'description':'Rugby life has been a wonderful adventure all throughout.',
    'date_posted':'August 20, 2020'
  },
  {
    'source':'Mean Machine',
    'title':'Embu Sevens.',
    'description':'Rugby life has been a wonderful adventure all throughout.',
    'date_posted':'August 20, 2018'
  }

]


# Create your views here.
def home(request) :

  return render(request, 'memoir/home.html')



def gallery(request) :

  context = {
    'memories':memories
  }


  return render(request, 'memoir/gallery.html', context)



def about(request) :

  return render(request, 'memoir/about.html')



def login(request) :

  return render(request, 'memoir/login.html')