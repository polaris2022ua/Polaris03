from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, phone, password=None):
        if not email:
            raise ValueError("User must have an email address.")
        if not username:
            raise ValueError("User must have an  username.")
        if not phone:
            raise ValueError("User must have an  phone.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            password=password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return 'user_{0}/{1}'.format(instance.id, filename)

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    username = models.CharField(max_length=40, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(verbose_name='data join', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to=user_directory_path, blank=True)
    hide_email = models.BooleanField(default=True)

    object = MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.username

    def get_profile_image_filname(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_image/{self.pk}/')]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


