from django.test import TestCase
from infinite.models import Game,Category
# Create your tests here.
class CategoryMethodTests(TestCase):
    def test_ensure_likes_are_positive(self):
    # Ensures the number of likes received for a Game are positive or zero.
        game = Game(category = Category.objects.create(name='testCat'),name='test', likes=-1,description = 'this is description')
        game.save()
        self.assertEqual((game.likes >= 0), True)

    def test_slug_line_creation(self):
        # Checks to make sure that when a category is created, an 
        # appropriate slug is created
        category = Category(name='Random Category String')
        category.save()
        self.assertEqual(category.slug, 'random-category-string')
