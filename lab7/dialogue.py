from datetime import time
import pymorphy2
import xlrd as xlrd
from faker import Faker

dict = {'Good':1,'Ok': 1, 'General': 1, 'Best': 1,
        'Good':2,'Ok': 2, 'General': 2, 'Best': 2,
        'Good':3,'Ok': 3, 'General': 3, 'Best': 3,}

fruitDict = {'Beijing Xuanwu Hospital': 'Beijing Xuanwu Hospital',
             'Xian Tangdu Hospital': 'Xian Tangdu Hospital',
             'Fourth Military Medical University': 'Fourth Military Medical University',
             'Beijing Union Medical College Hospital': 'Beijing Union Medical College Hospital',
             'Shanghai Changhai Hospital': 'Shanghai Changhai Hospital',
             'Xian High-tech Hospital': 'Xian High-tech Hospital',
             'Wuhan Tongji Hospital': 'Wuhan Tongji Hospital',
             'Chongqing Xinqiao Hospital': 'Chongqing Xinqiao Hospital',
             'Tianjin Eye Hospital': 'Tianjin Eye Hospital',
             'Beijing Obstetrics and Gynecology Hospital': 'Beijing Obstetrics and Gynecology Hospital',
             'Shanghai Huashan Hospital': 'Shanghai Huashan Hospital',
             'Xian Red Cross Hospital': 'Xian Red Cross Hospital',
             'PLA 301 Hospital': 'PLA 301 Hospital',
             'Sichuan West China Hospital': 'Sichuan West China Hospital',
             'Sanxiang Hospital': 'Sanxiang Hospital',
             'Guangzhou Cancer Hospital': 'Guangzhou Cancer Hospital',
             'Shanghai Changzheng Hospital': 'Shanghai Changzheng Hospital',
             'Xian Plastic Surgery Hospital': 'Xian Plastic Surgery Hospital',
             'Shanghai Hospital of Traditional Chinese Medicine': 'Shanghai Hospital of Traditional Chinese Medicine',
             'Xian Huiren Hospital': 'Xian Huiren Hospital',
             }
morph = pymorphy2.MorphAnalyzer()

class Conversation:
    def __init__(self,a):
        fake = Faker("En")
        Faker.seed(time.time())
        self.name = fake.word()
        self.grade = fake.int()
        self.scale = fake.int()
        self.online_consultation = fake.isinstance()
        self.main_departments = fake.word()
        self.number_of_patients = fake.int()
        self.service = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.quality = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.effectiveness = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])

    def __init__(self, b, ):
        fake = Faker("En")
        Faker.seed(time.time())
        self.name = fake.word()
        self.grade = fake.int()
        self.scale = fake.int()
        self.online_consultation = fake.isinstance()
        self.main_departments = fake.word()
        self.number_of_patients = fake.int()
        self.service = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.quality = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])
        self.effectiveness = fake.word(ext_word_list=['Best', 'Good', 'General','Ok'])

        mes = """Вы можете задать следующие вопросы：
-What kind of services does hospital 1 provide?
-What kind of quality does hospital 2 provide?
-What kind of effectiveness does hospital 2 provide?

        """

        answer = 'Apples are very sweet and have a hard taste'
        print(morph.lat2cyr(answer))

    def readData(self):
        # Read table data
        book = xlrd.open_workbook('hospital.csv')
        sheet1 = book.sheets()[0]
        nrows = sheet1.nrows
        ncols = sheet1.ncols
        values = []
        for row in range(nrows):
            row_values = sheet1.row_values(row)
            values.append(row_values)
        return values, nrows, ncols

    def send(self):
        # 接收用户输入信息
        msg = self.ui.textEdit_2.toPlainText()
        print(msg)
        self.ui.textBrowser_2.append('user:')
        self.ui.textBrowser_2.append(msg)
        self.ui.textBrowser_2.append('')

        # 删除 ？，。

        # 分词 俄语原形
        lis = [n for n in msg.split(' ')]
        lis2 = []
        print(lis)
        for word in lis:
            p = morph.parse(word)[0]
            lis2.append(p.normal_form)
        print(lis2)

        for word in lis2:
            for k, v in ('hospital.csv'):
                if word.lower() == k:
                    # 是第几个问题
                    question_num = v
                    # print('%s is %s' % (k, v))
                else:
                    continue
        name = ''
        for word in lis2:
            for k, v in ('hospital.csv'):
                # 哪个医院
                if word.lower() == k.lower():
                    Name = v
                else:
                    continue
        print(question_num, name)

        if name == '':
            info_msg = 'please tell which fruit you want to ask'

        else:
            data = self.readData()
            nrows = data[1]
            values = data[0]
            ncols = data[2]
            for row in range(nrows):
                cell = values[row][1]
                if name.lower() == cell.lower():
                    itemNum = row
                    print(itemNum)
                    print(values[itemNum])
                    break
                else:
                    continue

            name_sentence = morph.parse(name)[0].make_agree_with_number(2).word

            if question_num == 1:
                answer = f'{name_sentence} {values[itemNum][8]}service'
            elif question_num == 2:
                if values[itemNum][6] == 0:
                    answer = f'{name_sentence} {values[itemNum][9]} quality'

            elif question_num == 3:
                answer = f'{name} {values[itemNum][10]} effectiveness'




search = Conversation()

