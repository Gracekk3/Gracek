def vypocet_uspory(pocatecni_vklad, urokova_mira, doba_uspor):
    return pocatecni_vklad * (1 + urokova_mira / 100) ** doba_uspor

pocatecni_vklad = float(input("Zadejte počáteční vklad (Kč): "))
urokova_mira = float(input("Zadejte roční úrokovou míru (%): "))
doba_uspor = int(input("Zadejte dobu úspor (roky): "))

konecna_castka = vypocet_uspory(pocatecni_vklad, urokova_mira, doba_uspor)

print("Konečná částka úspory po", doba_uspor, "letech je", round(konecna_castka, 2), "Kč.")
