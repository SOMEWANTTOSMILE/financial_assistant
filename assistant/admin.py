from django.contrib import admin
from assistant.models import (Operation, IncomeCategory, UserIncome,
                              CostCategory, UserCost, DepositAccount,
                              Sources, PlannedCost)


admin.site.register(Operation)
admin.site.register(IncomeCategory)
admin.site.register(UserIncome)
admin.site.register(CostCategory)
admin.site.register(UserCost)
admin.site.register(DepositAccount)
admin.site.register(Sources)
admin.site.register(PlannedCost)
