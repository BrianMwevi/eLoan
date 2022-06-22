from django.db import models
from accounts.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class CustomerAccount(models.Model):
    account_holder = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='user_account')
    account_number = models.PositiveBigIntegerField(default=0, unique=True)
    balance = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_holder.username


@receiver(post_save, sender=User)
def generate_account_number(sender, instance, created, **kwargs):
    if created:
        import random
        import string
        account_number = "".join(random.choice(string.digits)
                                 for _ in range(0, 12))
        instance.account_number = int(account_number)
        instance.save()


class Debtor(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='debtor')
    account = models.ForeignKey(
        CustomerAccount, on_delete=models.CASCADE, related_name="account")
    loans = models.ManyToManyField('Loan', blank=True)
    paid_amount = models.FloatField(default=0, blank=True, null=True)
    date_created = models.DateField(
        auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.account_number}"


# @receiver(post_save, sender=Debtor)
# def create_account(self, instance, created, **kwargs):
#     if created:
#         import random
#         account_number = random.randint(0, 100)
#         account = Account.objects.create(
#             account_holder=instance.user, account_number=account_number)


# @receiver(post_save, sender=Creditor)
# def create_account(self, instance, created, **kwargs):
#     if created:
#         import random
#         account_number = random.randint(0, 100)
#         account = Account.objects.create(
#             account_holder=instance.user, account_number=account_number)


class Creditor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(
        CustomerAccount, on_delete=models.CASCADE, related_name="creditor_account")
    debtors = models.ManyToManyField(
        'Debtor')
    loans = models.ManyToManyField('Loan', blank=True)
    credit_given = models.FloatField(default=0, blank=True, null=True)
    credit_paid = models.FloatField(default=0, blank=True, null=True)
    date_created = models.DateField(
        auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.account_number}"


class Loan(models.Model):
    borrower = models.ForeignKey(
     User, on_delete=models.CASCADE, related_name='borrower')
    lender = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='lender')
    amount = models.FloatField(default=0)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    approved_date = models.DateField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.lender.username.title()} TO {self.borrower.username.title()} "


# @receiver(post_save, sender=Loan)
# def broadcast_loan(sender, instance, created, **kwargs):
#     if created:
#       creditors = Creditor.objects.all()
#       for creditor in creditors:
#         creditor.

        # class Transaction(models.Model):
        #     sender = models.ForeignKey(
        #         User, on_delete=models.CASCADE)
        #     receiver = models.ForeignKey(
        #         User, on_delete=models.CASCADE)
        #     amount = models.PositiveIntegerField(default=0)
        #     payment_date = models.DateField(auto_now_add=True)
        #     status = models.BooleanField(default=False)

        #     @classmethod
        #     def transact(cls, sender, receiver, amount):
        #         sender_account = Account.objects.get(account_holder=sender)
        #         receiver_account = Account.objects.get(account_holder=receiver)
        #         sender_account.balance -= amount
        #         receiver_account.balance += amount
        #         sender_account.save()
        #         receiver_account.save()
        #         cls.status = True
        #         cls.save()
        #         return [sender_account, receiver_account]

        #     def _str_(self):
        #         return f"{self.sender.username} TO {self.receiver.username}"
