from django.core.exceptions import ValidationError
from django.forms import ModelForm

from icallback_app.models import Widget


class WidgetCreationForm(ModelForm):
    class Meta:
        model = Widget
        fields = ('site_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['site_name'].label = "Site"
        self.fields['site_name'].help_text = "www.my-site.com"

    def clean(self):
        data = self.cleaned_data

        if len(data['site_name']) == 0:
            raise ValidationError('Site is empty!')

        return data

    def save(self, commit=True):
        inst = super().save(commit)

        print(inst)

        return inst
