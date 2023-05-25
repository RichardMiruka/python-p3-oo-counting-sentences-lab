#!/usr/bin/env python3
import re 
class MyString:
  def __init__(self,value = None):
      self.value = value
  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, new_value):
    if new_value is not None and not isinstance(new_value, str):
            print("The value must be a string.")
    else:
            self._value = new_value
   
  def is_sentence(self):
        if self._value is not None and self._value.endswith('.'):
            return True
        return False         
        
  def is_question(self):
        if self._value is not None and self._value.endswith('?'):
            return True
        return False
      
  def is_exclamation(self):
        if self._value is not None and self._value.endswith('!'):
            return True
        return False
  
  def count_sentences(self):
      if not self.value:
        return 0
      sentences = [sentence for sentence in re.split(r'[.!?]', self.value) if sentence]
      return len(sentences)
    
