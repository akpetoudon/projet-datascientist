#!/usr/bin/env python
# coding: utf-8

# Objectif
# Créez une classe appelée "Account" qui possède les attributs suivants :
# 
# numéro_compte (chaîne)
# account_balance (flottant)
# account_holder (chaîne)
# La classe doit avoir les méthodes suivantes :
# 
# dépôt(amount: float) - Cette méthode doit ajouter le montant passé en argument au solde du compte.
# retirer (montant : flottant) - Cette méthode doit soustraire le montant passé en argument du solde du compte, mais uniquement si le solde du compte est supérieur au montant retiré.
# check_balance() - Cette méthode doit renvoyer le solde actuel du compte.
# 
# Instructions
# Créez un nouveau fichier appelé "bank_account.py"
# Définissez la classe Compte et ses attributs comme spécifié ci-dessus.
# Définissez la méthode de dépôt(). Il devrait prendre en un seul argument, le montant à déposer, et l'ajouter au solde du compte.
# Définissez la méthode retrait(). Il devrait prendre en un seul argument, le montant à retirer, et le soustraire du solde du compte. La méthode ne doit exécuter le retrait que si le solde du compte est supérieur ou égal au montant à retirer.
# Définissez la méthode check_balance(). Il devrait retourner le solde du compte courant.
# Créez une instance de la classe Account et affectez-la à une variable appelée "my_account".
# Utilisez les méthodes de la classe pour déposer et retirer de l'argent du compte et vérifier le solde du compte.
# Testez le programme en créant plusieurs instances de la classe et en effectuant différentes transactions sur celles-ci.

# In[1]:


import re
import sys


# In[2]:


class Account:
    def __init__(self,name, account_number, balance,showBalanceAfterTransaction=True):
        self.name = account_holder
        self.account_number = account_number
        self.balance = balance
        self.startingBalance = balance
        self.showBalanceAfterTransaction = showBalanceAfterTransaction
        self.transactions = []
        
        
    def getName(self):
        return self.name


# Définissez la méthode de dépôt(). Il devrait prendre en un seul argument, le montant à déposer, et l'ajouter au solde du compte.

# In[3]:


def deposit(self, amount):
        print('%s: deposit $%0.2f.' % (self.name, amount))
        self.balance = float('%.2f' % (self.balance + amount))  # prevent accumulation error
        self.transactions.append(['d', amount])
        if self.showBalanceAfterTransaction:
            self.showBalance()


# Définissez la méthode retrait(). Il devrait prendre en un seul argument, le montant à retirer, et le soustraire du solde du compte. La méthode ne doit exécuter le retrait que si le solde du compte est supérieur ou égal au montant à retirer.

# In[4]:


def withdrawal(self, amount):
       if amount > self.balance:
           print("Sorry, you don't have that much!")
       else:
           print('%s: withdraw $%0.2f.' % (self.name, amount))
           self.balance = float('%.2f' % (self.balance - amount))  # prevent accumulation error
           self.transactions.append(['w', amount])
           if self.showBalanceAfterTransaction:
               self.showBalance()


# Définissez la méthode check_balance(). Il devrait retourner le solde du compte courant.

# In[7]:


def getBalance(self):
       return self.balance

def showBalance(self):
       print('%s: balance is $%0.2f.' % (self.name, self.balance))
       print()
       
def showTransactions(self):
       balance = self.startingBalance
       print('   op       amount     balance')
       print('--------  ----------  ----------')
       print('                      %10.2f  (starting)' % balance)
       for transaction in self.transactions:
           [op, amount] = transaction
           if op == 'w':
               opLabel = 'withdraw'
               balance -= amount
           else:
               opLabel = 'deposit'
               balance += amount
           print('%-8s  %10.2f  %10.2f' % (opLabel, amount, balance))
       print()


# Créez une instance de la classe Account et affectez-la à une variable appelée "my_account".

# In[ ]:


class Account:
   def __init__(self):
       self.name = my_account


# Utilisez les méthodes de la classe pour déposer et retirer de l'argent du compte et vérifier le solde du compte.

# In[ ]:


class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)


# Testez le programme en créant plusieurs instances de la classe et en effectuant différentes transactions sur celles-ci.

# In[ ]:


class Input:
    def getOperation(self):
        op = input('Enter d for deposit, w for withdrawal, t for transactions, or q to quit: ')
        if op not in set('qdwt'):
            print('Invalid operation.  Please try again.')
            op = None
        return op

    def validateDollarAmount(self, amountStr):
        tooMuchPrecision = re.compile('.*\.\d\d\d.*')
        if tooMuchPrecision.match(str(amountStr)):
            raise Exception('You cannot supply fractions of a cent.')

    def getAmount(self):
        amount = None
        try:
            value = input('Enter amount: ')
            amount = float(value)
            if amount <= 0:
                raise Exception('The amount must be positive.')
            self.validateDollarAmount(value)
        except ValueError:
            print('Invalid amount.  Please try again.')
        except Exception as e:
            print(e)
            amount = None

        return amount

class Test:
    def __init__(self):
        self.numTests = 0
        self.numPass = 0

    def testBalance(self, account, expected):
        self.numTests += 1
        actual = account.getBalance()
        name = account.getName()
        if actual == expected:
            self.numPass += 1
            print('%s: OK      balance = %.2f' % (name, actual))
        else:
            print('%s: ERROR   balance = %.2f, but expected %.2f' % (name, actual, expected))

    def summarizeResults(self):
        numFailed = self.numTests - self.numPass
        print()
        print('%d tests total' % self.numTests)
        if numFailed == 0:
            print('all passed')
        else:
            print('%d passed' % self.numPass)
            print('%d failed' % numFailed)
        return numFailed == 0

    def run(self):
        a1 = Account('a1', 0, False)
        self.testBalance(a1, 0)

        a2 = Account('a2', 100, False)
        self.testBalance(a2, 100)

        a1.deposit(10)
        a1.deposit(10)
        a1.deposit(10)
        a1.withdrawal(5)
        self.testBalance(a1, 25.0)

        a2.withdrawal(25)
        a2.withdrawal(15)
        a2.withdrawal(0.50)
        a2.deposit(15)
        self.testBalance(a2, 74.5)

        a1.withdrawal(3.25)
        a1.deposit(4)
        self.testBalance(a1, 25.75)

        a2.deposit(1.30)
        a2.withdrawal(11.29)
        self.testBalance(a2, 64.51)

        allPassed = self.summarizeResults()
        return allPassed
    
class App:
    defaultBalance = 0.0

    def usage(self):
        print('usage: %s [-t|amount]' % sys.argv[0])
        print('where -t means to run test')
        print('and amount is a starting balance dollar amount')

    def parseAndValidateBalance(self, value):
        try:
            balance = float(value)
            if balance < 0:
                raise Exception('The balance cannot be negative.')
            Input().validateDollarAmount(value)
        except ValueError:
            raise Exception('Invalid starting balance. Try something like 17.25 or 0 (the default).')
        return balance

    def getArgs(self):
        isTestFlag = False
        balance = App.defaultBalance

        if len(sys.argv) > 2:
            raise Exception('Unrecognized arguments.')
        elif len(sys.argv) == 2:
            value = sys.argv[1]
            if value == '-t':
                isTestFlag = True
            else:
                balance = self.parseAndValidateBalance(value)

        return (isTestFlag, balance)

    def processUserInputs(self, balance):
        print('Welcome to the bank.')
        account = Account('MySavings', balance)
        account.showBalance()
        account.processTransactions()

    def run(self):
        try:
            (isTestFlag, balance) = self.getArgs()
        except Exception as e:
            print(e)
            self.usage()
            sys.exit(1)

        if not isTestFlag:
            self.processUserInputs(balance)
        elif not Test().run():
            sys.exit(1)


def main():
    App().run()
    sys.exit(0)

main()

