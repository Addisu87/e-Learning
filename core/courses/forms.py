from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['subject', 'title', 'slug', 'overview']
        widgets = {
            'subject': forms.Select(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
            }),
            'title': forms.TextInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
            }),
            'overview': forms.Textarea(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
            }),
        }
        error_messages = {
            'title': {
                'required': 'The course title is required.'
            },
            'slug': {
                'required': 'The course slug is required.'
            },
            'subject': {
                'required': 'The course subject is required.'
            },
            'overview': {
                'required': 'The course overview is required.'
            }
        }
