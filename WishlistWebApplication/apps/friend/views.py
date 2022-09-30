from django.shortcuts import render


def friend_list_view(request):
    context = {}
    return render(request, 'friend/friendlist.html/', context)
