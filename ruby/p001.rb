#!/usr/bin/env ruby
=begin
Author - Tarek Allam.

Multiples of 3 and 5

Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
=end

list = 1...1000

puts [*list]

holding_list = []

for i in list
    if i % 3 == 0 || i % 5 == 0
        holding_list << i
    end
end

puts holding_list.inject{|sum,x| sum + x }
