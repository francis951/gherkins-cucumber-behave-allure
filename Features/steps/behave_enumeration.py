from behave import *
from behave import register_type
from parse_type import TypeBuilder
# -- ENUM: Yields True (for "yes"), False (for "no")
parse_response = TypeBuilder.make_enum({"yes": True, "no": False})
register_type(Response=parse_response)
@when('User asks "{q}"')
def step_question(context, q):
    print("Question is: ")
    print(q)
@then('response is "{a:Response}"')
def step_answer(context, a):
    print("Answer is: ")
    print(a)