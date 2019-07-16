import os
import sys
import json
from collections import deque
import random

random.seed(271)

"""
Processing of multi-domain dialogue dataset MetaLWOz
https://www.microsoft.com/en-us/research/project/metalwoz/
"""


class MetaLWOzData(object):
    def __init__(self, dirName):
        """
        Args:
            dirName (string): directory where to load the corpus
        """
        self.lines = {}
        self.dirName = dirName
        self.queryTrainFile = 'gen_data/chitchat.train.query'
        self.answerTrainFile = 'gen_data/chitchat.train.answer'
        self.queryDevFile = 'gen_data/chitchat.dev.query'
        self.answerDevFile = 'gen_data/chitchat.dev.answer'

        self.lines = self.loadLines(os.path.join(self.dirName,
                                                 'crowdsourced_task-oriented_dialogues',
                                                 'blis_collected_dialogues.json'))

    def loadLines(self, fileName):
        """
        Args:
            fileName (str): file to load
        Return:
            dict<dict<str>>: the extracted fields for each line
        """

        with open(fileName) as json_in:
            corpus_json = json.load(json_in)

        lines = []
        for dialogue in corpus_json:
            turn_q = deque([], maxlen=3)
            for turn in dialogue['turns']:
                if turn['authorType'] == 'bot':
                    lines.append({'context': list(turn_q), 'response': turn['text']})
                turn_q.append(turn['text'])
        return lines

    def spruceUpLine(self,line):
        line = line.replace("'", " ' ")
        line = line.replace(".", " . ")
        line = line.replace("!", " !")
        line = line.replace("?", " ?")
        line = line.replace('"','')
        line = line.replace(",",'')
        line = line.replace("-", ' ')
        return ' '.join(line.lower().split())

    def writeToFile(self):
        random.shuffle(self.lines)
        trainset_size = int(0.9 * len(self.lines))
        trainset, devset = self.lines[:trainset_size], self.lines[trainset_size:]

        with open(os.path.join(self.dirName, self.queryTrainFile), 'w+') as querytrainfile:
            with open(os.path.join(self.dirName, self.answerTrainFile), 'w+') as answertrainfile:
                with open(os.path.join(self.dirName, self.queryDevFile), 'w+') as querydevfile:
                    with open(os.path.join(self.dirName, self.answerDevFile), 'w+') as answerdevfile:
                        for ind, line in enumerate(trainset):
                            first_phrase = self.spruceUpLine(' '.join(line['context']))
                            second_phrase = self.spruceUpLine(line['response'])
                            querytrainfile.write(str(first_phrase)+'\n')
                            answertrainfile.write(str(second_phrase)+'\n')
                        for ind, line in enumerate(devset):
                            first_phrase = self.spruceUpLine(' '.join(line['context']))
                            second_phrase = self.spruceUpLine(line['response'])
                            querydevfile.write(str(first_phrase)+'\n')
                            answerdevfile.write(str(second_phrase)+'\n')


def main():
    dirName = os.getcwd()
    cornell = MetaLWOzData(dirName)
    cornell.writeToFile()

if __name__ == '__main__':
    main()
