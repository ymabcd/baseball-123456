class GameResult:
    def __init__(self, solved, strikes, balls):
        self.balls = balls
        self.strikes = strikes
        self.solved = solved


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)
        return GameResult(True, 3, 0)

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
