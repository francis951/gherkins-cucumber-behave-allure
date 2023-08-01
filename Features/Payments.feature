@high
Feature: Payment Process

@creditpayment @payment
Scenario: Credit card Transaction
Given User is on credit card payment screen

@debitpayment @payment
Scenario: Debit card Transaction
Given User is on debit card payment screen

Scenario: Cheque Transaction
Given User is on Cheque payment screen