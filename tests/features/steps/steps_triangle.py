from behave import *
# import explicit
from behave import given, when, then

@given(u'I am testing the input string parser')
def step(context):
    a = 10

@when(u'I pass in the string {text}')
def step(context, text): #@DuplicatedSignature
    response = triangle.parse_input(text)

@then(u'I should get {text}')
def step(context,text):     #@DuplicatedSignature
    raise NotImplementedError(u'STEP: Then I should get error')
KeyboardInterrupt