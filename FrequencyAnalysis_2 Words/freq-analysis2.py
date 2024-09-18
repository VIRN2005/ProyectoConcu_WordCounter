class Rank:
    def __init__(self, word, word2, number):
        self.word = word
        self.word2 = word2
        self.number = number

def main():
    mylist = []

    with open('part-r-00000', 'r') as file:
        for line in file:
            words = line.split()
            if len(words) >= 2:
                first_word = words[0]
                second_word = words[1]
            
                number = words[2]
                
                if int(number) >= 5000:
                    temp = Rank(first_word, second_word, int(number))
                    mylist.append(temp)
                    
                    with open('freq-results.txt', 'a') as file:
                        file.write(first_word + " " + second_word + " " + number + '\n')
                        
    mylist.sort(key=lambda x: x.number, reverse=True)
    with open('freq-results-sorted.txt', 'w') as file:
        for i in mylist:
            file.write(i.word + " "  + i.word2 + " " + str(i.number) + '\n')
    pass

if __name__ == "__main__":
    main()