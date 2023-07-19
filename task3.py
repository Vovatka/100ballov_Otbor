line = "ЙlДuюdЧЛWиlшSюbяNiGRtLJtжяGфFgцiи"
alph_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alph_en = "abcdefghijklmnopqrstuvwxy"
glasn_ru = "еёиоуыэюя"
glasn_en = "aeiouy"


def sog(s):
    """Возвращает истину, 
    если буква s является согласной"""
    if s not in glasn_en + glasn_ru:
        return True
    return False


def glas(s):
    """Возвращает истину, 
    если буква s является гласной"""
    if not sog(s):
        return True
    return False


def en(s):
    """Возвращает истину, 
    если буква s относится к английскому алфавиту"""
    if s in alph_en:
        return True
    return False


def ru(s):
    """Возвращает истину, 
    если буква s относится к русскому алфавиту"""
    if s in alph_ru:
        return True
    return False


new_line = ""
for s in line:
    if (((not (ru(s) <= sog(s))) and s.islower()) or
            ((not (glas(s) or s.isupper())) and en(s))):
        new_line += s
print(new_line)
