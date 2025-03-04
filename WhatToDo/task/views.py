from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import Task, SubTask
from appuser.models import AppUser


class IndexView(View):
    def get(self, request):
        if request.user and not request.user.is_authenticated:
            print("user not logged in so I redirect him to login page")
            return redirect(reverse('user:login'))
        user = request.user
        appuser = AppUser.objects.filter(user=user).first()
        tasks = Task.manage.all_user_tasks(appuser)
        context = {"tasks": tasks, "appuser": appuser}
        return render(request, "dashboard.html", context)


class ProfileView(View):
    def get(self, request):
        if not request.user or not request.user.is_authenticated:
            return redirect(reverse('user:login'))
        
        user = request.user
        appuser = AppUser.objects.filter(user=user).first()
        
        return render(request, "profile.html")
    

class SubTasksView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        sub_tasks = SubTask.objects.filter(main_task=task)

        context={'sub_tasks': list(sub_tasks), 'task_name': task.name}
        return render(request, "sub_tasks.html", context=context)


class TaskCreateView(View):
    def get(self, request):
        return render(request, "add_task.html")

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("user:login")

        appuser = AppUser.objects.get(user=request.user)

        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.get("status", 1)
        priority = request.POST.get("priority", 2)
        deadline_date = request.POST.get("deadline_date")

        task = Task.objects.create(
            user=appuser,
            name=name,
            description=description,
            status=status,
            priority=priority,
            deadline_date=deadline_date if deadline_date else None
        )
        task.save()

        return redirect("home:index") 