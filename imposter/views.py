from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response, Http404
from forms import OrderForm
from google.appengine.api import mail
#from django.core.files.images import ImageFile

def home(request):
  return HttpResponse("you have reached!")

def order(request):
  if request.method == "POST":
    order_form = OrderForm(request.POST, request.FILES)
    if order_form.is_valid():
      body = "Details of the order:"
      body = body + "\nName: " + order_form.cleaned_data['name']
      body = body + "\nCollege: " + order_form.cleaned_data['college']
      body = body + "\nContact No: " + str(order_form.cleaned_data['mobile_no'])
      body = body + "\nE-Mail: " + order_form.cleaned_data['email']
      #body = body + "\nArchive order present: " + order_form.cleaned_data['archive']
      body = body + "\nProduct ID: " + order_form.cleaned_data['pid']
      #body = body + "\nOwn choice present: " + order_form.cleaned_data['choice']
      body = body + "\n End of Order details."
      attachments = []
      if order_form.cleaned_data['choice'] == True:
        f = order_form.cleaned_data.get('f')
        #image = ImageFile(f)
        attachments.append((str(f.name),f.read()))
      mail.send_mail(sender="Order Daemon <i-mposter@appspot.gserviceaccount.com>",
                     to="Imposter <imposterincorporation@gmail.com>",
                     subject="New Order placed",
                     body=body,attachments=attachments)
      return render_to_response("success.html", locals(), context_instance=RequestContext(request))    
  else:
    order_form = OrderForm()
  return render_to_response("order.html", locals(), context_instance=RequestContext(request))
