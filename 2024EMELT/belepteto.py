from datetime import datetime

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


def second_task(m_clean_data):
    print('2. feladat')
    firstStudentTime = m_clean_data[0][1]
    lastStudentTime = m_clean_data[-1][1]
    print(f'Az első tanuló {firstStudentTime}-kor lépett be a főkapu')
    print(f'Az utolsó tanuló {lastStudentTime}-kor lépett ki a főkapun. ')

def third_task(m_clean_data):
    kesokList = ""
    for i in range(len(m_clean_data)):
        if m_clean_data[i][1] >= "07:50" and m_clean_data[i][1] <= "08:15":
            if(m_clean_data[i + 1][1] > "08:15"):
                kesokList += m_clean_data[i][1] + " " + m_clean_data[i][0]
            else:
                kesokList += m_clean_data[i][1] + " " + m_clean_data[i][0] + "\n"
            
    f = open("./kesok.txt", "w")
    kesokList.split(".")
    f.write(str(kesokList))
    f.close()

def fourth_task(m_clean_data):
    print('\n4. feladat')
    lunchCount = 0
    for i in range(len(m_clean_data)):
        if m_clean_data[i][2] == "3":
            lunchCount += 1
    print(f'A menzán aznap {lunchCount} tanuló ebédelt. ')
    return lunchCount

def fith_task(m_clean_data, m_lunchCount):
    print('\n5. feladat')
    libaryStudentListBad = []
    for i in range(len(m_clean_data)):
        if m_clean_data[i][2] == "4":
            libaryStudentListBad.append(m_clean_data[i][0])
    libaryStudentList = list(dict.fromkeys(libaryStudentListBad))
    print(f'Aznap {len(libaryStudentList)} tanuló kölcsönzött a könyvtárban.')
    if len(libaryStudentList) > m_lunchCount:
        print('Többen voltak, mint a menzán.')
    else:
        print('Nem voltak többen, mint a menzán.')


#SEGÍTSÉG!!
def sixth_task(m_clean_data):
    print("\n6. feladat")

    enters_w_time_before_1050 = {}
    returned_students = {}

    for item in m_clean_data:
        student_id = item[0]
        time = item[1]
        event_code = item[2]

        if event_code == '1' and time < "10:50":
            enters_w_time_before_1050[student_id] = time
        
        if event_code == "1" and "10:50" <= time <= "11:00":
            if student_id in enters_w_time_before_1050:
                returned_students[student_id] = time

    print(" ".join(returned_students))

def seventh_task(m_clean_data):
    print('\n7. feladat')

    request = input("Egy tanuló azonosítója=")

    firstEntry = ""
    lastEntry = ""

    student_exists = any(request in x for x in m_clean_data)
    if(student_exists == False):
        return print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")
        
    for item in m_clean_data:
        student_id = item[0]
        time = item[1]
        event_code = item[2]

        if student_id == request and event_code == "1" and firstEntry == "":
            firstEntry = time
        
        if student_id == request and event_code == "2":
            lastEntry = time
    start = datetime.strptime(firstEntry, "%H:%M")
    end = datetime.strptime(lastEntry, "%H:%M")
    diff = end - start

    hours, remainder = divmod(diff.total_seconds(), 3600)
    minutes = remainder // 60

    print(f"A tenuló érkezése és távozása között {int(hours)} óra {int(minutes)} perc telt el.")

clean_data = clean_up()
second_task(clean_data)
third_task(clean_data)
lunch_count = fourth_task(clean_data)
fith_task(clean_data, lunch_count)
sixth_task(clean_data)
seventh_task(clean_data)
