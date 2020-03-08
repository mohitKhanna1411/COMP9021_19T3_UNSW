
def find(sentence):
    full_stop_split_correct = []
    full_stop_split = sentence.split('.')
    print(full_stop_split)
    for words in full_stop_split:
        if words:
            words = words.strip()
            words = str(words).replace(",","")
            full_stop_split_correct.append(words)
    full_stop_split_correct = sorted(full_stop_split_correct, key= len)
    print("Shortest sentence: " + full_stop_split_correct[0] + " longest: "+ full_stop_split_correct[-1])

    space_split_correct = []
    space_split = sentence.split()
    print(space_split)
    for w in space_split:
        if w:
            w = str(w).replace(".","")
            w = str(w).replace(",","")
            space_split_correct.append(w)
    space_split_correct = sorted(space_split_correct, key= len)
    print("Shortest word: " + space_split_correct[0] + " longest: "+ space_split_correct[-1])
if __name__ == "__main__":
    find("mohit, khanna. I am the best. kl, karunga sare ke sare questionWithAnswers.")