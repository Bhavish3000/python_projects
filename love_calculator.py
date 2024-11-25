def calculate_love_score(name1, name2):
    compare1 = "TRUE"
    compare2 = "LOVE"
    true_count = 0
    love_count = 0
    combained_names = (name1+name2).upper()
    for letter in combained_names:
        if letter in compare1:
            true_count += 1
        if letter in compare2:
            love_count += 1
    love_score = int(str(true_count) + str(love_count))
    print(f"Love_score= {love_score}")
    
calculate_love_score(name1="priya", name2="bhavish")