from django.forms import ModelForm
from .models import Heart
from django import forms
from django.contrib.auth import authenticate, get_user_model

# choices for prediction form
gender = [
        ('1', 'Male'),
        ('0', 'Female')
]

chest_pain_type_choice = [
    ('0', 'Typical angina'),
    ('1', 'Atypical angina'),
    ('2', 'Non-anginal pain'),
    ('3', 'Asymptotic')
]

fasting_blood_sugar_choice = [
    ('1', 'Yes'),
    ('0', 'No')
]

resting_ecg_choice = [
    ('0', 'Normal'),
    ('1', 'ST-T wave abnormality'),
    ('2', 'Left venticular hypertropy')
]

exercise_induced_angina_choice = [
    ('1', 'Yes'),
    ('0', 'No')
]

slope_choice = [
    ('0', 'Upsloping'),
    ('1', 'Flat'),
    ('2', 'Downsloping')
]

no_of_major_vessel = [
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
]

thalassemia_choice = [
    ('1', 'Normal'),
    ('2', 'Alpha Thalassemia'),
    ('3', 'Beta Thalassemia')
]

User = get_user_model()


class Heart_form(ModelForm):
    chest_pain_type = forms.ChoiceField(widget=forms.Select, choices=chest_pain_type_choice)
    fasting_blood_sugar = forms.ChoiceField(widget=forms.Select, choices=fasting_blood_sugar_choice)
    resting_ecg = forms.ChoiceField(widget=forms.Select, choices=resting_ecg_choice)
    exercise_induced_angina = forms.ChoiceField(widget=forms.Select, choices=exercise_induced_angina_choice)
    slope = forms.ChoiceField(widget=forms.Select, choices=slope_choice)
    no_of_major_vessel = forms.ChoiceField(widget=forms.Select, choices=no_of_major_vessel)
    thalassemia = forms.ChoiceField(widget=forms.Select, choices=thalassemia_choice)

    class Meta:
        model = Heart
        fields = [
            'chest_pain_type', 'resting_bloodpressure',
            'serum_cholestrol', 'fasting_blood_sugar',
            'resting_ecg', 'max_heartrate', 'exercise_induced_angina',
            'oldpeak', 'slope', 'no_of_major_vessel', 'thalassemia'
        ]


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(ModelForm):
    username = forms.CharField(max_length=50)
    email_address = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender)

    class Meta:
        model = User
        fields = [
            'username',
            'email_address',
            'password',
            'confirm_password',
            'date_of_birth',
            'gender',
        ]

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email_address"]
        if commit:
            user.save()
        return user
