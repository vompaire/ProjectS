from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

@login_required
def profile(request):
    user = request.user
    return render(request, 'userprofile/userprofile.html', {'user': user})


def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'userprofile/userprofile.html', {'user': user})