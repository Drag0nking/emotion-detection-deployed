import imp
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd
from auth.settings import BASE_DIR
from login.models import UsersMood
from login.yturl import getYTURL
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from thought_feed.views import index

# Create your views here.


def indexView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request,'home.html')

def aboutView(request):
    return render(request,'aboutus.html') 

@login_required(login_url='login_url') 
def thoughtFeed(request):
    return index(request)


@login_required(login_url='login_url')  
def dashboardView(request):

    if request.method == "POST" :
        usrMood=request.POST.get("usrMood","neutral")
        songs=[]
        url=[]
        num=[]
        vid=[]
    
        userMoodFile="data/"+usrMood+".pkl" 
        
        numb=1
        pklFile=str(BASE_DIR / userMoodFile)
        df=pd.read_pickle(pklFile)
        for i in df.sample(5).index:
            songs.append(df["name"][i])
            url.append(df["url"][i])
            yt=getYTURL(df["name"][i]+" "+df['artists_song'][i])
            vid.append(yt)
            print(yt)
            num.append(numb)
            numb+=1
        zipped=zip(songs,url,vid)
        return render(request,'recommendedSongs.html',{"songs":zipped,"num":num})
    
    else:
        return render(request,'dashboard.html') 
 

def registerView(request): 
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == "POST" :
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Succesfully!')
                return redirect('login_url')

        context = {'form' :form}
        return render(request,'register.html',context) 



def loginView(request): 
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST" :
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is Incorrect!')
        
        context ={}

        return render(request,'login.html',context)
        
def logoutView(request): 
    logout(request)
    return redirect('login_url')


global a



# def recSongs(request):
#     songs=[]
#     url=[]
#     num=[]
#     vid=[]
#     usrMood= request.POST.get("usrMood", 'happy')
#     usrMood=usrMood.replace('"',"")

#     print(usrMood+" sdfsdfsdfsdfasdfasdf")
#     userMoodFile="data/"+usrMood+".pkl" 
    
#     numb=1
#     pklFile=str(BASE_DIR / userMoodFile)
#     df=pd.read_pickle(pklFile)
#     for i in df.sample(5).index:
#         songs.append(df["name"][i])
#         url.append(df["url"][i])
#         yt=pywhatkit.playonyt(df["name"][i]+" "+df['artists_song'][i],open_video=False)
#         vid.append(yt)
        
#         num.append(numb)
#         numb+=1
#     zipped=zip(songs,url,vid)
#     print('hello')
#     return render(request,'recommendedSongs.html',{"songs":zipped,"num":num})


