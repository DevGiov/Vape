#!/usr/bin/env python3
import argparse
import sys


def positive_float(value):
    try:
        v = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Valore non valido: {value}")
    if v < 0:
        raise argparse.ArgumentTypeError(f"Il valore deve essere >= 0: {value}")
    return v


def calcola_liquido(vg_ml, pg_ml, aroma_ml, nic_ml, nic_strength_mg_ml, aroma_in_pg=True):
    aroma_pg = aroma_ml if aroma_in_pg else 0.0
    aroma_vg = 0.0 if aroma_in_pg else aroma_ml

    nic_pg = nic_ml * 0.5
    nic_vg = nic_ml * 0.5

    totale_ml = vg_ml + pg_ml + aroma_ml + nic_ml
    totale_pg = pg_ml + aroma_pg + nic_pg
    totale_vg = vg_ml + aroma_vg + nic_vg
    nic_tot_mg = nic_ml * nic_strength_mg_ml

    nic_finale_mg_ml = nic_tot_mg / totale_ml if totale_ml > 0 else 0.0
    aroma_perc = (aroma_ml / totale_ml) * 100 if totale_ml > 0 else 0.0
    vg_perc = (totale_vg / totale_ml) * 100 if totale_ml > 0 else 0.0
    pg_perc = (totale_pg / totale_ml) * 100 if totale_ml > 0 else 0.0

    return {
        "totale_ml": totale_ml,
        "nicotina_mg_ml": nic_finale_mg_ml,
        "aroma_percento": aroma_perc,
        "vg_totale_ml": totale_vg,
        "pg_totale_ml": totale_pg,
        "vg_percento": vg_perc,
        "pg_percento": pg_perc,
        "rapporto": f"{vg_perc:.2f}/{pg_perc:.2f}",
        "nicotina_totale_mg": nic_tot_mg,
    }


def stampa_risultato(r):
    print("\n=== Liquido finale ===")
    print(f"Quantità totale        : {r['totale_ml']:.2f} ml")
    print(f"Nicotina finale        : {r['nicotina_mg_ml']:.2f} mg/ml")
    print(f"Nicotina totale        : {r['nicotina_totale_mg']:.2f} mg")
    print(f"Concentrazione aroma   : {r['aroma_percento']:.2f}%")
    print(f"VG totale              : {r['vg_totale_ml']:.2f} ml ({r['vg_percento']:.2f}%)")
    print(f"PG totale              : {r['pg_totale_ml']:.2f} ml ({r['pg_percento']:.2f}%)")
    print(f"Rapporto finale VG/PG  : {r['rapporto']}")


def main():
    parser = argparse.ArgumentParser(
        description="Calcolatore CLI per liquidi svapo (VG/PG/aroma/nicotina)."
    )

    parser.add_argument("--vg", type=positive_float, required=True,
                        help="ml di VG da aggiungere")
    parser.add_argument("--pg", type=positive_float, required=True,
                        help="ml di PG da aggiungere")
    parser.add_argument("--aroma", type=positive_float, default=10.0,
                        help="ml di aroma concentrato (default: 10)")
    parser.add_argument("--nic", type=positive_float, default=10.0,
                        help="ml di booster nicotina (default: 10)")
    parser.add_argument("--nic-strength", type=positive_float, default=20.0,
                        help="gradazione booster in mg/ml (default: 20)")
    parser.add_argument("--aroma-base", choices=["pg", "vg"], default="pg",
                        help="base dell'aroma concentrato: pg o vg (default: pg)")

    args = parser.parse_args()

    risultato = calcola_liquido(
        vg_ml=args.vg,
        pg_ml=args.pg,
        aroma_ml=args.aroma,
        nic_ml=args.nic,
        nic_strength_mg_ml=args.nic_strength,
        aroma_in_pg=(args.aroma_base == "pg"),
    )

    stampa_risultato(risultato)


if __name__ == "__main__":
    sys.exit(main())
