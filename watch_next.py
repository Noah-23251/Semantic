# Importing spacy and model
import spacy
nlp = spacy.load('en_core_web_md')

# Reading from movies.txt to create a list of descriptions
description_list = []
with open("movies.txt", "r") as movie_text:
    for line in movie_text:
        description_list.append(line)

# Setting target description
description_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
                         "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk " \
                         "can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery" \
                         " and trained as a gladiator."
model_description = nlp(description_to_compare)

# Using for loop to compile a list of the similarity between the target description and each movie description
similarity_list = []
for description in description_list:
    similarity_list.append(nlp(description).similarity(model_description))

# Finding the movie with the highest similarity
max_similarity = max(similarity_list)
max_index = similarity_list.index(max_similarity)
next_movie = description_list[max_index]

# Printing result with similarity score to 2 d.p.
print(f"Your next movie is {next_movie[:7]} based on a similarity of {round(max_similarity, 2)}")


