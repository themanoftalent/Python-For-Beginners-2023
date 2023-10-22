class WordCloudData:
    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        current_word = ""

        for i in range(0, len(input_string)):
            my
