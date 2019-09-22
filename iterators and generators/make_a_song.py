def make_song(num = 99, drink = 'soda'):
    while num >= 0:
        if num == 0:
            yield f"No more {drink}!"
            break
        elif num == 1:
            yield f"Only 1 bottle of {drink}"
            num -= 1
        else:
            yield f"{num} bottles of {drink} on the wall."
            num -= 1



# kombucha_song = make_song(5, "kombucha")
# print(next(kombucha_song)) # '5 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # '4 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # '3 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
# print(next(kombucha_song)) # 'Only 1 bottle of kombucha left!'
# print(next(kombucha_song)) # 'No more kombucha!'
# print(next(kombucha_song)) # StopIteration

default_song = make_song()
print(next(default_song)) # '99 bottles of soda on the w