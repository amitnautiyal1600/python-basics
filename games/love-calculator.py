def calculate_love_score(name1, name2) :
    first_word = "TRUE"
    first_digit = 0
    second_word = "LOVE"
    second_digit = 0
    for c in name1 :
        if c.lower() in first_word.lower() :
            first_digit +=1

        if c.lower() in second_word.lower() :
            second_digit +=1
    for c in name2 :
        if c.lower() in first_word.lower() :
            first_digit += 1

        if c.lower() in second_word.lower() :
            second_digit +=1

    print(f"Love Score = {first_digit}{second_digit}")



def calculate_love_score_second(name1, name2):
    combine_name = (name1+name2).lower()

    t_count = combine_name.count("t")
    r_count = combine_name.count("r")
    u_count = combine_name.count("u")
    e_count = combine_name.count("e")
    first_digit = str(t_count+r_count+u_count+e_count)

    l_count = combine_name.count("l")
    o_count = combine_name.count("o")
    v_count = combine_name.count("v")
    e_count = combine_name.count("e")
    second_digit = str(l_count+o_count+v_count+e_count)

    print(first_digit+second_digit)

calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score_second("Kanye West", "Kim Kardashian")
