from textblob import TextBlob

class TextBlobService:
    def get_sentiment(self, message):
        print(TextBlob)
        self.blob = TextBlob(message)
        print("blob:", self.blob)
        self.polarity = self.blob.sentiment.polarity
        self.subjectivity = self.blob.sentiment.subjectivity
        
        if self.polarity > 0.1:
           sentiment = 'positivo'
        elif self.polarity < -0.1:
           sentiment = 'negativo'
        else:
           sentiment = 'neutro'

        return {
            'sentiment': sentiment,
            'polarity': round(self.polarity, 3),
            'subjectivity': round(self.subjectivity, 3)
        }