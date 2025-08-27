with open("story.txt", "r")as f:
    story = f.read()

words=set()
start_of_word=-1

target_Start="<"
target_End =">"

for i , char in enumerate(story):
    if char == target_Start:
        start_of_word =i


    if char == target_End and start_of_word !=-1:

        word = story[start_of_word:i +1]
        words.add(word)
        start_of_word=-1


answers={}

for word in words:
    answer= input("enter a word for "+word + " :  ")
    answers[word] = answer


for word in words:
    story = story.replace(word, answers[word])



print(story)

    

    
