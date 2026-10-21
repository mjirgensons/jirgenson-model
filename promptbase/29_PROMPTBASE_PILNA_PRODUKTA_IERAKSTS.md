# 29. PromptBase: pilnā produkta pakete (prompts + kanons kā DIVI faili) (2026-10-21, v3)

## 0. Lēmumi (Martins, 13:43 un 13:59)
- Pārdod pilno produktu, nevis mazos promptus. Pircējs saņem **divus teksta failus** (nekādu PDF; PDF dedzina tokenus un nav vajadzīgs): `jirgenson_prompt_v1.1_en.txt` un `jirgenson_canon_v1.0_en.txt`, tieši tādus, kādi ir grāmatas 1.1 izdevumā un GitHub repozitorijā `mjirgensons/jirgenson-model`. Versijas: prompts **v1.1** (iekšējais E5 apzīmējums 1.3-c vairs netiek lietots), kanons v1.0. Vienfaila versija un PDF atcelti (21.10).
- **Viss, kas attiecas uz PromptBase, glabājas GitHub mapē `promptbase/`** tajā pašā repozitorijā (produkta faili + šis dokuments + 28), paralēli projektam.
- Piemēri ierakstā ir **īstās E5 izvades** (eksperiments 18.10: 88,9 pret 55,9; 30/30; izdomāti fakti 75 % → 11 %). Nekas nav sacerēts.

## 1. Faili (GitHub `promptbase/`, kopijas no repozitorija saknes)
| Fails | Saturs |
|---|---|
| `promptbase/jirgenson_prompt_v1.1_en.txt` | operatīvais prompts v1.1 (grāmatas 1.1 izdevums, I pielikums), teksts nemainīts |
| `promptbase/jirgenson_canon_v1.0_en.txt` | kanons v1.0 (H pielikums), teksts nemainīts |
Pircējs pievieno abus failus jaunai sarunai (vai kopē tekstu). Lietošanas norāde ir pircēja ceļvedī (§4), nevis failos.

## 2. Konts PromptBase (Martins; es kontu veidot nedrīkstu)
1. Chrome cilnē jau ir atvērts `promptbase.com/login?view=signup&sell=true`: **Continue with Google** (vai e-pasts → Continue). Konts ir bezmaksas.
2. Profils: vārds Martin Jirgenson, bio 2 rindas (autors, grāmata), saite uz Gumroad grāmatu, foto.
3. **Sell → Get Started** → pārdevēja forma. Stripe pieslēdz tajā pašā plūsmā vai pēc pirmā pārdevuma; izmaksa kontam ≥30 dienas un atlikums ≥$30 (tāpēc kontu atver šodien).
4. Publicēt var uzreiz pēc konta: ieraksts aiziet pārbaudē (komanda testē promptu), parasti dienas laikā līdz dažām dienām (laiks nav oficiāli norādīts).
5. Kad esi ielogojies, pasaki: es nolasu formu (lauki, limiti, vai skill pieņem vairākus failus) un aizpildu tekstus pa laukiem.

## 3. Kā divi faili nonāk pie pircēja (trīs ceļi, izvēlas pēc formas)
- **A. Claude Skill (SKILL.md)** ar kanonu kā otru failu, ja augšupielāde pieņem mapi/vairākus failus: dabiskais formāts, kategorija ar 2 800 ierakstiem un mediānu $9,99.
- **B. Teksta prompts + ceļvedis.** Prompta laukā 02b; pircēja ceļvedī ("guide to the prompt", redzams pēc pirkuma) kanona pilns teksts + saite uz abiem failiem GitHub (publiski, bezmaksas: tie jau ir repozitorijā) vai Gumroad produkts "Jirgenson Model Kit" ar 100 % kodu tikai pircējiem vai tieša lejupielāde). Test-promptā pārbaudītājiem jāiekļauj kanons, citādi vārti apstājas.
- **C. Divi ieraksti + Bundle** (produkta tips pastāv): "Operating Prompt" un "Canon" atsevišķi, komplektā kopā.
Paralēli visos gadījumos: **Gumroad "Jirgenson Model Kit"** (abi TXT faili) $29 ar savu saiti; PromptBase ierakstā "0 % via your link" nozīmē, ka no LinkedIn/X var sūtīt uz PromptBase ar savu saiti bez komisijas.

## 4. Ieraksta teksti (EN), gatavi ielīmēšanai
**Title:** `Jirgenson Model Business Analyst` (alternatīva: `Steer Don't Guess Business Analyst`)
**Model:** Claude (otrs ieraksts GPT pēc pārbaudes ar ChatGPT).
**Short description / tagline:** `A complete management method for AI: two files (operating prompt + canon). Tested blind on 10 real cases: 88.9/100 vs 55.9 without.`
**Description:**
```
📊 Not a template. A complete management method your AI follows: two files, the Operating Prompt and the Canon. Attach both to a new chat (Claude, ChatGPT, Gemini), describe your business, freelance work or family budget with your own numbers, and you get: where you really stand, the most dangerous event with its date, what to do today / this week / this month, what to protect first, what not to do now, what to measure, and two honest forecasts (if nothing changes / if the plan works).

🧪 Measured, not promised. Blind test, 10 realistic cases (cash crisis, non-paying client, 72-hour permit deadline, seasonal workshop, a teenager saving up; English, Latvian, Russian), 3 runs each, judged by a stronger model that could not see which answer was which, every pair judged twice in both orders:
• 88.9 / 100 with the method vs 55.9 without (+33, 95% CI +27.8 to +38.4)
• the judge preferred the method's answer 30 times out of 30
• answers containing an invented fact: 75% → 11%
• rule violations (too long, too many questions, wrong language): 52% → 0%
• worst answer with the method (75) beat the best answer without it (72)
Limits, stated plainly: an LLM judge, 10 cases, one model family (Claude Sonnet 5.5). The full method and the experiment are described in the book "Steer, Don't Guess".

🧭 What is inside: goals in refusal order (which goal you would give up last), red lines set before the crisis, levers you can move yourself vs conditions you cannot, two forecasts with ranges, a measurement rhythm. Four modes: EMERGENCY (one action for today, under 270 words), QUICK (full brief in 20 minutes), FULL (rounds of questions), PLAN CHECK (bring your list of goals). Answers in the language you write in.

⚠️ Not financial, legal or investment advice. The method never decides for you and never invents data: it proposes, you confirm.
```
**Guide to the prompt (pircējam pēc pirkuma):**
```
You received two files. 1) Open a new conversation. 2) Attach BOTH files (or paste both texts): the Operating Prompt tells the model how to work, the Canon is the theory it must obey; the prompt checks that the Canon is present and will not answer without it. 3) Describe your situation with numbers. Say "emergency" for one action today, "quick" for a 20-minute brief, "plan check" if you bring a list of goals, or just ask. 4) If you have no more data, say so: the model stops asking and labels its assumptions. Keep both files in a project or system instructions to reuse them. Updates to the files are free for buyers.
```
**Variables (PromptBase prasa `[iekavas]`):** prompta sākumā pievienot vienu rindu, ko pircējs aizpilda:
`My situation: [describe your business or situation with your numbers]. Mode: [emergency / quick / full / plan check, or leave blank]. Time: [e.g. 20 minutes, optional].`
Pārējais prompta teksts nemainās (tas nav kanona vai 02b labojums, tikai ievades rinda ierakstam).
**Test prompt (pārbaudītājiem):** tā pati rinda ar E5 uzdevumu "sezonāla velosipēdu darbnīca" + abu failu teksts (lai vārti atveras).
**Example input / output (3):** E5 īstās izvades: (1) QUICK, velosipēdu darbnīca EN (91,7); (2) EMERGENCY, frīlanseris RU (89,5) — rāda daudzvalodību; (3) PLAN CHECK, jogas studija 11 mērķi EN (88,2). Ņemu no `e5/buffer`, nemainot tekstu.
**Price:** sākums pie jauna pārdevēja griestiem ($4,99, nepārbaudīts oficiāli); pēc pirmajām atsauksmēm $19,99 → $29,99. Gumroad Kit $29 no pirmās dienas.
**Tags/kategorija:** Business, Finance, Plan, Coach. **Sīktēls:** grāmatas vāka motīvs, bez cenām un teksta.

## 5. Stratēģijas prioritāte pēc E5 (atbilde uz "visefektīvākā šobrīd")
1. LinkedIn ieraksts + ziņas kontaktiem ar eksperimenta skaitļiem (šonedēļ). 2. Podkāsti ar tēmu "mēs izmērījām AI padomus ar un bez vadības modeļa". 3. PromptBase + Gumroad Kit (šis dok.). 4. Konsultanti. 5. Emuāri ("we tested…" viesraksts). Grāmata ziņās kļūst par dziļumu pie instrumenta.

## 6. Nedarīt
Nepārrakstīt 02a/02b tirgus vajadzībām; neapgalvot "pierādīts visiem modeļiem"; Gemini recenzijas toni ("dzelžainie iemaukti", "vienīgais veids") lietot LinkedIn/X, ne tirgus aprakstā (R8, PromptBase atsaka par pārspīlējumiem).

## 7. Mērīt
PromptBase skatījumi/pārdevumi/atsauksmes nedēļā; Gumroad Kit un grāmata pēc LinkedIn ieraksta. Pārskats 25.10 un 1.11.
