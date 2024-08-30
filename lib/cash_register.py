#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
      self.discount = discount
      #instance variable
      self.total = 0
      self.items = []
      self.last_item = None
      
  pass
  def add_item(self, title, price,quantity=1):
    self.total +=price * quantity
    # self.items.append((title, price, quantity)) <== was for tracking then it gave me problems so I used number 17
    #.extend allows multiple items to be seen('egs', 'eggs')
    self.items.extend([title] * quantity)
    # this is for tracking the last item in the array of items
    self.last_item = (title, price, quantity) 
  
  def apply_discount(self):
    if self.discount > 0:
      discount_amount = (self.discount / 100) * self.total
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${self.total:.0f}.")
      # the :.0f at the end. I used it to prevent floats and decimals....I'm sure there is another way i.e using int method
    else:
      print("There is no discount to apply.")
    return self.items
  
  def void_last_transaction(self):
      if self.last_item:
        # this is for collecting data 
        title, price, quantity = self.last_item
        self.total -= price * quantity
        self.items.pop()  # Remove the last item from the list
        self.last_item = None  # Reset the last item tracker
      else:
        return "No transaction to void."