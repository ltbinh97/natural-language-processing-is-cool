import re
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, RegexpParser, word_tokenize, Tree

sentence = 'The painting stolen last week was recovered'
# Tokenize a sentence into tokens
sen_tok = word_tokenize(sentence) # ['The', 'painting', 'stolen', 'last', 'week', 'was', 'recovered']
# Add Post-of-Tagged for tokens
sen_pos = pos_tag(sen_tok)  # [('The', 'DT'), ('painting', 'NN'), ('stolen', 'VBN'), ('last', 'JJ'), ('week', 'NN'), ('was', 'VBD'), ('recovered', 'VBN')]

# define noun phrase grammar
chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
# create RegexpParser object
chunk_parser = RegexpParser(chunk_grammar)
# chunk the pos-tagged sentence in sen_pos
sen_chunk = chunk_parser.parse(sen_pos)
print(sen_chunk) # (S (NP The/DT painting/NN) stolen/VBN (NP last/JJ week/NN) was/VBD recovered/VBN)
# pretty_print the chunked sentence
Tree.fromstring(str(sen_chunk)).pretty_print()
#                                    S                                       
#      ______________________________|_____________________________           
#     |         |          |               NP                      NP        
#     |         |          |          _____|_______           _____|_____     
# stolen/VBN was/VBD recovered/VBN The/DT     painting/NN last/JJ     week/NN

# define verb phrase type 1 grammar
chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"
# create RegexpParser object
chunk_parser = RegexpParser(chunk_grammar)
# chunk the pos-tagged sentence in sen_pos
sen_chunk = chunk_parser.parse(sen_pos)
print(sen_chunk) # (S The/DT painting/NN (VP stolen/VBN last/JJ week/NN) was/VBD recovered/VBN)
# pretty_print the chunked sentence
Tree.fromstring(str(sen_chunk)).pretty_print()
#                                  S                                 
#    ______________________________|_____________________             
#   |         |         |          |                     VP          
#   |         |         |          |            _________|_______     
# The/DT painting/NN was/VBD recovered/VBN stolen/VBN last/JJ week/NN

# define verb phrase type 2 grammar
chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"
# create RegexpParser object
chunk_parser = RegexpParser(chunk_grammar)
# chunk the pos-tagged sentence in sen_pos
sen_chunk = chunk_parser.parse(sen_pos)
print(sen_chunk) #(S (VP The/DT painting/NN stolen/VBN) (VP last/JJ week/NN was/VBD) recovered/VBN)
# pretty_print the chunked sentence
Tree.fromstring(str(sen_chunk)).pretty_print()
#                                      S                             
#        ______________________________|_________________             
#       |                   VP                           VP          
#       |          _________|__________           _______|_______     
# recovered/VBN The/DT painting/NN stolen/VBN last/JJ week/NN was/VBD