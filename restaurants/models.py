from django.db import models
from django.contrib.auth.models import User


# Table storing the different restaurants
from django.urls import reverse


class Restaurant(models.Model):
    # Defining the possible cuisine types
    Grade_1 = 'Traditional / polish'
    Grade_2 = 'Italian'
    Grade_3 = 'American / burger'
    Grade_4 = 'Indian'
    Grade_5 = 'Thai'
    Grade_6 = 'Chinese'
    Grade_7 = 'Japanese / sushi'
    Grade_8 = 'Other'
    # All those grades will sit under restaurant_cuisine_type to appear in choices during the new restaurant's creation
    Cuisine_Type = (
        ('Traditional / polish', 'Traditional / polish'),
        ('Italian', 'Italian'),
        ('American / burger', 'American / burger'),
        ('Indian', 'Indian'),
        ('Thai', 'Thai'),
        ('Chinese', 'Chinese'),
        ('Japanese / sushi', 'Japanese / sushi'),
        ('Other', 'Other')
    )
    # Defining the possible categories for businesses (restaurant, pub, fast-food)
    Restaurant_category_1 = 'Restaurant'
    Restaurant_category_3 = 'Fast-food'
    Restaurant_category_2 = 'Pub'
    # They will appear under Category field as a drop down in the creation form
    Category_type = (
        ('Restaurant', 'Restaurant'),
        ('Fast-food', 'Fast-food'),
        ('Pub', 'Pub')
    )
    # Now listing all the fields for restaurant registration
    restaurant_name = models.CharField(max_length=200, unique=True)
    restaurant_address = models.CharField(max_length=200)
    restaurant_street_number = models.CharField(max_length=10)
    restaurant_city = models.CharField(max_length=200)
    restaurant_cuisine_type = models.CharField(choices=Cuisine_Type, max_length=50)
    restaurant_category = models.CharField(choices=Category_type, max_length=25)
    restaurant_website_link = models.CharField(max_length=250)
    restaurant_tel = models.CharField(max_length=15, default='Phone number')
    restaurant_email = models.CharField(max_length=200, default='Email address')
    picture = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class UserReview(models.Model):
    # Defining the possible grades
    Grade_1 = 1
    Grade_2 = 2
    Grade_3 = 3
    Grade_4 = 4
    Grade_5 = 5
    # All those grades will sit under Review_Grade to appear in choices
    Review_Grade = (
        (1, '1 - Not satisfied'),
        (2, '2 - Almost satisfied'),
        (3, '3 - Satisfied'),
        (4, '4 - Very satisfied'),
        (5, '5 - Exceptionally satisfied')
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_review_grade = models.IntegerField(default=None, choices=Review_Grade) # default=None pour eviter d'avoir un bouton vide sur ma template
    user_review_comment = models.CharField(max_length=1500)
    posted_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse('restaurants:reviews', args=[self.id])

    def get_edit_url(self):
        return reverse('restaurants:edit-review', args=(self.id,))
