# 28. PromptBase un prompt tirgi: novērtējums, stratēģija; visu pārdošanas ideju katalogs (2026-10-16)

## 1. Vai PromptBase reāli pārdod? Fakti (avoti §6)
| Rādītājs | Skaitlis | Avots / uzticamība |
|---|---|---|
| Apmeklējumi | ~532 tūkst./mēn., ASV 24 %, vid. 3:20 min | aipure (trešās puses mērījums), Semrush rāda "1M" noapaļoti |
| Katalogs | 130–260 tūkst. promptu, no tiem teksta ~43 500, "agent skills" ~4 400 | implo (konkurents), cartmango (konkurents) |
| Cenas | mediāna $5,99 (188 ieraksti); teksta promptiem $6,99; skills $9,99; 91 % ≤ $10; nekas virs $29,99 | cartmango izlase, neverificēta |
| Komisija | 20 % (plāni $19/mēn → 15 %, $39 → 10 %); **sava saite (referral) 0 %** | implo, aiprofitmode; oficiālā lapa nebija nolasāma |
| Jauns pārdevējs | cena ierobežota līdz $4,99, kamēr nav pārdevumu; 2 prompti dienā; izmaksa no $30 | implo |
| Noteikums | prompts nedrīkst būt bezmaksas citur | aiprofitmode FAQ |
| Reāli ieņēmumi | Trustpilot (19 atsauksmes, 4,1): viens top pārdevējs $16 000 par ~3 gadiem (~$450/mēn.); cits 7 pārdevumi 2 mēnešos; "significantly more sellers than actual buyers"; implo: pirmais mēnesis $6–28 | Trustpilot; implo |
| Kas pērk | teksta/biznesa prompti aug; "sistēmas prompti / custom GPT" ir vērtīgāki ar mazāk pārdevēju | emuāri bez datiem |

**Secinājums.** PromptBase ir **lielākais prompt tirgus, bet maza nauda**: pat labākie pārdevēji tur pelna simtus mēnesī, vairums gandrīz neko; vidējais čeks $4–6, no kā paliek $3–5. Tas **nav** grāmatas pārdošanas kanāls pats par sevi. Tas ir vērts kā **bezmaksas vitrīna**: (a) 500 tūkst. apmeklētāju mēnesī, kas meklē tieši promptus; (b) katrs ieraksts ir lapa ar aprakstu, kur drīkst norādīt autoru un grāmatu; (c) sava saite dod 0 % komisiju, tātad PromptBase var kalpot kā "maksājumu lapa" promptiem no LinkedIn/X bez Gumroad maksas. Risks: 20 % un $4,99 griesti sākumā; prompts nedrīkst būt bezmaksas citur (grāmatas pielikumi H/I ir maksas grāmatā, tātad nav "bezmaksas", bet jāuzmanās ar bezmaksas paraugu: pielikumi tajā nav).

## 2. Stratēģija: ko un kā izvietot
**Princips:** PromptBase pārdod mazus, konkrētus promptus par $3–10; Jirgensona modeļa pilnais komplekts (kanons 14 lpp. + operatīvais prompts) ir cita klase, to pārdod pie sevis (Gumroad) par augstāku cenu, bet PromptBase izmanto, lai cilvēki to atrastu. Eksperimentu (E5) pabeigšana ir priekšnoteikums pilnajam komplektam; mazos promptus var likt uzreiz.

### Produkti PromptBase (kārtība pēc ieviešanas)
| # | Produkts | Cena | Kad | Ko tas dod |
|---|---|---|---|---|
| P1 | **The Refusal Test** (mērķu sakārtošana atteikuma secībā, sešu lauku tabula): 1 prompts ChatGPT/Claude | $3,99 ($4,99 griesti) | tūlīt | ieeja; aprakstā: "from the book Steer, Don't Guess" + saite |
| P2 | **Red Zone Triage** (zonas, sarkanais protokols, viena darbība šodien) | $3,99 | tūlīt | ieeja |
| P3 | **Backward Plan** (no mērķa uz šo nedēļu, tabula "laiks līdz mērķim / kam jābūt patiesam") | $3,99 | tūlīt | ieeja |
| P4 | **Owner's Dashboard Builder** (mērķu tabula, svetofora panelis, sviras, ritms; §14 instrumenti) | $4,99 → $9,99 pēc pirmajiem pārdevumiem | 1–2 ned. | pāreja uz komplektu |
| P5 | **Jirgenson Model: Management Analyst (full system)** = 02a kanons + 02b prompts, versija pēc E5 | $19,99–29,99 PromptBase (ja atļauj pēc vēstures) / **Gumroad $29–39** ar savu saiti | pēc E5 | galvenais produkts |
| P6 | **Agent skill** (SKILL.md ar kanonu un promptu; kategorija "agent skills", mediāna $9,99) | $9,99–14,99 | pēc E5 | jauna kategorija, mazāk konkurences |
Katram ierakstam: 3 īsti izvades piemēri (prasa tirgus; vāji piemēri = atmaksas), apraksts ar vienu rindu par grāmatu, saite uz Gumroad grāmatu. Grāmatas pircējiem: pielikumos H/I jau ir pilnais komplekts, tāpēc P5 pircējiem piedāvāt grāmatu ar atlaidi, un otrādi.

### Darbības
1. Konts PromptBase + Stripe (Martins). Profilā: autora bio, saite uz Gumroad.
2. Es sagatavoju P1–P3: prompta tekstu (no kanona, nemainot terminus), 3 piemērus katram, aprakstu, tagus. Martins publicē (2 dienā).
3. Pēc 14 dienām: pārdevumi, skatījumi; ja >0, P4; ja 0, P1–P3 paliek kā vitrīna bez laika tērēšanas.
4. Pēc E5: P5 un P6; Gumroad produkts "Jirgenson Model Kit" ar savu saiti arī PromptBase.
5. Promptu vitrīnas papildkanāli (bezmaksas): **GPT Store** (custom GPT "Steer, Don't Guess Analyst" bez maksas, grāmatas saite; vislielākā plūsma, nav ieņēmumu), **Claude skills / implo.ai** (jauns, mazs), **Gumroad** (sava saite), **Etsy** (prompt paki pārdodas, 6,5 % + $0,20; liela auditorija, bet nav AI filtru).

## 3. Alternatīvas PromptBase (īsi)
- **Gumroad / sava saite:** 10 % + $0,50; pilna kontrole; jau ir.
- **Etsy:** 6,5 % + $0,20 + apstrāde; liela pircēju bāze, promptu paki tur pārdodas; prasa veikala izveidi (Etsy pārdevēja konts, $0,20 par ierakstu).
- **GPT Store:** bezmaksas custom GPT; nav naudas, ir atpazīstamība un saite.
- **implo.ai, Neura Market, FlowGPT, PromptHero:** mazi vai attēlu/workflow tirgi; FlowGPT krīt. Nav prioritāte.
- **AIPRM:** nav pārdošana.

## 4. Visu pārdošanas ideju katalogs (projekts kopumā, stāvoklis 2026-10-16)
| # | Ideja | Statuss | Kur |
|---|---|---|---|
| 1 | LinkedIn savi kontakti, READER pret atsauksmi | iet (18 nosūtīti 13.10) | 16, 23 |
| 2 | YouTube kanāli, 50 % afiliāts + dāvana | iet (23 + dienas tabulas) | 22, 23 |
| 3 | Podkāsti (viesis / pieminēšana), e-pasti no RSS | iet (42 + 187 rezerve) | 25 |
| 4 | Konsultanti (EOS, Scaling Up, Profit First…), komandas kods | sākts (EOS 902 saraksts) | 26 |
| 5 | Emuāri un biļeteni, viesraksts + afiliāts | gatavs (64) | 27 |
| 6 | Gumroad radītāji tajā pašā kategorijā | saraksts 39, nav sākts | 20 |
| 7 | X/Twitter radītāji (DM prasa Premium) | gaida | 21 |
| 8 | Reddit un kopienas (lēns, tikai paraugs) | gaida | 17 |
| 9 | "Best business books" saraksti un redaktori | gaida | 18 §5.4 |
| 10 | PromptBase / prompt tirgi (P1–P6) | jauns, šis dok. | 28 |
| 11 | GPT Store custom GPT (bezmaksas vitrīna) | jauns | 28 |
| 12 | Jirgenson Model Kit (kanons + prompts + šabloni) Gumroad $29–39 | pēc E5 (Toolkit ideja no 19 atlikta, pārdzimst kā Kit) | 19, 28 |
| 13 | Komandas licence / kods klientu komandām | ieviešana pēc pirmā pieprasījuma | 26 §5 |
| 14 | Amazon KDP (paperback, Kindle) | atlikts: vajag EPUB/LaTeX, Select konflikts | 18 |
| 15 | Digistore24 / ClickBank afiliātu tirgi | atlikts: bez vēstures un ar $15 neņem | 19 |
| 16 | Komplekti (StoryBundle, Ultimate Bundles) | vajag EPUB | 19 |
| 17 | Izdevēji 15–25 mērķēti | pēc 30–45 dienām ar pierādījumu | 18 |
| 18 | getAbstract Wish List / Blinkist | iesniegt (bezmaksas, lēns) | 18 |
| 19 | RU grāmata (jau Gumroad), tulkojumi | tulkojumi noraidīti pagaidām | 07, 15 |
| 20 | Pasākums "Steer Week" ar partneriem (16.–22. nov.) | iespēja, ja būs ≥10 partneri līdz 9. nov. | 19 §4 |
| 21 | Black Friday 27.–30. nov. otrais vilnis | plānā | 10, 19 |
| 22 | Paša YouTube kanāls / LinkedIn biļetens / Medium | lēnie paša kanāli, vēlāk | 27 §2 |
| 23 | Kurss (Udemy) / darbnīca uzņēmējiem | ideja, nav sākta | — |
| 24 | Audiogrāmata | ideja, nav sākta | — |
| 25 | Licence konsultantiem (metode kā viņu produkts) | ideja, pēc partneru rezultāta | — |
| — | Maksas reklāma | NĒ (lēmums) | — |

## 5. Lēmumi Martinam
(1) Atvērt PromptBase kontu un ļaut man sagatavot P1–P3 (es rakstu, tu publicē). (2) Vai GPT Store custom GPT bez maksas kā vitrīnu. (3) P5/P6 un Kit cena pēc E5.

## 6. Avoti
- Trustpilot PromptBase: https://ca.trustpilot.com/review/promptbase.com
- Trafiks: https://aipure.ai/products/promptbase ; https://semrush.com/website/promptbase.com/overview
- Cenu izlase (konkurents): https://cartmango.com/sell-ai-prompts/
- Noteikumi, alternatīvas (konkurents): https://implo.ai/promptbase-alternatives/
- Komisija, izmaksas (emuārs bez avotiem): https://aiprofitmode.com/how-to-sell-on-promptbase.html
- Cenu stratēģija (emuārs): https://greyjournal.net/hustle/how-to-sell-ai-prompts-2026/
Nepārbaudīts: PromptBase oficiālā pārdevēju lapa (nebija nolasāma); vai Claude prompti PromptBase ir atsevišķa kategorija; cik no 532 tūkst. ir pircēji.

## 7. Pārbaudīts tieši PromptBase (Chrome, 2026-10-18)
**Oficiālie noteikumi (promptbase.com/prompt-guidelines, /knowledge-base/payouts):** tikai **veidņu** prompti ar `[kvadrātiekavu]` mainīgajiem; angļu valodā; komanda **testē** promptu ar pārdevēja "test prompt" (viena aizpildīta versija) un salīdzina ar iesniegtajiem piemēriem; piemēriem jābūt dažādiem (ne vienādām ievadēm); atsaka: nav lietojuma, pārāk šaurs (>3 idejas), pārāk vienkāršs/uzminams, zema kvalitāte, **"AI generated prompts"** (masveidā ģenerēti; cilvēka rakstītus var apstrīdēt), plaģiāts, **nedrošs** (piem., čatbots ar medicīniskiem padomiem; mūsu gadījumā: jābūt rindai "not financial/legal advice", kas kanonā jau ir), dublē esošu. Sīktēls bez cenām un bez daudz teksta. Izmaksa: 20 % maksa; 80 % nonāk "pending" 72 h; Stripe izmaksa, kad kontam ≥30 dienas un atlikums ≥$30 (nedēļas/mēneša grafiks; agrāk par $3,99); Zoneless (USDC) katru dienu bez minimuma. Sell lapa: "0% fees via your link, 20% via marketplace"; var pārdot arī **agent skills (SKILL.md)**.
**Kā izskatās pārdotākie biznesa teksta prompti (3 nolasīti):**
- *Complete Startup Plan* (@drewz, $4,99, 603 pārdevumi, 13,5 tūkst. skatījumu, GPT): 466 tokeni; viens mainīgais `[industry/sector]`; izvade = garš strukturēts plāns (SWOT, PEST, 7P, pitch, FAQ, roadmap). Pircējs pērk **rezultāta struktūru**, nevis prompta gudrību.
- *Your Startup Consultant* (@promptifypro, **$34,99**, Claude): 5 268 tokeni; 5 mainīgie, katrs ar paskaidrojumu iekavās; izvade 16 fāzes ar tabulām, "decision gates", skaidri atrunātas pieņēmumi un "not validated". Tātad cena virs $4,99 ir iespējama, kad pārdevējam ir vēsture (277 pārdevumi, 5,0).
- *Business Decision Solutions Finder* (@tedem, $4,99, 4 800 tokeni): viens brīvā teksta `[BRIEF]` ar instrukcijām iekšā + izvēles skalas 1–5; izvade: auto-diagnoze, 3 virzieni, gatavs "ready-to-use prompt", pieņēmumu saraksts, atrunas, norādes uz citiem autora promptiem (savstarpēja reklāma).
**Secinājumi formai P1–P3:** (1) 3–5 mainīgie ar paskaidrojumu iekavās, viens no tiem brīvs apraksts; (2) izvade stingri strukturēta: tabula + īsas sadaļas ar pieņēmumiem un "kas nav zināms"; (3) viens piemērs ar pilnu izvadi (kafejnīca), test prompt = tā pati ievade; (4) apraksts ar 3 emoji rindām (tirgus norma) un rindu "from the method in Steer, Don't Guess (book link)"; (5) katra prompta beigās norāde uz pārējiem diviem un uz grāmatu; (6) teksts rakstīts cilvēka valodā, lai nekrīt zem "AI generated"; (7) atruna "not financial, legal or investment advice; the owner decides".
