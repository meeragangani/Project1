from django.db import models
import random
import datetime
from django.urls import reverse
import os
from django.conf import settings
from django.http import HttpResponse, Http404


# Create your models here.

class Login(models.Model):
    # user_id=models.AutoField(primary_key=True)

    image = models.ImageField(upload_to='static', height_field=None, width_field=None, max_length=100, null=True,
                              blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    department_head = models.BooleanField(default=False)
    designation = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField(auto_now=True)
    user_name = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    full_time = models.BooleanField(default=False)
    part_time = models.BooleanField(default=False)
    x = 0

    def __str__(self):
        return self.first_name

    def user_authenticate(self, request, username=None, password=None, is_superuser=False):
        l = Login.objects.get(user_name=username)
        print(l)
        if l.password == password and l.is_superuser == is_superuser:
            return True
        else:
            return False

    def user_login(self, request, username=None):
        l = Login.objects.get(user_name=username)
        print(l)
        c = request.session['id'] = l.id
        print(c)
        return username

    def user_logout(self, request):
        try:
            del request.session['id']
            return True
        except KeyError:
            return False


from .models import Login


class Daily(models.Model):
    title = models.CharField(max_length=100, default="")
    dailyreport = models.TextField(max_length=1000, default="")
    datetime = models.DateTimeField(auto_now=False)
    workhours = models.IntegerField(null=True, blank=True)

    uploadfile = models.FileField(upload_to='static', null=True, blank=True)
    User = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.User) + " " + str(self.datetime)

    def get_dailyreport(self, request):
        c = request.session['id']
        l = Login.objects.get(id=c)
        name = l.first_name
        print(name)
        reports = {}
        count = 0
        e = Daily.objects.filter(User=l.id)
        for e1 in e:
            report = {"datetime": e1.datetime, "title": e1.title, "dailyreport": e1.dailyreport,
                      "uploadfile": e1.uploadfile, "workhours": e1.workhours, "id": e1.id, "user": e1.User}
            count = count + 1
            reports[count] = report

        return reports

    def create_dailyreport(self, request, title, report, myfile, workhour):
        c = request.session['id']
        l = Login.objects.get(id=c)
        d = datetime.datetime.now()
        e = Daily.objects.create(title=title, dailyreport=report, uploadfile=myfile, datetime=d, workhours=workhour,
                                 User=l)

        e.save()


from .models import Daily


class Feedback(models.Model):
    feedback = models.TextField(max_length=1000, null=True, blank=True)
    Daily = models.ForeignKey(Daily, on_delete=models.CASCADE)
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False)
    notification = models.CharField(max_length=200, null=True, blank=True)

    def set_feedback(self, request, report):
        pass

    def get_feedback(self, request, user):
        feed = {}
        count = 0
        f = Feedback.objects.filter(Daily=user)

        if not f:
            for f1 in f:
                fd = Feedback.objects.get(Daily=f1.Daily, user=f1.user)
                fd.delete()
                fd.save()
            return None
        else:

            for f1 in f:
                fe = {"feedback": f1.feedback, "report": f1.Daily, "sender": f1.user, "datetime": f1.datetime}

            return fe


class Fact(models.Model):
    fact = models.CharField(max_length=200)

    def get_fact(self, request):
        f = Fact.objects.all()
        facts = {}
        for fn in f:
            facts[fn.id] = fn.fact
        n = random.randint(1, 50)
        f1 = facts.get(n)
        return f1


class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


