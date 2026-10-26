# E5 — Iterāciju salīdzinājums: 2 → 3 (prompts v1.3-c pret bāzi v1.1-c)

*Standarta dokuments pēc katras iterācijas. Skaitļi no `iter_3/analysis/summary.md` un `figure_data/*.csv`; katrs skaitlis izsekojams līdz konkrētam tiesneša vērtējumam. Salīdzinājums ir pret **pēdējo pieņemto** versiju v1.1-c (iter. 1 atbildes, pārvērtētas šajā iterācijā), nevis pret iter. 2 noraidīto v1.2-c.*

## 1. Īsā atbilde

**Jā — v1.3-c ir labāks par v1.1-c.** Vidēji **+4,38** punkti [+1,97; +7,47], **visos 10 uzdevumos**, Vilkoksons p = 0,002. Pieņemšanas noteikums (29 §5.4) **izpildīts visos četros punktos** → v1.3-c var kļūt par jauno bāzi (stājas spēkā ar Martina apstiprinājumu).

Tas ir pirmais rezultāts eksperimentā, kas ir skaidri ārpus trokšņa joslas (±1,51) un kura TI neietver nulli. Tas sasniegts ar to, ka **pārkāpumi pazuda pilnībā (0,35 → 0,00)** un **izdomātie fakti gandrīz pilnībā (1,20 → 0,11)**, nezaudējot obligātos elementus (94 % → 97 %).

Divas atrunas: (1) pāru salīdzinājumā tiesnesis izvēlas v1.3-c **15 reizes, v1.1-c — 10** (5 neizšķirti) — skaidrs, bet ne pārliecinošs pārsvars; v1.1-c uzvar tur, kur tā garākās atbildes dziļāk aprēķina sliktāko scenāriju (T06, T08); (2) atlikušie zaudējumi ir tik mazi, ka nākamā izmaiņu paka, visticamāk, vairs nevar pierādīt uzlabojumu ar šo uzdevumu komplektu (sk. §6).

Galvenais rezultāts nemainās: ar kanonu un promptu **+33,0 pret bez prompta** [+27,8; +38,4], 10/10 uzdevumos, 30/30 pāru.

## 2. Ko gribējām (changes_v1.3, fiksēts pirms datiem)
Saglabāt iterācijas 2 ieguvumus (izdomāto faktu izzušana, T04 forma, T03 nobeigums) un salabot divus v1.2-c blakusefektus: (1) riska hipotēzes, ko CH7 izmeta kopā ar vispārinājumiem; (2) vārdu budžeta pārkāpumi, ko teikums par garumu nemainīja. Prognoze +1,5…+3 pret v1.1-c; izdomātie fakti ≤0,3; pārkāpumi ≤0,25.

## 3. Ko mainījām un kāpēc (v1.3-c = v1.1-c + CH6 + CH7b + CH10 + CH11; CH8, CH9 atgriezti)
| ID | Kāpēc | Ko mainījām |
|---|---|---|
| CH6 | T04 v1.1-c: 488–554 vārdi, 6–8 "?" | FULL kārta: pieci jautājumi = piecas "?"; viss raunds zem budžeta |
| CH7b | v1.1-c izdomātie fakti 1,01–1,32; v1.2-c CH7 izmeta arī riska hipotēzes | ārējās zināšanas tikai kā pārbaude vai marķēts pieņēmums **+** ticami riski paliek kā hipotēzes ar pārbaudes darbību |
| CH10 | T03 M8 (nobeigums nogriezts) | PLAN CHECK nobeigumu nedrīkst īsināt |
| CH11 | teikums "beidz 10–15 % zem" nemainīja garumu | mainīti paši skaitļi L5: iekšējie griesti ≈10 % zem personas limita |

4 455 vārdi (+12,0 % pret v1.0). sha256 693dd23c…

## 4. Ko ieguvām (iterācija 3: 30 jaunas atbildes, 120 vērtējumi)
| Rādītājs | A (bez prompta) | v1.1-c (tās pašas atbildes, iter. 3) | **v1.3-c** | Labāk? |
|---|---|---|---|---|
| Kopvērtējums | 55,9 | 84,5 | **88,9** | **jā, +4,38** |
| Pāru preference pret v1.1-c | — | 10 uzvaras | **15 uzvaras** (5 neizšķ.) | jā, mēreni |
| Pārkāpumi / atbildi | 0,98 | 0,35 | **0,00** | **jā** |
| Izdomātie fakti / atbildi | 1,72 | 1,20 | **0,11** | **jā** |
| Obligātie elementi | 54 % | 94 % | **97 %** | jā |
| C1 precizitāte | 6,9 | 7,3 | **8,5** | jā |
| C2 diagnoze | 6,8 | 8,2 | 8,1 | ≈ (−0,1) |
| C3 praktiskums | 6,0 | 8,0 | 8,0 | = |
| C4 atbilstība | 6,4 | 7,8 | **8,6** | jā |
| C5 kontrole | 4,0 | 8,0 | 8,3 | jā |
| C6 godīgums | 6,1 | 8,2 | **8,7** | jā |

Pa uzdevumiem (Δ v1.3-c − v1.1-c): **T04 +15,9**, T07 +8,3, T10 +6,2, T03 +4,8, T01 +1,8, T05 +1,8, T08 +1,8, T09 +1,2, T06 +1,1, T02 +0,8 — **visi pozitīvi**.
Noturības pārbaude (tikai 60 izsaukumi, kuros abas versijas vērtētas kopā): Δ +3,45 [+0,90; +6,53], 8/10 — arī izpilda §5.4.
**§5.4:** (1) Δ 4,38 > 1,51 un TI apakšējā +1,97 > −1 ✓; (2) neviens kritērijs nekrīt > 1,0 ✓ (C2 −0,08); (3) pārkāpumi nepieaug ✓ (0,35 → 0,00); (4) garums +12,0 % ≤ +15 % ✓. Hold-out šajā iterācijā nav mērīts (protokolā pēc izvēles; D0.9).

Versiju gaita (katra savā iterācijā; starp iterācijām tiesneša līmenis nedaudz svārstās, tāpēc salīdzināmas tikai vienas iterācijas iekšienē): v1.0 85,9 → v1.1-c 86,2 → v1.2-c 82,5 (noraidīts) → **v1.3-c 88,9**.

## 5. Vai sasniedzām? Pa izmaiņām
| ID | Verdikts | Kāpēc |
|---|---|---|
| CH6 | **izdevās** | T04 jautājumu skaits un garums: 0 pārkāpumu (v1.1-c 6/6); T04 +15,9 |
| CH7b | **izdevās 4 no 5 mērķiem** | izdomātie fakti 0,11; T04 M2, T10 M6, T02 M2 atgūti; **T04 M7 nav** — piemērs promptā ("tirgus maiņa, kas var skart galveno klientu") sašaurināja hipotēzi līdz vienam klientam |
| CH10 | **izdevās** | T03 M8 6/6 → 0/6 |
| CH11 | **izdevās** | 0 budžeta pārkāpumu visos 120 vērtējumos; elementi nesamazinājās. Blakusefekts: atbildes 10–15 % īsākas, un daļā uzdevumu tiesnesis pāros dod priekšroku v1.1-c dziļākajam sliktākā scenārija aprēķinam |

### 5b. Elementu līmenī (6 kopīgie vērtējumi, v1.1-c → v1.3-c)
| Uzlabojās → **paturam** | v1.1-c → v1.3-c |
|---|---|
| T04 F2/H2/M4 (jautājumu skaits) | 6 → 0 |
| T04 M8, H1 (garums) | 4 → 0 |
| T03 M8 (nobeigums) | 6 → 0 |
| T07 F2/H1 (garums), T08 M7, T10 M1 | 2 → 0 |
| T09 M6, H6; T06 M4 | 1 → 0 |
| Izdomātie fakti (visi uzdevumi, tie paši izsaukumi) | 1,20 → 0,07 |
| Pārkāpumi (visi uzdevumi) | 0,35 → 0,00 |

| Pasliktinājās vai nemainījās → **labojam v1.4-c (melnraksts)** | v1.1-c → v1.3-c | Ko darām |
|---|---|---|
| T04 M7 (AI faktors visā tirgū, ne tikai pie klienta) | 2 → 6 | CH12: piemērs "a shift in their whole market, not only at their main client" |
| T09 M5, M7 (iziešana kā variants pirms nomas lēmuma) | 1 → 3, 0 → 2 | CH13: R14 + "orderly exit among the options; which mistake costs less" |
| T02 M4 (naudas plūsmas zemākais punkts) | 0 → 2 | CH14: R2 + "show the lowest balance and its day" |
| T08 M3/M4, T03 M1 (pa vienai atbildei) | 0 → 2 | netiek labots (nav sistēmisks) |
| Sliktākā scenārija dziļums T06/T08 (pāri), C2 −0,27 kopīgajos izsaukumos | — | netiek labots (CH11 ieguvums lielāks); uzraudzīt |

## 6. Ko darām tālāk — **lēmums Martinam** (nekas netiek sākts bez tā)
1. **v1.3-c kā jaunā bāze** — §5.4 izpildīts mehāniski; vajag Martina "jā" (tāpat kā v1.1-c 16.10.).
2. **Paka v1.4-c ir sagatavota, bet netiek ģenerēta** (`iter_3/error_analysis/changes_v1.4.md/.json/.diff`; `02b_v1.4-c.md` sha256 d153e545…, 4 496 vārdi, +13,1 % pret v1.0). Tā labo trīs šaurus cēloņus. **Prognoze +0,5…+1,2 — zem trokšņa joslas ±1,51.** Ar 10 uzdevumiem × 3 atkārtojumiem pat strādājoša paka, visticamāk, neizpildīs §5.4(1); divas šādas iterācijas pēc kārtas iedarbina protokola pārtraukšanas noteikumu (a).
3. Tāpēc pirms iterācijas 4 ir vērts izvēlēties vienu no:
   - **(A) iterācija 4 ar v1.4-c**, kā plānots (mēra elementu līmenī; kopvērtējumā, visticamāk, troksnis);
   - **(B) kontroles komplekts (hold-out H01–H10) tagad** — protokols to paredz iterācijā 3 pēc izvēles (29 §2.4; pārtraukšanas noteikums (b) §2.5); tas ir vienīgais vēl neveiktais tests un atbild, vai v1.3-c ieguvums nav pielāgošanās 10 uzdevumiem;
   - **(C) uzreiz gala kārta** ar v1.3-c kā gala kandidātu (hold-out + 3 apstiprinājuma modeļi + J2).
   Mans ieteikums: **(B)**, jo izstrādes komplekts tuvojas griestiem (elementi 97 %, pārkāpumi 0), un nākamā informatīvākā atbilde ir par pārnesamību, nevis par vēl vienu nelielu labojumu.

**Ko šī iterācija iemāca par prompta optimizāciju:** (1) "kas uzlabojās — paturam, kas pasliktinājās — atgriežam" strādā: no v1.2-c paturētās trīs izmaiņas un divas labotās deva +4,4 pēc −2,2; (2) skaitlis promptā maina uzvedību, teikums par to — nē (CH11 pret CH8); (3) piemērs noteikumā tiek lasīts burtiski un var sašaurināt pašu noteikumu (CH7b → T04 M7); (4) pēc pārkāpumu un izdomāto faktu novēršanas atlikušās kļūdas ir šauras, un šis mērījums vairs neizšķir mazus uzlabojumus.

## 7. Kur ir dati
`E:\GitHub\E5_eksperiments\iter_3\` — `analysis/` (summary, fig1–fig4, fig6, fig7, figure_data, panel_iter_3.png, momentuzņēmumi), `judgments/` (120), `responses/` (30), `packs/` (gen 30, judge 120), `hardchecks/`, `error_analysis/` (kļūdu analīze, neapstrādātās tabulas v1.3-c un bāzei v1.1-c, changes_v1.4.md/.json/.diff), `decisions.md`, `SALIDZINAJUMS.md`. J2 (Gemini) materiāls: `00_kopejais/kalibracija/j2_gemini/iter_3/`.
