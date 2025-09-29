from src.tracker import get_wallet_portfolio

def test_portfolio():
    wallet = "0xTestWallet"
    portfolio = get_wallet_portfolio(wallet)
    assert "Ethereum" in portfolio
    assert "Bitcoin" in portfolio