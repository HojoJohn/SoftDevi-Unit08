def make_card(rank,suit):
    rn = rank
    if rank ==1:
        r = "Jack"
    elif rank == 12:
        r = "Queen"
    elif rank ==13:
        r = "King"
    elif rank == 14:
        r = "Ace"
    tuple = (rank,suit,str(rn)+'of'+suit)
    return tuple