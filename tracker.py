import argparse

def get_wallet_portfolio(wallet_address):
    portfolio = {"Ethereum": 1.2, "Bitcoin": 0.05, "Solana": 10}
    return portfolio

def main():
    parser = argparse.ArgumentParser(description="June Crypto Portfolio Tracker")
    parser.add_argument("--wallet", type=str, required=True, help="Your wallet address")
    args = parser.parse_args()

    portfolio = get_wallet_portfolio(args.wallet)
    print(f"Portfolio for {args.wallet}:")
    for coin, amount in portfolio.items():
        print(f"{coin}: {amount}")

if __name__ == "__main__":
    main()