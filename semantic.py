# Importing spacy and model
import spacy
nlp = spacy.load('en_core_web_md')

# First code extract
print("Task 1")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Second code extract
print("\nTask 2")
tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Third code extract
print("\nTask 3")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car", "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - " + str(similarity))


# Task 4
# The results for web_core_sm are generally much lower than for web_core_md. Both models give a 1.0 result when the text
# is identical, but where there are differences the web_core_web_sm model will give a lower similarity rating.