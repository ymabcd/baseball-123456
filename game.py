class GameResult:
    def __init__(self, solved, strikes, balls):
        self.__balls = balls
        self.__strikes = strikes
        self.__solved = solved

    def get_solved(self):
        return self.__solved

    def get_strikes(self):
        return self.__strikes

    def get_balls(self):
        return self.__balls
class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)
        if guessNumber == self.question:
            return GameResult(True, 3, 0)
        else:
            strikes = 0
            for i in range(len(self.question)):
                if self.question.find(guessNumber[i]) == i:
                    strikes += 1
            return GameResult(False, strikes, 0)

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if self.isDuplicatedNumber(guessNumber):
            raise TypeError()

    def isDuplicatedNumber(self, guessNumber):
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]
