from django.db import models
from users.models import CustomUser


class Sources(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sum = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class CostCategory(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class IncomeCategory(models.Model):
    name = models.CharField(max_length=255)
    income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class UserIncome(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey(Sources, on_delete=models.CASCADE)
    datatime = models.DateField()

    def __str__(self):
        return self.name


class UserCost(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey(Sources, on_delete=models.CASCADE)
    datatime = models.DateField()

    def __str__(self):
        return self.name


class DepositAccount(models.Model):
    deposit_number = models.CharField(max_length=255, unique=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    percent_deposit = models.PositiveSmallIntegerField()
    bank_name = models.CharField(max_length=255)


class Operation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    deposit_account = models.ForeignKey(DepositAccount, on_delete=models.CASCADE, blank=True)
    Budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True)


class PlannedCost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CostCategory, on_delete=models.CASCADE)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey(Sources, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

