import os
import sys

"""
Processing of movie dialogue dataset from Cornell
http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html
"""


class CornellData:
    """
    """

    def __init__(self, dirName):
        """
        Args:
            dirName (string): directory where to load the corpus
        """
        self.lines = {}
        self.dirName = dirName
        self.queryTextFile = 'gen_data/chitchat.train.query'
        self.answerTextFile = 'gen_data/chitchat.train.answer'

        self.MOVIE_LINES_FIELDS = ["lineID", "characterID",
                              "movieID", "character", "text"]

        self.lines = self.loadLines(os.path.join(
            self.dirName, 'cornell movie-dialogs corpus', "movie_lines.txt"))

        # TODO: Cleaner program (merge copy-paste) !!

    def loadLines(self, fileName):
        """
        Args:
            fileName (str): file to load
        Return:
            dict<dict<str>>: the extracted fields for each line
        """
        lines = {}

        with open(fileName, 'r', encoding='iso-8859-1') as f:
            for line in f:
                values = line.split(" +++$+++ ")

                # Extract fields
                lineObj = {}
                for i, field in enumerate(self.MOVIE_LINES_FIELDS):
                    lineObj[field] = values[i]

                lines[lineObj['lineID']] = lineObj

        return lines

    def spruceUpLine(self,line):
        line = line.replace("'", " ' ")
        line = line.replace(".", " .")
        line = line.replace("!", " !")
        line = line.replace("?", " ?")
        line = line.replace('"','')
        line = line.replace(",",'')
        return line.lower()

    def writeToFile(self):
        with open(os.path.join(self.dirName, self.queryTextFile), 'w+') as queryfile:
            with open(os.path.join(self.dirName, self.answerTextFile), 'w+') as answerfile:
                line_numb = len(self.lines.keys())
                keys = list(self.lines.keys())
                i = 0
                while i < line_numb-1:
                    first_phrase = self.spruceUpLine(self.lines[keys[i+1]]['text'])
                    second_phrase = self.spruceUpLine(self.lines[keys[i]]['text'])
                    queryfile.write(str(first_phrase.encode('utf-8')))
                    answerfile.write(str(second_phrase.encode('utf-8')))
                    i = i+2



def main():
    dirName = os.getcwd()
    cornell = CornellData(dirName)
    cornell.writeToFile()

if __name__ == '__main__':
    main()
    