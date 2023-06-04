# Python Data Visualization

Ez a projekt bemutatja, hogyan lehet a `pandas`, `matplotlib` és `seaborn` Python csomagokat használni adatok átlagolásához hónapok szerint és az eredmények vizualizálásához.

## Használat

1. Klónozd le ezt a repót a gépedre.
2. Telepítsd a szükséges csomagokat a következő parancs segítségével: `pip install -r requirements.txt`.
3. Helyezd az `adatok2.csv` fájlt a scripttel azonos könyvtárba.
4. Futtasd a scriptet a `python app.py` parancs segítségével.

## Funkciók

A script a következő funkciókat tartalmazza:

1. Beolvassa az `adatok2.csv` fájlt.
2. Átlagolja az 'ESTIMATE' oszlop értékeit hónapok szerint.
3. Négy diagramot készít a kapott adatokból:
   - Egy vonaldiagram az átlagos értékek megjelenítésére hónapok szerint a matplotlib segítségével.
   - Egy oszlopdiagram ugyanezeknek az adatoknak a megjelenítésére a seaborn segítségével.
   - Egy hisztogram a 'ESTIMATE' oszlop értékeinek eloszlásának megjelenítésére a matplotlib segítségével.
   - Egy dobozdiagram a 'ESTIMATE' oszlop értékeinek eloszlásának megjelenítésére a seaborn segítségével.
