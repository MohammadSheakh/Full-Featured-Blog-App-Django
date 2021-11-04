from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User # eta amra ageo import korsi ..  jehetu amra User model nia kaj korbo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # LogOut obosthay keo post create korte chaile take login page e nia jabe age ..
                                        # PostCreateView class e add korlam
                                        # UserPassesTestMixin -> Nijer post chara onno kono post edit kora jabe na ! Update view e add korte hobe
from django.views.generic import (
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )

# Some dummy data
    # list of dictionaries
posts = [
    {
        'author':'Mohammad',
        'title' : 'Blog Post 1',
        'content':'First post content',
        'date_posted':'Augest 27, 2018',
    },
    {
        'author':'Sheakh',
        'title' : 'Blog Post 2',
        'content':'Second post content',
        'date_posted':'Augest 28, 2018',
    }
        # Instead of using this dummy data, let's run a query on our Post model
        # And sheta amra context e pass korbo.. First amader ke Post model ta import korte hobe
]

# Create your views here.
def home(request):
        #return HttpResponse('')
        # context is a dictionary
    context = {
        #'postsKey': posts # we assign list of posts
        'postsKey': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) # ekhon amra template theke context er maddhome data ke access korte parbo


class PostListView(ListView): # ListView theke inherit korlam
    # ListView er moddhe model nam e ekta variable create korte hobe, and eta amader listView ke bolbe .. kon model ta create korte hobe
    #-> in order to create the list
    model = Post # listview create korte hole .. ei kaj ta amader korte hobe

    template_name = 'blog/home.html' # -> <app> / <model>_<viewtype>.html

    context_object_name = 'postsKey'
    # ordering = ['date_posted'] # oldest to newest
    ordering = ['-date_posted']  # newest to oldest
    paginate_by = 4


class UserPostListView(ListView): # ListView theke inherit korlam
    # ListView er moddhe model nam e ekta variable create korte hobe, and eta amader listView ke bolbe .. kon model ta create korte hobe
    #-> in order to create the list
    model = Post # listview create korte hole .. ei kaj ta amader korte hobe

    template_name = 'blog/user_posts.html' # -> <app> / <model>_<viewtype>.html

    context_object_name = 'postsKey'
    # ordering = ['date_posted'] # oldest to newest
    #ordering = ['-date_posted']  # newest to oldest
    paginate_by = 4
    """
        we want to add a filter to this that only gets the posts from a certain user.. and that is going to come directly from the URL
        so, when we create a new URL pattern for this.. we will specify the username and the URL path itself.  So, we will set that 
        whenever we create URL pattern here in a second .. but for now.. lets just assume that we have a username variable passed into the URL >>
        in order to modify the query set that this list view returns.. we can override a method called get_query_set and change the query set
        from within there.. so lets do that
    """

    def get_queryset(self):  # queryset should be one word
            # now we want to get the user associated with the username that we are going to get from the URl ..
            # So at this point if that user does not exist then we will want to return a 404 telling the user that .. that page does not exist
            # and its better that returning an empty page .. and for do that .. we can use a shortcut called get object or 404
            # and as the name implies there it will get an object from the database if that object exists and if it does not exist then it will
            # just return a 404.. so first we need to import that and that is from django shortcuts
        user = get_object_or_404(User, username=self.kwargs.get('username')) # User model theke amra object ta chai
             # we want to get the username from the URL and to do that we can say self.kwargs >> kwargs are going to be the query parameter
             # we can get the username from url .. if that user exists ! then we will catch them in a user variable.. if that dont exist then
             # thats gonna return a 404 .. So, now we can limit our result for this list view by finishing our post create
        return Post.objects.filter(author=user).order_by('-date_posted')
             # so returning that filter post query and our get_query set method is what will limit our posts on that page to that specific user
             # that has their user name as the parameter and the URL .. Now lets create that path in our URL patterns that contains username
            # parameter




class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView): # this is going to be a view with a form.. where we create a new post ..
    # so the only other thing we need to provide are the field that we want to be in that form
                                                 # LogOut obosthay keo post create korte chaile take login page e nia jabe age ..
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # form.instance means .. jei form ta amra submit korte chacchi .. submit korar age .. shetar instance niye ..author ke send koro .. is ie  equal to currnt logged in user
                                            # ekhon amra form ta validate korte parbo ..  so.. now we will return .
        return super().form_valid(form)  # parent class e form_valid method ta run kortese .. amra method ta override korlam .. karon.. jeno author ta check kore ney .. run korar age ..
        # ekhon amader ke home page e redirect kore dite hobe .. jeno .. home page e gia onno post e shathe ei matro create houwa post tao dekhte paowa jay

        """
            the way to tell django.. how to find the url of the model object .. is to create getAbsoluteUrl method .. in our model .. that returns 
            the path in any specific instance ...   
            lets go to Blog Model ..
        """


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # UserPassesTestMixin -> Nijer post chara onno kono post edit kora jabe na !
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # form save method
        form.instance.author = self.request.user

        return super().form_valid(form)


    def test_func(self): # ei function user ke onno manush der post update kora theke bachabe ..
        post = self.get_object() # that will get the post that we are currently tring to update ...
        # ekhon amra check korbo je .. current user post er author kina ..
        if self.request.user == post.author: # Current logged in user ==  author of this post
            # then allow them to update that post
            return True

        return False # otherwise return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # user ke logged in hote hobe .. and user ke post er author hote hobe .. then she Post delete korte parbe
    model = Post
    success_url = '/' #  post delete hoye gele home page e move korbe

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


def about(request):
    #return HttpResponse('')
    return render(request, 'blog/about.html', {'title':'About'}) # ,
