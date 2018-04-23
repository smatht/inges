from django.core.exceptions import ObjectDoesNotExist

from fondos.models import Caja, TipoCaja


def getOrOpenCaja(tipoCaja, obra):
    try:
        cja = Caja.objects.get(tipoCaja=tipoCaja, destino=obra, fCierre=None)
    except ObjectDoesNotExist:
        cja = abrirCaja(obra, tipoCaja)
    return cja


def abrirCaja(obra, tipoCaja = None):
    if tipoCaja is None:
        tipoCaja = TipoCaja.objects.get(pk=1)
    cja = Caja(tipoCaja=tipoCaja, destino=obra)
    cja.save()
    return cja


class Moneda:
    # Variables estaticas
    one = ['', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve']
    tenp = ['Diez', 'Once', 'Doce', 'Trece', 'Catorce', 'Quince', 'Dieciseis', 'Diecisiete', 'Dieciocho', 'Diecinueve']
    tenp2 = ['', '', 'Veinte', 'Treinta', 'Cuarenta', 'Cincuenta', 'Sesenta', 'Setenta', 'Ochenta', 'Noventa']

    ###########################################################################################################
    # Constructor
    def __init__(self, valor):
        self.valor = valor

    ###########################################################################################################
    # metodos de clase

    # Uso interno
    def once(self, num):
        word = ''
        word = self.one[int(num)]
        word = word.strip()
        return word

    # Uso interno
    def ten(self, num):
        word = ''
        if num[0] == '1':
            word = self.tenp[int(num[1])]
        else:
            text = self.once(num[1])
            word = self.tenp2[int(num[0])]
            if text != '':
                if word != '':
                    word = word + " y " + text
                else:
                    word = text
        word = word.strip()
        return word

    # Uso interno
    def ten2(self, num):
        word = ''
        if num[0] == '1':
            word = self.tenp[int(num[1])]
        else:
            text = self.once(num[1])
            word = 'Veinti'
            word = word + text
        word = word.strip()
        return word.capitalize()

    # Uso interno
    def hundred(self, num):
        word = ''
        text = self.ten2(num[1:]) if (int(float(num[1:])) > 20 and int(float(num[1:])) < 30) else self.ten(num[1:])
        word = self.one[int(num[0])]
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
    def thousand(self, num):
        word = ''
        pref = ''
        text = ''
        length = len(num)
        if length == 6:
            text = self.hundred(num[3:])
            pref = self.hundred(num[:3])
        if length == 5:
            text = self.hundred(num[2:])
            if int(num[:2]) > 19 and int(num[:2]) < 30:
                pref = self.ten2(num[:2])
            else:
                pref = self.ten(num[:2])
        if length == 4:
            text = self.hundred(num[1:])
            word = self.one[int(num[0])]
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
    def million(self, num):
        word = ''
        pref = ''
        text = ''
        length = len(num)
        if length == 9:
            text = self.thousand(num[3:])
            pref = self.hundred(num[:3])
        if length == 8:
            text = self.thousand(num[2:])
            pref = self.ten(num[:2])
        if length == 7:
            text = self.thousand(num[1:])
            word = self.one[int(num[0])]
        if num[0] != '0' or num[1] != '0' or num[2] != '0':
            word = word + " Million "
        word = word + text
        if length == 9 or length == 8:
            word = pref + word
        word = word.strip()
        return word

    # Uso interno
    def billion(self, num):
        word = ''
        pref = ''
        text = ''
        length = len(num)
        if length == 12:
            text = self.million(num[3:])
            pref = self.hundred(num[:3])
        if length == 11:
            text = self.million(num[2:])
            pref = self.ten(num[:2])
        if length == 10:
            text = self.million(num[1:])
            word = self.one[int(num[0])]
        if num[0] != '0':
            word = word + " Billion "
        word = word + text
        if length == 12 or length == 11:
            word = pref + word
        word = word.strip()
        return word

    # Uso externo
    def toText(self):
        a = str(int(self.valor))
        leng = len(a)
        num = 'Cero'
        if leng == 1:
            if a == '0':
                num = 'Cero'
            else:
                num = self.once(a)
        if leng == 2:
            if int(a) in range(21, 30):
                num = self.ten2(a)
            else:
                num = self.ten(a)
        if leng == 3:
            num = self.hundred(a)
        if leng > 3 and leng < 7:
            num = self.thousand(a)
        if leng > 6 and leng < 10:
            num = self.million(a)
        if leng > 9 and leng < 13:
            num = self.billion(a)
        return num
