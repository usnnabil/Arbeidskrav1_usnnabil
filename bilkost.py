# Arbeidskrav 1 i PY1010-1 24H Grunnleggende programmering med Python
# Skrevet av: Nabil Safadi
# Beskrivelse: Program som regner ut årlige kostnader for elbil og bensinbil

Dager_i_aaret = 365
Kjoerelengde = 10000
Forsikring_elbil_kr_aar = 5000
Forsikring_bensinbil_kr_aar = 7500
Trafikkforsikringsavgift_kr_dag = 8.38
Drivstofforbruk_elbil_kWh_km = 0.2
Stroempris_kr_kWh = 2.0
Drivstofforbruk_bensinbil_kr_km = 1.0
Bomavgift_elbil_kr_km = 0.1
Bomavgift_bensinbil_kr_km = 0.3

# Like utgifter for begge biler
Trafikkforsikringsavgift_aar = Trafikkforsikringsavgift_kr_dag * Dager_i_aaret

# Elbil - utgifter
Drivstoff_utgift_elbil_aar = Drivstofforbruk_elbil_kWh_km * Stroempris_kr_kWh * Kjoerelengde
Bomavgift_elbil_aar = Bomavgift_elbil_kr_km * Kjoerelengde
Elbil_utgifter_aar = (Forsikring_elbil_kr_aar + Trafikkforsikringsavgift_aar
                      + Drivstoff_utgift_elbil_aar + Bomavgift_elbil_aar)

# Bensinbil - utgifter
Drivstoff_utgift_bensinbil_aar = Drivstofforbruk_bensinbil_kr_km * Kjoerelengde
Bomavgift_bensinbil_aar = Bomavgift_bensinbil_kr_km * Kjoerelengde
Bensinbil_utgifter_aar = (Forsikring_bensinbil_kr_aar + Trafikkforsikringsavgift_aar
                         + Drivstoff_utgift_bensinbil_aar + Bomavgift_bensinbil_aar)

#Differanse i utgifter mellom elbil og bensinbil
Differanse = Bensinbil_utgifter_aar - Elbil_utgifter_aar

print('Elbil utgifter per år: ', Elbil_utgifter_aar, 'kr')
print('Bensinbil utgifter per år: ', Bensinbil_utgifter_aar, 'kr')
print('Differanse i utgifter mellom elbil og bensinbil: ', Differanse, 'kr per år i elbilens favør')