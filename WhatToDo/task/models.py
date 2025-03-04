from django.db import models
from appuser.models import AppUser


class TaskManager(models.Manager):
    def all_user_tasks(self, user):
        return self.filter(user=user)


class Task(models.Model):
    STATUS_CHOICES = [
        (1, "To Do"),
        (2, "In Progress"),
        (3, "Done"),
    ]
    
    PRIORITY_CHOICES = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    ]

    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    create_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline_date = models.DateField(blank=True, null=True)
    
    manage = TaskManager()
    objects = models.Manager()

    def __str__(self):
        return self.name


class SubTask(models.Model):
    STATUS_CHOICES = [
        (1, "To Do"),
        (2, "In Progress"),
        (3, "Done"),
    ]
    
    PRIORITY_CHOICES = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    main_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    create_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.main_task.name}"
