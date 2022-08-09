# You can find information on how to convert numbers to a different base here:
# https://www.tutorialspoint.com/computer_logical_organization/number_system_conversion.htm

# You can find information on how to convert numbers to roman numerals here:
# https://www.romannumerals.org/converter


def binarify(num): 
  """convert positive integer to base 2"""
  digits = []
  if num <= 0: 
      return '0'
  else:
      while num > 0 :
          digits.append(str(num % 2))
          num = num // 2
  return ''.join(digits[::-1])

#test
binarify(29)

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  digits = []
  if num <= 0:  
      return '0' 
  else: 
      while num > 0:
          digits.append(str(num % base))
          num = num // base 
  return ''.join(digits[::-1])

#test
int_to_base(29, 2)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""  
  if string == '0' or base <= 0 : return 0 
  result = sum([int(x)*(base**i) for i, x in zip(reversed(range(0,len(string))), string)])
  return result 

#test
base_to_int('11101', 2)

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  if str1 == '0' or base1 <= 0 : return 0 
  result1 = sum([int(x)*(base1**i) for i, x in zip(reversed(range(0,len(str1))), str1)])
  if str2 == '0' or base2 <= 0 : return 0 
  result2 = sum([int(x)*(base2**i) for i, x in zip(reversed(range(0,len(str2))), str2)])
  result = result1 + result2
  return result 

#test
flexibase_add('11101', '11101', 2, 2)

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  if str1 == '0' or base1 <= 0 : return 0 
  result1 = sum([int(x)*(base1**i) for i, x in zip(reversed(range(0,len(str1))), str1)])
  if str2 == '0' or base2 <= 0 : return 0 
  result2 = sum([int(x)*(base2**i) for i, x in zip(reversed(range(0,len(str2))), str2)])
  result = result1 * result2
  return result 

#test
flexibase_multiply('11101', '11101', 2, 2)

def romanify(num):
  """given an integer, return the Roman numeral version"""
  roman_numerals = [
      (1000, 'M'),
      (900, 'CM'),
      (500, 'D'),
      (400, 'CD'),
      (100, 'C'),
      (90, ''),
      (50, ),
      (40, ),
      (10, ''),
      (5, ''),
      (1, ''),
      ]
  result = ""
  return resuls


# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.