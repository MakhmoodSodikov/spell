class Spell:
    def __init__(self):
        pass

    def __get_correct_thresh(self, word1, word2):
        return max(1, min(len(word1), len(word2)))

    def __remove_redundant_symbols(self, word):
        new_word = []
        ch_set = list(set(word))
        for ch in word:
            if ch in ch_set:
                new_word.append(ch)
                ch_set.remove(ch)

        return ''.join(new_word)

    def __same_two_words(self, thresh, word1, word2):
        # сделанный
        # сделаанныый
        # оба слова свернутся в сделаный и будут посимвольно проверены
        # если после удаления повторов слова разной длины -> вернем False

        diff_counter = 0

        if len(word1) != len(word2):
            word1 = self.__remove_redundant_symbols(word1)
            word2 = self.__remove_redundant_symbols(word2)

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_counter += 1

        return diff_counter <= thresh

    def same_words(self, words_list, thresh=2, smart_thresh=False):
        same_words_dict = {key: [] for key in words_list}

        for word1 in words_list:
            for word2 in words_list:
                if word1 == word2:
                    continue
                if smart_thresh:
                    thresh = self.__get_correct_thresh(word1, word2)

                if self.__same_two_words(thresh, word1, word2):
                    same_words_dict[word1].append(word2)

        return same_words_dict

    def word_from_dict(self, word, words_list, thresh=2, smart_thresh=False):
        same_words_list = []

        for other_word in words_list:
            if smart_thresh:
                thresh = self.__get_correct_thresh(word, other_word)

            if self.__same_two_words(thresh, word, other_word):
                same_words_list.append(other_word)

        return same_words_list
