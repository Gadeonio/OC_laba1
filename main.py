# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy
n_kol = 0

class myData:
    def __init__(self, id, count, priority, start):
        self.id = id
        self.count = count
        self.priority = priority
        self.start = start

    '''def get_by_id(self, idet):
        return self if self.id == idet else None'''



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

    def priority_id(self, data, n_kol):
        element_priority = None
        for element in data:
            
            if element.count == 0:
                continue
            if element_priority is None:
                element_priority = element
            elif element_priority.priority < element.priority:
                element_priority = element
        return -1 if element_priority is None else element_priority.id - 1

    def give_id(self, data, tick=0):
        data_in = []
        global n_kol
        for element in data:
            n_kol = n_kol + 1
            if element.count == 0:
                continue
            if element.start > tick:
                continue
            else:
                data_in.append(element)
        id_start = self.priority_id(data_in, n_kol)
        if id_start == -1:
            id_start = self.priority_id(data, n_kol)
        return id_start

    def min_count_id(self, data, priority=0):
        element_priority = None
        global n_kol
        for element in data:
            n_kol = n_kol + 1
            if element.count == 0:
                continue
            if element_priority is None:
                element_priority = element
            elif element_priority.count > element.count:
                element_priority = element
        return -1 if element_priority is None else element_priority.id - 1


class Strategy_FIFS(Strategy):
    def do_algorithm(self, data):
        result = ""
        data_res = data
        flag_run = True
        #Количество итераций
        n = 0
        global n_kol
        n_kol = 0
        while flag_run:
            n_kol = n_kol + 1
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
                    if n >= mD.start:
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
                
                    if mD.count == 0:
                        continue
                    flag_run = True
                    if current_id == -1:
                        current_id = mD.id
                    if mD.priority != 0:
                        if n >= mD.start:
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
        global n_kol
        n_kol = 0
        n_while = 0
        while flag_run:
            n_kol = n_kol + 1
            current_priority = -1
            if n_current == 0:
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
                        if n >= mD.start:
                            if current_priority < mD.priority:
                                current_id = mD.id
                                current_priority = mD.priority

                while data_res[current_id - 1].count == 0:
                    n_kol = n_kol + 1
                    n_while = n_while + 1
                    
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
                else:
                    result = result + '_'
                if n_current == n_robin:
                    n_current = 0
        print("Среднее время готовности", n / n_kol)
        return result


class Strategy_SJF(Strategy):
    def do_algorithm(self, data):
        '''result = ""
        data_res = data
        sum_proc_time = 0
        for element in data:
            sum_proc_time = sum_proc_time + element.count
        while sum_proc_time > 0:
            id_min = self.min_count_id(data_res)
            while data_res[id_min].count > 0:
                data_res[id_min].count = data_res[id_min].count - 1
                sum_proc_time = sum_proc_time - 1
                result = result + str(id_min + 1)
        return result'''
        n = 0
        global n_kol
        n_kol = 0
        result = ""
        data_res = data
        sum_proc_time = 0
        for element in data:
            n_kol = n_kol + 1
            sum_proc_time = sum_proc_time + element.count
        sum_proc_time_max = sum_proc_time
        while sum_proc_time > 0:
            n_kol = n_kol + 1
            id_start = self.give_id(data, sum_proc_time_max - sum_proc_time)
            if id_start == -1:
                id_min = self.min_count_id(data_res)
            else:
                id_min = id_start
            while data_res[id_min].count > 0:
                n_kol = n_kol + 1
                n = n + 1
                data_res[id_min].count = data_res[id_min].count - 1
                sum_proc_time = sum_proc_time - 1
                result = result + str(id_min + 1)
        print("Среднее время готовности", n / n_kol)
        return result

class Strategy_Pong(Strategy):
    def do_algorithm(self, data):
        result = ""
        data_res = data
        n = 0
        global n_kol
        n_kol = 0
        sum_proc_time = 0
        for element in data:
            n_kol = n_kol + 1
            sum_proc_time = sum_proc_time + element.count
        sum_proc_time_max = sum_proc_time
        while sum_proc_time > 0:
            n_kol = n_kol + 1
            partners = self.give_partners(data_res, sum_proc_time_max - sum_proc_time)
            
            while self.partners_not_null(partners):
                n_kol = n_kol + 1
                for element in partners:
                    n_kol = n_kol + 1
                    n = n + 1
                    element.count = element.count - 1
                    id_change = element.id - 1
                    data_res[id_change].count = element.count
                    sum_proc_time = sum_proc_time - 1
                    result = result + str(id_change + 1)
        print("Среднее время готовности", n / n_kol)
        return result

    def give_partners(self, data, tick):
        partners = []
        data_res = copy.deepcopy(data)
        id_start = self.give_id(data, tick)
        if id_start == -1:
            id_min = self.min_count_id(data_res)
        else:
            id_min = id_start
        element = data[id_min]
        partners.append(element)
        data_res[id_min].count = 0
        id_start = self.give_id(data_res, tick)
        if id_start == -1:
            id_min = self.min_count_id(data_res)
        else:
            id_min = id_start
        if data_res[id_min].count != 0:
            partners.append(data_res[id_min])
        return partners

    def partners_not_null(self, data):
        global n_kol
        not_null = True
        for element in data:
            n_kol = n_kol + 1
            if element is None:
                not_null = False
            if element.count == 0:
                not_null = False
        return not_null





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    context = Context(Strategy_FIFS())
    context.do_some_business_logic()
    context = Context(Strategy_RR_soft())
    context.do_some_business_logic()
    context = Context(Strategy_SJF())
    context.do_some_business_logic()
    context = Context(Strategy_Pong())
    context.do_some_business_logic()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
