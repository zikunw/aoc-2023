import math
import time

def main():
    part2() 
    #print(totalCardValue("KK677"))
    #print(checkHand_2("77J32"))
    
card = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}

hand_type = {
    "High Card": 0,
    "One Pair": 1,
    "Two Pairs": 2,
    "Three of a Kind": 3,
    "Full House": 4,
    "Four of a Kind": 5,
    "Five of a Kind": 6,
}

def checkCardSize(card1, card2):
    return card[card1] > card[card2]

def totalCardValue(hand):
    i = 100**4
    total = checkHand(hand) * 100**5
    for c in hand:
        total += card[c] * i
        i /= 100
    return total

def checkHand(hand):
    
    offset = (100 ** 5) * 10
    # count the number of each card
    card_count = {}
    for card in hand:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
            
    # check for five of a kind
    if 5 in card_count.values():
        return hand_type["Five of a Kind"] * offset
    
    if 4 in card_count.values():
        return hand_type["Four of a Kind"] * offset
    
    if 3 in card_count.values() and 2 in card_count.values():
        return hand_type["Full House"] * offset
    
    if 3 in card_count.values():
        return hand_type["Three of a Kind"] * offset
    
    if 2 in card_count.values():
        if len(card_count.values()) == 3:
            return hand_type["Two Pairs"] * offset
        else:
            return hand_type["One Pair"] * offset
        
    return hand_type["High Card"] * offset

def part1():
    with open("day7/input.txt", "r") as file:
        lines = file.readlines()
        hands = list(map(lambda x: (list(x[0]), int(x[1])), [n.strip().split() for n in lines]))
        
        print(hands)
        
    hands_values = list(map(lambda x: (checkHand(x[0]) + totalCardValue(x[0]), x[1]), hands))
    
    hands_values.sort(key=lambda x: x[0])
    
    print(hands_values)
    
    s = 0
    i = 1
    for h in hands_values:
        print(h[1], i)
        s += h[1] * i
        i += 1
    print(s)
    
def part2():
    with open("day7/input.txt", "r") as file:
        lines = file.readlines()
        hands = list(map(lambda x: (list(x[0]), int(x[1])), [n.strip().split() for n in lines]))
        
        #print(hands)
        for h in hands:
            print(h[0], hand_type_2_rev[int(checkHand_2(h[0])/(10*100**5))])
        
    hands_values = list(map(lambda x: (checkHand_2(x[0]) + totalCardValue_2(x[0]), x[1]), hands))
    
    hands_values.sort(key=lambda x: x[0])
    
    #print(hands_values)
    
    s = 0
    i = 1
    for h in hands_values:
        #print(h[1], i)
        s += h[1] * i
        i += 1
    print(s)
    
card_2 = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 0,
    "Q": 11,
    "K": 12,
    "A": 13
}

hand_type_2 = {
    "High Card": 0,
    "One Pair": 1,
    "One Pair with J": 1,
    "Two Pairs": 3,
    "Two Pairs with J": 3,
    "Three of a Kind": 5,
    "Three of a Kind with J": 5,
    "Full House": 7,
    "Full House with J": 7,
    "Four of a Kind": 9,
    "Four of a Kind with J": 9,
    "Five of a Kind": 11,
    "Five of a Kind with J": 11,
}

hand_type_2_rev = {
    0: "High Card",
    1: "One Pair",
    2: "One Pair with J",
    3: "Two Pairs",
    4: "Two Pairs with J",
    5: "Three of a Kind",
    6: "Three of a Kind with J",
    7: "Full House",
    8: "Full House with J",
    9: "Four of a Kind",
    10: "Four of a Kind with J",
    11: "Five of a Kind",
    12: "Five of a Kind with J",
}

def totalCardValue_2(hand):
    i = 100**4
    total = 0
    for c in hand:
        total += card_2[c] * i
        i /= 100
    #print(hand, total)
    return total

def checkHand_2(hand):
    offset = (100 ** 5) * 10
    # count the number of each card
    card_count = {}
    for card in hand:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    
    num_jacks = 0
    if "J" in card_count:
        num_jacks = card_count["J"]
        card_count.pop("J")
    
    #print(hand, card_count, num_jacks)  
    
    if num_jacks == 5:
        return hand_type_2["Five of a Kind with J"] * offset
    
    # check for five of a kind
    if 5 in card_count.values():
        return hand_type_2["Five of a Kind"] * offset
    
    if 4 in card_count.values() and num_jacks == 1:
        return hand_type_2["Five of a Kind with J"] * offset
    
    if 3 in card_count.values() and num_jacks == 2:
        return hand_type_2["Five of a Kind with J"] * offset
    
    if 2 in card_count.values() and num_jacks == 3:
        return hand_type_2["Five of a Kind with J"] * offset
    
    if num_jacks == 4:
        return hand_type_2["Five of a Kind with J"] * offset
    
    # 4 of a kind with J
    if 4 in card_count.values():
        return hand_type_2["Four of a Kind"] * offset
    
    if 3 in card_count.values() and num_jacks == 1:
        return hand_type_2["Four of a Kind with J"] * offset
    
    if 2 in card_count.values() and num_jacks == 2:
        return hand_type_2["Four of a Kind with J"] * offset
    
    if num_jacks == 3:
        return hand_type_2["Four of a Kind with J"] * offset
    
    # full house with J
    if 3 in card_count.values() and 2 in card_count.values():
        return hand_type_2["Full House"] * offset
    
    if 3 in card_count.values() and num_jacks == 1:
        return hand_type_2["Full House with J"] * offset
    
    if sum([1 for i in card_count.values() if i == 2]) == 2 and num_jacks == 1:
        return hand_type_2["Full House with J"] * offset
        
    # 3 of a kind with J
    if 3 in card_count.values():
        return hand_type_2["Three of a Kind"] * offset
    if 2 in card_count.values() and num_jacks == 1:
        return hand_type_2["Three of a Kind with J"] * offset
    if num_jacks == 2:
        return hand_type_2["Three of a Kind with J"] * offset
    
    if 2 in card_count.values():
        if len(set(hand)) == 3:
            return hand_type_2["Two Pairs"] * offset
        else:
            return hand_type_2["One Pair"] * offset
        
    if 2 in card_count.values() and num_jacks == 1:
        return hand_type_2["Two Pairs with J"] * offset
    
    if num_jacks == 1:
        return hand_type_2["One Pair with J"] * offset
    
    return hand_type_2["High Card"] * offset

    
main()