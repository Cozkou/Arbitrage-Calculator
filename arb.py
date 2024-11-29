def arbitrage_calculator(odds_a, odds_b, stake):
    """
    Calculate potential outcomes based on two betting odds.
    :param odds_a: Odds for option A (lower odds)
    :param odds_b: Odds for option B (higher odds)
    :param stake: Total amount to bet
    :return: A dictionary with potential outcomes
    """
    if odds_a < odds_b:
        lower_odds = odds_a
        higher_odds = odds_b
    else:
        lower_odds = odds_b
        higher_odds = odds_a

    # Calculate the stakes
    stake_b = stake / higher_odds
    stake_a = stake - stake_b

    # Calculate potential outcomes
    outcome_a = stake_a * lower_odds
    outcome_b = stake_b * higher_odds

    results = {
        "Stake A": stake_a,
        "Stake B": stake_b,
        "Outcome if A wins": outcome_a,
        "Outcome if B wins": outcome_b,
        "Profit if A wins": outcome_a - stake,
        "Profit if B wins": 0  # Break even for higher odds
    }
    return results


def main():
    print("Arbitrage Betting Calculator")
    odds_a = float(input("Enter the lower odds: "))
    odds_b = float(input("Enter the higher odds: "))
    stake = float(input("Enter the total stake: "))

    results = arbitrage_calculator(odds_a, odds_b, stake)

    print("\n--- Betting Summary ---")
    print(f"Stake on option A: £{results['Stake A']:.2f}")
    print(f"Stake on option B: £{results['Stake B']:.2f}")
    print(f"Potential outcome if option A wins: £{results['Outcome if A wins']:.2f}")
    print(f"Potential outcome if option B wins: £{results['Outcome if B wins']:.2f}")
    print(f"Profit if option A wins: £{results['Profit if A wins']:.2f}")
    print(f"Profit if option B wins: £{results['Profit if B wins']:.2f}")


if __name__ == "__main__":
    main()