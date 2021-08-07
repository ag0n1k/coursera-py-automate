from enum import Enum
from typing import List
import random
import re

qs = """1. How many days do we have in a week?
Answer: Seven
2. How many days are there in a normal year?
Answer: 365 (not a leap year)
3. How many colors are there in a rainbow?
Answer: 7
4. Which animal is known as the ‘Ship of the Desert?’
Answer: Camel
5. How many letters are there in the English alphabet?
Answer: 26
6. How many consonants are there in the English alphabet?
Answer: 21
7. How many sides are there in a triangle?
Answer: Three
8. Which month of the year has the least number of days?
Answer: February
9. Which are the vowels in the English alphabet series?
Answer: A, E, I, O, U
10. Which animal is called King of Jungle?
Answer: Lion
11. How many primary colors are there?
Answer: Three (red, yellow, blue)
12. How many days are there in the month of February in a leap year?
Answer: 29 days
13. What do you call a house made of ice?
Answer: Igloo
14. Which is the largest animal in the world?
Answer: Blue whale
15. Which is the tallest animal on the earth?
Answer: Giraffe
16. Which festival is known as the festival of colors?
Answer: Holi
17. Which festival is called the festival of light?
Answer: Diwali
18. What is the top color in a rainbow?
Answer: Red
19. What type of bird lays the largest eggs?
Answer: Ostrich
20. Which festival is known as the ‘Festival of flowers’?
Answers: Onam
21. In which direction does the sunrise?
Answer: East
22. Which is the world’s largest flower?
Answer: Rafflesia
23. How many zeros are there in one hundred thousand?
Answer: Five
24. How many hours are there in two days?
Answer: 48 hours (24+24)
25. How many months of the year have 31 days?
Answer: 7 (January, March, May, July, August, October and December)
26. How many weeks are there in one year?
Answer: 52
27. Which are the colors in a rainbow?
Answer: Violet, Indigo, Blue, Green, Yellow, Orange, Red
28. How many bones does an adult human have?
Answer: 206
29. Who was the first man to walk on the moon?
Answer: Neil Armstrong
30. How many millimeters are there in 1cm?
Answer: 10
31. Which is the nearest star to planet earth?
Answer: Sun
32. Which is the longest river on the earth?
Answer: Nile
33. Which is the principal source of energy for earth?
Answer: Sun
34. How many lungs does the human body have?
Answer: Two
35. What is the standard taste of the water?
Answer: Water is tasteless
36. Which is the tallest mountain in the world?
Answer: Mount Everest
37. Which is the fastest animal on the land?
Answer: Cheetah
38. Which continent is known as ‘Dark’ continent?
Answer: Africa
39. Which planet is known as the Red Planet?
Answer: Mars
40. Which is the most sensitive organ in our body?
Answer: Skin
41. Which is the largest ocean in the world?
Answer: Pacific Ocean
42. Which day is observed as World Environment Day?
Answer: June 5
43. How many years are there in a century?
Answer: One Hundred
44. Which is the largest country in the world?
Answer: Russia (By area)
45. Who invented the Computer?
Answer: Charles Babbage
46. How many players are there in a cricket team?
Answer: 11
47. Which day is observed as World Literacy Day?
Answer: September 8
48. Who is the inventor of Radio?
Answer: Marconi
49. Which place is known as the roof of the world?
Answer: Tibet
50. How many teeth does a healthy adult have including the wisdom teeth?
Answer: 32
51. Which gas is most abundant in the earth’s atmosphere?
Answer: Nitrogen
52. How many people are there in the world?
Answer: Over 7 billion
53. Which is the continent with the most number of countries?
Answer: Africa
54. Which is the most common non-contagious disease in the world?
Answer: Tooth Decay
55. How many strings does a violin have?
Answer: Four
56. How many planets are there in our solar system?
Answer: 8
57. Which is the hottest continent on Earth?
Answer: Africa
58. Which is the smallest continent in the world?
Answer: Australia
59. How many years are there in a millennium?
Answer: 1000
60. Which country is home to the kangaroo?
Answer: Australia
61. Who painted the Mona Lisa?
Answer: Leonardo da Vinci
62. Who invented the telephone?
Answer: Alexander Graham Bell
63. What does the Internet prefix WWW stand for?
Answer: World Wide Web
64. How much of Earth’s surface is covered by ocean?
Answer: 71%
65. Who discovered Penicillin in 1928?
Answer: Alexander Fleming
66. How many stars are there in the American flag?
Answer: 50
67. What do you call a type of shape that has five sides?
Answer: Pentagon
68. Which way is anti-clockwise, left or right?
Answer: Left
69. How many equal sides does an isosceles triangle have?
Answer: 2
70. Which is the coldest location in the earth?
Answer: East Antarctica
71. Who discovered electricity?
Answer: Benjamin Franklin
72. Which is the most widely spoken language in the world?
Answer: Mandarin (Chinese)
73. Which two parts of the body continue to grow for your entire life?
Answer: Nose and Ears
74. The largest ‘Democracy’ in the world?
Answer: India
75. Who is the inventor of Television?
Answer: John Logie Baird
76. Which is the largest plateau in the world?
Answer: Tibetan Plateau
77. Which is the instrument used to measure Blood pressure?
Answer: Sphygmomanometer
78. What color symbolizes peace?
Answer: White
79. Who is the founder of Microsoft?
Answer: Bill Gates
80. During which year did World War I begin?
Answer: 1914
81. How many Cricket world cups does India have?
Answer: 2
82. Global warming is caused by the excess of which type of gas?
Answer: Carbon dioxide
83. How many cards are there in a complete pack of cards?
Answer: 52
84. What is the name of the biggest rain forest in the world?
Answer: The Amazon
85. Which African nation is famous for chocolate?
Answer: Ghana
86. What makes up (approx.) 80% of our brain’s volume?
Answer: Water
87. Which instrument is used for measuring wind speed?
Answer: Anemometer
88. ‘Stars and Stripes’ is the nickname of the flag of which country?
Answer: United States of America
89. Which language is used by the computer to process data?
Answer: Binary language
90. What covers approximately 71% of the Earth’s surface: Land or water?
Answer: Water
91. Which is the hardest substance available on earth?
Answer: Diamond
92. Which is the biggest desert in the world?
Answer: Sahara desert
93. Which country gifted The Statue of Liberty to the United States?
Answer: France
94. What is the name of the Greek God of music?
Answer: Apollo
95. What does the “SIM” in the SIM card stand for?
Answer: Subscriber Identity Module
96. Which is the first element on the periodic table of elements?
Answer: Hydrogen
97. Which is the longest written Constitution in the world?
Answer: India
98. What is the largest joint in the human body?
Answer: Knee
99. Which is the smallest bone in the human body?
Answer: Stapes (Ear bone)
100. Which instrument is used to measure Atmospheric Pressure?
Answer: Barometer
101. Which is the largest continent in the world?
Answer: Asia
102. Who is the inventor of the electric Bulb?
Answer: Thomas Alva Edison
103. On whose memory Nobel Prize is awarded?
Answer: Alfred Nobel
104. Who is the first woman to go to space?
Answer: Valentina Tereshkova
105. What is HCl?
Answer: Hydrochloric acid
106. What is currency of China?
Answer: Renminbi"""

authors = [
    'Mike', 'Kile', 'John'
]

themes = [
    'USA', 'Physics', 'Life'
]


class Difficulty(Enum):
    Extreme = 5
    Hard = 4
    Medium = 3
    Easy = 2
    Simple = 1


class Question(object):
    # - текст вопроса
    # - автор вопроса
    # – сложность вопроса
    # - верные варианты ответов
    # - тема вопроса
    # - задан ли вопрос
    # – ответ пользователя
    # – баллы за вопрос
    text: str
    author: str
    difficult: int
    difficulty: Difficulty
    right_answers: [str]
    theme: str
    asked: bool = False
    answer: str
    rate: int

    def __init__(self, text, right_answers: str):
        self.text = text
        if '(' in right_answers:
            self.right_answers = re.findall('(.*)\\s\\(.*\\)', right_answers).pop()
        else:
            self.right_answers = right_answers
        self.right_answers = self.right_answers.split(',')
        self.theme = themes[random.randint(0, len(themes) - 1)]
        self.author = authors[random.randint(0, len(authors) - 1)]
        self.difficult = random.randint(1, 5)
        self.difficulty = Difficulty(self.difficult)
        self.rate = self.difficult * 10


def read_data() -> list:
    s = qs.split('\n')
    return [
        Question(
            text=re.findall('\\d+\\.\\s(.*)\\?', s[i-1].replace('\n', '')).pop(),
            right_answers=s[i].replace('Answer: ', '')
        )
        for i in range(1, len(s), 2)
    ]


def end(questions: List[Question]):
    print("Вот и все!")
    print(f"Отвечено на {len(list(filter(lambda q: q.asked is not False, questions)))} из {len(questions)}")


def ask(number: int, question: Question):
    print(f"Вопрос {number}, тема {question.theme}, сложность {question.difficulty.name}")
    print(f"{question.text}?")
    question.answer = input("-> ")
    if question.answer in question.right_answers \
            or question.answer.capitalize() in question.right_answers:
        print(f"Ответ верный, получено {question.rate} баллов")
    else:
        print(f"Ответ неверный. Верный ответ - {question.right_answers[0]}")
    question.asked = True


def main():
    ask_length = 2
    questions = read_data()

    for i, q in enumerate([questions[random.randrange(0, len(questions))] for _ in range(ask_length)], start=1):
        ask(number=i, question=q)
    end(questions)


if __name__ == '__main__':
    main()
