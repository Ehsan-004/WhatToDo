from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from appuser.models import AppUser


class RegisterView(View):
    def get(self, request):
        return render(request, 'sign-up.html')

    def post(self, request):
        username = request.POST.get('username', False)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)

        if not all([username, email, password]):

            if User.objects.filter(username=username).exists():
                messages.error(request, "نام کاربری قبلاً استفاده شده است!")
                return render(request, 'register.html')
            
            user = User.objects.create_user(username=username, email=email, password=password)
            appuser = AppUser.objects.create(user=user)
            appuser.save()
            user.save()
            messages.success(request, "ثبت‌نام موفق بود!")
            return redirect(reverse('user:login'))


class CustomLoginView(View):
    def get(self, request):
        return render(request, 'sign-in.html')

    def post(self, request):
        username = request.POST.get('username', False) #  TODO: using email to login
        password = request.POST.get('password', False)
        
        print(username, password)
        
        if not all([username, password]):
            messages.error(request, "لطفاً همه‌ی فیلدها را پر کنید!")
            return render(request, 'sign-in.html')
        
        user = authenticate(request, username=username, password=password)
                
        if user:
            login(request, user)
            messages.success(request, "logged in successfully!")
            print("cannot og user in")
            return redirect(reverse('home:index'))
        else:
            print("cannot log user in")
            messages.error(request, "wrong credentials!")
            return render(request, 'sign-in.html')

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "شما با موفقیت خارج شدید!")
        return redirect(reverse('user:login'))


# class ChangePasswordView(View):
#     def get(self, request):
#         return render(request, 'change_password.html')

#     def post(self, request):
#         old_password = request.POST.get('old_password')
#         new_password = request.POST.get('new_password')
#         confirm_password = request.POST.get('confirm_password')

#         if not request.user.check_password(old_password):
#             messages.error(request, "رمز عبور فعلی اشتباه است!")
#             return render(request, 'appuser/change_password.html')

#         if new_password != confirm_password:
#             messages.error(request, "رمز عبور جدید و تأیید آن یکسان نیست!")
#             return render(request, 'appuser/change_password.html')
        
#         request.user.set_password(new_password)
#         request.user.save()
#         update_session_auth_hash(request, request.user)
#         messages.success(request, "رمز عبور با موفقیت تغییر کرد!")
#         return redirect('home')




# class ResetPasswordView(PasswordResetView):
#     template_name = 'appuser/reset_password.html'
#     email_template_name = 'appuser/reset_password_email.html'
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         messages.success(self.request, "اگر ایمیل شما در سیستم باشد، لینک تغییر رمز ارسال خواهد شد.")
#         return super().form_valid(form)

