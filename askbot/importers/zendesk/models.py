from django.db import models

class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    entry_id = models.IntegerField()
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    is_informative = models.BooleanField()
    is_processed = models.BooleanField(default = False)

class User(models.Model):
    user_id = models.IntegerField()
    askbot_user_id = models.IntegerField(null = True)
    created_at = models.DateTimeField()
    is_active = models.BooleanField()
    last_login = models.DateTimeField(null = True)
    name = models.CharField(max_length = 255)
    openid_url = models.URLField(null = True)
    organization_id = models.IntegerField(null = True)
    phone = models.CharField(max_length = 32, null = True)
    restriction_id = models.IntegerField()
    roles = models.IntegerField()
    time_zone = models.CharField(max_length = 255)
    updated_at = models.DateTimeField()
    uses_12_hour_clock = models.BooleanField()
    email = models.EmailField(null = True)
    is_verified = models.BooleanField()
    photo_url = models.URLField()

class Forum(models.Model):
    description = models.CharField(max_length = 255, null = True)
    display_type_id = models.IntegerField()
    entries_count = models.IntegerField()
    forum_id = models.IntegerField()
    is_locked = models.BooleanField()
    name = models.CharField(max_length = 255)
    organization_id = models.IntegerField(null = True)
    position = models.IntegerField(null = True)
    updated_at = models.DateTimeField()
    translation_locale_id = models.IntegerField(null = True)
    use_for_suggestions = models.BooleanField()
    visibility_restriction_id = models.IntegerField()
    is_public = models.BooleanField()
