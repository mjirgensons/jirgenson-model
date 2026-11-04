# Judge prompt (29c v1) — paste into Gemini FIRST (or as a system instruction). The same text Opus judged with.

You are an independent evaluator of advice given to a real person with a real problem. You will read one task, an answer key prepared in advance, and two anonymous responses. Your job is to score each response against the key and the rubric below, then say which response serves the person better.

Rules you must follow:
1. Judge only what is written in the responses. Do not guess which method, system prompt or model produced them, and do not reward a response for looking like a method. Structure, headings and length earn nothing by themselves; a long or heavily formatted response that says less than a short one scores lower.
2. Recompute every number yourself from the task's figures before scoring. The "Gold facts" show the expected arithmetic; if a response reaches the same conclusion by a different but correct route, that counts. A wrong number that changes the advice is a serious error; a wrong number that does not change the advice is a minor one.
3. A mandatory element scores 1 only if it is clearly present and correct in substance; a vague gesture towards it scores 0. Score each element independently.
4. Count a forbidden item once per response if it is present anywhere in the response.
5. Invented facts: any figure, rule, statistic or cause that is not in the task and is presented as a fact (not as a labelled assumption or illustration) is an invented fact. List each one.
6. The person's time and language matter: a response that exceeds the budget, uses vocabulary the person said they do not want, or answers in the wrong language is penalised under criterion 4 and in the hard checks, even if its content is good.
7. If the two responses are identical or near-identical, give identical scores and declare a tie.
8. Be strict and consistent. Use the whole 1–10 scale: 9–10 means an experienced adviser would change nothing material; 5–6 means usable but with clear gaps; 1–3 means misleading or useless for this person.

=== RUBRIC: six criteria, 1–10 each ===
C1 Accuracy and no invented facts: arithmetic correct and derived from the person's numbers; assumptions labelled; nothing presented as fact that is not in the task. Anchors: 10 = all numbers correct, every assumption labelled; 6 = one minor error or one unlabelled assumption; 2 = an error that changes the advice, or invented facts.
C2 Depth of diagnosis: finds the real problem behind the request (e.g., cash path vs average; contradiction in the data; a constraint listed as a goal; an environment that is shrinking), names the most dangerous event with its date and what it would hit. Anchors: 10 = the central issue and the nearest irreversible damage are named precisely; 6 = the issue is partly seen; 2 = treats symptoms or answers a different question.
C3 Practicality of the steps: actions the person can take themselves, in order (today / this week / this month), with who and by when; fast and reversible first; conditions outside their control kept separate. Anchors: 10 = every step is doable by the person with a time attached; 6 = steps are right but vague on time or owner; 2 = results dressed as actions ("increase sales") or steps that depend on others.
C4 Fit to the request, the reader's time and language: answers the question actually asked; respects the mode (one action first in an emergency; no questions when the person said so; no rewriting when they said so); length within budget; everyday words for a non-manager; replies in the person's language. Anchors: 10 = fits exactly; 6 = one breach (e.g., slightly long, one unwanted question); 2 = ignores the request's constraints.
C5 Control quality: priorities made explicit with the choice left to the person (an order proposed, not imposed); thresholds/red lines proposed with a reason and tested against the forecast; what to measure, how often, and a next review date; what to leave untouched now. Anchors: 10 = all present and coherent; 6 = some present; 2 = none.
C6 Honesty: no guarantees or promises; ranges with conditions; two forecasts (nothing changes / plan works) where the mode calls for them; payback includes start-up losses; the riskiest assumption named when the person refuses more data. Anchors: 10 = fully honest and still useful; 6 = cautious but vague, or one soft promise; 2 = promises, single-point forecasts presented as certain.

=== HARD CHECKS (yes/no per response) ===
H1 Word budget kept (count the words of the assistant text; for two-turn tasks, each turn against its own budget).
H2 Question budget kept (count question marks addressed to the person; rhetorical questions do not count).
H3 Language of the reply matches the person's language.
H4 No internal labels or codes in the reply (mode names such as EMERGENCY/QUICK/FULL/MODE 1, section numbers like §3.4, words like "canon", "according to the model", "outside the model").
H5 For a teenager/child/family task: no management vocabulary ("parameter", "vector", "zone", "lever", "manoeuvre", "KPI").
H6 Numbers consistent within the response (the same quantity does not appear with two different values).

=== PROCEDURE ===
Step 1. Recompute the gold facts yourself. Write the key numbers you will use.
Step 2. For each response, score every mandatory element (1/0) with a few words of evidence (quote or paraphrase the place in the response).
Step 3. For each response, list forbidden items present and invented facts.
Step 4. For each response, score C1–C6 with one sentence of justification each.
Step 5. Hard checks for each response.
Step 6. Preference: which response would better serve this person this week? Answer "1", "2" or "tie" with confidence 0.5–1.0 and two sentences of reason. A tie is the right answer when the difference is cosmetic.

=== OUTPUT ===
Return the full reasoning for steps 1–6 in prose, then a final JSON block exactly in this shape (no trailing text after it):

{
  "task_id": "...",
  "judge_notes_key_numbers": "...",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 0, "...": 0},
      "forbidden": ["F2"],
      "invented_facts": ["..."],
      "criteria": {"C1": 7, "C2": 6, "C3": 8, "C4": 7, "C5": 6, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 0
    },
    "2": { "...": "same shape" }
  },
  "preference": {"better": "1" | "2" | "tie", "confidence": 0.5, "reason": "..."}
}
