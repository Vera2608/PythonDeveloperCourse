from infectieziekte import Infectieziekte
from persoon import Persoon

t = Infectieziekte("Tuberculose")
t.symptomen = ["hoesten", "vermoeidheid", "niezen", "koorts"]

p = Persoon("Jan")
p.add_ziekte(t)
print(p.overzicht_ziekten())