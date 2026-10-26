# J2 = Gemini: otrā tiesneša saskaņas pārbaude (iterācijas 0 pāri)

**Kāpēc.** Mūsu tiesnesis J1 (Claude Opus 5.5) ir tās pašas saimes modelis kā ģenerators (Sonnet 5.5). Lai izslēgtu "savējo" nobīdi, tie paši pāri jāvērtē citas saimes tiesnesim — Gemini — ar **tieši to pašu tiesneša promptu un tām pašām pakām**, neko nemainot. Pēc tam es salīdzinu Gemini un Opus spriedumus pāris pa pārim (preference, elementi, kritēriji) un pierakstu saskaņu pārskatā (30 §10, §8).

**Izlase (fiksēta pirms vērtēšanas, `J2_selection.csv`).** 10 pāri — viens no katra uzdevuma T01–T10: nepāra uzdevumi — kanons+prompts v1.0 pret A (bez prompta); pāra uzdevumi — kanons+prompts v1.0 pret B (vispārīgs padomdevēja prompts). Atkārtojuma numurs noteikts pēc formulas ((n−1)÷2 mod 3)+1, lai neizvēlētos "ērtus" pārus. Katrs pāris divās kārtībās (12 un 21) = 20 pakas.

## Faili
| Fails | Kas tas ir |
|---|---|
| `J2_GEMINI_A_kartiba_12_10_pakas.md` | **Obligātā daļa.** 10 pakas (kārtība 12), katra pilnīga: tiesneša prompts + uzdevums + atslēga + 2 anonīmas atbildes + izvades formāts. ~2 300–3 100 vārdi katra. |
| `J2_GEMINI_B_kartiba_21_10_pakas.md` | **Ieteicamā daļa.** Tie paši 10 pāri apgrieztā kārtībā (atbilde 1 ↔ 2). Vajadzīga, lai pārbaudītu pozīcijas nobīdi un piemērotu "abas kārtības sakrīt" noteikumu arī Gemini. |
| `packs/*.md` | Tās pašas 20 pakas pa vienai failā (ja ērtāk ielīmēt no atsevišķa faila). |
| `29c_E5_JUDGE_PROMPT_v1.md` | Tiesneša prompts tāds, kāds ir protokolā 29c (tas pats teksts, kas katras pakas sākumā). Atsevišķi ielīmēt **nevajag** — tas jau ir pakā. |
| `J2_selection.csv` | Izlases saraksts ar SHA-256 katrai pakai (reproducējamība). |
| `summary_iter_0_J1_rezultati_NERADIT_GEMINI.md` | Mūsu J1 rezultāti — **tikai tev**. Gemini tos nedrīkst redzēt, citādi tas nav akls vērtējums. |

## Procedūra (katrai pakai)
1. **Jauna Gemini saruna** (bez atmiņas, bez iepriekšējām pakām, bez failiem par Jirgensona modeli). Ja Gemini ir "personalizācija"/atmiņa — izslēgt.
2. Ielīmē **visu bloku** starp `========== PAKA k/10 ==========` un `========== PAKAS BEIGAS ==========` (pašas līnijas var neņemt). Neko nepievieno, nepaskaidro, neuzvedini.
3. Gemini atbildē jābūt 6 soļiem prozā un beigās ```json blokam. Ja JSON bloka nav vai tas ir nepilnīgs — vienu reizi atbildi "Please output the JSON block exactly in the required format." un ņem to.
4. **Saglabā VISU Gemini atbildi** (ne tikai JSON) failā ar pakas nosaukumu, piem. `T01_C-v1.0-r1_vs_A-r1_12.md`, mapē `E:\GitHub\E5_eksperiments\iter_0\judgments_J2_gemini\` (vai atsūti man šeit). Pieraksti Gemini modeļa versiju (piem. "Gemini 2.5 Pro", datums) — vienu reizi pietiek.
5. Ja Gemini atsakās vai nogriež atbildi — pieraksti, atkārto jaunā sarunā vienu reizi; oriģinālu patur.

Minimums: A daļa (10 pakas). Pilnais komplekts: A + B (20). Laiks: ~3–5 min uz paku.

## Ko es izdarīšu pēc tam
Parsēšu Gemini JSON tāpat kā J1 (`e5_collect.py`), salīdzināšu pāris pa pārim: preferences saskaņa (gaidāms ≥ 8/10), elementu sakritība, kritēriju starpība, kopvērtējuma korelācija; pierakstīšu 30 §8 un §10. Ja Gemini sistemātiski nesakrīt ar Opus — tas ir atradums, nevis kļūda, un tas nonāk pārskatā.
