#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topics):
    max_topics = 0
    team_count = 0
    num_people = len(topics)
    
    for i in range(num_people):
        for j in range(i + 1, num_people):
            known_topics = 0
            num_subjects = len(topics[i])
            for k in range(num_subjects):
                if topics[i][k] == '1' or topics[j][k] == '1':
                    known_topics += 1
            
            if known_topics > max_topics:
                max_topics = known_topics
                team_count = 1
            elif known_topics == max_topics:
                team_count += 1
                
    return [max_topics, team_count]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
