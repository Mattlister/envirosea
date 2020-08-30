from django import forms
from .models import Booking, Trips


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        trips = Trips.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in trips]

        self.fields['trips'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
