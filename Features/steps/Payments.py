from behave import *

@given('user is on credit card payment screen')
def credit_card_pay(context):
    print('User is on credit card payment screen')
@given('user is on debit card payment screen')
def debit_card_pay(context):
    print('user is on debit card payment screen')
@given('user is on cheque payment screen')
def cheque_pay(context):
    print('user is on cheque payment screen')