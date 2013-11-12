from django import forms


class LoginForm(forms.Form):
    '''Login Form for all users'''
    email  = forms.EmailField(label='',
                    widget=forms.TextInput(
                        attrs={'placeholder': 'Email',
                               'class':'input-large ',
                               'style':'width:290px',
                               'id':'email',
                               'onfocus':"this.placeholder = ''",
                               'onblur':"this.placeholder = 'Email'"}
                    ))
    password  = forms.CharField(
            label='', widget=forms.PasswordInput(
                attrs={'placeholder':'password',
                       'class':'input-large ',
                       'style':'width:290px',
                       'id':'password',
                       'onfocus':"this.placeholder = ''",
                       'onblur':"this.placeholder = 'password'"}
            ))