from django.shortcuts import render
from django.contrib.auth.models import User
from chat.models import ChatModel
# Create your views here.


#User = get_user_model()


def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/index.html', context={'users': users})


def chatPage(request, username):
    print(request.user.username)
    print(username)

    user_obj = User.objects.get(username=username)
    #user_obj = User.objects.exclude(username=username)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
        print(thread_name)
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
        print("else")
        print(thread_name)
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    print(message_objs)

    return render(request, 'chat/main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})
  #  return render(request, 'main_chat.html', context={'user': user_obj, 'users': users})


