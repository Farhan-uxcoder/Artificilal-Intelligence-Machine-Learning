def count_charecters(sentence):

    word_count = len(sentence.split())
    digit_count = sum(1 for char in sentence if char.isdigit())
    upper_count = sum(1 for char in sentence if char.isupper())
    lower_count = sum(1 for char in sentence if char.islower())
    return word_count,digit_count,upper_count,lower_count
try:
    sen = input("enter the sentence ")
    word_count,digit_count,upper_count,lower_count = count_charecters(sen)
    print(f"In the sentence {sen} we have the following : \n")
    print(f"Number of words are {word_count} ")
    print(f"Number of digits is {digit_count}")
    print(f"Number of lower case letters is {lower_count}")
    print(f"Number of upper case letters is {upper_count}")

except ValueError:
    print("Please enter the correct value")

