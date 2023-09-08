#!/usr/bin/env python

# Greedy algorithm for coin change problem

import click


def greedy_coin(amount):
    """
    Greedy algorithm for coin change problem
    """
    print(f"Your change for {amount} is:")
    coins = [0.25, 0.10, 0.05, 0.01]
    coin_lookup = {0.25: "quarter", 0.10: "dime", 0.05: "nickel", 0.01: "penny"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            amount = round(
                amount, 2
            )  # to avoid floating point errors. e.g. 0.01 + 0.01 + 0.01 = 0.030000000000000002
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict


@click.command()
@click.argument("amount", type=float)
def main(amount):
    """
    Return the change for a given amount using the least amount of coins

    Args:\n
        amount (float): Amount of change to return

    Returns:\n
        dict: Dictionary of coins and their counts

    Examples:\n
        $ ./greedy_coin.py 0.67\n
        Your change for 0.67 is:\n
        2 quarter\n
        1 dime\n
        1 nickel\n
        2 penny\n
    """
    greedy_coin(amount)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
