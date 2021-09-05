from django import test
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from rest_framework.test import APITestCase
from .models import Things
from rest_framework import status


class ThingsModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user=get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_thing=Things.objects.create(
            title='Title of thing',
            purchaser=test_user,
            description='Words'
        )
        test_thing.save()


    def test_thing_content(self):
        thing = Things.objects.get(id=1)

        self.assertEqual(thing.title, 'Title of thing')
        self.assertEqual(str(thing.purchaser), 'tester')
        self.assertEqual(thing.description, 'Words')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('things_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_things = Things.objects.create(
            purchaser = test_user,
            title = 'Title of Blog',
            description = 'Words'
        )
        test_things.save()

        response = self.client.get(reverse('things_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'title': test_things.title,
            'description': test_things.description,
            'purchaser': test_user.id,
        })


    def test_create(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        url = reverse('things_list')
        data = {
            "title":"Testing is Fun!!!",
            "description":"when the right tools are available",
            "purchaser":test_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Things.objects.count(), 1)
        self.assertEqual(Things.objects.get().title, data['title'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_things= Things.objects.create(
            purchaser = test_user,
            title = 'Title of Blog',
           description = 'Words'
        )

        test_things.save()

        url = reverse('things_detail',args=[test_things.id])
        data = {
            "title":"Testing is Still Fun!!!",
            "purchaser":test_user.id,
            "description":test_things.description,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Things.objects.count(), test_things.id)
        self.assertEqual(Things.objects.get().title, data['title'])


    def test_delete(self):
        """Test the api can delete a post."""

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_things = Things.objects.create(
            purchaser = test_user,
            title = 'Title of Blog',
            description = 'Words'
        )

        test_things.save()

        things = Things.objects.get()

        url = reverse('things_detail', kwargs={'pk': things.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)