from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}. You can now log in.')
            return redirect('login')
        else:
            # Clear messages before rendering the form
            storage = messages.get_messages(request)
            storage.used = True
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})


# def password_reset_view(request):
#     user = ...

#     send_password_reset_email(request, user)
#     return redirect(request)
