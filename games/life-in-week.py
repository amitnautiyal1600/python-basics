def life_in_weeks(age):
    total_life = 90;
    remaining_life = total_life - age
    print(remaining_life)
    weeks = remaining_life * 13 * 4
    print(f"You have {weeks} weeks left.")


life_in_weeks(20)