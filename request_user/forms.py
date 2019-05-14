from django import forms
from django.contrib.auth.forms import UserCreationForm
from request_user.models import RequestUser
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RequestUserForm(forms.Form):
    name = forms.CharField()
    mobile_no = forms.CharField()
    email = forms.EmailField()
    address= forms.CharField(widget=forms.Textarea)


class RequestUserFormModel(forms.ModelForm):
    def validate_even(value):
        if value % 2 != 0:
            raise ValidationError(
                ('%(value)s is not an even number'),
                params={'value': value},
            )

    def clean_email(self):
        email = self.cleaned_data['email']
        if "fred@example.com" not in email:
            raise forms.ValidationError("You have forgotten about Fred!")
        return email

    def clean_name(self, *args, **kwargs):
        name= self.cleaned_data.get("name")
        if not "CFE" in name:
            raise forms.ValidationError("This is not a valid name")
        else:
            return name

    def clean_email(self, *args, **kwargs):
        email= self.cleaned_data.get("email")
        if not email.endswith('edu'):
            raise forms.ValidationError("This is not a valid email")
        else:
            return email



    CHOICES = (
        (11, 'Credit Card'),
        (12, 'Student Loans'),
        (13, 'Taxes'),
        (21, 'Books'),
        (22, 'Games'),
        (31, 'Groceries'),
        (32, 'Restaurants'),
    )
    name = forms.CharField(label="Enter Name", widget=forms.TextInput(attrs={"placeholder":"Enter Name","class": "form-control"}))
    email = forms.CharField(label="Email",widget=forms.TextInput(attrs={"placeholder":"Enter Name","class": "form-control"}))
    mobile_no = forms.CharField(max_length=50,required=False,label="Mobile No",widget=forms.TextInput(attrs={"placeholder":"Enter Name","class": "form-control"}))
    address = forms.CharField(label="Mobile No",widget=forms.Textarea(attrs={"placeholder":"Enter Name","class": "form-control","rows":10, "col":20}))
    #description = forms.CharField(widget=forms.Textarea)
    #pin_code = forms.CharField()
    #services_need = forms.CharField(max_length=200)
    booking_date = forms.DateField(label="Booking Data",widget=forms.TextInput(attrs={"placeholder":"Enter Date","class": "form-control"}))
    budget = forms.DecimalField(initial=19.9,label="Budget",widget=forms.TextInput(attrs={"placeholder":"Enter Budegt","class": "form-control"}))
    #total_person = forms.CharField(max_length=100)
    #veg_non_veg = forms.ChoiceField(choices=CHOICES)
    #services_id = forms.ChoiceField(choices=CHOICES)
    #services_cat_id = forms.ChoiceField(choices=CHOICES)
    #country_id = forms.ChoiceField(choices=CHOICES)
    #city_id = forms.ChoiceField(choices=CHOICES)
    #location_id = forms.ChoiceField(choices=CHOICES)
    #status = forms.IntegerField(validators=[validate_even])

    class Meta:
         model = RequestUser
         fields = ('name', 'mobile_no', 'email','address','booking_date','budget')

