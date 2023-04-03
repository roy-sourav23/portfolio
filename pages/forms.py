from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    fname = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "First Name",
                # "class": "textarea is-success is-medium",
            }
        ),
        label="First Name",
    )

    lname = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Last Name",
            }
        ),
        label="Last Name",
    )

    email = forms.EmailField(
        required=True,
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "Email",
            }
        ),
        label="Email",
    )

    phone = forms.RegexField(
        regex=r"^\+?1?\d{9,15}$",
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                "placeholder": "Phone Number",
            },
        ),
        label="Phone No.",
        max_length=12,
    )

    message = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Message",
            }
        ),
        label="Message",
    )

    class Meta:
        model = Message
        fields = (
            "fname",
            "lname",
            "email",
            "phone",
            "message",
        )
