import os
from infinite.models import Category, Game, UserProfile, Comment, User
from django.test import TestCase
from django.forms import fields as django_fields

class FormClassTests(TestCase):
    def test_module_exists(self):
        project_path = os.getcwd()
        infinite_app_path = os.path.join(project_path, 'infinite')
        forms_module_path = os.path.join(infinite_app_path, 'forms.py')
        self.assertTrue(os.path.exists(forms_module_path), f"We could not find the infinite's forms.py module!")
    
    def test_category_form_class(self):
        import infinite.forms
        self.assertTrue('CategoryForm' in dir(infinite.forms), f"The class CategoryForm not found!")
        from infinite.forms import CategoryForm
        category_form = CategoryForm()
        self.assertEqual(type(category_form.__dict__['instance']), Category, f"The CategoryForm does not link to the Category model!")
        fields = category_form.fields
        expected_fields = {
            'name': django_fields.CharField,
            'slug': django_fields.CharField
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys(), f"The field '{expected_field_name}' not found!")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"The field '{expected_field_name}' has wrong type!")
        
    def test_Game_form_class(self):
        import infinite.forms
        self.assertTrue('GameForm' in dir(infinite.forms), f"The class GameForm not found!")
        from infinite.forms import GameForm
        game_form = GameForm()
        self.assertEqual(type(game_form.__dict__['instance']), Game, f"The GameForm does not link to the Game model!")
        fields = game_form.fields
        expected_fields = {
            'name': django_fields.CharField,
            'slug': django_fields.CharField,
            'released_date': django_fields.DateField,
            'description': django_fields.CharField,
            'picture': django_fields.ImageField,
            'likes': django_fields.IntegerField
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys(), f"The field '{expected_field_name}' not found!")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"The field '{expected_field_name}' has wrong type!")

    def test_User_form_class(self):
        import infinite.forms
        self.assertTrue('UserForm' in dir(infinite.forms), f"The class UserForm not found!")
        from infinite.forms import UserForm
        user_form = UserForm()
        self.assertEqual(type(user_form.__dict__['instance']), User, f"The UserForm does not link to the User model!")
        fields = user_form.fields
        expected_fields = {
            'password': django_fields.CharField,
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys(), f"The field '{expected_field_name}' not found!")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"The field '{expected_field_name}' has wrong type!")
       
    def test_UserProfile_form_class(self):
        import infinite.forms
        self.assertTrue('UserProfileForm' in dir(infinite.forms), f"The class UserProfileForm not found!")
        from infinite.forms import UserProfileForm
        userprofile_form = UserProfileForm()
        self.assertEqual(type(userprofile_form.__dict__['instance']), UserProfile, f"The UserProfileForm does not link to the UserProfile model!")
        fields = userprofile_form.fields
        expected_fields = {
            'picture': django_fields.ImageField,
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys(), f"The field '{expected_field_name}' not found!")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"The field '{expected_field_name}' has wrong type!")
      
    def test_Comment_form_class(self):
        import infinite.forms
        self.assertTrue('CommentForm' in dir(infinite.forms), f"The class CommentForm not found!")
        from infinite.forms import CommentForm
        comment_form = CommentForm()
        self.assertEqual(type(comment_form.__dict__['instance']), Comment, f"The CommentForm does not link to the Comment model!")
        fields = comment_form.fields
        expected_fields = {
            'comment': django_fields.CharField
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys(), f"The field '{expected_field_name}' not found!")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"The field '{expected_field_name}' has wrong type!")


      
            