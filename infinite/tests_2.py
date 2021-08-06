from django.test import TestCase
from django.urls import reverse
from infinite.models import Category,Game
from django.contrib.auth.models import User
# Create your tests here.

def add_game(category, name,released_date,description,picture,likes=0):
    """
    Helper function to add a test game"""
    p = Game.objects.get_or_create(category=category, name=name)[0]
    p.description=description
    p.picture=picture
    p.likes=likes
    p.released_date=released_date
    p.save()
    return p
def create_user_object():
    """
    Helper function to create a User object.
    """
    user = User.objects.get_or_create(username='testuser',
                                      first_name='Test',
                                      last_name='User',
                                      email='test@test.com')[0]
    user.set_password('testabc123')
    user.save()
    return user
class IndexViewTests(TestCase):
    def test_index_view_with_no_games(self):
        """If no games exist, the appropriate message should be displayed."""
        response = self.client.get(reverse('infinite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no games present.')
        self.assertQuerysetEqual(response.context['games'], [])

    def test_index_view_with_games(self):
        """
        Checks whether games are displayed correctly when present.
        """
        add_game(Category.objects.get_or_create(name='Shooter')[0],'11','2000-01-01','this is game','./static/images/background.jpg')
        response = self.client.get(reverse('infinite:index'))
        self.assertEqual(response.status_code, 200)
        num_games = len(response.context['games'])
        self.assertEquals(num_games, 1)
    def test_myaccount(self):
        """Checks whether my account are displayed correctly"""
        create_user_object()
        self.client.login(username='testuser', password='testabc123')
        response = self.client.get(reverse('infinite:myaccount'))
        self.assertEqual(response.status_code, 200)


