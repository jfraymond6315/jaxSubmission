# jaxSubmission
# This is the README file for Jack Raymond's code exercise submission to Asymmetrik.
# I've chose the Mobile Device Keyboard exercise (provides autocompletion suggestions based on a user entered string fragment.)
# 
# Directions for execution:
# 1. Download the file jaxSubmission.py to your server
# 2. On your server, switch to the directory where you've downloaded jaxSubmission.py 
# 3. Create a python session and enter the following commands:
# import jaxSubmission
# jaxSubmission.AutocompleteProvider.train("The third thing that I need to tell you is that this thing does not think thoroughly.")
# myList=jaxSubmission.AutocompleteProvider.getWords("thi")
# for i in range(len(myList)):
#     print(myList[i], '(', jaxSubmission.Candidate.getConfidence(myList[i]), '), ', end='')
#
# (Verify that the output includes the following words and Confidence values:)
#     "thing" (2), "think" (1), "third" (1), "this" (1)
#
# myList=jaxSubmission.AutocompleteProvider.getWords("nee")
# for i in range(len(myList)):
#     print(myList[i], '(', jaxSubmission.Candidate.getConfidence(myList[i]), '), ', end='')
#
# (Verify that the output includes the following words and Confidence values: "need" (1) )
#
# myList=jaxSubmission.AutocompleteProvider.getWords("th")
# for i in range(len(myList)):
#     print(myList[i], '(', jaxSubmission.Candidate.getConfidence(myList[i]), '), ', end='')
# 
# (Verify that the output includes the following words and Confidence values:)
#     "that" (2), "thing" (2), "think" (1), "this" (1), "third" (1), "the" (1), "thoroughly" (1)
# 
# quit()
#
# (That's the end of the test.)
#
# An AWS Solutions Architect / Systems Architect / Systems Engineer who can write code - not bad.
# Call Jack at 410-746-4786 before the competition picks him up!
# ; )
#
