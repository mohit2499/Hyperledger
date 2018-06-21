from django import forms


PlatformChoices= [
    ('mastercard', 'Mastercard'),
    ('gdpr', 'GDPR'),
    ('azure', 'Azure'),
    ('google', 'Google'),
    ]
placeholder= [
    ('option', 'Option'),]

class transferfrom(forms.Form):
    Platform = forms.ChoiceField(choices=PlatformChoices)
    Extract = forms.ChoiceField(choices=placeholder)
    Recipient = forms.ChoiceField(choices=placeholder)



