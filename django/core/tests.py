from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse

from core.models import Movie
from core.views import MovieList


class MovieListPaginationTestCase(TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active"><a class="page-link" href="?page={}">{}</a></li>
    """

    def setUp(self):
        for n in range(15):
            Movie.objects.create(
                title='Title {}'.format(n),
                year=1999 + n,
                runtime=140,
                plot='Writer Aaron Mahnke launched his podcast "Lore" in 2015 and it '
            )

    def testFirstPage(self):
        movie_list_path = reverse('core:MovieList')
        request = RequestFactory().get(path=movie_list_path)
        response = MovieList.as_view() (request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(self.ACTIVE_PAGINATION_HTML.format(1,1), response.rendered_content)
