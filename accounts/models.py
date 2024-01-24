from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,username,password,**extra_fields):
        if not username or not extra_fields.get("email"):
            raise ValueError(_("The Username and Email must be set"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault("age",0)
        superuser=self.create_user(username,password,**extra_fields)
        superuser.is_staff=True
        superuser.save()
        return superuser

class Roles(models.Model):
    rolename=models.CharField(max_length=50,default="role")
    
    def __str__(self) -> str:
        return f"{self.rolename}"
class User(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True,blank=False)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    role=models.ForeignKey(Roles,on_delete=models.SET_NULL,null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    objects=UserManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']
    
    @property
    def is_superuser(self):
        return self.is_staff
    
    def has_module_perms(self,*args,**kwargs):
        if self.is_staff:
            return True
    
    def has_perm(self,*args,**kwargs):
        if self.is_staff:
            return True

    def __str__(self):
        return self.username
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name