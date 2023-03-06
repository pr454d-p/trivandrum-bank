from django import forms
from .models import Details,Branches
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class DetailsForm(forms.ModelForm):
    genders = (('Male','Male'),('Female','Female'),('Other','Other'))
    gender = forms.ChoiceField(choices=genders,widget=forms.RadioSelect)
    date_of_birth = forms.DateField(widget=DateInput(attrs={'onchange':"calculateAge()"}))
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="IN"))

    class Meta:
        model = Details
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branches.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branches.objects.filter(district_id=district_id).order_by('branch')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('branch')