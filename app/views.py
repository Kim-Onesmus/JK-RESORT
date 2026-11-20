from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import InquiryForm


def home(request):
    return render(request, 'app/home.html')


# def events(request):
#     return render(request, 'app/events.html')


# def contact(request):
#     if request.method == 'POST':
#         form = InquiryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Thanks for getting in touch. Your enquiry has been received.')
#             return redirect('contact')
#     else:
#         inquiry_type = request.GET.get('type', InquiryForm.Meta.model.InquiryType.GENERAL)
#         allowed_types = InquiryForm.Meta.model.InquiryType.values
#         if inquiry_type not in allowed_types:
#             inquiry_type = InquiryForm.Meta.model.InquiryType.GENERAL
#         form = InquiryForm(initial={'inquiry_type': inquiry_type})
#     return render(request, 'app/contact.html', {'form': form})