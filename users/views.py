# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm #default form
# # warning/notification message dekhanor jonno
# from django.contrib import messages
# # jei form gula create korlam .. she gula import korte hobe age
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.decorators import login_required
# from .models import Profile  # updated by Rayhan vai
#
#
# # Create your views here.
# def register(request):
#     #request ta 2 type er GET/POST
#     if  request.method == 'POST':
#         #user_form = UserCreationForm(request.POST) # form er ekta post request ase      # default form
#         user_form = UserRegisterForm(request.POST)  # form er ekta post request ase
#         if user_form.is_valid():
#             user_form.save() # new account ta save korlam
#             username = user_form.cleaned_data.get('username')
#             #jodi form ta valid hoy.. lets go ahead and grab the username that will submitted for now
#             # so the validated form data will be in this form.cleaned data dictionary and this will have been nicely converted
#             # into python.types list from the form
#             # ekhon amra ekta flash message dekhabo .. jeta information thik vabe submit hoise
#             messages.success(request, f'Hi {username} ! Welcome to our family.. Your account has been created ! You are now able to log in.')
#             return redirect('login')
#     else:
#         #user_form = UserCreationForm()
#         user_form = UserRegisterForm()
#     # Now lets render a template that uses this form
#     return render(request, 'users/register.html', {'form':user_form}) # lets pass in our form as the context to the template
#     #so that we can access the form within the template
#
#     # now lets redirect the user to a different page .. karon amra ekta form submit korar pore abar ei form ei fire ashte chai na
#
#
# """
#     different type er message ase
#         messages.debug
#         messages.info
#         messages.success
#         messages.warning
#         messages.error
# """
#
# #  For more details ->> LV-24 ########
# # class based view use korle process ta ektu alada
# @login_required # user must be logged in to view this page
# def profile(request):
#     """
#         lets collect current informaton from these forms of the logged in user.. these are model forms that are expecting to
#         be working on a specific model object, so we can collect data from the form just by passing in an instance of the object
#         that it expects (cz, worng data accept kora jabe na ) .. so, the user update form that will be an instance of a user
#         and the profile update form, that will be an instance of a profile.. so to do this we can just say when we instantiate these forms..
#          { instance =request.user } so that will be the current logged in user and for the profile update form ...
#          { instance=request.user.profile } to get that user's profile
#
#          ei small change gula korlei they created those forms with the current users information.. so the user update form will have the
#          username and email filled in and the profile form will have current image filled in
#     """
#     """
#         ekhon upor er register function er moto .. amra ekta check korte chai.. je eta ki ekta POST route naki na.. ar POST route hoile
#         amra dekhte chai information jegula input deowa hobe shegula valid kina ! valid hoilei shudhu matro amra information gula
#         save korbo ...
#
#             request.method ta POST hole kichu forms create koro.. eta tokhon e run korbe jokhon amra new data input dia form submit korbo..
#             cz, we want to pass in POST data into our forms so we wanted to keep the instances set like they are now, bcz, it has to know
#             what user and profile that we want to update.. instance er age request.POST parameter pathate hobe..
#         #
#             and finally with the profile from we are also going to be getting some additional data and this is going to be filed data coming in
#             with the request. and that will be whatever image, the user tries to upload. So, right after the request.POST data, will also add request.FILES in parameter also
#
#         #
#         data jehetu input neowa hoye gese .. ekhon amra check korbo shegula valid kina.. data valid na hole.. amra kono data e save korbo na
#
#     """
#     #lets create instance of those forms
#     if request.method == 'POST':
#         user_update_form = UserUpdateForm(request.POST, instance=request.user) # instansiate that as empty for now .. 2nd update e amra intance add kortesi..
#         profile_update_form = ProfileUpdateForm(request.POST, instance=request.user.profile) # data input nilam
#             # ebar ei duita form er instance ke template e pathaite hobe
#             # we can create a context.. which is a dictionary
#
#         ## print(request.POST)
#         if user_update_form.is_valid() and profile_update_form.is_valid():
#             user_update_form.save()  # valid holei save korbo
#                              #   print("user just updated!", profile_update_form.cleaned_data, request.POST.get("image"))
#             if 'image' in request.FILES:
#                 ex = Profile.objects.get(user=request.user).delete()
#                 puf = ProfileUpdateForm(request.POST, request.FILES)
#                 puf = profile_update_form.save(commit=False)
#                 puf.user = request.user
#                 puf.save()
#             else:
#                 print("File is Empty , So no apply")
#             ## profile_update_form.save()
#             messages.success(request,
#                              f'Hello !.. Your information has been updated ! Thanks for being with us :D .')
#             # and then we will also redirect them back to the profile page ..
#             # kahini hocce apnr image post hocce na. baki sob asteece front end theke but image asce nah
#             return redirect('profile')
#             # you want to do a redirect here instead of letting it fall down here to our render template function call..
#             # and the reason is bcz of something called the post get redirect pattern.. So, you have ever reloaded your browser after submitting a form and then
#             # a weird message comes up ! says, are you sure that you want to reload ? bcz, the data will be resubmitted or something like that..
#             # that is bcz your browser is basically telling you that your about to run another POST request, when you reload your page.. so, us.. we redirecting
#             # here causes the browser to send a get request and then we dont get that wierd message.. if we try to reload
#         else:
#             messages.success(request,
#                              f'Sorry ! Thanks for being with us :D .')
#             return redirect('profile')
#     else:
#         user_update_form = UserUpdateForm(instance=request.user)  # instansiate that as empty for now .. 2nd update e amra intance add kortesi..
#         profile_update_form = ProfileUpdateForm(instance=request.user.profile)
#
#
#
#
#     context ={
#         'user_update_form__':user_update_form,
#         'profile_update_form':profile_update_form,
#     }
#     return render(request, 'users/profile.html', context) # context take template e pathay dilam..
#     # jate amra ei form gula ke template theke access korte pari

#######################################################################
################################################################
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # default form
# warning/notification message dekhanor jonno
from django.contrib import messages
# jei form gula create korlam .. she gula import korte hobe age
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Added This Line
from .models import Profile


# Create your views here.
def register(request):
    # request ta 2 type er GET/POST
    if request.method == 'POST':
        # user_form = UserCreationForm(request.POST) # form er ekta post request ase      # default form
        user_form = UserRegisterForm(request.POST)  # form er ekta post request ase
        if user_form.is_valid():
            user_form.save()  # new account ta save korlam
            username = user_form.cleaned_data.get('username')
            # jodi form ta valid hoy.. lets go ahead and grab the username that will submitted for now
            # so the validated form data will be in this form.cleaned data dictionary and this will have been nicely converted
            # into python.types list from the form
            # ekhon amra ekta flash message dekhabo .. jeta information thik vabe submit hoise
            messages.success(request,
                             f'Hi {username} ! Welcome to our family.. Your account has been created ! You are now able to log in.')
            return redirect('login') # blog-home .. registration korar pore age home page e nia geleo .. ekhon age log in korte bolbe ../
    else:
        # user_form = UserCreationForm()
        user_form = UserRegisterForm()
    # Now lets render a template that uses this form
    return render(request, 'users/register.html',
                  {'form': user_form})  # lets pass in our form as the context to the template
    # so that we can access the form within the template

    # now lets redirect the user to a different page .. karon amra ekta form submit korar pore abar ei form ei fire ashte chai na


"""
    different type er message ase
        messages.debug
        messages.info
        messages.success
        messages.warning
        messages.error
"""


#  For more details ->> LV-24 ########
# class based view use korle process ta ektu alada
@login_required  # user must be logged in to view this page
def profile(request):
    """
        lets collect current informaton from these forms of the logged in user.. these are model forms that are expecting to
        be working on a specific model object, so we can collect data from the form just by passing in an instance of the object
        that it expects (cz, worng data accept kora jabe na ) .. so, the user update form that will be an instance of a user
        and the profile update form, that will be an instance of a profile.. so to do this we can just say when we instantiate these forms..
         { instance =request.user } so that will be the current logged in user and for the profile update form ...
         { instance=request.user.profile } to get that user's profile

         ei small change gula korlei they created those forms with the current users information.. so the user update form will have the
         username and email filled in and the profile form will have current image filled in
    """
    """
        ekhon upor er register function er moto .. amra ekta check korte chai.. je eta ki ekta POST route naki na.. ar POST route hoile
        amra dekhte chai information jegula input deowa hobe shegula valid kina ! valid hoilei shudhu matro amra information gula
        save korbo ...

            request.method ta POST hole kichu forms create koro.. eta tokhon e run korbe jokhon amra new data input dia form submit korbo..
            cz, we want to pass in POST data into our forms so we wanted to keep the instances set like they are now, bcz, it has to know
            what user and profile that we want to update.. instance er age request.POST parameter pathate hobe..
        #
            and finally with the profile from we are also going to be getting some additional data and this is going to be filed data coming in
            with the request. and that will be whatever image, the user tries to upload. So, right after the request.POST data, will also add request.FILES in parameter also

        #
        data jehetu input neowa hoye gese .. ekhon amra check korbo shegula valid kina.. data valid na hole.. amra kono data e save korbo na

    """
    # lets create instance of those forms
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST,
                                          instance=request.user)  # instansiate that as empty for now .. 2nd update e amra intance add kortesi..
        profile_update_form = ProfileUpdateForm(request.POST, instance=request.user.profile)  # data input nilam
        # ebar ei duita form er instance ke template e pathaite hobe
        # we can create a context.. which is a dictionary

        # Change from Here
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()  # valid holei save korbo
            if 'image' in request.FILES:
                ex = Profile.objects.get(user=request.user).delete()
                puf = ProfileUpdateForm(request.POST, request.FILES)
                puf = puf.save(commit=False)
                puf.user = request.user
                puf.save()
            else:
                print("File is Empty , So no apply")
            # Change Ended
            messages.success(request,
                             f'Hello !.. Your information has been updated ! Thanks for being with us :D .')
            # and then we will also redirect them back to the profile page ..
            # kahini hocce apnr image post hocce na. baki sob asteece front end theke but image asce nah
            return redirect('profile')
            # you want to do a redirect here instead of letting it fall down here to our render template function call..
            # and the reason is bcz of something called the post get redirect pattern.. So, you have ever reloaded your browser after submitting a form and then
            # a weird message comes up ! says, are you sure that you want to reload ? bcz, the data will be resubmitted or something like that..
            # that is bcz your browser is basically telling you that your about to run another POST request, when you reload your page.. so, us.. we redirecting
            # here causes the browser to send a get request and then we dont get that wierd message.. if we try to reload
        else:
            messages.success(request,
                             f'Sorry ! Thanks for being with us :D .')
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(
            instance=request.user)  # instansiate that as empty for now .. 2nd update e amra intance add kortesi..
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form__': user_update_form,
        'profile_update_form': profile_update_form,
    }
    return render(request, 'users/profile.html', context)  # context take template e pathay dilam..
    # jate amra ei form gula ke template theke access korte pari





