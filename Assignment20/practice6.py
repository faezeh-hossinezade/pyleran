import random

boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman","hasan"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]

def random_pairs(boys, girls):

    if len(boys) != len(girls):
        raise ValueError("تعداد پسران و دختران باید برابر باشد.")

    random.shuffle(girls) 
    return list(zip(boys, girls))


results = random_pairs(boys, girls)
print(results)
