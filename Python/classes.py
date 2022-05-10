class Bank:
	def __init__(self, balance):
		self.moneyBalance = balance
	def withdrawMoney(self, amount):
		self.moneyAmount = int(amount)
		if self.checkBalance(amount):
			self.moneyBalance = int(self.moneyBalance - self.moneyAmount)
			return True
		else:
			return False
	def checkBalance(self, balanceAmount):
		if int(balanceAmount) <= self.moneyBalance:
			return True
		else:
			return False


Garanti = Bank(10)

peopleList = {"Berkay": "11", "Kübra": "2", "Jack": "7"}
keys = list(peopleList.keys())
i = 0
for person in peopleList:
	if Garanti.withdrawMoney(peopleList[person]):
		print(f"{keys[i]} is withdrawed {peopleList[person]} dollar, current balance is {Garanti.moneyBalance}")
		i = i + 1
	else:
		print(f"{keys[i]} cannot withdraw {peopleList[person]} dollar, current balance is {Garanti.moneyBalance}")
		i = i + 1
