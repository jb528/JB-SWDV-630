class teams:
    def __init__(self,members):
        self.__myTeam = members
        
    def __len__(self):
        return len(self.__myTeam)
    
    
    def __contains__(self, x):
        return x in self.__myTeam
    
    def __iter__(self):
        return iter(self.__myTeam)
    
def main():
    classmates = teams(['John','Steve','Tim'])
    print(len(classmates))
    print('John in team:','John' in classmates)
    print('Steve in team:','Steve' in classmates)
    print('Tim in team:','Tim' in classmates)
    print('')
    print('Sam in team:','Sam' in classmates)
    print('')
    
    for t in classmates:
        print(t)
    print('')
    print('Is len method implemented in classmates:','__len__' in dir(classmates))
    
main()
    

    