from django import forms


class DonorSearch(forms.Form):
    blood_group_s_choice = (
        ("empty" , "Select blood group"),
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),
    )
    select_blood_group = forms.ChoiceField(
        choices=blood_group_s_choice,
        widget=forms.Select(
            attrs={'class':'form-control',
            'required':'True',
            },
            ),
    )

    select_location = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control',
            'required':'True', 
            'placeholder':'where do you need?. e.g. dhaka'
            }
        ),
    )
    