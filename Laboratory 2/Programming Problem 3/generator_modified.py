import random

def get_words(filename):
    fp = open(filename, 'r')
    temp_list = []
    for each_line in fp:
        each_line = each_line.strip()
        temp_list.append(each_line)
    fp.close()
    return temp_list

articles = get_words('articles.txt')
nouns = get_words('nouns.txt')
verbs = get_words('verbs.txt')
prepositions = get_words('prepositions.txt')

def sentence():
    return noun_phrase() + ' ' + verb_phrase()

def noun_phrase():
    return random.choice(articles) + ' ' + random.choice(nouns)

def verb_phrase():
    return random.choice(verbs) + ' ' + noun_phrase() + ' ' + prepositional_phrase()

def prepositional_phrase():
    return random.choice(prepositions) + ' ' + noun_phrase()

def main():
    number = int(input('Enter number of sentences: '))
    for count in range(number):
        print(sentence())

if __name__ == '__main__':
    main()