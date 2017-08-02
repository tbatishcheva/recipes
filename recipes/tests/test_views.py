from django.test import TestCase
from recipes.models import Recipe, Cuisine

from unittest import skip


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')

    @skip
    def test_can_save_a_POST_request(self):

        self.client.post('cuisine/new', data={'name': 'finland'})
        self.assertEqual(Cuisine.objects.count(), 1)
        cuisine = Cuisine.objects.first()

        self.client.post('/recipe/new', data={'name': 'Bread',
                                              'description': 'just bread',
                                              'cuisine': cuisine,
                                              'cooking_time': 1
                                              })

        self.assertEqual(Recipe.objects.count(), 1)
        new_item = Recipe.objects.first()
        self.assertEqual(new_item.name, 'Bread')

