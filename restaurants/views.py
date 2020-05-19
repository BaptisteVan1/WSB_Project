# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import Restaurant, UserReview
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic.list import ListView
from django.db.models import Q, Min, Max, Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import requests




# View showing the restaurant list. This will bo home-ish page
def index(request):
    restaurants_list = Restaurant.objects.order_by('-id')
    template = loader.get_template('restaurants/index.html')
    context = {
        'restaurants_list': restaurants_list
    }
    return HttpResponse(template.render(context, request))


# Detail page for each restaurant with all info such as address, cuisine type, pics, menu, external links and so on
def details(request, restaurant_id):
    # calling restaurant ID and displaying it's data
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    # calling a review and displaying it's data
    user_review_list = UserReview.objects.filter(restaurant__id=restaurant_id)
    user_reviews = []
    print(user_review_list)
    for user_review in user_review_list:
        if user_review.posted_by == request.user:
            user_reviews.append({"user_review_grade": user_review.user_review_grade,
                                 "user_review_comment": user_review.user_review_comment,
                                 "posted_by": user_review.posted_by,
                                 "edit": user_review.get_edit_url,
                                 "id": user_review.id})
        else:
            user_reviews.append({"user_review_grade": user_review.user_review_grade,
                                 "user_review_comment": user_review.user_review_comment,
                                 "posted_by": user_review.posted_by,
                                 "id": user_review.id})

    return render(request, 'restaurants/details.html', {'restaurant': restaurant,
                                                        'user_review_list': user_reviews,})

# View used to create a new restaurant in the DB
class new_restaurant (LoginRequiredMixin, CreateView):
    template_name = 'restaurants/new-restaurant.html'
    form_class = NewRestaurant

    # Post the data into the DB
    def post(self, request):
        form = NewRestaurant(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False) # saves the form
            form.instance.created_by = self.request.user # adds the user logged in
            print(restaurant)  # Print so I can see in cmd prompt that something posts as it should
            restaurant.save() # now actually writes it to the DB
            # this return below need reverse_lazy in order to be loaded once all the urls are loaded
            return HttpResponseRedirect(reverse_lazy('restaurants:index'))
        return render(request, 'restaurants/new-restaurant.html', {'form': form})


# This class posts user reviews in the DB that are later displayed in details
class Reviewing (LoginRequiredMixin, CreateView):
    template_name = 'restaurants/reviewing.html'
    form_class = UserReviewForm

    # Get the initial information needed for the form to function: restaurant field
    def get_initial(self, *args, **kwargs):
        initial = super(Reviewing, self).get_initial(**kwargs)
        initial['restaurant'] = self.kwargs['restaurant_id']
        return initial

    # Post the data into the DB
    def post(self, request, restaurant_id, *args, **kwargs):
        form = UserReviewForm(request.POST)
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        if form.is_valid():
            review = form.save(commit=False)
            form.instance.posted_by = self.request.user
            print(review)  # Print so I can see in cmd prompt that something posts as it should
            review.save()
            # this return below need reverse_lazy in order to be loaded once all the urls are loaded
            return HttpResponseRedirect(reverse_lazy('restaurants:details', args=[restaurant.id]))
        return render(request, 'restaurants/details.html', {'form': form})


class EditReview (LoginRequiredMixin, UpdateView):
    template_name = 'restaurants/review_edit.html'
    form_class = EditReviewForm
    model = UserReview
    slug = 'review'
    # Post the data into the DB
    def post(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(UserReview, pk=pk)
        form = UserReviewForm(request.POST, instance=obj)
        restaurant = obj.restaurant
        if form.is_valid():
            edit_review = form.save(commit=False)
            form.instance.posted_by = self.request.user
            print(edit_review)  # Print so I can see in cmd prompt that something posts as it should
            edit_review.save()
            return HttpResponseRedirect(reverse_lazy('restaurants:details', args=[restaurant.id]))
        return render(request, 'restaurants/details.html', {'form': form})

# This view allows user to use a basic filtering search for restaurants:
class SearchResults(ListView):
    model = Restaurant
    template_name = 'restaurants/search.html'

    def get_queryset(self): # new
        q = self.request.GET.get('q')
        object_list = Restaurant.objects.filter(
            Q(restaurant_name__icontains=q) | Q(restaurant_city__icontains=q) | Q(restaurant_category__icontains=q) |
            Q(restaurant_cuisine_type__icontains=q))
        print(q)
        return object_list


def welcome(request):
    template = loader.get_template('restaurants/welcome.html')
    context={}
    return HttpResponse(template.render(context, request))
