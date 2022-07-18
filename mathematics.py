from problem import Problem
import random
import operator
from math import floor

class Mathematics():
  def __init__(self, difficulty):
    self.answer = ""
    self._var_1 = 0
    self._var_2 = 0
    self._operator = ""
    self._operators = ""
    self.math_problem = ""
    self._difficulty = difficulty 

  def math_setup(self):
    self._setup_difficulty()
    self._set_random_operator()
    self._set_random_vars()
    self._find_solution()
    self._create_problem()
    
  def get_vars(self):
    """returns the values of the math variables"""
    return self._var_1, self._var_2
  
  def _set_random_operator(self):
    """randomly selects the math operator"""
    self._operator = random.choice(list(self._operators.keys()))
  
  def _set_random_vars(self):
    """randomly selects the math variables. If the difficulty is hard then the
      subtraction and division operation will have a chance of getting larger random variables"""
    if self._difficulty == "hard" and self._operator != "*" and self._operator != "+":
      self._var_1 = random.randint(1, 20)
      self._var_2 = random.randint(1, 20)
    else:
      self._var_1 = random.randint(1, 10)
      self._var_2 = random.randint(1, 10)


  def _find_solution(self):
    """finds the solution to the math problem randomly generated"""
    self.answer = self._operators.get(self._operator)(self._var_1, self._var_2)
    if self._operator == "/":
      if self.answer - floor(self.answer) != 0:
        self._make_answer_valid()
    self.answer = int(self.answer)

  def _make_answer_valid(self):
    """makes sure the solution to division is a whole number
      makes sure there are no negative numbers on easy difficulty"""
    self._set_random_vars()
    self._find_solution()

  def _create_problem(self):
    """creates the math problem as a stringS"""
    # self.problem = str(self._var_1) + " " + self._operator + " " + str(self._var_2)
    problem_list = [self._var_1, self._operator, self._var_2]
    for i in problem_list:
      self.math_problem += str(i)

  def get_problem(self):
    return self.math_problem


  def _setup_difficulty(self):
    """Sets the possible operatos based on the difficuly chosen.
      Easy: Additon and subtraction
      Medium: Addition, subtraction and negative numbers
      Hard: Addition, subtraction, multiplication and division"""
    if self._difficulty == "easy":
      self._operators = {
        '+': operator.add,
        '-': operator.sub
      }
    elif self._difficulty == "medium":
      self._operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
      }
    
    elif self._difficulty == "hard":
      self._operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
      }
  

  def get_answer(self):
    """Returns the solution to class problem"""
    return str(self.answer)
