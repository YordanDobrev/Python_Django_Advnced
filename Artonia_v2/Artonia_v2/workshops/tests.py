import decimal
from datetime import date, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from Artonia_v2.workshops.models import Workshop, WorkshopRegistration
from Artonia_v2.accounts.models import ArtoniaUser

User = get_user_model()


class WorkshopModelTestCase(TestCase):
    def setUp(self):
        self.user = ArtoniaUser.objects.create_user(
            email='instructor@example.com',
            username='instructoruser',
            password='testpass123'
        )

        self.workshop = Workshop.objects.create(
            title='Test Art Workshop',
            instructor=self.user,
            description='A comprehensive art workshop',
            materials_provided='Basic art supplies',
            prerequisites='None',
            date=date.today() + timedelta(days=30),
            duration_hours=decimal.Decimal('2.50'),
            location='Online Studio',
            is_online=True,
            meeting_url='https://zoom.us/meeting',
            capacity=20,
            price=decimal.Decimal('49.99'),
            image_url='https://example.com/workshop.jpg'
        )

    def test_workshop_creation(self):
        """Test workshop can be created with valid data"""

        self.assertTrue(isinstance(self.workshop, Workshop))
        self.assertEqual(str(self.workshop), 'Test Art Workshop')

    def test_workshop_default_ordering(self):
        """Test default ordering by date"""

        future_workshop = Workshop.objects.create(
            title='Future Workshop',
            instructor=self.user,
            description='Another workshop',
            date=date.today() + timedelta(days=60),
            duration_hours=decimal.Decimal('1.50'),
            location='Offline Studio',
            capacity=15,
            price=decimal.Decimal('29.99'),
            image_url='https://example.com/future.jpg'
        )

        workshops = list(Workshop.objects.all())
        self.assertEqual(workshops[0], self.workshop)
        self.assertEqual(workshops[1], future_workshop)

    def test_workshop_registration(self):
        """Test workshop registration functionality"""

        participant = ArtoniaUser.objects.create_user(
            email='participant@example.com',
            username='participantuser',
            password='testpass456'
        )

        # Register for workshop
        registration = WorkshopRegistration.objects.create(
            workshop=self.workshop,
            participant=participant
        )

        self.assertTrue(isinstance(registration, WorkshopRegistration))
        self.assertEqual(registration.workshop, self.workshop)
        self.assertEqual(registration.participant, participant)

    def test_duplicate_registration_prevention(self):
        """Test preventing duplicate workshop registrations"""

        participant = ArtoniaUser.objects.create_user(
            email='duplicate@example.com',
            username='duplicateuser',
            password='testpass789'
        )

        WorkshopRegistration.objects.create(
            workshop=self.workshop,
            participant=participant
        )

        with self.assertRaises(IntegrityError):
            WorkshopRegistration.objects.create(
                workshop=self.workshop,
                participant=participant
            )

    def test_workshop_capacity_validation(self):
        """Test workshop capacity constraints"""

        participants = [
            ArtoniaUser.objects.create_user(
                email=f'participant{i}@example.com',
                username=f'participant{i}',
                password=f'testpass{i}'
            ) for i in range(21)
        ]

        # Register first 20 participants
        for participant in participants[:20]:
            WorkshopRegistration.objects.create(
                workshop=self.workshop,
                participant=participant
            )

    def test_workshop_past_date_validation(self):
        """Test prevention of creating workshops with past dates"""

        with self.assertRaises(ValidationError):
            past_workshop = Workshop(
                title='Past Workshop',
                instructor=self.user,
                description='Workshop in the past',
                date=date.today() - timedelta(days=1),
                duration_hours=decimal.Decimal('2.00'),
                location='Past Location',
                capacity=10,
                price=decimal.Decimal('39.99'),
                image_url='https://example.com/past.jpg'
            )
            past_workshop.full_clean()

    def test_workshop_online_url_requirement(self):
        """Test online workshops require a meeting URL"""

        with self.assertRaises(ValidationError):
            invalid_online_workshop = Workshop(
                title='Invalid Online Workshop',
                instructor=self.user,
                description='Online workshop without URL',
                date=date.today() + timedelta(days=45),
                duration_hours=decimal.Decimal('3.00'),
                location='Online',
                is_online=True,
                meeting_url=None,
                capacity=15,
                price=decimal.Decimal('59.99'),
                image_url='https://example.com/invalid.jpg'
            )
            invalid_online_workshop.full_clean()

    def test_workshop_price_validation(self):
        """Test workshop price constraints"""

        with self.assertRaises(ValidationError):
            invalid_price_workshop = Workshop(
                title='Invalid Price Workshop',
                instructor=self.user,
                description='Workshop with invalid price',
                date=date.today() + timedelta(days=40),
                duration_hours=decimal.Decimal('1.50'),
                location='Price Studio',
                capacity=10,
                price=decimal.Decimal('-10.00'),
                image_url='https://example.com/price.jpg'
            )
            invalid_price_workshop.full_clean()

    def test_workshop_participant_count(self):
        """Test counting workshop participants"""

        participants = [
            ArtoniaUser.objects.create_user(
                email=f'participant{i}@example.com',
                username=f'participant{i}',
                password=f'testpass{i}'
            ) for i in range(5)
        ]

        for participant in participants:
            WorkshopRegistration.objects.create(
                workshop=self.workshop,
                participant=participant
            )

        self.assertEqual(self.workshop.participants.count(), 5)
