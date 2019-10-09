#!/usr/bin/python

import argparse

def find_max_profit(prices):
  el = 0

  # Profit of the first iteration
  max_profit = prices[1] - prices[0]
  cur_profit = prices[1] - prices[0]
  
  # Loop through the whole price list and end loop when we reach the end
  while el < len(prices):
    
    # Compare current price to current price + subsequent prices
    for price in prices[el+1:]:
      if price - prices[el] > cur_profit:

        # Save current profit for that iteration
        cur_profit = price - prices[el]
        
    # If current price is greater than max profit then save to max profit
    if cur_profit > max_profit:
      max_profit = cur_profit
     
    # Increment to next element of prices and compare the subsequent prices
    el += 1
    
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))