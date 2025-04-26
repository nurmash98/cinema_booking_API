from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.movies.models import Movie

class MovieAPITests(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            duration=100,
            release_date="2025-01-01",
            posterUrl="https://example.com/poster.jpg"
        )
        self.list_url=reverse('movie-list')
        self.detail_url = reverse('movie-detail', kwargs={'pk': self.movie.pk})
    def test_list_movies(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_movie(self):
        data = {
            "title": "Inception",
            "description": "A mind-bending thriller",
            "duration": 148,
            "release_date": "2010-07-16",
            "posterUrl": "http://example.com/inception.jpg"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("message", response.data)
    
    def test_update_movie(self):
        data = {
            "title": "Updated Title",
            "description": "Updated",
            "duration": 120,
            "release_date": "2024-05-01",
            "posterUrl": "http://example.com/new.jpg"
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Фильм успешно обновлён")
    def test_delete_movie(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Фильм успешно удалён")