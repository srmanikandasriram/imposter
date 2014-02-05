from django import forms
from django.forms.util import ValidationError

class OrderForm(forms.Form):
  name = forms.CharField(label = "Name*", required = True)
  college = forms.CharField(label = "College*", required = True, help_text = "To make sure I'mposterians are present in your college to deliver the product")
  mobile_no = forms.IntegerField(label = "Contact No*", required = True, help_text = "Don't worry. The information is absolutely secure.")
  email = forms.EmailField(label = "E-Mail*", required = True)
  archive = forms.BooleanField(label = "Do you wish to order a poster from I'mposter Archives?", required = False)
  pid = forms.CharField(label = "Product ID", required = False)
  choice = forms.BooleanField(label = "Do you wish to print a poster of your choice?", required = False)
  f = forms.ImageField(label = "Image", required = False, help_text = "A high resolution image (like a HD Wallpaper etc) is preferred.")
