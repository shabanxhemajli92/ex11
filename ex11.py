user=input("Type your phrase: ")

vowel_list=["a","e","i","o","u"]

def inator(user):
    if user[-1] in vowel_list:
        print(f"{user} - inator  {str(len(user))}000")
    else:
        print(user + "inator"+ str(len(user))+"000")    

inator(user)