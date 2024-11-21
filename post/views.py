from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .models import Event, RSVP
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .forms import EventForm
from .forms import RSVPForm
from .models import Event


# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
        
    #return HttpResponse('<h1> WELCOME HOME !!! </h1>')
    return render(request, 'post/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def video(request):
    #return HttpResponse('<h1> THIS IS ABOUT PAGE </h1>') 
    return render(request, 'post/video.html')

def marketplace(request):
    #return HttpResponse('<h1> THIS IS MARKET PLACE PAGE </h1>') 
    return render(request, 'post/marketplace.html')

def groups(request):
    #return HttpResponse('<h1> THIS IS MARKET PLACE PAGE </h1>') 
    return render(request, 'post/groups.html')

def gaming(request):
    #return HttpResponse('<h1> THIS IS MARKET PLACE PAGE </h1>') 
    return render(request, 'post/gaming.html')
def home(request):
    # Fetch all posts (you might want to paginate or filter this)
    posts = Post.objects.all().order_by('-date_posted')  # Order by the date posted
    return render(request, 'post/home.html', {'posts': posts})

def logout_view(request):
    logout(request)
    return render(request, 'user/logout.html')
@login_required
def video(request):
    return render(request, 'post/video.html')

@login_required
def marketplace(request):
    return render(request, 'post/marketplace.html')

@login_required
def groups(request):
    return render(request, 'post/groups.html')

@login_required
def gaming(request):
    return render(request, 'post/gaming.html')

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()
    return render(request, 'post/create_event.html', {'form': form})

@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    rsvp, created = RSVP.objects.get_or_create(user=request.user, event=event)

    if request.method == 'POST':
        form = RSVPForm(request.POST, instance=rsvp)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = RSVPForm(instance=rsvp)

    return render(request, 'post/rsvp_event.html', {'form': form, 'event': event})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    rsvp = RSVP.objects.filter(event=event, user=request.user).first()  # Get the RSVP status for the current user
    return render(request, 'post/event_detail.html', {'event': event, 'rsvp': rsvp})

def event_list(request):
    events = Event.objects.all()  # Fetch all events from the database
    return render(request, 'post/event_list.html', {'events': events})