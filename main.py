# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class myData:
    def __init__(self, id, count, priority, pred):
        self.id = id
        self.count = count
        self.priority = priority
        self.pred = pred

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self, strategy):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def do_some_business_logic(self):
        massive = []
        with open("examp.txt", "r") as f:
            for line in f:
                lines = line

                id = int(lines[:lines.find(" ")])
                lines = lines[lines.find(" ") + 1: ]

                count = int(lines[:lines.find(" ")])
                lines = lines[lines.find(" ") + 1:]

                priority = int(lines[:lines.find(" ")])
                lines = lines[lines.find(" ") + 1:]

                pred = int(lines)

                mD = myData(id, count, priority, pred)
                massive.append(mD)
        result = self._strategy.do_algorithm(massive)
        print(result)


class Strategy:
    def do_algorithm(self, data):
        pass


class Strategy_FIFS(Strategy):
    def do_algorithm(self, data):
        result = ""
        data_res = data
        flag_run = True
        #Количество итераций
        n = 0
        n_kol = 0
        while flag_run:
            flag_run = False
            current_priority = -1
            current_id = -1
            for mD in data_res:
                n_kol = n_kol + 1
                if mD.count == 0:
                    continue
                flag_run = True
                if current_id == -1:
                    current_id = mD.id
                if mD.priority != 0:
                    if n >= mD.pred:
                        if current_priority < mD.priority:
                            current_id = mD.id
                            current_priority = mD.priority
            if current_id != -1:
                n = n + 1
                ident = current_id - 1
                result = result + str(current_id)
                data_res[ident].count = data_res[ident].count - 1
        print("Среднее время готовности", n/n_kol)
        return result


'''class Strategy_RR_soft(Strategy):
    def do_algorithm(self, data):
        n_robin = 2
        n_current = 0
        result = ""
        data_res = data
        flag_run = True
        # Количество итераций
        n = 0
        n_kol = 0
        while flag_run:
            if n_current == 0:
                flag_run = False
                current_priority = -1
                current_id = -1
                for mD in data_res:
                    n_kol = n_kol + 1
                    if mD.count == 0:
                        continue
                    flag_run = True
                    if current_id == -1:
                        current_id = mD.id
                    if mD.priority != 0:
                        if n >= mD.pred:
                            if current_priority < mD.priority:
                                current_id = mD.id
                                current_priority = mD.priority
            
            if current_id != -1 and n_current < n_robin:
                n = n + 1
                n_current = n_current + 1
                if 
                
                ident = current_id - 1
                result = result + str(current_id)
                data_res[ident].count = data_res[ident].count - 1
            else:
                n_current = 0
                
        print("Среднее время готовности", n / n_kol)
        return result
'''

class Strategy_RR_soft(Strategy):
    def do_algorithm(self, data):
        n_robin = 2
        n_current = 0
        current_id = 0
        result = ""
        data_res = data
        flag_run = True
        # Количество итераций
        n = 0
        n_kol = 0
        n_while = 0
        while flag_run:
            n_kol = n_kol + 1
            if n_current == 0:
                n_kol = n_kol + 1
                current_id = current_id + 1
                if current_id >= len(data_res) + 1:
                    current_id = 1
                for mD in data_res:
                    n_kol = n_kol + 1
                    if mD.count == 0:
                        continue
                    flag_run = True
                    if current_id == -1:
                        current_id = mD.id
                    if mD.priority != 0:
                        if n >= mD.pred:
                            if current_priority < mD.priority:
                                current_id = mD.id
                                current_priority = mD.priority

                while data_res[current_id - 1].count == 0:
                    n_while = n_while + 1
                    n_kol = n_kol + 1
                    current_id = current_id + 1
                    if current_id >= len(data_res) + 1:
                        current_id = 1
                    if n_while == len(data_res) + 1:
                        flag_run = False
                        break

            if current_id != 0:
                n_current = n_current + 1
                n = n + 1
                ident = current_id - 1
                if data_res[ident].count != 0:
                    data_res[ident].count = data_res[ident].count - 1
                    result = result + str(current_id)
                if n_current == n_robin:
                    n_current = 0
        print("Среднее время готовности", n / n_kol)
        return result
class Strategy_SJF(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #context = Context(Strategy_FIFS())
    context = Context(Strategy_RR_soft())
    context.do_some_business_logic()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
