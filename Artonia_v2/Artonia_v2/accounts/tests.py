from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()


class AccountsModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            description='Test user description',
            image_url='https://example.com/testimage.jpg'
        )

        # Create test groups and permissions
        self.test_group = Group.objects.create(name='Test Group')
        self.test_permission = Permission.objects.create(
            name='Test Permission',
            codename='test_permission',
            content_type_id=1
        )

    def test_user_creation(self):
        """Test user creation with custom fields"""
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.description, 'Test user description')
        self.assertEqual(self.user.image_url, 'https://example.com/testimage.jpg')

    def test_user_group_assignment(self):
        """Test user group assignment"""
        self.user.groups.add(self.test_group)
        self.assertTrue(self.user.groups.filter(name='Test Group').exists())
        self.assertEqual(self.user.groups.count(), 1)

    def test_user_permission_assignment(self):
        """Test user permission assignment"""
        self.user.user_permissions.add(self.test_permission)
        self.assertTrue(self.user.user_permissions.filter(codename='test_permission').exists())
        self.assertEqual(self.user.user_permissions.count(), 1)

    def test_user_string_representation(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), 'testuser')

    def test_user_field_constraints(self):
        """Test user field constraints"""
        # Test optional fields
        optional_user = User.objects.create_user(
            username='optionaluser',
            email='optional@example.com',
            password='testpass456'
        )
        self.assertIsNone(optional_user.description)
        self.assertIsNone(optional_user.image_url)


class AccountsViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_registration(self):
        """Test user registration process"""
        registration_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpassword123!',
            'password2': 'complexpassword123!'
        }

        response = self.client.post(reverse('register'), data=registration_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration

        # Check user was created and logged in
        new_user = User.objects.get(username='newuser')
        self.assertIsNotNone(new_user)

    def test_user_login(self):
        """Test user login functionality"""
        login_response = self.client.login(
            username='testuser',
            password='testpass123'
        )
        self.assertTrue(login_response)

