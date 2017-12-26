from django.test import TestCase

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')


    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Must use subscriptions/subscripition_form.html"""
        self.assertTemplateUsed(self.response, "subscriptions/subscription_form.html")

    def test_html(self):
        """HTML must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')
    def test_csrf(self):
        """HTML must contain CSRF"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')