from django.utils import timezone
from Artonia_v2.mixins import ReadOnlyMixin
from Artonia_v2.workshops.models import Workshop, WorkshopRegistration
from django import forms


class CreateWorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        exclude = ('participants', 'instructor')

    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Workshop name...'}))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Workshop description...'
    }))

    materials_provided = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Materials provided...'
    }))

    prerequisites = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Prerequisites...'
    }))

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=timezone.now().date
    )

    duration_hours = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'type': 'number',
            'placeholder': 'Duration in Hours',
        })
    )

    location = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Location...'
    }))

    is_online = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }),
        required=False,
        label='Online Workshop?',
    )

    meeting_url = forms.CharField(widget=forms.URLInput(attrs={
        'placeholder': 'Meeting URL...'
    }),
        required=False
    )

    capacity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Capacity...'
        })
    )

    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Price...'
        })
    )

    image_url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Put Workshop Image URL...'
    }))


class UpdateWorkshopForm(CreateWorkshopForm):
    pass


class DeleteWorkshopForm(ReadOnlyMixin, forms.ModelForm):
    class Meta:
        model = Workshop
        exclude = ['instructor', 'participants', 'is_online']

    read_only_fields = ['title', 'description', 'materials_provided', 'prerequisites', 'date', 'duration_hours',
                        'location', 'meeting_url', 'capacity', 'price', 'image_url'
                        ]


class WorkshopRegistrationForm(forms.ModelForm):
    class Meta:
        model = WorkshopRegistration
        fields = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.workshop = kwargs.pop('workshop', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        existing_registration = WorkshopRegistration.objects.filter(
            participant=self.user,
            workshop=self.workshop
        ).exists()

        if existing_registration:
            raise forms.ValidationError("You have already registered for this workshop.")

        return cleaned_data
