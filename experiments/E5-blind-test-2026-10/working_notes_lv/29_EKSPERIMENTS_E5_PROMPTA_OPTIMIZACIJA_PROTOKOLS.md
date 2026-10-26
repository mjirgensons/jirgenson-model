# 29. Eksperiments E5: operatīvā prompta iteratīva optimizācija (protokols v1)

**Datums:** 2026-10-15 (Toronto). **Autors:** Claude (Fable 5.1) pēc Martina uzdevuma; lēmumi — Martina.
**Statuss:** protokols sagatavots; iterācija 0 **nav sākta**. Pirms sākuma jāizpilda §11 kontrolsaraksts un jāatbild uz §12 jautājumiem.
**Saistītie faili (reproducējamības pakete):**

| Fails | Saturs | Statuss |
|---|---|---|
| `29_…PROTOKOLS.md` | šis dokuments | v1 |
| `29a_E5_TASKS_DEV_v1.md` | 10 izstrādes uzdevumi (T01–T10): teksti, atbilžu atslēga | **iesaldēts**, hash §8 |
| `29b_E5_TASKS_HOLDOUT_v1.md` | 10 kontroles uzdevumi (H01–H10), aizzīmogoti | **iesaldēts**, hash §8 |
| `29c_E5_JUDGE_PROMPT_v1.md` | tiesneša prompts, rubrika, formula, kalibrācija | v1 |
| `29d_E5_CONTROL_PROMPTS_v1.md` | nosacījumi A / B / C, kontroles prompts B | v1 |
| `02a_CANON_v1.0_EN.md`, `02b_OPERATING_PROMPT_v1.0_EN.md` | kanons (fiksēts) un prompts v1.0 (sākumpunkts) | esoši |
| `registry/e5_results_template.csv`, `registry/e5_pairwise_template.csv` | rezultātu tabulu formāts | v1 |
| `scripts/e5_analyze.py` | statistika un grafiki no rezultātu CSV; demo ar sintētiskiem datiem | v1 |
| `scripts/e5_hardchecks.py` | automātiskās pārbaudes (vārdu skaits, jautājumi, valoda, aizliegtie vārdi) | v1 |

---

## 0. Kopsavilkums vienā lappusē

**Jautājums.** Vai operatīvo promptu (02b) var ar kontrolētām iterācijām padarīt izmērāmi labāku, un cik liels ir tā pienesums salīdzinājumā ar (A) modeli bez prompta un (B) labu vispārīgu konsultanta promptu?

**Kā.** 10 iesaldēti uzdevumi × 3 nosacījumi × 3 atkārtojumi × akls LLM-tiesnesis ar iepriekš sagatavotu atbilžu atslēgu. Pēc katras iterācijas: kļūdu analīze → promptā tiek ieviestas 1–5 mērķētas izmaiņas ar katrai izmaiņai pierakstītu hipotēzi → jauna versija vN+1 → tas pats tests. Pieci cikli. Beigās: kontroles komplekts (10 citi uzdevumi, aizzīmogoti), kas nav izmantots nevienā lēmumā, un pārbaude uz citiem modeļiem.

**Lēmuma noteikums (iepriekš fiksēts).** Versiju vN pieņem, ja uz izstrādes komplekta tās vidējais kopvērtējums pārsniedz vN−1 par vairāk nekā trokšņa joslu (§5.2), neviens no sešiem kritērijiem nepasliktinās vairāk par 1 punktu, un (kad ir mērīts) kontroles komplekts nav sliktāks par vN−1 vairāk kā par trokšņa joslu. Pretējā gadījumā izmaiņas atceļ vai sadala (ablācija).

**Ko eksperiments pierāda un ko ne.** Pierāda: ar šiem uzdevumiem, šo modeli, šo tiesnesi un šo rubriku versija vN dod par X punktiem (95 % TI …) augstāku vērtējumu nekā v1.0 / nekā A / nekā B. Nepierāda: ka prompts "novērš halucinācijas", ka tas darbojas ar jebkuru modeli vai jebkuru uzdevumu, ka LLM-tiesneša vērtējums sakrīt ar cilvēka vērtējumu (skat. §9). Formulējumi pārdošanas tekstos: tikai pēc D11 (07).

**Galvenās atšķirības no E1 (J pielikums).** Pilni uzdevumu teksti, tiesneša prompts un atbilžu atslēgas ir saglabāti un iesaldēti; 3 atkārtojumi, nevis 1; tiesnesis akls ar pozīciju maiņu; otrs kontroles nosacījums B; kontroles komplekts pret pārpielāgošanos; statistika ar ticamības intervāliem; katra prompta izmaiņa ar hipotēzi un pierakstītu rezultātu.

---

## 1. Mērķis un hipotēzes

**Mērķis.** Soli pa solim, ar atkārtojamu procedūru, uzlabot operatīvo promptu (02b), nemainot kanonu (02a), un uzrādīt uzlabojumu katrā iterācijā ar skaitļiem un grafikiem.

**Iepriekš reģistrētās hipotēzes.**
- **H1 (grāmatas apgalvojums).** C(v1.0) > A: ar kanonu un promptu vērtējums ir augstāks nekā bez tiem. Sagaidāms pēc E1 (+7…+11 punkti 60 skalā).
- **H2 (saturs vs struktūra).** C(v1.0) > B: pienesums nav tikai no labas struktūras. *Nav pārbaudīts nekad.* Šis ir zinātniski svarīgākais salīdzinājums.
- **H3 (iterācijas).** C(vN) ≥ C(vN−1) katrā pieņemtajā iterācijā; C(v1.5) − C(v1.0) > 0 ar 95 % TI, kas neietver nulli.
- **H4 (pārnesamība uz citiem uzdevumiem).** Uzlabojums C(v1.5) − C(v1.0) kontroles komplektā ir vismaz puse no uzlabojuma izstrādes komplektā. Ja nē — prompts ir pārpielāgots 10 uzdevumiem.
- **H5 (pārnesamība uz citiem modeļiem).** Uzlabojuma zīme saglabājas uz vismaz 2 no 3 pārējiem modeļiem (Opus 5.5, Haiku 5.5, Fable 5.1 / vai ārējs modelis).

**Nulles hipotēze katrā salīdzinājumā:** vidējā pāru starpība = 0. Trokšņa josla tiek izmērīta iterācijā 0 (§5.2), nevis pieņemta.

**Kas tiek optimizēts.** Tikai `02b` teksts. Kanons `02a` ir fiksēts v1.0: ja kļūdu analīze rāda, ka problēma ir kanonā, to pieraksta kā "kanona kandidātu" nākamajam eksperimentam (E6), bet šajā eksperimentā nemaina.

---

## 2. Dizains

### 2.1 Mainīgie

| Loma | Mainīgais | Vērtības |
|---|---|---|
| Neatkarīgais | nosacījums | **A** bez prompta; **B** vispārīgs strukturēts konsultanta prompts (29d); **C** kanons v1.0 + prompts vN |
| Neatkarīgais | prompta versija | v1.0 (iter. 0), v1.1-c … v1.5-c (kandidāti), pieņemtās kļūst par v1.1 … |
| Atkarīgais | kopvērtējums 0–100 (29c formula) = elementi 40 + kritēriji 60 − 2 × pārkāpumi | |
| Atkarīgie (sekundārie) | elementu %, kritēriju summa (salīdzināma ar E1 60 skalu), 6 kritēriji atsevišķi, pārkāpumu skaits, izdomāto faktu skaits, pāru uzvaru daļa, cietās pārbaudes | |
| Kontrolētie | ģenerējošais modelis un versija, temperatūra/noklusējums, piegādes veids (API/čats), datums, uzdevumu teksti, tiesneša prompts un modelis | fiksēti iterācijas ietvaros, reģistrēti |
| Bloķējošais | uzdevums (T01–T10) | pāru salīdzinājums pa uzdevumiem |

### 2.2 Modeļi

- **Izstrādes (ģenerējošais) modelis:** **Claude Sonnet 5.5** — vidējā klase, kurā prompta kvalitāte ir redzamāka nekā uz spēcīgākā modeļa (griestu efekts) un kas atbilst tam, ko lietos vairums lasītāju. *Alternatīva:* Haiku 5.5, ja mērķis ir vājākā modeļa noturība (E1 rādīja, ka tieši tur kombinācija klibo).
- **Tiesnesis J1:** **Claude Opus 5.5** (spēcīgākais pieejamais; E1 nepārtrauktība). **Tiesnesis J2:** citas saimes modelis (GPT vai Gemini), ja Martinam ir piekļuve; ja nav — Fable 5.1. J2 vērtē iterācijā 0 (kalibrācija un saskaņa) un pēdējā iterācijā; J1 vērtē visās.
- **Apstiprinājuma modeļi (pēdējā iterācija):** Opus 5.5, Haiku 5.5, Fable 5.1 un, ja iespējams, viens ārējs modelis — tikai C(v1.0) pret C(v1.5) un A.
- Tiesnesis un ģenerators **nedrīkst** būt viens un tas pats modelis (pašpreferences nobīde). Ja J1 = Opus, tad Opus apstiprinājuma kārtu vērtē J2.

### 2.3 Atkārtojumi un apjoms

Katrs (uzdevums × nosacījums) tiek ģenerēts **k = 3** reizes neatkarīgās jaunās sarunās (temperatūra — saskarnes noklusējums; nevis 0, jo lasītājs saņem noklusējumu; reģistrē). Divas konfigurācijas:

| | Standarta (ieteicamā) | Minimālā |
|---|---|---|
| Iterācija 0 | A, B, C(v1.0) × 10 uzd. × k=3 = 90 ģenerācijas + C(v1.0) otrs neatkarīgs bloks (troksnis) 30 = **120**; kontroles komplekts A, B, C × 10 × 3 = **90** | A, C × 10 × 2 = 40; kontroles A, C × 10 × 2 = 40 |
| Iterācijas 1–5 (katra) | A (atkārtoti, vienlaicīgā kontrole), C(vN−1), C(vN) × 10 × 3 = **90** | C(vN) × 10 × 2 = 20 (A un C(vN−1) no iepriekšējās kārtas) |
| Pēdējā iterācija papildus | kontroles komplekts C(v1.5), B × 10 × 3 = 60; 3 apstiprinājuma modeļi × C(v1.0), C(v1.5), A × 10 × 2 = 180 | kontroles C(v1.5) × 10 × 2 = 20 |
| Tiesneša izsaukumi | ≈ 2 × ģenerācijas (katrs pāris divās kārtībās) + pāru salīdzinājumi | ≈ 2 × |

Minimālā konfigurācija der ātrai iekšējai cilpai; **publicējams secinājums tikai no standarta konfigurācijas**.

### 2.4 Uzdevumu komplekti

- **Izstrādes komplekts (29a):** T01–T10, iesaldēts. Uz tā tiek pieņemti visi lēmumi par prompta izmaiņām.
- **Kontroles komplekts (29b):** H01–H10, iesaldēts un aizzīmogots (hash §8). Izmanto tikai mērīšanai: iterācijā 0, pēc izvēles iterācijā 3 (rezultātus saglabā failā, ko prompta redaktors neatver), un pēdējā iterācijā. **Nevienu prompta izmaiņu nedrīkst pamatot ar kontroles komplekta rezultātu.**
- Pārklājums: 10 uzdevumos ir visi režīmi (EMERGENCY ×2, QUICK ×4 t. sk. divpakāpju "datu vairāk nav", FULL 1. kārta, PLAN CHECK, pusaudzis), trīs valodas (EN ×8, LV, RU), un katram uzdevumam sava "lamata" (tabula 29a sākumā). Neviena situācija nesakrīt ar grāmatas varoņiem vai E1 situācijām.
- Katram uzdevumam iepriekš ir: *gold facts* (aritmētika, ko tiesnesis pārrēķina), 8–10 obligātie elementi ar pamatojumu "kāpēc", 3–5 aizliegtie elementi, vārdu un jautājumu budžets.

### 2.5 Iterāciju cikls

```
iter 0  ──►  iter 1  ──►  iter 2  ──►  iter 3  ──►  iter 4  ──►  iter 5
v1.0         v1.1-c       v1.2-c       v1.3-c       v1.4-c       v1.5-c
A, B, C      A, C(prev),  …            … (+holdout  …            A, B, C(prev), C(new)
+troksnis    C(new)                     neatvērts)                + holdout + 3 modeļi
```

Katrā iterācijā: ģenerē → cietās pārbaudes (skripts) → tiesnesis (akls, 2 kārtības) → analīze (skripts) → kļūdu analīze → izmaiņu paka ar hipotēzēm → jauna versija → žurnāls. Sīkāk §6.

**Pārtraukšanas noteikumi.** (a) Divas iterācijas pēc kārtas bez pieņemamas izmaiņas → apstāties, veikt ablāciju un pārskatīt rubriku vai uzdevumus, nevis turpināt "spiest". (b) Ja kontroles komplekts iterācijā 3 rāda kritumu > trokšņa josla pret v1.0 → pārpielāgošanās: atgriezties pie pēdējās versijas, kurai tā nebija.

---

## 3. Uzdevumu komplekta principi (kā tie tapa un kā tos drīkst mainīt)

1. **Katram uzdevumam viena lamata**, kas atbilst konkrētam prompta noteikumam (R8 garantijas, R12 bīstamākais kā notikums ar datumu, §9.5 izaugsme sarkanajā zonā, CL19 "datu vairāk nav", L1 valoda, MODE 1 nepārrakstīt, offset (b) pretruna datos, offset (c) mirstoša vide). Tā tiesneša rezultāti rāda, *kurš noteikums* nestrādā.
2. **Atbilžu atslēga pamatota ar lasītāja labumu, ne ar prompta vārdiem.** Katram obligātajam elementam ir "kāpēc" (ko tas dod cilvēkam), lai elementu saraksts neatlīdzinātu tikai "izskatās pēc metodes". Vairāki elementi apzināti darbojas *pret* garu, strukturētu atbildi (vārdu budžets, bez žargona, bez jautājumiem).
3. **Aritmētika pārbaudīta** ar skriptu pirms iesaldēšanas (visi gold facts pārrēķināti 2026-10-15).
4. **Iesaldēšana:** pēc hash ierakstīšanas (§8) uzdevumu tekstus nemaina. Ja tiesnesis atrod kļūdu atslēgā, to pieraksta žurnālā, laboto versiju marķē v2, un salīdzinājumus starp v1 un v2 rezultātiem neveic.
5. **Kontroles komplekts ir strukturāli paralēls** (katrs H spoguļo kādu T), lai H4 mērītu pārnesamību uz *citām situācijām*, nevis uz *citām prasmēm*.

---

## 4. Vērtēšana

### 4.1 Rubrika (29c)
- **Obligātie elementi (40 p.)**: uzdevumam specifiski, binārie, ar pierādījumu citātu.
- **Seši kritēriji (60 p.)**: C1 precizitāte un nav izdomātu faktu; C2 diagnozes dziļums; C3 soļu praktiskums; C4 atbilstība pieprasījumam, laikam, valodai; C5 vadības kvalitāte (prioritātes, sliekšņi, mērīšana, nākamā pārbaude); C6 godīgums (bez garantijām, diapazoni, divas prognozes). Tie paši seši, kas E1 — tāpēc 60 punktu summa ir salīdzināma ar J pielikuma tabulu (ar atrunu, ka tiesneša prompts tagad ir cits).
- **Pārkāpumi**: aizliegtie elementi + nokrītušās cietās pārbaudes; −2 p. katrs.
- **Pāru preference**: kurš labāk kalpo cilvēkam šonedēļ; uzvara tikai, ja sakrīt abās kārtībās.

### 4.2 Aklums un pozīcijas
Tiesnesis neredz sistēmas promptus, nosacījumu un modeļu nosaukumus. Katrs pāris tiek vērtēts divreiz ar samainītu kārtību; rezultāti vidējoti. **Atzīstams ierobežojums:** C atbildes var atpazīt pēc struktūras, tāpēc aklums ir daļējs; mazinājums — tiesneša 1. noteikums (struktūra neko nedod), kontroles nosacījums B (arī strukturēts) un garuma kalibrācija (29c).

### 4.3 Cietās pārbaudes (skripts `e5_hardchecks.py`)
Vārdu skaits pret budžetu; jautājumu skaits; valoda (latīņu/kirilicas/latviešu diakritikas īpatsvars); iekšējie marķieri ("§", "EMERGENCY", "QUICK", "canon", "according to the model"); žargons pusaudža/ģimenes uzdevumos; skaitļu nekonsekvence (tiesnesis). Skripts dod objektīvu vērtību, tiesnesis — otru; nesakritības pieraksta.

### 4.4 Tiesnešu neatkarība un saskaņa
- Tiesnesis ≠ ģenerators. Vēlams cita saime (J2).
- Kalibrācija pirms iterācijas 0 (29c): identitātes tests, iestādītas kļūdas tests, garuma tests, divu tiesnešu saskaņa uz 10 pāriem (vidējā absolūtā starpība kritēriju summā; Koena kappa preferencei; slieksnis κ ≥ 0,4, citādi rubrikas enkurus precizē un versiju maina).
- Tiesnesis pārrēķina aritmētiku pats (kā E1).

---

## 5. Statistika un lēmumu noteikumi

### 5.1 Pamatvienība
Pāru starpība **pa uzdevumiem**: katram uzdevumam vidējais pār k atkārtojumiem un 2 kārtībām, tad starpība starp nosacījumiem (C − A, C − B, vN − vN−1). n = 10 pāri (uzdevumi); papildus — pa atkārtojumiem (n = 30) kā jutīguma analīze.

### 5.2 Trokšņa josla (iterācija 0)
C(v1.0) tiek ģenerēts divos neatkarīgos blokos (3 + 3 atkārtojumi, dažādās dienās vai sesijās). Starpība starp blokiem pa uzdevumiem dod **tests–retests troksni**: tā standartkļūda SE₀. **Trokšņa josla = 2 × SE₀** (vidējam kopvērtējumam). Minimālais nosakāmais efekts (MDE) tiek ierakstīts žurnālā pirms 1. iterācijas. Orientējoši (no E1 izkliedes): ja SE₀ ≈ 1,5 p., josla ≈ 3 p. 100 skalā.

### 5.3 Aprēķini (skripts `e5_analyze.py`)
- Vidējais, SD, **bootstrap 95 % TI** (10 000 pārpaņemšanu pa uzdevumiem) katrai pāru starpībai.
- **Vilkoksona zīmju-rangu tests** pa uzdevumiem (n = 10; mazs spēks, tāpēc TI ir galvenais) un zīmju tests.
- **Efekta lielums**: Koena d pāru starpībai.
- **Uzvaru daļa** pāru preferencē ar Vilsona 95 % TI.
- Kritēriji atsevišķi (6 līnijas), elementu % un pārkāpumi — lai redzētu, *kur* versija uzlabojas un vai kaut kas nepasliktinās.
- Vairāku salīdzinājumu korekcija: galvenais tests iterācijā ir viens (vN pret vN−1 kopvērtējumā); pārējie — aprakstoši.

### 5.4 Pieņemšanas noteikums versijai vN (fiksēts iepriekš)
1. Δ(vN − vN−1) kopvērtējumā izstrādes komplektā > trokšņa josla **un** bootstrap 95 % TI apakšējā robeža > −1 p.;
2. neviens kritērijs C1–C6 vidēji nekrīt vairāk par 1,0 p.; pārkāpumu skaits nepieaug;
3. ja kontroles komplekts tajā iterācijā mērīts: Δ kontroles komplektā > −trokšņa josla;
4. prompta garums (tokeni) nav pieaudzis vairāk par 15 % pret v1.0 bez pierādīta ieguvuma (garš prompts ir pats par sevi risks, 02b degradation_rule).
Ja 1. izpildās, bet 2. ne — izmaiņu paku sadala un atkārto (ablācija). Ja nekas neizpildās — versiju noraida, hipotēzes pieraksta kā noraidītas.

### 5.5 Gala secinājums (iterācija 5)
Ziņo: C(v1.5) − C(v1.0), C(v1.5) − A, C(v1.5) − B izstrādes un kontroles komplektā, ar TI; uzvaru daļas; pa kritērijiem; uz 3 apstiprinājuma modeļiem. Formulējums: "ar šiem uzdevumiem, modeļiem, tiesnesi un rubriku". Nekādu "pierādīts vispār".

---

## 6. Iterācijas procedūra (soļi vienai iterācijai)

| # | Solis | Kas to dara | Iznākums / fails |
|---|---|---|---|
| 1 | Iesaldē versiju vN-c: teksts, SHA-256, tokenu skaits | redaktors (Claude) | `e5/prompts/02b_v1.N-c.md`, žurnāls |
| 2 | Ģenerē atbildes: katram (uzdevums, nosacījums, atkārtojums) jauna saruna; divpakāpju uzdevumos 2. ziņu sūta vārds vārdā | izpildītājs (§7) | `e5/responses/iter_N/{cond}_{task}_{run}.md` + `responses_index.csv` (modelis, datums, piegādes veids) |
| 3 | Cietās pārbaudes | skripts | `hardchecks_iter_N.csv` |
| 4 | Sagatavo tiesneša pakas: pāri (C(vN) vs A; C(vN) vs C(vN−1)), nejauša kārtība, abas kārtības; marķē "Response 1/2"; atslēga no 29a | skripts/izpildītājs | `judge_packs_iter_N/` ar nejaušības sēklu |
| 5 | Tiesnesis vērtē; JSON tiek parsēts | J1 (un J2 iter. 0 un 5) | `judgments_iter_N.csv` (garais formāts) |
| 6 | Analīze: tabulas, TI, grafiki | skripts | `e5/figures/iter_N/…png`, `summary_iter_N.md` |
| 7 | **Kļūdu analīze** tikai izstrādes komplektā: katrs nokritušais elements/pārkāpums C(vN) atbildēs tiek klasificēts: (a) noteikums promptā ir, bet netiek ievērots; (b) noteikuma nav; (c) noteikumi pretrunīgi/neskaidri; (d) modeļa spēju robeža; (e) tiesneša kļūda. Tabula: uzdevums × elements × klase | redaktors | `error_analysis_iter_N.md` |
| 8 | **Izmaiņu paka vN+1-c**: 1–5 izmaiņas; katrai: ID, mērķa kļūdu klase un elementi/uzdevumi, prompta sadaļa, precīzs diff, sagaidāmais efekts (kuri kritēriji/uzdevumi), blakusrisks. Ne vairāk par vienu izmaiņu vienā prompta sadaļā uz vienu hipotēzi | redaktors; Martins apstiprina | `changes_v1.N+1.md` |
| 9 | Lēmums par vN pēc §5.4; ieraksts 01 (versija), 02 (prompta bibliotēka), 03 (E5 rinda), 07 (lēmums) | Martins | projekta dokumenti |

**Kļūdu analīzes disciplīna.** Izmaiņu pamatojums drīkst balstīties tikai uz C(vN) atbildēm izstrādes komplektā. Uzdevumu tekstus, atslēgu un tiesneša promptu *nemaina*, lai "uzlabotu" rezultātu. Ja kļūdu klase ir (d) — modeļa robeža — to pieraksta un nevis "stumj" ar vēl garākiem noteikumiem.

**Laika un apjoma aplēse vienai standarta iterācijai:** 90 ģenerācijas + ≈ 200 tiesneša izsaukumi. Ar apakšaģentiem šajā vidē: 2–4 stundas mašīnlaika pa paketēm; manuāli čata saskarnēs: ≈ 2–3 darba dienas; ar API skriptu: < 1 stunda.

---

## 7. Izpildes varianti

| Variants | Kā | Plusi | Mīnusi | Kad lietot |
|---|---|---|---|---|
| **(a) Šajā čatā ar apakšaģentiem** | Claude palaiž katram (uzdevums, nosacījums, atkārtojums) atsevišķu aģentu (sonnet/opus/haiku/fable), katrs ar tīru kontekstu; tiesnesis — cits aģents ar 29c | ātri; viss paliek projektā; pilna reģistrācija | A nav "tīrs" (aģentam ir vides sistēmas prompts → marķēt `A-harness`); viena modeļu saime; tiesnesis tajā pašā saimē | iterāciju cilpa 1–4 (ātra mācīšanās) |
| **(b) Manuāli čata saskarnēs** (claude.ai, ChatGPT, Gemini) | Martins pēc run-sheet: jauna saruna, pielikums, prompts, uzdevums; kopē atbildes failos | tīrs A; citas saimes tiesnesis; atbilst tam, kā lasītājs lieto | lēni; cilvēka kļūdas kopēšanā; temperatūra nav zināma | kalibrācija (J2) un gala apstiprinājums |
| **(c) API skripts** | Python ar Anthropic/OpenAI/Gemini API, fiksēti parametri, automātiska reģistrācija | tīrākais, reproducējamākais, lētākais laikā | vajag API atslēgas un nelielu izstrādi; no šīs vides API var nebūt sasniedzams | gala apstiprinājums un publicējamā versija |

**Ieteikums:** iterācijas 0–4 pēc (a) ar pilnu reģistrāciju; iterācija 5 (gala) pēc (c) vai (b) ar tīru A un citas saimes tiesnesi. Secinājumus par H1/H2 publicē tikai no (b)/(c) datiem.

**Run-sheet vienai ģenerācijai (visiem variantiem):**
1. Jauna saruna, bez atmiņas un projekta zināšanām (C: tikai kanons).
2. C: pievieno `02a` → sūta `02b vN` → sūta uzdevuma 1. ziņu. B: sistēmas prompts no 29d → uzdevuma ziņa. A: tikai uzdevuma ziņa.
3. Divpakāpju uzdevumos: pēc atbildes sūta 2. ziņu vārds vārdā.
4. Saglabā atbildi(-es) failā `{cond}_{task}_{run}.md`; indeksā: modelis, versija, datums/laiks, piegādes veids, temperatūra (ja zināma).
5. Nekādu labojumu atbildēs. Ja saskarne nogriež atbildi — pieraksta un atkārto (jauna saruna), oriģinālu patur.

---

## 8. Reproducējamības pakete un hash

SHA-256 iesaldētajiem failiem (aprēķināts 2026-10-15; pārbaudīt ar `sha256sum`):

| Fails | SHA-256 |
|---|---|
| `29a_E5_TASKS_DEV_v1.md` | `{{HASH_29A}}` |
| `29b_E5_TASKS_HOLDOUT_v1.md` | `{{HASH_29B}}` |
| `29c_E5_JUDGE_PROMPT_v1.md` | `{{HASH_29C}}` |
| `29d_E5_CONTROL_PROMPTS_v1.md` | `{{HASH_29D}}` |
| `02a_CANON_v1.0_EN.md` (lietotāja 2026-10-13 fails) | `{{HASH_02A}}` |
| `02b_OPERATING_PROMPT_v1.0_EN.md` (lietotāja 2026-10-13 fails) | `{{HASH_02B}}` |

Katrai iterācijai reģistrē: modeļu ID un versiju virknes, datumu, piegādes veidu, temperatūru, nejaušības sēklu pāru kārtībai, tiesneša prompta versiju, visu atbilžu failus, visus tiesneša izvadus (pilnu tekstu, ne tikai JSON), skripta versiju. Kāds cits, kam ir šī pakete, var atkārtot eksperimentu; **sagaidāms, ka skaitļi atšķirsies trokšņa joslas robežās, bet efekta zīme un lielums — ne.**

---

## 9. Validitātes draudi un mazināšana

| Drauds | Kāpēc tas ir drauds | Mazināšana šajā protokolā | Paliek |
|---|---|---|---|
| LLM-tiesnesis ≠ cilvēks | tiesnesis var atlīdzināt formu, garumu, "pārliecinošumu" | rubrika ar enkuriem; 1. noteikums; garuma kalibrācija; aritmētikas pārrēķins; divi tiesneši; B kontrole | jā: nav cilvēka vērtējuma. Ieteikums: 2–3 reāli uzņēmēji novērtē 10 pārus iterācijas 5 beigās |
| Pašpreference (tiesnesis tajā pašā saimē) | Claude var dot priekšroku Claude stilam | J2 no citas saimes; kappa pārbaude | daļēji, ja J2 nav pieejams |
| Daļējs aklums | C atbildes atpazīstamas pēc struktūras | pozīciju maiņa; B ar līdzīgu struktūru; tiesnesim aizliegts minēt metodi | jā |
| Atslēga rakstīta "pēc prompta" | elementi var atlīdzināt prompta ievērošanu, ne labumu | katram elementam "kāpēc" lasītājam; vairāki elementi pret garumu/žargonu; seši vispārīgie kritēriji ziņoti atsevišķi | daļēji; tāpēc ziņo arī kritēriju summu un B salīdzinājumu |
| Pārpielāgošanās 10 uzdevumiem | 5 iterācijas uz tiem pašiem uzdevumiem | aizzīmogots kontroles komplekts; H4; pārtraukšanas noteikums (b) | jā, ja kontroles komplekts arī ir viena autora rakstīts |
| Autors raksta gan uzdevumus, gan promptu | zināšana par uzdevumiem ietekmē prompta izmaiņas | uzdevumi iesaldēti pirms; kontroles komplekta rezultāti neatvērti līdz beigām; izmaiņas pamatotas ar kļūdu klasēm, ne ar uzdevumu | daļēji |
| Nejaušība (stohastiska izvade) | viena ģenerācija = troksnis | k = 3; trokšņa josla izmērīta; TI | jā, ar mazu n |
| Modeļa versijas maiņa iterāciju laikā | rezultāts mainās bez prompta izmaiņas | A atkārtoti katrā iterācijā (vienlaicīgā kontrole); versiju virknes reģistrētas | daļēji |
| A nav "tīrs" variantā (a) | vides sistēmas prompts | marķējums `A-harness`; gala apstiprinājums ar `A-clean` | jā iterācijās 1–4 |
| Garš prompts degradē modeli | katra iterācija pievieno noteikumus | tokenu limits §5.4(4); izmaiņas var arī *īsināt* | — |
| Vairāku salīdzinājumu inflācija | daudz kritēriju, daudz testu | viens galvenais tests iterācijā; pārējie aprakstoši | — |

---

## 10. Grafiki (ko katrs rāda; failu nosaukumi no skripta)

1. `fig1_total_by_iteration.png` — **galvenais**: vidējais kopvērtējums (0–100) pa iterācijām trim līnijām: A, B (tikai tur, kur mērīts), C(vN); 95 % TI; horizontāla trokšņa josla ap v1.0. Atbild: vai katra iterācija uzlabo.
2. `fig2_criteria_by_version.png` — seši kritēriji (1–10) pa versijām, grupēti stabiņi. Atbild: *kur* uzlabojums (un vai kaut kas krīt).
3. `fig3_task_heatmap.png` — siltumkarte: uzdevums × versija, vērtība = C − A starpība. Atbild: kuri uzdevumi (lamatas) paliek neatrisināti.
4. `fig4_winrate.png` — pāru uzvaru daļa C pret A un C pret vN−1 ar Vilsona TI. Atbild: cik bieži C ir labāks, neatkarīgi no skalas.
5. `fig5_dev_vs_holdout.png` — izstrādes vs kontroles komplekts katrai mērītajai versijai. Atbild: pārpielāgošanās (H4).
6. `fig6_distribution.png` — kastveida diagrammas (visi atkārtojumi) pa versijām. Atbild: vai uzlabojas arī sliktākais gadījums, ne tikai vidējais.
7. `fig7_elements_violations.png` — elementu % un pārkāpumu vidējais skaits pa versijām. Atbild: vai prompts tiek *ievērots*.
8. (pēdējā iterācijā) `fig8_models.png` — C(v1.0) vs C(v1.5) vs A uz katra apstiprinājuma modeļa (H5).

Skripts `scripts/e5_analyze.py demo` uzģenerē visus grafikus no **sintētiskiem** datiem (skaidri marķētiem), lai formu varētu apstiprināt pirms īstiem datiem. Īstie dati: `e5_analyze.py run --results … --pairwise …`.

---

## 11. Kontrolsaraksts pirms iterācijas 0

- [ ] Martins apstiprina: izstrādes modelis (Sonnet 5.5), tiesnesis J1 (Opus 5.5), J2 (cits), izpildes variants (§7), konfigurācija (standarta/minimālā).
- [ ] 29a/29b izlasīti un apstiprināti (vai labojumi veikti **pirms** hash ierakstīšanas); pēc tam hash ierakstīts §8 un faili vairs nemainās.
- [ ] `02b v1.0` teksts nokopēts uz `e5/prompts/02b_v1.0.md`, hash un tokenu skaits pierakstīts.
- [ ] Tiesneša kalibrācija (29c): identitātes, iestādītas kļūdas, garuma testi; J1–J2 saskaņa uz 10 pāriem (κ ≥ 0,4).
- [ ] Skripti nostrādā uz demo datiem; CSV veidnes saprotamas.
- [ ] Kontroles komplekta rezultātu mape izveidota ar noteikumu "neatvērt līdz iterācijai 5".
- [ ] Ieraksts 03 (E5 rinda "UZSĀKTS", datums) un 07 (lēmumi par modeļiem un variantu).

---

## 12. Atvērtie lēmumi Martinam

1. **Izpilde:** iterācijas 0–4 šajā čatā ar apakšaģentiem (ātri, `A-harness`), gala kārta ar API/čatu (`A-clean`)? Vai viss manuāli?
2. **Ārējais tiesnesis J2:** ir piekļuve GPT vai Gemini (čats pietiek kalibrācijai un gala kārtai)? Ja nē — J2 = Fable 5.1, ar atrunu §9.
3. **Izstrādes modelis:** Sonnet 5.5 (ieteikts) vai Haiku 5.5 (vājākā modeļa noturība)?
4. **Konfigurācija:** standarta (k = 3, A atkārtoti katrā iterācijā) vai minimālā?
5. **Cilvēka pārbaude beigās:** vai ir 2–3 uzņēmēji, kas novērtētu 10 pārus (pēc tās pašas rubrikas)? Tas būtu pirmais ne-LLM datu punkts.

---

## 13. Žurnāls (aizpilda iterāciju gaitā)

| Datums | Iterācija | Versija | Modelis / tiesnesis | Dev: C − A (TI) | Dev: vN − vN−1 (TI) | Holdout | Lēmums | Piezīmes |
|---|---|---|---|---|---|---|---|---|
| 2026-10-15 | — | v1.0 | — | — | — | — | protokols sagatavots | gaida §12 |
