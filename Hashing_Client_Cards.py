import random


random.seed(1019336)
a = 41
N = 10007    # Prime closest to 2n where n = 5000 clients


def hashFunction(client):
    H = 0
    length = len(client)
    for k in range(length):
        H += ord(client[k]) * (a**(length - (k+1)))
    return H % N


class Client:
    def __init__(self, cardNum, amount):
        self.moneySpent = amount
        self.cardNum = cardNum

    def add(self, amount):
        self.moneySpent += amount


if __name__ == "__main__":

    # List Initialization with 0
    # hashTable and totalExpenses are to be kept "parallel"
    hashTable = []

    for i in range(N):
        hashTable.append(-1)
    cards = []

    # Calculate the first 13 pre-determined digits
    r = random.choice([(48, 57), (65, 90)])
    setChars = chr((random.randint(*r)))

    for i in range(12):
        r = random.choice([(48, 57), (65, 90)])
        setChars += chr((random.randint(*r)))

    # Generation of Client Cards / Not to be used for search only for reference
    for i in range(5000):
        cards.append(setChars)
        for _ in range(3):
            r = random.choice([(48, 57), (65, 90)])
            cards[i] += (chr((random.randint(*r))))

    # Random visits
    collisions = 0
    for i in xrange(1000):
        tempCollisionCounter = 0
        x = random.randint(0, 4999)  # Select random client that visits the store
        amount = random.randint(1, 12000)/100.0  # Amount of money spent on the visit

        hashVal = hashFunction(cards[x])
        if hashTable[hashVal] == -1:
            hashTable[hashVal] = Client(cards[x], amount)
        else:
            if hashTable[hashVal].cardNum == cards[x]:
                hashTable[hashVal].add(amount)
            else:
                for j in range(hashVal, N):
                    tempCollisionCounter += 1
                    collisions += 1

                    if hashTable[j] == -1:
                        hashTable[j] = Client(cards[x], amount)
                        break

                    elif hashTable[j].cardNum == cards[x]:
                        hashTable[j].add(amount)
                        collisions -= tempCollisionCounter  # We don't factor in the search collisions
                        break

    print "\n\nNumber of collisions while creating hashTable = " + str(collisions)
    print "Number a used in hashFunction is a = " + str(a)
    maxAmount = 0

    for i in range(N):
        if hashTable[i] == -1:
            continue
        if hashTable[i].moneySpent > maxAmount:
            maxAmount = hashTable[i].moneySpent
            CardNo = hashTable[i].cardNum

    print '\nClient with largest sum spent: ' + CardNo
    print 'The maximum amount spent is = ' + str(maxAmount)

