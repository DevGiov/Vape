# Vape Calculator

Calcolatore CLI per liquidi svapo (VG/PG/aroma/nicotina).

## Installazione

```bash
pip install -e .
```

Oppure esegui direttamente:

```bash
python vape.py --vg 50 --pg 50
```

## Utilizzo

```bash
python vape.py --vg <ml> --pg <ml> [opzioni]
```

### Argomenti

| Argomento | Obbligatorio | Default | Descrizione |
|---|---|---|---|
| `--vg` | ✅ | — | ml di VG da aggiungere |
| `--pg` | ✅ | — | ml di PG da aggiungere |
| `--aroma` | ❌ | 10.0 | ml di aroma concentrato |
| `--nic` | ❌ | 10.0 | ml di booster nicotina |
| `--nic-strength` | ❌ | 20.0 | gradazione booster in mg/ml |
| `--aroma-base` | ❌ | pg | base dell'aroma: `pg` o `vg` |

### Esempi

Calcolo base (50ml VG + 50ml PG):

```bash
python vape.py --vg 50 --pg 50
```

Con aroma e nicotina personalizzati:

```bash
python vape.py --vg 40 --pg 40 --aroma 15 --nic 10 --nic-strength 18
```

Aroma in base VG:

```bash
python vape.py --vg 60 --pg 40 --aroma-base vg
```

## Output

Il tool restituisce:

- Quantità totale di liquido
- Nicotina finale (mg/ml) e totale (mg)
- Concentrazione aroma (%)
- Volumi e percentuali VG/PG
- Rapporto finale VG/PG

## License

MIT — Copyright (c) 2026 Danilo De Giovanni
