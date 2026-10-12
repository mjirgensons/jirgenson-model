# JIRGENSON MODEL CANON v1.0 (canon-id: JMC-1)

PURPOSE: Machine-readable core of the Jirgenson Management Model (theory, algorithm, terminology). Use as the single source of truth. MUST = mandatory rule. Terms are fixed: do not replace them with synonyms.

## 0. THESIS
0.1 Any result can be treated as a process in which points of control can be found. Management = (1) know where you go: GOAL VECTOR G; (2) know where you really are: STATE VECTOR S; (3) reduce the gap: ERROR VECTOR E = S ⊖ G (deviation of the state from the goal). Everything else is a way to do this regularly, precisely, and on course.
0.2 Problems are solved by priority, not by order of arrival. Intake queue may follow arrival order; the solving queue follows G (refusal order) and the zones of E.

## 1. GOAL VECTOR
1.1 G = ordered list of measurable parameters, n ≤ 9. This is a design limit of the model for a human working without software or AI assistance; it is consonant with Miller's 7±2 but is NOT a claim about the exact capacity of human working memory. For software- or LLM-operated systems the number of parameters may be larger by orders of magnitude; the refusal order, zones and all other rules stay unchanged. Where the number of parameters is large, group them hierarchically and aggregate; a longer flat list does not make the order easier to confirm.
1.2 ORDER = REFUSAL ORDER. Ask: "If circumstances force you to drop goals one by one, which first, second, … last?" The last remaining = rank 1 (highest). The first dropped = rank n (lowest). Order is the owner's subjective choice. MUST NOT be chosen for the owner (an AI may propose; the owner confirms).
1.3 The same set of goals in a different order is a different vector (different decisions in crisis).
1.4 Scan six areas: Finance; Clients; Sales; Processes and quality; People; Development and owner (owner's time, health, money, freedom). Take 0-3 parameters per area (an area may stay empty only by a conscious, recorded choice); total ≤ 9. For non-business subjects adapt the areas but keep the scan.
1.5 Six fields of a goal: (1) parameter; (2) definition: how counted, which source; (3) target value and deadline; (4) current value; (5) permissible deviation; (6) check rhythm and owner. No number, unit, or deadline = a wish, not a goal.
1.6 Goal ≠ method. Goal = what to achieve. Method = how. Methods belong to the concept (§5), not to G.
1.7 Defects of G (check all five): mutually exclusive goals; loss of an objectively necessary requirement (legal, safety and contractual requirements are constraints, not goals to be dropped); unstable goals (order changes constantly); violated order (secondary saved at the cost of primary); duplicates (one goal under two names).
1.8 G may depend on time, G(t) (manoeuvre, §9). At any moment it is fixed and recorded.
1.9 Control is defined only if (i) the order of goals is clear AND (ii) permissible and impermissible means are clear.
1.10 Four layers: (1) constraints (law, safety, contracts, human limits): they are not dropped in order, they define which actions are permissible; (2) minimum acceptable levels; (3) improvement goals, ranked by the refusal order; (4) a rule for allocating the remaining resources (urgency, risk, price). The refusal order elicits preferences; it is not a complete decision algorithm. If saving a top goal requires violating a constraint, the constraint decides: find another way, or stop and change the conditions.

## 2. STATE VECTOR
2.1 S has the same rows and order as G; values are measured facts now. S here = the measured values of the goal parameters; the full state of the system is wider (obligations, capacities, dependencies, wear, skills): build forecasts on the full state, not only on the panel.
2.2 ONE INDICATOR = ONE DEFINITION, ONE MAIN SOURCE, ONE OWNER OF THE CALCULATION; other sources may be used for reconciliation.
2.3 Measurement, not feeling. "Many / few / normal" are not values. Panic and bravado both replace facts with feelings. Accept the state as it is.
2.4 Measurement uncertainty is objective and cannot be removed fully. The question is whether it is admissible for the goal: it must be clearly smaller than the goal's permissible deviation, otherwise noise is being managed.
2.5 For every number ask: who counted, how, for which period.
2.6 If no source exists, the first action is to build a minimal measurement system.
2.7 Indicators change behaviour: add a protective indicator and an independent check where gaming is likely.

## 3. ERROR VECTOR AND ZONES
3.0 The error is the effect of the combined action of the environmental factors (§16) and of the owner's actions; the zones measure how strongly the factors have deflected the trajectory from the goal.
3.1 E is computed per row as the deviation of the state from the goal (state minus goal), with the sign documented per parameter. Zones are defined by permissible sets of values, not by |E|; for a one-sided goal an excess above the goal is not a violation.
3.2 Zones are defined per parameter in advance, in a calm moment:
- GREEN (norm): error within tolerance. No corrective intervention on the current deviation; prevention is assessed separately by future risk.
- YELLOW (acceptable): worse than norm, no harm to structure. Observe, find the cause, prepare a lever.
- RED (emergency): a parameter is outside the permissible limit; irreversible loss has not yet occurred. Returning to at least yellow is the main task; the rest is postponed. Catastrophe lies beyond red.
- UNDEFINED (grey): data missing, stale, contradictory or too imprecise. Measure first; never treat it as green.
3.3 Threshold rules: tolerance ≥ measurement uncertainty; the red boundary lies where damage becomes hard to reverse; thresholds are recorded in calm and revised rarely, never inside a crisis. If a parameter oscillates near a boundary, use different entry and exit thresholds or confirmation by several measurements.
3.4 RED PROTOCOL: (1) check immediate danger (safety, mandatory obligations, law): protective action and escalation first; (2) freeze secondary work; (3) concentrate time, money and attention on the red parameter and the levers acting on it; (4) if several reds exist, first the one that threatens the nearest irreversible damage (time, scale, probability, speed of the lever), then by the rank of the goal; account for dependencies between threats.
3.5 Triage of a new problem: (a) which goal does it belong to? (b) in which zone is its parameter? (c) is it more important than what is being done now?
3.6 Stability margin = the largest disturbance absorbed without leaving the permissible region. Build it in advance (example: cash reserve).
3.7 Control quality = one aggregate score of E. It is subjective (choice of goals, order, aggregation rule). The optimum is not always needed or reachable; "good enough" = all errors within permissible zones.
3.8 'Error' covers different things; keep them apart: gap to the final goal; deviation from the plan at a given moment; forecast error; measurement uncertainty; constraint violation.

## 4. CONTROL VECTOR (LEVERS)
4.1 Result ≠ lever. Lever = a parameter changed directly by the owner's decision. Conditions = environmental factors that cannot be changed (§16.3); list separately; never plan on them.
4.2 Controlled vs free parameters. Free ones change when levers change, are not in G, their values are acceptable for the current task, but check whether they have become constraints or risk indicators. If a free parameter becomes important, move it into G and add a lever.
4.3 Lagging (outcome) vs leading indicators. Each financial goal needs ≥ 1 leading indicator. A leading indicator carries information about the likely future result over a stated horizon; the predictive link must be tested.
4.4 Information rank (decreasing value): processes that may open a threat or an opportunity; possibility has opened; it began to realize / trend; deviation within permissible; deviation at the edge; beyond the limit. "All normal" does not call for moving levers; its value for the decision is small, though it refines the risk estimate. Opportunities count as well as threats.
4.5 Lever test: can it be moved by the owner, today? delay to effect? reversible? Start with fast and reversible levers.
4.6 No lever found: the goal is not directly manageable (decompose it) or the level of responsibility is wrong.
4.7 In a red zone, move first the levers that act on the red parameter. A single lever is an optional simple-experiment mode: causal conclusions need comparison, alternative explanations and enough observation time. In an emergency a package of actions is allowed; check the interactions of levers.

## 5. CONCEPT
5.1 One plan per goal; all plans together = general concept. Plans MUST NOT contradict each other (check pairs).
5.2 Five questions of a plan: (1) levers and their order; (2) resources; (3) constraints: what will not be done even if faster; (4) leading indicator; (5) deadline, owner, first checkpoint. A missing answer is the next task. A plan fits one page.
5.3 Constraints are written in advance, in calm.

## 6. FULL CONTROL CYCLE (8 STAGES)
| # | Stage | Control question |
|---|---|---|
| 1 | Notice the pressure | Is the factor real, not imagined? Do we know enough about the environment to recognize it? |
| 2 | Recognize the situation | Would two independent observers see the same by the same parameters? What measures each? |
| 3 | Set the goal vector | Any defects in G (§1.7)? Is every goal measurable? |
| 4 | Build the concept and solve predictability | Is forecasting solved? General concept and plan per goal exist? |
| 5 | Build structures | Each section has a personal owner, authority, resources? |
| 6 | Observe and coordinate | Is the plan running? Who looks at E and when? |
| 7 | Improve the concept | Review by the same questions as stages 1-4. |
| 8 | Finish or maintain | Who keeps the result? What happens to people and resources? Or how is readiness maintained (rhythm changes: monthly instead of weekly)? |
6.1 Stages 1 and 8 are always present. Middle stages may be merged or detailed, never dropped.
6.2 A skipped stage either remains unperformed or is performed by someone else (market, bank, competitor, debts, crisis).
6.3 Stages 1-4 = forecasting part (forecast and control law). Stages 5-7 = executing part (runs the law and adapts it to circumstances).
6.4 Only the forecast-based scheme (§8, level 3) carries all eight stages.

## 7. PREDICTABILITY
7.1 One can control only what can be foreseen well enough. Besides ordinary stability (deviation decays), there is predictability for the controller: the controller can foresee the object's behaviour well enough to control it. It is a joint property of object + person at the wheel (objective and subjective merge). It depends on three things: the environmental factors (§16), the object's own changes, and the quality of control. Predictability is not controllability: a payment date is predictable, but the money may not exist.
7.2 What looks random to you may be predictable and managed by someone else. Ask: who foresees it and how? Randomness in the model means a probabilistic description, not denial of causes; part of the uncertainty can be reduced by information, the rest remains and is carried in decisions.
7.3 One object can be predictable by some parameters and unpredictable by others. Ageing of objects and fatigue of the controller reduce predictability.
7.4 The probabilities of all variants of the future sum to 1. Control shifts probability weight to the chosen variant. Required control cannot be computed from one probability: compare scenarios (probability of the goal under different actions, cost, risk of adverse outcomes); where probabilities are unknown, use ranges and qualitative scenarios, labelled.
7.5 Responsible negative forecast: name the risk early and attach action (within the model, levers are engaged earlier, so failure probability should fall; the effect depends on the quality of the action). A forecast without action produces panic and worse decisions.
7.6 A forecast has a range and conditions; compare it with facts regularly.
7.7 Always produce two forecasts with numbers and dates: "if nothing changes" and "if the plan works". Name who foresees each critical segment.

## 8. SCHEMES OF CONTROL
- Level 1, by plan [open loop]: no feedback from reality; cannot adapt.
- Level 2, by deviation [feedback on deviation]: measures the deviation and corrects. Typically lags (detect, transmit, decide, act, inertia; in control theory described as phase lag) and, with unfavourable delays and gains, may oscillate. Variant: by disturbance (react to a measured cause before the deviation appears).
- Level 3, by forecast [forecast with correction]: the loop closes through the predicted future, corrected by facts; a forecast or an advance signal is used to act before the disturbance. Feedback is retained because forecasts err. Needs a model and discipline; with a poor model it can be worse than feedback. The levels are schemes, not a ladder: they are combined. Small-business form: rolling 3-6 month forecast updated weekly or monthly.

## 9. MODES
9.1 Steady (balancing) mode: G constant, oscillation around it. Manoeuvre: G moves in time.
9.2 Error is a reason to change the plan. The goal changes only when conditions or priorities changed; record the change.
9.3 Strength and duration of a manoeuvre are measured in the system's own time units, not in calendar time.
9.4 A manoeuvre = a corridor of permissible errors along the goal trajectory (values and times at checkpoints). A smooth manoeuvre has three periods: exit from the old mode, then steady manoeuvre, then entry into the new mode. Check that the whole area of movement lies in the controllable region; route around break points. Unconditionally stable manoeuvre = disturbances cannot leave the corridor; conditionally stable = trajectory is corrected on the way.
9.5 Launch conditions are recorded before the manoeuvre, as measurable events, never as a date wish. Do not start a GROWTH manoeuvre while any parameter is red. A RECOVERY manoeuvre (exit from a crisis) starts in the red zone: the emergency itself is its launch condition.
9.6 Review rhythm follows the speed of change and the time to damage: levers weekly; error vector weekly for fast parameters (cash) and monthly for slow ones; concept quarterly; goal vector every 6-12 months.

## 10. THREE OFFSETS (check before acting)
An offset = a shift of an anchor point of the plan relative to reality: of the goal, of the starting state, or of the environment.
| | Offset | Question | Action |
|---|---|---|---|
| a | Badly defined goal (mutually exclusive: two trains in opposite directions) | Any goals that cannot be met together? | Return to refusal test; remove the contradiction |
| b | Wrong initial state ("window taken for exit") | Do my numbers match the source data? | Audit data; re-measure |
| c | Doomed enclosing system ("Titanic test": goal belongs to a dying process) | Is the environment growing or dying? | Change the environment, not the tactics |
10.1 "Titanic test" names offset (c) only. Doomed means: sustained decline over several periods, exit of strong players, no niche where the economics converge on your horizon; weigh the cost of a wrong exit.
10.2 Backward planning (§12) cannot be built under (a) or (b); under (c) the best route ends in a dead end.
10.3 Offset (c) is the strongest environmental factor: it is directed against the goal and exceeds the owner's means (§16.6).

## 11. SEVEN STEPS OF ENTERING CONTROL
1 Calm the noise (agree on facts, not opinions). 2 Read the state without distortion (data audit). 3 Restore the trajectory of the past (12-36 months: speed and acceleration, not a point). 4 Decompose nested processes (what improves, what worsens). 5 Find the enclosing shell (industry, cycle, regulation); principle "judo, not boxing": amplify what already moves the right way. 6 Build a multi-variant forecast (scenarios with probabilities and decision points). 7 Decide and accept the consequences (act or consciously refrain; effects arrive with delay; one lever at a time).

## 12. BACKWARD MOVE (BACKWARD PLANNING AND DYNAMIC PROGRAMMING)
12.0 Three different things; do not conflate: backward planning (practical technique: start from the result, ask what must be true immediately before it); dynamic programming (mathematical theory of multi-step optimization, often solved backward in time, broader than backward planning); Bellman's principle (a property of optimal policies).
12.1 Backward planning: choose the end state; ask what must be true one step before it; repeat back to today. Bellman's principle: whatever the initial state and the first decision, the remaining decisions must be optimal with respect to the state resulting from the first decision. In practice: the best next move depends on the state, provided the state is described sufficiently completely (if history matters, include it in the state). (Richard Bellman, 1920-1984, RAND; "programming" = planning.)
12.2 Five diagnostic questions (does the task suit Bellman-type optimization?): (1) can the task be split into steps with a defined horizon? (2) is the transition rule known; if rules change over time, is the dependence stated explicitly? (3) is the state described sufficiently completely, with history included if it matters? (4) does the best next move depend on the state rather than on the path? (5) can the result be evaluated as a consistent composition (in the simplest case a sum) of step evaluations? Perfect "yes" answers are rare; use them as a discipline check. If the first three cannot be answered, the task is not yet understood well enough to be controlled.
12.3 For a concrete finite task, backward optimization requires a defined initial state, a defined target state, and transition rules. A start error beyond tolerance leads astray (do not take an open window for an exit).
12.4 The goal must belong to a living enclosing process. JIRGENSON HYPOTHESIS (the model's working principle, not a Bellman theorem): the better the goal is aligned with the direction of the enclosing system, the lower the resistance that must be overcome. Convergence of trajectories from different starts ("all roads lead to Rome") holds for some stable systems; it is a property of the system dynamics, not of the method.
12.5 Output: table with two columns, "time before goal" and "what must be true"; the first row answers "what to do this week". Check resources and financing of every step.
12.6 Formal (finite horizon, deterministic): V_t(S_t) = min over U in Ω of [ C_t(S_t,U) + V_{t+1}(S_{t+1}) ], S_{t+1} = f_t(S_t,U); the terminal value V_N(S_N) may be a function; for a random environment use an expectation or a risk criterion and a transition distribution.

## 13. COMPLETENESS TEST (nine categories)
(1) Goal vector; (2) State vector; (3) Error vector; (4) Levers; (5) Concept; (6) Structures; (7) Forecast (including environmental factors, §16); (8) Scheme; (9) Mode. If any category is empty, stable control is not yet in place: request the missing input. A rough version is enough to start: fill each category with at least one line. If the object's behaviour is not predictable (§7), control is not possible.

## 14. INSTRUMENTS
Goal table; data sources; traffic-light dashboard (parameter, goal, now, error, trend, zone); lever list with owners; one-page plan per goal; rolling forecast; meeting calendar. Implementation: 1 choose parameters; 2 assign a source to each; 3 build minimal measurement; 4 fill state honestly; 5 set zones; 6 set meeting rhythm.

## 15. LIMITS AND HONESTY
15.1 No guarantees of results. Example numbers are illustrative.
15.2 The model never chooses the owner's priorities, and never invents data.
15.3 An AI assistant proposes, the owner confirms; data come from the owner; unknown data are requested, not guessed.
15.4 The model does not remove the limits of language models (errors, loss of context). If output degrades or disagrees with the owner's numbers, treat it as RED: diagnose first (data, calculation, rule version, canon), correct the source of the error, and only then reset the context and re-supply this canon and the vectors G and S.
15.5 A citation of a canon section shows where the rule comes from, not that the rule or its application is correct.
15.6 If the assistant is connected to data or can act: minimal access rights, separate read and write, human confirmation for high-impact actions, logging, personal-data protection, an automation stop switch, a test environment.

## 16. ENVIRONMENTAL FACTORS
16.1 Definition: everything that acts on the path toward the goal and carries it along or deflects it from the goal vector: weather, prices, competitors, an industry trend, and also the owner's own lack of knowledge, time or money. There are infinitely many; each has a direction and a strength. Whether a factor comes from the world around or from the owner is not essential. A factor is a role, not a thing: the same item may be state, factor or lever; do not count it twice in one calculation.
16.2 Factors act simultaneously. The total effect is, as a first approximation, the vector sum of their directions and strengths; interactions, thresholds and nonlinearities exist. Factors along the goal make the path easier; against it, harder; sideways, they deflect.
16.3 Some factors can be neutralized or used by choosing the right instrument (a lever applied to the factor itself: the rudder, not the oar); others cannot be changed and are conditions (§4.1).
16.4 A factor must first be recognized and its strength assessed; recognition is a separate skill (§7). An unrecognized factor is not compensated (a yacht with an unnoticed drift arrives elsewhere).
16.5 The error vector and its zones measure the total effect of the factors on the trajectory (§3.0): the cause is the factors, the effect is the error. The factors are examined before the error.
16.6 Rule: when the strongest factor is directed against the goal and exceeds the owner's means, tactics are powerless: ride with it or change the environment or the goal (offset (c), "Titanic test", §10).
16.7 Every plan lists the main factors for each goal with direction, strength and the instrument chosen. A plan with no factors listed is incomplete.
