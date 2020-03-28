from coinbase.wallet.client import Client
from coinbase.wallet.error import APIError
import uuid

client = Client('key', 'secret')

address_map = {
	'coinbase account id': 'address to send to'
}

def send(acct):
	try:
		# get current USD exchange rate for the currency
		rate = client.get_exchange_rates(currency=acct.balance.currency).rates.USD
		# only send 95% of full amount, leave a bit in wallet (optional)
		send_amount = float(acct.balance.amount) * .95;
		# only send if amount is more than $10
		if ( send_amount * float(rate) ) > 10.00:
			print("sending %s %s, total balance = %s"%(send_amount, acct.balance.currency, acct.balance.amount))

			# send request, use address_map to find the crypto address to send to 
			response = client.send_money(acct.id, to=address_map[acct.id],
				amount=round(send_amount, 8),
				currency=acct.balance.currency,
				description='automated send via coinbase-sender',
				idem='coinbase_sender_' + str(uuid.uuid4()))

			print(response)

	except APIError as err:
		print(err)

def main():
	accounts = client.get_accounts()
	# only get accounts with positive crypto balances
	accounts_with_balances = [acct for acct in accounts.data if float(acct.balance.amount) > 0]

	for acct in accounts_with_balances:
		if acct.id in address_map:
			send(acct)

main()