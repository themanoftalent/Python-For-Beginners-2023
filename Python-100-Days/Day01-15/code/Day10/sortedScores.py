unsorted= [37,89,41,37,65,91,53, 53]

highestScore = 100
def sort_scores(unsorted, highestScore):
    scores = [0]*(highestScore+1)
    for score in unsorted:
        scores[score] +=1
    sortedScores = []
    for indx,val in enumerate(scores):
        sortedScores.extend([indx]*val)
    return sortedScores
print sort_scores(unsorted, highestScore)
