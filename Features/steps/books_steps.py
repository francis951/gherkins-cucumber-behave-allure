from behave import *

@given(u"Book details")
def book_impl(context):
    print('Book details entered')
    
@then(u"Varify book name")
def book_impl(context):
    print('Varify the book name')
    
    
@given('user enters "{name}" and "{password}"')
def step_implpy(context, name, password):
    print("Username for login: {}".format(name))
    print("Password for login: {}".format(password))
@then('user should be logged in')
def step_implpy(context):
      pass