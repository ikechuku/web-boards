from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import home, board_topics, new_topic
from .models import Board

class HomeTests(TestCase):
           
    # database instance for HomeTest
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django')
        url = reverse('home')
        self.response = self.client.get(url)

    # test if Django is returning a status code 200 (success) for home view
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    # test if Django is using the correct view function to render home view
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
 
    #  test if the response body contains a given text
    def test_home_view_contains_link_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

class BoardTopicsTests(TestCase):
    # database instance for BoardTopicsTests
    def setUp(self):
        Board.objects.create(name='Django', description='Django Board.')

    # test if Django is returning a status code 200 (success) for an existing Board.
    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # test if Django is returning a status code 404 (page not found) for a Board that doesn’t exist in the database.
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)


    # test if Django is using the correct view function to render the topics.
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
            board_topics_url = reverse('board_topics', kwargs={'pk': 1})
            response = self.client.get(board_topics_url)
            homepage_url = reverse('home')
            self.assertContains(response, 'href="{0}"'.format(homepage_url))

class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django Board')

    def test_new_topic_view_success_status_code(self):
            url = reverse('new_topic', kwargs={'pk': 1})
            response = self.client.get(url)
            self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))

        