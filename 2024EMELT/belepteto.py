inputFileRaw = open("./bedat.txt", "r")
inputFile = inputFileRaw.read()
inputFileRaw.close()



#Cleanup
def clean_up():
    splitFile = inputFile.split("\n")
    for i in range(len(splitFile)):
        splitFile[i] = splitFile[i].split(" ")
    splitFile.pop(-1)
    return splitFile


def second_task(m_cleanData):
    print('2. feladat')
    firstStudentTime = m_cleanData[0][1]
    lastStudentTime = m_cleanData[-1][1]
    print(f'Az első tanuló {firstStudentTime}-kor lépett be a főkapu')
    print(f'Az utolsó tanuló {lastStudentTime}-kor lépett ki a főkapun. ')

def third_task(m_cleanData):
    kesokList = ""
    for i in range(len(m_cleanData)):
        if m_cleanData[i][1] >= "07:50" and m_cleanData[i][1] <= "08:15":
            if(m_cleanData[i + 1][1] > "08:15"):
                kesokList += m_cleanData[i][1] + " " + m_cleanData[i][0]
            else:
                kesokList += m_cleanData[i][1] + " " + m_cleanData[i][0] + "\n"
            
    f = open("./kesok.txt", "w")
    kesokList.split(".")
    f.write(str(kesokList))
    f.close()

def fourth_task(m_cleanData):
    print('\n4. feladat')
    lunchCount = 0
    for i in range(len(m_cleanData)):
        if m_cleanData[i][2] == "3":
            lunchCount += 1
    print(f'A menzán aznap {lunchCount} tanuló ebédelt. ')
    return lunchCount

def fith_task(m_cleanData):
    print('\n5. feladat')
    libaryStudentListBad = []
    for i in range(len(m_cleanData)):
        if m_cleanData[i][2] == "4":
            libaryStudentListBad.append(m_cleanData[i][0])
    print(libaryStudentListBad)
    libaryStudentList = []
    for i in range(len(libaryStudentListBad)):
       if libaryStudentListBad[i] != libaryStudentList

cleanData = clean_up()
second_task(cleanData)
third_task(cleanData)
lunchCount = fourth_task(cleanData)
fith_task(cleanData)
