from django.test import TestCase

from app.models import Inquiry


class ResortPageTests(TestCase):
    def test_primary_pages_render(self):
        for path, heading in (
            ('/', b'Relax'),
            ('/accommodation/', b'Accommodation'),
            ('/meetings-events/', b'Meetings & Events'),
            ('/media/', b'Media Gallery'),
            ('/contact/', b'Contact Us'),
        ):
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, heading.decode())

    def test_booking_link_prefills_enquiry_type(self):
        response = self.client.get('/contact/?type=booking')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<option value="booking" selected>', html=False)

    def test_contact_form_saves_enquiry(self):
        response = self.client.post('/contact/', {
            'inquiry_type': Inquiry.InquiryType.EVENT,
            'name': 'Alex Guest',
            'email': 'alex@example.com',
            'phone': '',
            'message': 'A small family gathering.',
        })
        self.assertRedirects(response, '/contact/')
        self.assertEqual(Inquiry.objects.count(), 1)
        self.assertEqual(Inquiry.objects.get().inquiry_type, Inquiry.InquiryType.EVENT)

    def test_invalid_contact_form_is_not_saved(self):
        response = self.client.post('/contact/', {
            'inquiry_type': Inquiry.InquiryType.BOOKING,
            'name': 'Alex Guest',
            'email': 'not-an-email',
            'message': 'Please get back to me.',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Inquiry.objects.count(), 0)
        self.assertContains(response, 'Enter a valid email address.')
