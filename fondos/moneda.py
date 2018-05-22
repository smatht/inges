# -*- coding: utf-8 -*-


class Moneda:
    # Variables estaticas
    _one = ['', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve']
    _tenp = ['Diez', 'Once', 'Doce', 'Trece', 'Catorce', 'Quince', 'Dieciseis', 'Diecisiete', 'Dieciocho', 'Diecinueve']
    _tenp2 = ['', '', 'Veinte', 'Treinta', 'Cuarenta', 'Cincuenta', 'Sesenta', 'Setenta', 'Ochenta', 'Noventa']

    ###########################################################################################################
    # Constructor
    def __init__(self, valor):
        self.valor = valor

    ###########################################################################################################
    # metodos de clase

    # Uso interno
    def _once(self, num):
        word = ''
        word = self._one[int(num)]
        word = word.strip()
        return word

    # Uso interno
    def _ten(self, num):
        word = ''
        if num[0] == '1':
            word = self._tenp[int(num[1])]
        else:
            text = self._once(num[1])
            word = self._tenp2[int(num[0])]
            if text != '':
                if word != '':
                    word = word + " y " + text
                else:
                    word = text
        word = word.strip()
        return word

    # Uso interno
    def _ten2(self, num):
        word = ''
        if num[0] == '1':
            word = self._tenp[int(num[1])]
        else:
            text = self._once(num[1])
            word = 'Veinti'
            word = word + text
        word = word.strip()
        return word.capitalize()

    # Uso interno
    def _hundred(self, num):
        word = ''
        text = self._ten2(num[1:]) if (num[1:] > 20 and num[1:] < 30) else self._ten(num[1:])
        word = self._one[int(num[0])]
        if num[0] != '0':
            if num == '100':
                word = "Cien"
            elif int(num) < 200:
                word = "Ciento "
            else:
                if word == 'Cinco':
                    word = "Quinientos "
                elif word == 'Siete':
                    word = "Setecientos "
                elif word == 'Nueve':
                    word = "Novecientos "
                else:
                    word = word + "cientos "
        word = word + text
        word = word.strip()
        return word

    # Uso interno
    def _thousand(self, num):
        word = ''
        pref = ''
        text = ''
        length = len(num)
        if length == 6:
            text = self._hundred(num[3:])
            pref = self._hundred(num[:3])
        if length == 5:
            text = self._hundred(num[2:])
            if int(num[:2]) > 20 and int(num[:2]) < 30:
                pref = self._ten2(num[:2])
            else:
                pref = self._ten(num[:2])
        if length == 4:
            text = self._hundred(num[1:])
            word = self._one[int(num[0])]
            if word == 'Uno':
                word = ''
        if num[0] != '0' or num[1] != '0' or num[2] != '0':
            word = word + " Mil "
        word = word + text
        if length == 6 or length == 5:
            word = pref + word
        word = word.strip()
        return word

    # Uso interno
    def _million(self, num):
        word = ''
        pref = ''
        text = ''
        length = len(num)
        if length == 9:
            text = self._thousand(num[3:])
            pref = self._hundred(num[:3])
        if length == 8:
            text = self._thousand(num[2:])
            pref = self._ten(num[:2])
        if length == 7:
            text = self._thousand(num[1:])
            word = self._one[int(num[0])]
        if num[0] != '0' or num[1] != '0' or num[2] != '0':
            word = word + " Million "
        word = word + text
        if length == 9 or length == 8:
            word = pref + word
        word = word.strip()
        return word

    # Uso interno
    def _billion(self, num):
        word = ''
        pref = ''
        text = ''
        length = len(num)
        if length == 12:
            text = self._million(num[3:])
            pref = self._hundred(num[:3])
        if length == 11:
            text = self._million(num[2:])
            pref = self._ten(num[:2])
        if length == 10:
            text = self._million(num[1:])
            word = self._one[int(num[0])]
        if num[0] != '0':
            word = word + " Billion "
        word = word + text
        if length == 12 or length == 11:
            word = pref + word
        word = word.strip()
        return word

    # Uso externo
    def toText(self):
        a = str(int(self.valor))  # Entero
        d = str(round((self.valor-int(self.valor)), 2))[2:]  # Decimal
        leng = len(a)
        num = 'Cero'
        con = 'Cero'
        if len(d) == 1:
            d = d + '0'
        if leng == 1:
            # tratamiento entero
            if a == '0':
                num = 'Cero'
            else:
                num = self._once(a)
        if leng == 2:
            # tratamiento entero
            if int(a) in range(21, 30):
                num = self._ten2(a)
            else:
                num = self._ten(a)
            # tratamiento decimal
            if int(d) in range(21, 30):
                con = self._ten2(d)
            else:
                con = self._ten(d)
        if leng == 3:
            num = self._hundred(a)
        if leng > 3 and leng < 7:
            num = self._thousand(a)
        if leng > 6 and leng < 10:
            num = self._million(a)
        if leng > 9 and leng < 13:
            num = self._billion(a)

        # tratamiento entero
        if d == '00':
            d = '0';
        # if d != '00':
        #     if int(d) in range(21, 30):
        #         con = self._ten2(d)
        #     else:
        #         con = self._ten(d)
        return  (num + ' CON ' + d + '/100').upper() + ' cv.'
