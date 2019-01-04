from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse  # allows django to create urls


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()  # sets up a client
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@test.com',
            password='Password1'
        )
        self.client.force_login(self.admin_user)  # forces login for our tests
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='Password1',
            name='Test user'
        )

    def test_users_listed(self):
        """Tests that users are listed on user page"""
        url = reverse('admin:core_user_changelist')  # comes from django admin
        res = self.client.get(url)

        # checks these items exists and checks that the http request was 200
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        # creates url from django admin edit page
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
