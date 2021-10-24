#Author: Saad Ur Rehman
#Self-Checout Algorithm in Python


import sys

class CheckoutMachine:
    #value of coins
    coins = [1, 2, 5, 10, 20, 50, 100, 200] 
    
    #constructor for class
    #sets initial amount
    def __init__(self, amt):
        self._amt = amt

    def getAmount(self):
        return self._amt

    def setAmount(self, amount):
        self._amt = amount

    def getMinCoins(self):
        m = len(self.coins)
        return self.calculateMinCoins(m,self._amt)

    def calculateMinCoins(self, m, V):
        #a table stores the value for number of coins
        coinTable = [0 for i in range(V + 1)] 
    
        # if value is zero
        coinTable[0] = 0
    
        # Assign maximum integer value to all values 
        for i in range(1, V + 1): 
            coinTable[i] = sys.maxsize 
    
        # Calculate minimum number of coins by looping from 1 to value
        for i in range(1, V + 1): 
            
            #loop over entire length of coins array
            for j in range(m):
                # Iterate over all coins lesser than i 
                if (self.coins[j] <= i): 
                    subResult = coinTable[i - self.coins[j]] 
                    if (subResult != sys.maxsize and subResult + 1 < coinTable[i]): 
                        coinTable[i] = subResult + 1
        return coinTable[V]

def main():
    value = int(input("Enter amount for checkout machine: "))
    cMachine1 = CheckoutMachine(value)
    print("Minimum coins required is", cMachine1.getMinCoins())

if __name__ == '__main__':
    main()

'''
------------ Algorithm Complexity--------------
The calculateMinCoins function calculates the minimum number of coins.

In worst case scenarios, the loop inside the function will run V*M times.

    def calculateMinCoins(self, m, V):
        coinTable = [0 for i in range(V + 1)]                                        1
        coinTable[0] = 0                                                             1
        for i in range(1, V + 1):                                                    V
            coinTable[i] = sys.maxsize 

        for i in range(1, V + 1):                                                    V
            for j in range(m):                                                       M
                if (self.coins[j] <= i): 
                    subResult = coinTable[i - self.coins[j]]                         1
                    if (subResult != sys.maxsize and subResult + 1 < coinTable[i]): 
                        coinTable[i] = subResult + 1                                 1
        return coinTable[V]


Complexity: 1 + 1 + V + V*M + 1
            2 + V(1+M) + 1
            V*M + 3
            O(V*M)

The complexity of algorithm is O(m)


'''
