from abc import ABCMeta, abstractmethod                                                                                                                           
from ansible.module_utils.six import with_metaclass                                                                                                               
                                                                                                                                                                  
class basenumbers(with_metaclass(ABCMeta, object)):                                                                                                               
    def __init__(self):                                                                                                                                           
        self.a = 40                                                                                                                                               
                                                                                                                                                                  
    @abstractmethod                                                                                                                                               
    def sum(self, a=None, b=None, c=None, d=3, e=4):                                                                                                              
        pass                                                                                                                                                      
                                                                                                                                                                  
class numbers(basenumbers):                                                                                                                                       
    def __init__(self):                                                                                                                                           
        self.a = 40                                                                                                                                               
        self.b = 50                                                                                                                                               
        self.c = 60                                                                                                                                               
                                                                                                                                                                  
    def sum(self, a=None, b=None, c=None, d=True, e=4):
        print(a)
        print(b)
        print(c)
