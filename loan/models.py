from django.db import models
from accounts.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class CustomerAccount(models.Model):
    account_holder = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='user_account')
    account_number = models.PositiveBigIntegerField(default=0, unique=True)
    balance = models.PositiveIntegerField(default=0)
    creditors = models.ManyToManyField(User, related_name="creditors")
    debtors = models.ManyToManyField(User, related_name="debtors")
    updated_at = models.DateTimeField(auto_now=True)

    def generate_account_number():
        import random
        import string
        account_number = "".join(random.choice(string.digits)
                                 for _ in range(0, 12))
        return account_number

    def __str__(self):
        return f"{self.account_holder.username.title()}"


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        account_number = CustomerAccount.generate_account_number()
        try:
            account = CustomerAccount.objects.get(
                account_number=account_number)
            create_account(sender, instance, created, **kwargs)
        except CustomerAccount.DoesNotExist:
            account = CustomerAccount.objects.create(
                account_holder=instance, account_number=account_number)
            create_profile(instance, account)


def create_profile(instance, account):
    if instance.is_lender:
        creditor = Creditor.objects.create(user=instance, account=account, )
    else:
        debtor = Debtor.objects.create(user=instance, account=account, )


class Debtor(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='debtor')
    account = models.ForeignKey(
        CustomerAccount, on_delete=models.CASCADE, related_name="account")
    loans = models.ManyToManyField('Loan', blank=True)
    paid_amount = models.FloatField(default=0)
    due_amount = models.FloatField(default=0)
    date_created = models.DateField(
        auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.account.account_number}"


class Creditor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(
        CustomerAccount, on_delete=models.CASCADE, related_name="creditor_account")
    loans = models.ManyToManyField('Loan', blank=True)
    credit_given = models.FloatField(default=0)
    credit_paid = models.FloatField(default=0)
    date_created = models.DateField(
        auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.account.account_number}"


class Loan(models.Model):
    borrower = models.ForeignKey(
     User, on_delete=models.CASCADE, related_name='borrower', null=True)
    lender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lender', blank=True, null=True)
    amount = models.FloatField(default=0)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)
    approved = models.BooleanField(default=False)
    approved_date = models.DateField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.borrower.username.title()} : Ksh{self.amount} "


class Transaction(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver')
    amount = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username.title()} TO {self.receiver.username.title()}: Ksh {self.amount}"


@receiver(post_save, sender=Transaction)
def transact(sender, instance, created, **kwargs):
    if created:

        sender_account = CustomerAccount.objects.get(
            account_holder=instance.sender)
        receiver_account = CustomerAccount.objects.get(
            account_holder=instance.receiver)
        if sender_account.balance <= instance.amount:
            raise ValueError(
                f"You've inssufficient balance. Balance is Ksh {sender_account.balance}")
        else:
            sender_account.balance -= instance.amount
            receiver_account.balance += instance.amount
            sender_account.debtors.add(instance.receiver)
            receiver_account.creditors.add(instance.sender)
            sender_account.save()
            receiver_account.save()
            instance.completed = True
            instance.save()
