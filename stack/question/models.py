from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.name
 
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    like = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '{}'.format(self.user)


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tag = models.ManyToManyField(Tag)
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    comment = GenericRelation(Comment)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}'.format(self.user, self.title)

    @property
    def get_answers(self):
        answers = Answer.objects.filter(id=id)
        return answers

    @property
    def count_answers(self):
        return self.answers.all().count()


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(Question, related_name='answers')
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    comment = GenericRelation(Comment)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.title)


class Vote(models.Model):
    ACTIVITY_CHOICES = (
        ('U', 'up'),
        ('D', 'down'),
        ('N', 'null'),
    )
    choice = models.CharField(max_length=5, choices=ACTIVITY_CHOICES, default='N')
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    rating = models.IntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return 'id-{}, rating - {}, user - {}, choice - {}'.format(self.id, self.rating, self.user, self.choice)


