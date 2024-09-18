
class Rank:
    def __init__(self, word, number):
        self.word = word
        self.number = number

def main():
    mylist = []
    
    with open('part-r-00000', 'r') as file:
        for line in file:
            words = line.split()
            if len(words) >= 2:
                first_word = words[0]
                second_word = words[1]
                
                if int(second_word) >= 5000:
                    
                    temp = Rank(first_word, int(second_word))
                    mylist.append(temp)
                    
                    with open('freq-results.txt', 'a') as file:
                        
                        file.write(first_word + " " + second_word + '\n')
                        
    mylist.sort(key=lambda x: x.number, reverse=True)
    with open('freq-results-sorted.txt', 'w') as file:
        for i in mylist:
            file.write(i.word + " " + str(i.number) + '\n')
    pass

if __name__ == "__main__":
    main()