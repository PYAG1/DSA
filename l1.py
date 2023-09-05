def lineaer(cards,query):
    position = 0
    while True :
        if cards[position]== query:
            print(position)
        position+=1
        if position == len(cards):
            return -1

    

### linear search is O(N)