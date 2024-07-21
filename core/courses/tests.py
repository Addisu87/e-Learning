
# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from core.courses.models import Module, Course


class ContentCreateUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.course = Course.objects.create(
            title='Test Course', owner=self.user)
        self.module = Module.objects.create(
            course=self.course, title='Test Module')
        self.client.login(username='testuser', password='12345')

    def test_get_content_create_view(self):
        response = self.client.get(
            reverse('content_create', args=[self.module.id, 'text']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/manage/content/form.html')

    def test_post_content_create_view(self):
        response = self.client.post(reverse('content_create', args=[self.module.id, 'text']), {
            'title': 'Test Content',
            'body': 'This is a test content.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Content.objects.filter(module=self.module).exists())

# More tests can be added
