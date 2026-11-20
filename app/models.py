from django.db import models


class Inquiry(models.Model):
    class InquiryType(models.TextChoices):
        BOOKING = 'booking', 'Booking / accommodation'
        EVENT = 'event', 'Meetings & events'
        GENERAL = 'general', 'General question'

    inquiry_type = models.CharField(max_length=16, choices=InquiryType.choices)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    message = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_inquiry_type_display()} from {self.name}'
