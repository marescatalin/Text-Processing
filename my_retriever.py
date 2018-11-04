import math
class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        self.maximumArticles = 0

        maximumArticles = 0
        for word in self.index.keys():
            for article in self.index[word]:
                if article > self.maximumArticles:
                    self.maximumArticles = article

    # Method performing retrieval for specified query
    def forQuery(self, query):
        bestArticles, articleMatrix = [], ([0] * (self.maximumArticles + 1))


        if (self.termWeighting == 'binary'):
            for key in query.keys():
                if key in self.index:
                    for article,count in self.index[key].items(): articleMatrix[article] += 1

            frequencySum = ([0] * (self.maximumArticles + 1))

            for word in self.index.keys():
                for article, frequency in self.index[word].items():
                    frequencySum[article] += math.pow(1, 2)

            # Square root the sum for each article
            sqrFrequencySum = [math.sqrt(x) for x in frequencySum]

            # Normalise the tf computed for each article
            for number in range(1, self.maximumArticles): articleMatrix[number] = articleMatrix[number] / sqrFrequencySum[number]


            for x in range(10):
                indexOfMaxValue = articleMatrix.index(max(articleMatrix))
                bestArticles.append(indexOfMaxValue)
                articleMatrix[indexOfMaxValue] = 0

            return bestArticles


        elif (self.termWeighting == 'tf'):

        #Computing the terms that are both in the query and article
            for key in query.keys():
                if key in self.index:
                    for article,frequency in self.index[key].items():
                        articleMatrix[article] += frequency*query[key]

        #Computing the square root of the square sum of the frequency of each term for each article
            frequencySum = ([0] * (self.maximumArticles + 1))

            for word in self.index.keys():
                for article, frequency in self.index[word].items():
                    frequencySum[article] += math.pow(frequency, 2)

            #Square root the sum for each article
            sqrFrequencySum =[math.sqrt(x) for x in frequencySum]


        #Normalise the tf computed for each article
            for number in range(1, self.maximumArticles): articleMatrix[number] = articleMatrix[number] / sqrFrequencySum[number]


            for x in range(10):
                indexOfMaxValue = articleMatrix.index( max(articleMatrix))
                bestArticles.append(indexOfMaxValue)
                articleMatrix[indexOfMaxValue] = 0

            return bestArticles





        elif (self.termWeighting == 'tfidf'):

            idfScore = {}
            #Compute the total number of documents / term occurance in the data set
            for term in self.index:
                idfScore[term] = math.log10(self.maximumArticles/len(self.index[term].items()))

                # Computing the terms that are both in the query and article
            for key in query.keys():
                if key in self.index:
                    for article, frequency in self.index[key].items():
                            articleMatrix[article] += (frequency * idfScore[key])

                # Computing the square root of the square sum of the frequency of each term for each article
            frequencySum = ([0] * (self.maximumArticles + 1))

            for word in self.index.keys():
                for article, frequency in self.index[word].items():
                    frequencySum[article] += math.pow(frequency*(idfScore[word]), 2)

                # Square root the sum for each article
            sqrFrequencySum = [math.sqrt(x) for x in frequencySum]

                # Normalise the tf computed for each article
            for number in range(1, self.maximumArticles): articleMatrix[number] = articleMatrix[number] / sqrFrequencySum[number]


            for x in range(10):
                indexOfMaxValue = articleMatrix.index(max(articleMatrix))
                bestArticles.append(indexOfMaxValue)
                articleMatrix[indexOfMaxValue] = 0

            return bestArticles











