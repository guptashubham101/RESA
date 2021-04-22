from django.conf import settings
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class  ExtractedRecipe(models.Model):
    userId = models.ForeignKey('User',on_delete=models.CASCADE,)
    recipe_template = models.TextField()
    recipe_url = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    modification_date = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=50)
    recipe_title = models.CharField(max_length=50)
    class Meta:
        db_table = 'extracted_recipe'

    def __str__(self):
        return "%s" % (self.id)

class Ingredients(models.Model):

    recipeId = models.ForeignKey('ExtractedRecipe',on_delete=models.CASCADE,)
    ingredient_name = models.TextField()

    class Meta:
        db_table = 'ingredients'

    def __str__(self):
        return "%s" % (self.id)
class User_Manager(BaseUserManager):
# password = None, first_name, last_name, school_ID, university_name
    

    def create_user(self, email,username,first_name, last_name, contact_number, password = None, ):
        if not email:
            raise ValueError("user must have email address")
        if not first_name:
            raise ValueError("user must have First Name")
        if not last_name:
            raise ValueError("user must have Last Name")
        if not contact_number:
            raise ValueError("user must have University Name")
       
        user = self.model(
            email= self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            contact_number = contact_number,
           
           
            )
        user.set_password(password)
        user.save(using = self.db)
        return user
    def create_superuser(self, email, username, password, first_name, last_name, university_name, school_ID,
                         contact_number=None):
            
        user = self.create_user(
                email= self.normalize_email(email),
                first_name = first_name,
                last_name = last_name,
                contact_number = contact_number,
                username= username,
                password= password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_supperuser = True
        user.save(using = self.db)
        return user
class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique = True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique = True)
    contact_number = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)
    modification_date = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'username'
    is_admin = models.BooleanField(default=False)
    date_login = models.DateTimeField(verbose_name='last login', auto_now = True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=False)
    is_supperuser = models.BooleanField(default= False)
    

    USERNAME_FIELD ='username'
    class Meta:
        db_table = 'user'
    objects = User_Manager()
    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj =None):
        return self.is_admin 
    def has_module_perms(self, app_labbel):
        return True
    # def __str__(self):
    #     return "%s" % (self.id)
