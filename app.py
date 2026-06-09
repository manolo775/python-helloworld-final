print("Hello World din VS Code si GitHub!")
# cod python
# print("Hello World din VS Code si GitHub pe 5 iunie!")
import json
import os
from datetime import datetime
# Configurare: Numele fișierului în care se vor salva datele
FICHIER_DATE = "triaj_pacienti.json"
def incarca_datele():
"""Încarcă pacienții din fișierul JSON. Dacă fișierul nu există, returnează o listă goală."""
if not os.path.exists(FICHIER_DATE):
return []
try:
with open(FICHIER_DATE, "r", encoding="utf-8") as f:
return json.load(f)
except Exception as e:
print(f"[EROARE] Nu s-au putut încărca datele: {e}")
return []
def salveaza_datele(lista_pacienti):
"""Salvează lista de pacienți în fișierul JSON."""
try:
with open(FICHIER_DATE, "w", encoding="utf-8") as f:
json.dump(lista_pacienti, f, indent=4, ensure_ascii=False)
print("[INFO] Datele au fost salvate cu succes pe disc.")
except Exception as e:
print(f"[EROARE] Salvarea datelor a eșuat: {e}")
def adauga_pacient():
"""Interfața din terminal pentru introducerea unui pacient nou."""
print("\n--- ÎNREGISTRARE PACIENT NOU ---")
nume = input("Introduceți numele și prenumele pacientului: ").strip()
if not nume:
print("[EROARE] Numele nu poate fi gol!")
return
print("Selectați Codul de Urgență (Protocol Triaj):")
print("1 - CRITIC (Roșu) - Necesită asistență imediată")
print("2 - URGENT (Galben) - Timp de așteptare redus")
print("3 - STANDARD (Verde) - Non-urgent / Consult normal")
optiune_cod = input("Alegeți codul (1-3): ").strip()
if optiune_cod not in ["1", "2", "3"]:
print("[EROARE] Opțiune invalidă! Codul trebuie să fie 1, 2 sau 3.")
return
prioritate = int(optiune_cod)
ora_sosire = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Creăm structura de date (entitatea)
nou_pacient = {
"nume": nume,
"prioritate": prioritate,
"ora_sosire": ora_sosire
}
# Încărcăm starea actuală, adăugăm noul pacient și sortăm coada logic
coada_actuala = incarca_datele()
coada_actuala.append(nou_pacient)
# Sortare arhitecturală: prioritatea (1 înainte de 3), apoi ordinea sosirii (FIFO)
coada_actuala.sort(key=lambda x: (x["prioritate"], x["ora_sosire"]))
# Salvăm starea actualizată în fișier
salveaza_datele(coada_actuala)
print(f"[SUCCES] Pacientul {nume} a fost adăugat în coada de triaj.")
def afiseaza_coada_triaj():
"""Citește datele din fișier și le afișează ordonat în terminal."""
coada_actuala = incarca_datele()
print("\n=======================================================")
print(" COADA ACTUALĂ DE TRIAJ (UPU)")
print("=======================================================")
if not coada_actuala:
print(" [INFO] Nu există pacienți în sala de așteptare.")
print("=======================================================")
return
# Mapare cod numeric -> etichetă vizuală pentru utilizator
etichete_prioritate = {1: "  CRITIC", 2: "  URGENT", 3: "  STANDARD"}
for index, p in enumerate(coada_actuala, start=1):
status_vizual = etichete_prioritate.get(p["prioritate"], "Necunoscut")
print(f"{index}. [{status_vizual}] {p['nume']} | Sosit la: {p['ora_sosire']}")
print("=======================================================\n")
def meniu_principal():
"""Bucla principală a aplicației (Main Event Loop)."""
while True:
print("\n=== SISTEM INTERACTIV HMS - MODUL TRIAJ ===")
print("1. Adaugă pacient nou în triaj")
print("2. Vizualizează coada de așteptare curentă (ordonată)")
print("3. Ieșire program")
optiune = input("Selectați o opțiune (1-3): ").strip()
if optiune == "1":
adauga_pacient()
elif optiune == "2":
afiseaza_coada_triaj()
elif optiune == "3":
print("[INFO] Aplicația se închide. Toate datele rămân salvate în 'triaj_pacienti.json'.")
break
else:
print("[EROARE] Opțiune invalidă! Vă rugăm să selectați 1, 2 sau 3.")
# Punctul de intrare în aplicație
if __name__ == "__main__":
meniu_principal()
import json
import os
from datetime import datetime
FICHIER_DATE = "triaj_pacienti.json"
def incarca_datele():
if not os.path.exists(FICHIER_DATE):
return []
try:
with open(FICHIER_DATE, "r", encoding="utf-8") as f:
return json.load(f)
except Exception:
return []
def salveaza_datele(lista_pacienti):
try:
with open(FICHIER_DATE, "w", encoding="utf-8") as f:
json.dump(lista_pacienti, f, indent=4, ensure_ascii=False)
except Exception:
pass
def adauga_pacient():
print("\n--- ÎNREGISTRARE PACIENT NOU ---")
nume = input("Introduceți numele și prenumele pacientului: ").strip()
if not nume:
print("[EROARE] Numele nu poate fi gol!")
return
print("Selectați Codul de Urgență (Protocol Triaj):")
print("1 - CRITIC (Roșu) - Necesită asistență imediată")
print("2 - URGENT (Galben) - Timp de așteptare redus")
print("3 - STANDARD (Verde) - Non-urgent / Consult normal")
optiune_cod = input("Alegeți codul (1-3): ").strip()
if optiune_cod not in ["1", "2", "3"]:
print("[EROARE] Opțiune invalidă! Codul trebuie să fie 1, 2 sau 3.")
return
prioritate = int(optiune_cod)
ora_sosire = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nou_pacient = {
"nume": nume,
"prioritate": prioritate,
"ora_sosire": ora_sosire
}
coada_actuala = incarca_datele()
coada_actuala.append(nou_pacient)
# DEFECTUL NR. 1: Logica de sortare prioritizează invers (Cazul Verde înaintea celui Roșu)
coada_actuala.sort(key=lambda x: (x["prioritate"], x["ora_sosire"]), reverse=True)
salveaza_datele(coada_actuala)
print(f"[SUCCES] Pacientul {nume} a fost adăugat în coada de triaj.")
def afiseaza_coada_triaj():
coada_actuala = incarca_datele()
print("\n=======================================================")
print(" COADA ACTUALĂ DE TRIAJ (UPU)")
print("=======================================================")
if not coada_actuala:
print(" [INFO] Nu există pacienți în sala de așteptare.")
print("=======================================================")
return
# Se asigură maparea completă pentru a preveni erori de tip KeyError
# DEFECTUL NR. 2: Etichetare vizuală înșelătoare (Zăpăcește utilizatorul)
etichete_prioritate = {1: "  STANDARD", 2: "  URGENT", 3: "  CRITIC"}
for index, p in enumerate(coada_actuala, start=1):
# Utilizare defensivă cu .get() pentru siguranță runtime totală
status_vizual = etichete_prioritate.get(p["prioritate"], "Nespecificat")
# DEFECTUL NR. 3: Mascarea identității pacientului în interfață (Data Masking defectuos)
nume_afisat = p['nume'][:3] + "***"
print(f"{index}. [{status_vizual}] {nume_afisat} | Sosit la: {p['ora_sosire']}")
print("=======================================================\n")
def meniu_principal():
while True:
print("\n=== SISTEM INTERACTIV HMS - MODUL TRIAJ ===")
print("1. Adaugă pacient nou în triaj")
print("2. Vizualizează coada de așteptare curentă (ordonată)")
print("3. Ieșire program")
optiune = input("Selectați o opțiune (1-3): ").strip()
if optiune == "1":
adauga_pacient()
elif optiune == "2":
afiseaza_coada_triaj()
elif optiune == "3":
print("[INFO] Aplicația se închide.")
break
else:
print("[EROARE] Opțiune invalidă!")
if __name__ == "__main__":
meniu_principal()
import json
import os
from datetime import datetime
FICHIER_DATE = "triaj_pacienti.json"
def incarca_datele():
if not os.path.exists(FICHIER_DATE):
return []
try:
with open(FICHIER_DATE, "r", encoding="utf-8") as f:
return json.load(f)
except Exception:
return []
def salveaza_datele(lista_pacienti):
try:
with open(FICHIER_DATE, "w", encoding="utf-8") as f:
json.dump(lista_pacienti, f, indent=4, ensure_ascii=False)
except Exception:
pass
def adauga_pacient():
print("\n--- ÎNREGISTRARE PACIENT NOU ---")
nume = input("Introduceți numele și prenumele pacientului: ").strip()
if not nume:
print("[EROARE] Numele nu poate fi gol!")
return
print("Selectați Codul de Urgență (Protocol Triaj):")
print("1 - CRITIC (Roșu) - Necesită asistență imediată")
print("2 - URGENT (Galben) - Timp de așteptare redus")
print("3 - STANDARD (Verde) - Non-urgent / Consult normal")
optiune_cod = input("Alegeți codul (1-3): ").strip()
if optiune_cod not in ["1", "2", "3"]:
print("[EROARE] Opțiune invalidă! Codul trebuie să fie 1, 2 sau 3.")
return
prioritate = int(optiune_cod)
ora_sosire = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nou_pacient = {
"nume": nume,
"prioritate": prioritate,
"ora_sosire": ora_sosire
}
coada_actuala = incarca_datele()
coada_actuala.append(nou_pacient)
# DEFECTUL NR. 1: Logica de sortare prioritizează invers (Cazul Verde înaintea celui Roșu)
coada_actuala.sort(key=lambda x: (x["prioritate"], x["ora_sosire"]), reverse=True)
salveaza_datele(coada_actuala)
print(f"[SUCCES] Pacientul {nume} a fost adăugat în coada de triaj.")
def afiseaza_coada_triaj():
coada_actuala = incarca_datele()
print("\n=======================================================")
print(" COADA ACTUALĂ DE TRIAJ (UPU)")
print("=======================================================")
if not coada_actuala:
print(" [INFO] Nu există pacienți în sala de așteptare.")
print("=======================================================")
return
# Se asigură maparea completă pentru a preveni erori de tip KeyError
# DEFECTUL NR. 2: Etichetare vizuală înșelătoare (Zăpăcește utilizatorul)
etichete_prioritate = {1: "  STANDARD", 2: "  URGENT", 3: "  CRITIC"}
for index, p in enumerate(coada_actuala, start=1):
# Utilizare defensivă cu .get() pentru siguranță runtime totală
status_vizual = etichete_prioritate.get(p["prioritate"], "Nespecificat")
# DEFECTUL NR. 3: Mascarea identității pacientului în interfață (Data Masking defectuos)
nume_afisat = p['nume'][:3] + "***"
print(f"{index}. [{status_vizual}] {nume_afisat} | Sosit la: {p['ora_sosire']}")
print("=======================================================\n")
def meniu_principal():
while True:
print("\n=== SISTEM INTERACTIV HMS - MODUL TRIAJ ===")
print("1. Adaugă pacient nou în triaj")
print("2. Vizualizează coada de așteptare curentă (ordonată)")
print("3. Ieșire program")
optiune = input("Selectați o opțiune (1-3): ").strip()
if optiune == "1":
adauga_pacient()
elif optiune == "2":
afiseaza_coada_triaj()
elif optiune == "3":
print("[INFO] Aplicația se închide.")
break
else:
print("[EROARE] Opțiune invalidă!")
if __name__ == "__main__":
meniu_principal()
=== SPITAL HMS - MODUL PACIENȚI ===
1. Adăugare pacient nou
2. Căutare pacient / Vizualizare fișă
3. Actualizare fișă medicală (Diagnostic/Alergii)
4. Ieșire
Alege o opțiune (1-4):1
Sima Virgil
Toma Maria
Iancu Ionut
Diaconescu Virgil
Popescu ion
Dorobantu Vladut
Alege o opțiune (1-4):2
diaconu Vladut
Alege o opțiune (1-4):3
diaconu Vladut
Diagnostic: Gripa
Alergii: Niciuna
Fișa medicală a pacientului Diaconescu Vladut a fost actualizată cu succes.
Alege o opțiune (1-4):3
sima Virgil 
Diagnostic: Răceală
Alergii: Penicilină
Fișa medicală a pacientului Sima Virgil a fost actualizată cu succes.
Alege o opțiune (1-4):4
4
=== SPITAL HMS - MODUL PACIENȚI ===
1. Adăugare pacient nou
2. Căutare pacient / Vizualizare fișă
3. Actualizare fișă medicală (Diagnostic/Alergii)
4. Ieșire
Alege o opțiune (1-4):1
Iancu Ionut
Alege o opțiune (1-4):1
Toma Maria
Alege o opțiune (1-4):1
Diaconescu Virgil
Alege o opțiune (1-4):1
Popescu ion
Alege o opțiune (1-4):1
Dorobantu Vladut
Alege o opțiune (1-4):1
Ciusdei Ion
Alege o opțiune (1-4):1
Valentin Popescu
Alege o opțiune (1-4):2
diaconu Vladut
Fișa medicală a pacientului Diaconescu Virgil:
Diagnostic: Gripa
Alergii: Niciuna
Alege o opțiune (1-4):3
diaconu Vladut
Diagnostic: Gripa
Alergii: Niciuna
Fișa medicală a pacientului Diaconescu Virgil a fost actualizată cu succes.
=== SPITAL HMS - MODUL PACIENȚI ===
1. Adăugare pacient nou
2. Căutare pacient / Vizualizare fișă
3. Actualizare fișă medicală (Diagnostic/Alergii)
4. Ieșire
Alege o opțiune (1-4):2
diaconu Vladut
Fișa medicală a pacientului Diaconescu Virgil:
Diagnostic: Gripa
Alergii: Niciuna
Alege o opțiune (1-4):4
===  SISTEM AUTOMAT DE ALERTE FARMACIE ===
 Toate stocurile și termenele de valabilitate sunt optime.
===========================================
=== HMS - MANAGEMENT FARMACIE SPITAL ===
1. Afișare Inventar Detaliat
2. Adăugare / Suplimentare Stoc
3. Eliberare Medicament (Scădere Stoc)
4. Ieșire
Alege o opțiune:2
Nume medicament: Paracetamol
Cantitate de adăugat: 100
2027-12-12 14:30:00
Stocul pentru Paracetamol a fost actualizat. Cantitate adăugată: 100. Stoc curent: 100.
Alege o opțiune:2
Nume medicament: Ibuprofen
Cantitate de adăugat: 50
2027-12-12 14:31:00
Stocul pentru Ibuprofen a fost actualizat. Cantitate adăugată: 50. Stoc curent: 50.
Alege o opțiune:2
Nume medicament: Amoxicilină
Cantitate de adăugat: 200
2027-12-12 14:32:00
Stocul pentru Amox
icilină a fost actualizat. Cantitate adăugată: 200. Stoc curent: 200.
Alege o opțiune:3
Nume medicament: Paracetamol
Cantitate de eliberat: 20
2027-12-12 14:33:00
Stocul pentru Paracetamol a fost actualizat. Cantitate eliberată:
    20. Stoc curent: 80.
Alege o opțiune:4
=== SISTEMUL SE ÎNCHIDE. TOATE DATELE RĂMÂN SALVATE. ===
===  SISTEM AUTOMAT DE ALERTE FARMACIE ===
 Toate stocurile și termenele de valabilitate sunt optime.
===========================================

=== HMS - MANAGEMENT FARMACIE (VERSIUNE CU BUG-URI) ===
1. Afișare Inventar Detaliat
2. Adăugare / Suplimentare Stoc
3. Eliberare Medicament
4. Ieșire
Alege o opțiune:1
=== INVENTAR FARMACIE ===
Nume Medicament | Stoc Curent | Ultima Actualizare
Paracetamol | 80 | 2027-12-12 14:33:00
Ibuprofen | 50 | 2027-12-12 14:31:00
Amoxicilină | 200 | 2027-12-12 14:32:00

Alege o opțiune:3
Nume medicament: Paracetamol
Cantitate de eliberat: 90
2027-12-12 14:35:00
[EROARE] Stoc insuficient pentru Paracetamol. Stoc curent: 80. Nu se poate elibera cantitatea solicitată.
Alege o opțiune:4
=== SISTEMUL SE ÎNCHIDE. TOATE DATELE RĂMÂN SALVATE. ===
