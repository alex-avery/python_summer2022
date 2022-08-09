# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:31:14 2020

@author: rzava
"""


# You can find information on how to convert numbers to a different base here:
# https://www.tutorialspoint.com/computer_logical_organization/number_system_conversion.htm

# You can find information on how to convert numbers to roman numerals here:
# https://www.romannumerals.org/converter


def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  while num != 0:
      digits.append(num%2)
      num = num // 2
  digits = [str(i) for i in digits[::-1]]
  return ''.join(digits)

binarify(29)

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0: return '0'
  digits = []
  while num != 0:
      digits.append(num % base)
      num = num // base
  digits = [str(i) for i in digits]
  return ''.join(digits)


def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  result = 0 
  string = [int(i) for i in string]
  n = len(string)
  print(string)
  for i in range(0, n):
      result += string[i] * base ** (n - i - 1)
  return result 

base_to_int("11101", 2)

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  num_one = base_to_int(str1, base1)
  num_two = base_to_int(str2, base2)
  result = num_one + num_two
  return result 

flexibase_add("11101", "11101", 2, 2)

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  num_one = base_to_int(str1, base1)
  num_two = base_to_int(str2, base2)
  result = num_one * num_two
  return result 

flexibase_multiply("11101", "11101", 2, 2)

def romanify(num):
  """given an integer, return the Roman numeral version"""
  we_r_romans = {1 : 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
                 40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
                 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
  rom_num = []
  #make i into an integer before operating
  for i in list(we_r_romans.keys())[::-1]:
    while num >= i:
        rom_num.append(i)
        num = num - i
  result = [we_r_romans[i] for i in rom_num]
  return ''.join(result)

romanify(1459)

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