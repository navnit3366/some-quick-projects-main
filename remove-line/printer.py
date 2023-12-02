'''printer v0.0'''


def pprint(n, *args, **kwargs):
    n = int(n)
    deb = 2 * n * ' ' + '|'
    print(deb, *args, **kwargs)


class print_dataclass:

    def __init__(self, prev_len, prev_end, __niv__) -> None:
        self.prev_len = prev_len
        self.prev_end = prev_end
        self.__niv__ = __niv__
        self.check_data()

    def check_data(self):
        assert isinstance(self.__niv__, int)
        assert isinstance(self.prev_len, int)
        assert self.prev_len >= 0
        assert isinstance(self.prev_end, str)

    def __str__(self):
        return f"len:{self.prev_len}-end:{self.prev_end}-niv:{self.__niv__}"


class best_print:
    '''
    # use
    >>> printer = best_print()
    print("rr")
    printer.print("eeeeeee")
    printer.print("fff") #print "fff" without his end
    printer.erase_cur_line() #erase "fff" by rewriting with blank
    printer.erase_cur_line() #do nothing
    printer.erase_cur_line() #do nothing
    
    print("3")
    '''

    def __init__(self, d=None) -> None:
        if d == None:
            self.prev_len = 0  #len of the last line
            self.prev_end = ""  #end of the last print asked
            self.__niv__ = 0
        elif isinstance(d, print_dataclass):
            self.prev_len = d.prev_len  #len of the last line
            self.prev_end = d.prev_end  #end of the last print asked
            self.__niv__ = d.__niv__
            #print("'",self.__niv__)
        else:
            print("d shoyld be None or a instance of ")

    def get_data(self):
        return print_dataclass(self.prev_len, self.prev_end, self.__niv__)

    def print(self, *values, **b):
        '''
        # use
        >>> printer = best_print()
        printer.print("my line")
        '''

        #save lenght #will be reuse if the user want to erase that print
        self.prev_len = len(str(values[-1]).split("\n")[-1])
        #print(self.prev_len,end="")
        # get niv
        if b.get("in_fct"):
            self.__niv__ = int(self.__niv__ or 0) + 1
        self.__niv__ = int(self.__niv__ or 0)
        deb = 2 * self.__niv__ * ' ' + ' | '

        # add (last "end" value) and (niv) at the beginning
        values = list(values)  #tuple to list #for modif
        values[0] = self.prev_end + deb + str(values[0])
        # reset add (last "end") by the new one
        self.prev_end = b["end"] if "end" in b else "\n"

        #set end to ""
        b["end"] = ""
        ###remove kwarks that is not used for print
        if "in_fct" in b: del b['in_fct']

        # print
        #self.pprint(*values, **b)
        print(*values, **b)

        return self.get_data()

    def erase_cur_line(self, len_nb: int = None):
        '''
        remove last line.
        Can't remove more than one line ahead
        '''
        len_nb = len_nb or self.prev_len
        #print("-",len_nb,end="",sep="")
        print('\r', " " * len_nb, "\r", sep="",
              end="")  #get at deb, rewrite with blank, get at deb
        self.prev_end = ""
        self.prev_len = 0
        return self.get_data()

    def reset_printer(self):
        '''prevent problem when returning to previous level'''
        self.prev_end = "\n"
        self.prev_len = 0

    def change_niv(self):
        '''reset printer and send data'''
        self.reset_printer()
        return self.get_data()

    def print_progress(self, i, n, newline=False):
        end = "\n" if newline else ""
        if i == n: end = "\n"
        self.print(f"Progress [{'#'*i + ' ' * (n-i)}]\r", end=end)


if __name__ == "__main__":

    def test_fct(d):
        printer = best_print(d)
        printer.print("eeeeeee_in_fct", in_fct=True)
        printer.print("eeeeeee_in_fct")
        test_fct2(printer.change_niv())
        printer.print("eeeeeee_in_fct")
        printer.print("eeeeeee_in_fct")
        #printer.erase_cur_line()

    def test_fct2(d):
        printer = best_print(d)
        printer.print("eeeeeee_in_fct2", in_fct=True)
        printer.print("eeeeeee_in_fct2")
        #printer.erase_cur_line()
        return printer

    printer = best_print()
    #print("rr")
    printer.print("eeeeeee")
    printer.print("eeeeeee")
    printer.print("fff")  #print "fff" without his end
    printer.erase_cur_line()  #erase "fff" by rewriting with blank
    printer.erase_cur_line()  #do nothing
    printer.erase_cur_line()  #do nothing
    test_fct(d=printer.change_niv())

    printer.print("fff")
    print("3")
    #prend le "niv" en local et le "end" en global et le "len" en global
