import math
class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        maximumArticles = 0
        for word in self.index.keys():
            for article in self.index[word]:
                if article > maximumArticles:
                    maximumArticles = article
        self.maximumArticles = maximumArticles

    # Method performing retrieval for specified query
    def forQuery(self, query):
        bestArticles, articleMatrix = [], ([0] * (self.maximumArticles + 1))


        if (self.termWeighting == 'binary'):
            for key in query.keys():
                if key in self.index:
                    for article,count in self.index[key].items(): articleMatrix[article] += 1

            for x in range(10):
                indexOfMaxValue = articleMatrix.index(max(articleMatrix))
                bestArticles.append(indexOfMaxValue)
                articleMatrix[indexOfMaxValue] = 0

            return bestArticles


        elif (self.termWeighting == 'tf'):
            for key in query.keys():
                if key in self.index:
                    for article,count in self.index[key].items():
                        articleMatrix[article] += count*query[key]

        #find how many words are in each article
            wordsInEachArticle = ([0] * (self.maximumArticles + 1))
            for word in self.index.keys():
                for article in self.index[word]:
                    wordsInEachArticle[article] += 1

            print(wordsInEachArticle)
            breakpoint()


        #Divide how many words in each article by

            for x in range(10):
                indexOfMaxValue = articleMatrix.index( max(articleMatrix))
                bestArticles.append(indexOfMaxValue)
                articleMatrix[indexOfMaxValue] = 0
            return bestArticles


        elif (self.termWeighting == 'tfidf'):
            queryIDFScores = {}

            for word in query.keys():
                if word in self.index:
                    queryIDFScores[word] = self.maximumArticles/ len(self.index[word].keys())

            for word in query.keys():
                if word in self.index:
                    for article,count in self.index[word].items():
                        articleMatrix[article] += count*query[word]*queryIDFScores[word]

            for x in range(10):
                indexOfMaxValue = articleMatrix.index(max(articleMatrix))
                bestArticles.append(indexOfMaxValue)
                articleMatrix[indexOfMaxValue] = 0

            return bestArticles












