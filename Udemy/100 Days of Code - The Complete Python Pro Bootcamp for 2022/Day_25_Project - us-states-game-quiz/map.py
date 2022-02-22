from turtle import Turtle
import pandas

WORD_SIZE = 7

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


class Map(Turtle):

    def __init__(self):
        super().__init__()
        self.x_cor = 0
        self.y_cor = 0
        self.hideturtle()
        self.missing_states = states
        self.correct_answers = []
        self.num_states = len(data)

    def on_the_map(self, right_answer):
        if right_answer not in self.correct_answers:
            data_answer = data[data["state"] == right_answer]
            self.x_cor = data_answer.x
            self.y_cor = data_answer.y
            self.hideturtle()
            self.penup()
            self.speed("fast")
            self.goto(int(self.x_cor), int(self.y_cor))
            self.write(arg=right_answer, align="Center", font=("Arial", WORD_SIZE, "normal"))
            self.correct_answers.append(right_answer)
            self.missing_states.remove(right_answer)

    def checking_answer(self, answer):
        """Put the State here(str) and if it is correct it will appear on the map"""
        for state in data.state:
            if state == answer:
                self.on_the_map(answer)

    def new_csv(self):
        data = {"missing_states": self.missing_states}
        missing_states = pandas.DataFrame(data)
        missing_states.to_csv("states_to_learn")
