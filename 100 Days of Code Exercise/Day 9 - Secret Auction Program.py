# Create a Secret Auction Program
class SecretAuction:
    """Create a secret auction"""

    def __init__(self):
        self.bids = {}
        self.auction()

    def auction(self):
        name = input("What is your name? \n")
        price = float(input("What is your bid amount? $ \n"))
        self.bids[name] = price
        continue_bid = input("To continue bid type 'yes' else type 'no' \n")
        if continue_bid == "yes":
            self.auction()
        elif continue_bid == "no":
            self.highest_bid()

    def highest_bid(self):
        # max(self.bids.items(), key=operator.itemgetter(1))[0] import operator
        max_bid = 0
        max_bidder = []
        for b in self.bids:
            if self.bids[b] > max_bid:
                max_bid = self.bids[b]

        for n, b in self.bids.items():
            if b == max_bid:
                max_bidder.append(n)
        if len(max_bidder) == 1:
            print("Winner is {} with a bid of ${}".format(max_bidder[0], max_bid))
        else:
            print(
                "There is a tie between bidders {} with a bid of ${}".format(
                    ", ".join(max_bidder), max_bid
                )
            )


if __name__ == "__main__":
    SecretAuction()
