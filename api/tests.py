# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import TodoList

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

# Create your tests here.
class ModelTestCase(TestCase):
    """This class defines the test suite for the TodoList model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd") 
        self.todolist_id = 100
        self.todolist = TodoList(id=self.todolist_id, owner=user)

    def test_model_can_create_a_todolist(self):
        """Test the todolist model can create a todolist."""
        old_count = TodoList.objects.count()
        self.todolist.save()
        new_count = TodoList.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.client.force_authenticate(user=user)
        self.client = APIClient()
        self.todolist_data = {'description': 'Go to Ibiza Have Fun', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.todolist_data,
            format="json")

    def test_api_can_create_a_todolist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/todolists/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_todolist(self):
        """Test the api can get a given bucketlist."""
        todolist = TodoList.objects.get(id=1)
        response = self.client.get(
            '/todolists/',
            kwargs={'pk': todolist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todolist)

    def test_api_can_update_todolist(self):
        """Test the api can update a given bucketlist."""
        todolist = TodoList.objects.get()
        change_todolist = {'description': 'Something new todo task'}
        res = self.client.put(
            reverse('details', kwargs={'pk': todolist.id}),
            change_todolist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_todolist(self):
        """Test the api can delete a bucketlist."""
        todolist = TodoList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': todolist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
