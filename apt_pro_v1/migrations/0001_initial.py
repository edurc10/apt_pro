# Generated by Django 4.1.7 on 2023-03-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aptdeal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deal_date", models.CharField(max_length=8)),
                ("price", models.PositiveIntegerField()),
                ("prev_price", models.PositiveIntegerField()),
                ("apt_size_id", models.PositiveIntegerField()),
                ("apt_floor", models.CharField(max_length=3)),
                ("is_cancel", models.CharField(max_length=1)),
                ("cancel_date", models.CharField(max_length=8)),
                ("deal_type", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "broker_address",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("reg_date", models.DateTimeField()),
            ],
            options={
                "db_table": "aptdeal",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AptdealToday",
            fields=[
                ("id", models.PositiveIntegerField(primary_key=True, serialize=False)),
                ("deal_date", models.CharField(max_length=8)),
                ("price", models.PositiveIntegerField()),
                ("prev_price", models.PositiveIntegerField()),
                ("apt_size_id", models.PositiveIntegerField()),
                ("apt_floor", models.CharField(max_length=3)),
                ("is_cancel", models.CharField(max_length=1)),
                ("cancel_date", models.CharField(max_length=8)),
                ("deal_type", models.CharField(max_length=100)),
                ("broker_address", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "aptdeal_today",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AptdealTodayDate",
            fields=[
                (
                    "date",
                    models.CharField(max_length=14, primary_key=True, serialize=False),
                ),
            ],
            options={
                "db_table": "aptdeal_today_date",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Aptinfo",
            fields=[
                (
                    "apt_id",
                    models.PositiveIntegerField(primary_key=True, serialize=False),
                ),
                ("apt_name", models.CharField(max_length=100)),
                ("construct_year", models.CharField(max_length=4)),
                ("local_code", models.CharField(max_length=5)),
                ("dong_code", models.CharField(max_length=5)),
                (
                    "serial_code",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("jibun", models.CharField(blank=True, max_length=100, null=True)),
                ("road_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "road_building_main_code",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                (
                    "road_building_sub_code",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                (
                    "road_sigungu_code",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                (
                    "road_serial_code",
                    models.CharField(blank=True, max_length=2, null=True),
                ),
                (
                    "road_ground_code",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("dong_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "dong_main_code",
                    models.CharField(blank=True, max_length=4, null=True),
                ),
                (
                    "dong_sub_code",
                    models.CharField(blank=True, max_length=4, null=True),
                ),
                (
                    "dong_sigungu_code",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                (
                    "dong_jibun_code",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("regdate", models.DateTimeField()),
                ("modifydate", models.DateTimeField(blank=True, null=True)),
                ("naver_id", models.CharField(max_length=10)),
                ("hogang_id", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "aptinfo",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Aptsizeinfo",
            fields=[
                (
                    "apt_size_id",
                    models.PositiveIntegerField(primary_key=True, serialize=False),
                ),
                ("apt_id", models.PositiveIntegerField()),
                ("apt_size", models.CharField(max_length=10)),
                ("regdate", models.DateTimeField()),
                ("max_price", models.PositiveIntegerField()),
                ("modifydate", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "aptsizeinfo",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Visitlog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("visitip", models.CharField(max_length=15)),
                ("visittime", models.DateTimeField()),
                ("visitrefer", models.CharField(max_length=300)),
                ("visitagent", models.CharField(max_length=300)),
            ],
            options={
                "db_table": "visitlog",
                "managed": False,
            },
        ),
    ]
