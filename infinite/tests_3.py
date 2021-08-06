from django.http import response
from django.test import TestCase
import os
import importlib
from django.urls import reverse

# Create your tests here.

class UrlsPartTests(TestCase):
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.infinite_app_dir = os.path.join(self.project_base_dir, 'infinite')
    def test_urls_created(self):
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'infinite_team_project', 'urls.py'))
        self.assertTrue(urls_module_exists, f"Your project's urls.py module does not exist!")

    def test_infinite_has_urls_module(self):
        module_exists = os.path.isfile(os.path.join(self.infinite_app_dir, 'urls.py'))
        self.assertTrue(module_exists, f"The infinite app's url.py module is missing!")
    
class UrlsPageMappingTests(TestCase):

    def setUp(self):
        self.views_module = importlib.import_module('infinite.views')
        self.views_module_listing = dir(self.views_module)
        self.project_urls_module = importlib.import_module('infinite_team_project.urls')
        self.app_urls_module = importlib.import_module('infinite.urls')

    def test_index(self):
        index_mapping_exists=False
        response = self.client.get(reverse('infinite:index'))
        for mapping in self.project_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'index':
                    index_mapping_exists = True
        self.assertTrue(index_mapping_exists, f"The index URL mapping could not be found!")
        self.assertEquals(reverse('infinite:index'), '/infinite/', f"The index URL lookup failed!")
        self.assertEquals(response.status_code, 200, f"Requesting the index page failed!")

    def test_about(self):
        about_mapping_exists=False
        response = self.client.get(reverse('infinite:about'))
        for mapping in self.app_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'about':
                    about_mapping_exists = True
        self.assertTrue(about_mapping_exists, f"The about URL mapping could not be found!")
        self.assertEquals(response.status_code, 200, f"Requesting the about page failed!")
    
    def test_myaccount(self):
        myaccount_mapping_exists=False
        for mapping in self.app_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'myaccount':
                    myaccount_mapping_exists = True
        self.assertTrue(myaccount_mapping_exists, f"The myaccount URL mapping could not be found!")

    
    def test_likelist(self):
        likelist_mapping_exists=False
        for mapping in self.app_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'likelist':
                    likelist_mapping_exists = True
        self.assertTrue(likelist_mapping_exists, f"The likelist URL mapping could not be found!")


    def test_show_category(self):
        show_category_mapping_exists=False
        for mapping in self.app_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'show_category':
                    show_category_mapping_exists = True
        self.assertTrue(show_category_mapping_exists, f"The show_category URL mapping could not be found!")

    def test_show_game(self):
        show_game_mapping_exists=False
        for mapping in self.app_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'show_game':
                    show_game_mapping_exists = True
        self.assertTrue(show_game_mapping_exists, f"The show_game URL mapping could not be found!")

    def test_search(self):
        search_mapping_exists=False
        for mapping in self.app_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'search':
                    search_mapping_exists = True
        self.assertTrue(search_mapping_exists, f"The search URL mapping could not be found!")
