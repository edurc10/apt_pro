# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# from django.conf import settings
# from django.utils import timezone
# import re


# class AptProV1Post(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField()
#     published_date = models.DateTimeField(blank=True, null=True)
#     author = models.ForeignKey('AuthUser', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'apt_pro_v1_post'


class Aptdeal(models.Model):
    deal_date = models.CharField(max_length=8)
    price = models.PositiveIntegerField()
    prev_price = models.PositiveIntegerField()
    apt_size_id = models.PositiveIntegerField()
    apt_floor = models.CharField(max_length=3)
    is_cancel = models.CharField(max_length=1)
    cancel_date = models.CharField(max_length=8)
    deal_type = models.CharField(max_length=100, blank=True, null=True)
    broker_address = models.CharField(max_length=100, blank=True, null=True)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'aptdeal'


class AptdealToday(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    deal_date = models.CharField(max_length=8)
    price = models.PositiveIntegerField()
    prev_price = models.PositiveIntegerField()
    apt_size_id = models.PositiveIntegerField()
    apt_floor = models.CharField(max_length=3)
    is_cancel = models.CharField(max_length=1)
    cancel_date = models.CharField(max_length=8)
    deal_type = models.CharField(max_length=100)
    broker_address = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'aptdeal_today'


class AptdealTodayDate(models.Model):
    date = models.CharField(primary_key=True, max_length=14)

    class Meta:
        managed = False
        db_table = 'aptdeal_today_date'


class Aptinfo(models.Model):
    apt_id = models.PositiveIntegerField(primary_key=True)
    apt_name = models.CharField(max_length=100)
    construct_year = models.CharField(max_length=4)
    local_code = models.CharField(max_length=5)
    dong_code = models.CharField(max_length=5)
    serial_code = models.CharField(max_length=100, blank=True, null=True)
    jibun = models.CharField(max_length=100, blank=True, null=True)
    road_name = models.CharField(max_length=100, blank=True, null=True)
    road_building_main_code = models.CharField(max_length=5, blank=True, null=True)
    road_building_sub_code = models.CharField(max_length=5, blank=True, null=True)
    road_sigungu_code = models.CharField(max_length=5, blank=True, null=True)
    road_serial_code = models.CharField(max_length=2, blank=True, null=True)
    road_ground_code = models.CharField(max_length=1, blank=True, null=True)
    dong_name = models.CharField(max_length=100, blank=True, null=True)
    dong_main_code = models.CharField(max_length=4, blank=True, null=True)
    dong_sub_code = models.CharField(max_length=4, blank=True, null=True)
    dong_sigungu_code = models.CharField(max_length=5, blank=True, null=True)
    dong_jibun_code = models.CharField(max_length=1, blank=True, null=True)
    regdate = models.DateTimeField()
    modifydate = models.DateTimeField(blank=True, null=True)
    naver_id = models.CharField(max_length=10)
    hogang_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'aptinfo'


class Aptsizeinfo(models.Model):
    apt_size_id = models.PositiveIntegerField(primary_key=True)
    apt_id = models.PositiveIntegerField()
    apt_size = models.CharField(max_length=10)
    regdate = models.DateTimeField()
    max_price = models.PositiveIntegerField()
    modifydate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aptsizeinfo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Visitlog(models.Model):
    visitip = models.CharField(max_length=15)
    visittime = models.DateTimeField()
    visitrefer = models.CharField(max_length=300)
    visitagent = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'visitlog'

# class Post(models.Model):  
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title