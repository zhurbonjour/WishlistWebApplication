from django.db import models
# from django.conf import settings
# from venv.src.WishlistWebApplication.apps.account.models import Account


class FriendList(models.Model):
    """Список друзей пользователя"""
    user = models.OneToOneField('account.Account', on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField('account.Account', blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

#     refactor next functions later to business logic layer
    def add_friend(self, account):
        """Добаление нового друга"""
        if account not in self.friends.all():
            self.friends.add(account)
            self.save()

    def remove_friend(self, account):
        """Удаление друга"""
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        """Дружба закончилась, удаляем из друзей"""
        remover_friends_list = self
        remover_friends_list.remove_friend(removee)
        friend_list = FriendList.objects.get(user=removee)
        friend_list.remove_friend(self.user)

    def is_mutual_friends(self, friend):
        """Проверка, что пользователи - друзья"""
        if friend in self.friends.all():
            return True
        return False


class FriendRequest(models.Model):
    """
    Запрос в друзья происходит между двумя участниками акта:
        отправителем запроса (sender) и
        получателем запроса (receiver),
    он [запрос] может быть неактивным (is_active) либо если принят,
        либо если оклонен
    """
    sender = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        """
        Принятие поступившей заявки в друзья
        и обновление списков друзей обоих
        """
        receiver_friends_list = FriendList.objects.get(user=self.receiver)
        if receiver_friends_list:
            receiver_friends_list.add_friend(self.sender)
            sender_friends_list = FriendList.objects.get(user=self.sender)
            if sender_friends_list:
                sender_friends_list.add_friend(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        """
        Отклонение заявки в друзья
        Отклонение происходит за счет установки поля is_active
        в значение False
        """
        self.is_active = False
        self.save()

    def cancel(self):
        """
        Отмена заявки в друзья
        Отмена происходит за счет установки поля is_active
        в значение False
        """
        self.is_active = False
        self.save()

