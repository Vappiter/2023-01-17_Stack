str_test1 = '((())'

class Stack:
    def __init__(self, str_test:str):
      self.staples = []
      self.st_test = str_test
      
    def is_empty(self):
      if self.size_stack() == 0:
       return True
      else:
       return False
   
    def push_stack(self, plus: str):
      self.staples.append (plus)   
      
    def pop_stack (self):
      var_size = self.size_stack() - 1
      return self.staples.pop(var_size)
    
    def peek_stack(self):
      var1 = self.size_stack()
      return self.staples(var1)    
  
    def size_stack(self):
      return len(self.staples)  
    
    def result (self):
        
      for var1 in self.st_test:
        if var1 in ['(', '{', '[']:
         test1.push_stack(var1)   
        else:
           if test1.is_empty() and var1 in [')', '}', ']']:
            return print ('Несбалансированная последовательность скобок - 2')   
           current_char  = test1.pop_stack()
           if current_char == '(':
            if var1 != ')':
             return print ('Несбалансированная последовательность скобок')
           if current_char == '{':
            if var1 != '}':
             return print ('Несбалансированная последовательность скобок')        
           if current_char == '[':
            if var1 != ']':
             return print ('Несбалансированная последовательность скобок')
      if len(self.st_test) == 0:
       return print ('Введена пустая строка')      
      if not test1.is_empty():
       return print ('Несбалансированная последовательность скобок')            
      return print ('Сбалансированная последовательность скобок !!!')

if __name__ == '__main__':
    
 test1 = Stack(str_test1)
 test1.result()
    