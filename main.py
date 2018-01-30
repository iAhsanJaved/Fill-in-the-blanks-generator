import nltk


def readFile(fileName):
    paragraph = ''
    file = open(fileName, "r")
    paragraph = file.read()
    file.close()
    return paragraph

def tokenization(paragraph):
    sents = nltk.sent_tokenize(paragraph)
    words = [nltk.word_tokenize(sent) for sent in sents]
    return sents, words

def posTagging(words):
    posWords = [nltk.pos_tag(word) for word in words]
    return posWords


fileName = raw_input('Enter the file name: ')

# -------------Read File-------------
print '---------------------------------------------------'
print 'Paragraph'
print '---------------------------------------------------'
paragraph = readFile(fileName)
print paragraph


# Step-1--------Tokenization---------
sents, words = tokenization(paragraph)


# Step-2--------POS Tagging---------
posWords = posTagging(words)

# Step-3--------Printing POS--------
print '\n---------------------------------------------------'
print 'Part of Speech'
print '---------------------------------------------------'
print posWords


# Step-4--------Printing Nouns--------
print '\n---------------------------------------------------'
print 'Print Nouns'
print '---------------------------------------------------'
for posWord in posWords:
    for x in posWord:
        if (x[1] == 'NN'):
            print x[0] + '=> NOUN'
    print '\n'

# Step-5--------Replace Nouns with '____'--------
i = 0
fillSents = sents
answers = []
for posWord in posWords:
    for x in posWord:
        if (x[1] == 'NN'):
            fillSents[i] = fillSents[i].replace(x[0], '__________')
            answers.append(x[0])
    i = i + 1

# Step-6--------Printing Fill in the blanks--------
print '---------------------------------------------------'
print 'Fill in the blanks'
print '---------------------------------------------------'
i = 1
for fillSent in fillSents:
    print str(i) + '. ' + fillSent
    print '\n'
    i = i + 1



