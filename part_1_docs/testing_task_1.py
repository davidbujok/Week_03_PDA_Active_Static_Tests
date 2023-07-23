class CardGame: # Missing parentheses


  def check_for_ace(self, card):
    if card.value = 1: # assign operator, but it should be == equality 
      return True
    else # missing colon at the end of else
      return False
   

  dif highest_card(self, card1 card2): # incorrect function declaration, starts with word dif, the key word should be def
  if card1.value > card2.value:
    return card # the variable card doesn't exist, it's either card1 or card2
  else:
    return card2
  


def cards_total(self, cards): # incorrect indentation, key word self suggest it's part of the class, hence it needs to be indented 
  total # variable without assigning statement, it's just a random word
  for card in cards:
    total += card.value
    return "You have a total of" + total # return statement in for loop will not count the values as it will always reset to the last value and string + integer concatenation won't work 