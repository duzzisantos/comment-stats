## Let us find the longest and most common comments on facebook and twitter

twitterComments = []
facebookComments = []
emptyComment = ""
terminated = False

while not terminated:
    print("Enter Facebook comment (ends with empty string): ", end="")
    facebook = input()
    print("Enter Twitter comment (ends with empty string): ", end="")
    twitter = input()

    if facebook != emptyComment and twitter != emptyComment:
        facebookComments.append(facebook)
        facebookComments.sort(key=len)
        facebookComments.reverse()
        longestFacebookComment = facebookComments[0]
        mostFrequentFacebookComment = facebookComments.count(
            longestFacebookComment)
        twitterComments.append(twitter)
        twitterComments.sort(key=len)
        twitterComments.reverse()
        longestTwitterComment = twitterComments[0]
        mostFrequentTwitterComment = twitterComments.count(
            longestTwitterComment)
    else:
        print("\n Most occurring longest Facebook comment: " +
              longestFacebookComment.upper())
        print("Frequency: " + str(mostFrequentFacebookComment))
        print("\n Most occurring longest Twitter comment: " +
              longestTwitterComment.upper())
        print("\n Frequency: " + str(mostFrequentTwitterComment))
        terminated = True