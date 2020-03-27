# This is Jack Raymond's code exercise submission to Asymmetrik
#     "Mobile Device Keyboard" autocompletion classes and functions
# See the accompanying README
# This file is best viewed in a tool like Notepad++
#
def removePunctuation(inString):
    # Function to remove punctuation and special characters from the input string
    # Returns the input string without punctuation and special characters 
    #
    # Create a string containing the characters to be removed
    punctuation='~!@#$%^&*()_-+={}[]|\:;<,>.?/'
    #
    # Examine each character in the input string
    for x in Instring:
        # If the character is in "punctuation", then replace it with a null
        if x in punctuation:
            inString = inString.replace(x, "")
    return inString

class Candidate:
    def getWord(thisFragment, thisKeyword):
        # Given a string fragment and a keyword,
        #     return the keyword if the fragment is a prefix for the keyword,
        #     i.e., if the keyword is an autocomplete candidate for the string fragment
        #
        # While the keywords in the dictionary should already all be lowercase,
        #     let's make sure we're comparing lowercase to lowercase,
        #     just in case this function is reused in a way that may not
        #     adhere to that assumption
        #
        lowerKeyword = thisKeyword.lower()
        if lowerKeyword[0:len(thisFragment.lower())] == thisFragment.lower():
            return thisKeyword
        else:
            return 'NO MATCH'
        #
    def getConfidence(thisKeyword):
        # For a given keyword (i.e., autocomplete candidate),
        #     if the keyword is in the dictionary,
        #         return the Confidence value
        #     otherwise,
        #         return zero
        if thisKeyWord in acDictionary:
            return acDictionary[thisKeyword]
        else:
            return 0

class AutocompleteProvider:
    # Initialize the dictionary that will hold the words from the training passage(s)
    #     and the counts of the frequency of each word's appearance in the training passage(s).
    # Each keyword's total count from the training passage(s) will be used as its Confidence
    #     level when being returned as an autocompletion candidate for a string fragment.
    global acDictionary
    acDictionary={}
    #
    def train(passage):
        # Input arg is a string passage whose contents (words) are the candidates 
        #     for the autocompletion algorithm
        #
        # Convert the input passage to lowercase
        lowerPassage = passage.lower()
        #
        # Remove punctuation and special characters from the passage
        nopuncPassage = removePunctuation(lowerPassage)
        #
        # Split the passage into a list of strings
        # Recognized delimiters are whitespace
        wordList = nopuncPassage.split()
        #
        # Create a unique set from the word list with no duplicates
        wordSet = set(wordList)
        #
        # Add the words and their frequency counts(Confidence) to the dictionary
        for word in wordSet:
            if (word in acDictionary) == True:
                # The word is already in the dictionary, so add its word count 
                # from the new passage to the existing count for that word
                acDictionary[word] = acDictionary[word] + wordList.count(word)
            else:
                # The word is not already in the dictionary, so add it and its word count
                acDictionary[word] = wordList.count(word)
        #
    def getWords(fragment):
        # Given a string (word) fragment, search the dictionary for autocomplete candidates,
        #     and order the results list by Confidence level
        #     (i.e., order by the candidate word's frequency of occurrence in the training passages)
        #
        # Initialize the autocomplete candidateList to be returned to the caller
        candidateList=[]
        #
        # Loop through the dictionary to check whether yhe lowercase version of the fragment
        #     is a prefix for each dictionary keyword. 
        #     If it is, then add the keyword to the candidateList
        #
        for keyWord in acDictionary:
            if Candidate.getWord(fragment.lower(), keyword) == keyword:
                # A match!
                # Insert the candidate word into the candidateList in order based on its Confidence (desc).
                # There are three use-cases:
                #     1) The list is empty, so append the new candidate to the end of the list
                #     2) The candidate Confidence is less than or equal to the that of the last entry,
                #         so append the new candidate to the end of the list
                #     3) The candidate Confidence is greater than that of some entry in the list,
                #         so insert the candidate into the list before the entry with lower Confidence
                #
                if len(candidatelist) > 0:
                    if Candidate.getConfidence(keyword) <= Candidate.getConfidence(candidatelist[len(candidateList)-1]):
                        # Use-case 2) Candidate Confidence is less than or equal to that of the last entry
                        candidateList.append(keyword)
                    else:
                        # Use-case 3) Candidate Confidence is greater than that of some entry in the list.
                        # Walk though the list and insert the candidate into the list before the entry
                        #     whose Confidence is <= this one
                        #
                        for i in range(len(candidateList)):
                            if Candidate.getConfidence(keyword) >= Candidate.getConfidence(candidateList[i]):
                                candidateList.insert(i, keyword)
                                # Break out of this loop
                                break
                else:
                    # Use-case 1) The list is empty, so append the new candidate keyword
                    candidateList.append(keyword)
        #
        return candidateList



