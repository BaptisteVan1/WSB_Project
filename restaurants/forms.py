from django import forms
from .models import UserReview, Restaurant


# Form for user reviews per restaurant
class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        #  restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.filter(pk=id))
        fields = [
            'restaurant',
            'user_review_grade',
            'user_review_comment'
        ]
        widgets = {
            'restaurant': forms.HiddenInput,
            'user_review_grade': forms.RadioSelect,
            'user_review_comment': forms.Textarea
        }
        labels = {
            'user_review_grade': 'Chose a satisfaction level:',
            'user_review_comment': 'And write your comments:'
        }

# Form for editing user reviews per restaurant
class EditReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = [
            'restaurant',
            'user_review_grade',
            'user_review_comment'
        ]
        widgets = {
            'restaurant': forms.HiddenInput,
            'user_review_grade': forms.RadioSelect,
            'user_review_comment': forms.Textarea
        }
        labels = {
            'user_review_grade': 'Chose a satisfaction level:',
            'user_review_comment': 'And write your comments:'
        }




# for for creating a new restaurant
class NewRestaurant(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields =[
            'restaurant_name',
            'restaurant_address',
            'restaurant_street_number',
            'restaurant_city',
            'restaurant_cuisine_type',
            'restaurant_category',
            'restaurant_website_link',
        ]

        widgets = {
            'restaurant_name': forms.TextInput(attrs={'placeholder': 'Your restaurant\'s name'}),
            'restaurant_address': forms.TextInput(attrs={'placeholder': 'ex: Main Street'}),
            'restaurant_street_number': forms.TextInput(attrs={'placeholder': 'ex: 123'}),
            'restaurant_city': forms.TextInput(attrs={'placeholder': 'ex: San Francisco'}),
            'restaurant_cuisine_type': forms.Select,
            'restaurant_category': forms.Select,
            'restaurant_website_link': forms.TextInput(attrs={'placeholder': 'ex: www.MyRestaurant.com'}),
        }

        labels = {
            'restaurant_name': 'Restaurant name:',
            'restaurant_address': 'Address:',
            'restaurant_street_number': 'Street number:',
            'restaurant_city': 'City:',
            'restaurant_cuisine_type': 'Cuisine type:',
            'restaurant_category': 'Category',
            'restaurant_website_link': 'Website',
        }
