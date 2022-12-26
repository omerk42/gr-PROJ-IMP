from allauth.account.forms import SignupForm, LoginForm,ResetPasswordForm, EmailAwarePasswordResetTokenGenerator
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import ChangePasswordForm

User = get_user_model()

"""
FOR MORE INFO GO HERE 
https://django-allauth.readthedocs.io/en/latest/forms.html

"""

class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Email
        self.fields['email'].widget.attrs['data-jsv-validators'] = 'require,email,length'
        self.fields['email'].widget.attrs['data-jsv-min'] = '6'
        self.fields['email'].widget.attrs['data-jsv-max'] = '255'
        # Username
        self.fields['username'].widget.attrs['data-jsv-validators'] = 'require,length'
        self.fields['username'].widget.attrs['data-jsv-min'] = '6'
        self.fields['username'].widget.attrs['data-jsv-max'] = '255'
        # Password
        self.fields['password1'].widget.attrs['data-jsv-validators'] = 'require,length'
        self.fields['password1'].widget.attrs['data-jsv-min'] = '6'
        self.fields['password1'].widget.attrs['data-jsv-max'] = '255'
        # Password Confirm
        self.fields['password2'].widget.attrs['data-jsv-validators'] = 'require,length,compare'
        self.fields['password2'].widget.attrs['data-jsv-compare'] = 'password1'
        self.fields['password2'].widget.attrs['data-jsv-min'] = '6'
        self.fields['password2'].widget.attrs['data-jsv-max'] = '255'


class UserLoginForm(LoginForm):
    """
    Form that will be rendered on user login
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Username
        self.fields['login'].widget.attrs['data-jsv-validators'] = 'require,length'
        self.fields['login'].widget.attrs['data-jsv-min'] = '6'
        self.fields['login'].widget.attrs['data-jsv-max'] = '255'
        # Password
        self.fields['password'].widget.attrs['data-jsv-validators'] = 'require,length'
        self.fields['password'].widget.attrs['data-jsv-min'] = '6'
        self.fields['password'].widget.attrs['data-jsv-max'] = '255'


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class UserResetPasswordForm( ResetPasswordForm):
    """
    Form that will be rendered when user want to reset password
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Email
        self.fields['email'].widget.attrs['data-jsv-validators'] = 'require,length,email'
        self.fields['email'].widget.attrs['data-jsv-min'] = '12'
        self.fields['email'].widget.attrs['data-jsv-max'] = '255'
