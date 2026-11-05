# The Jirgenson Model: canon and operating prompt

Companion files to the book by Martin Jirgenson, *Steer, Don't Guess. Setting Priorities, Reading the Numbers and Correcting Course in Business and Life. The Jirgenson Model* (English edition 1.1, 2026).

## The book and the method

- **The book:** [Steer, Don't Guess on Amazon](https://www.amazon.com/dp/B0HPBR6BNX) (Kindle, paperback, hardcover). [Read Chapter 1 free](https://mjirgensons.github.io/blog/free-sample/).
- **The site:** [mjirgensons.github.io](https://mjirgensons.github.io/), with articles that apply the model to real situations, for example [levers of control](https://mjirgensons.github.io/blog/levers-of-control/), [backward planning](https://mjirgensons.github.io/blog/backward-planning/) and [how to prevent AI hallucinations](https://mjirgensons.github.io/blog/how-to-prevent-ai-hallucinations/).
- **What the model is:** [The Jirgenson Model, a management method for small business](https://mjirgensons.github.io/blog/jirgenson-model-management-method/).
- **The author:** [Martin Jirgenson](https://mjirgensons.github.io/author/) on [Goodreads](https://www.goodreads.com/author/show/73234443.Martin_Jirgenson) and [LinkedIn](https://www.linkedin.com/in/martin-jirgenson-3098609a/); ORCID [0009-0001-3034-3552](https://orcid.org/0009-0001-3034-3552).

## Files

- `jirgenson_canon_v1.0_en.txt`: the canon of the model (Appendix H of the book). A compact rulebook, sections §0 to §16, canon-id JMC-1.
- `jirgenson_prompt_v1.1_en.txt`: the operating prompt (Appendix I of the book, edition 1.1). It tells the assistant how to work with the canon. It is written in English; the assistant replies in the language you write in.

## How to use

1. Download both files (Download or Raw, then save).
2. Open a new conversation with a language model (an assistant).
3. Attach the canon file to the message or paste its full text.
4. Send the prompt as your first message.
5. Describe your situation in plain words as your second message. Sample messages are given in Appendix I of the book.

Without the canon the assistant will not start and will ask for it: this is by design.

## Versions

Canon v1.0 and prompt v1.1 (edition 1.1 of the book, 18 October 2026; tested in Appendix J). Updates appear here under a new version number; each file states its version on its first line.

## Experiment

**E5, a blind test of the operating prompt** on ten small-business crisis scenarios: the canon plus the operating prompt scored 88.8 out of 100 against 56.2 for the same model without a prompt, and answers with an invented fact fell from 7 in 10 to 1 in 120. The full record (scenarios and answer key, every prompt version tested, all 240 answers, all 600 blind judge records, scripts, figures and limits) is archived on Zenodo with a permanent DOI: [10.5281/zenodo.23964934](https://doi.org/10.5281/zenodo.23964934), also on [Hugging Face](https://huggingface.co/datasets/SteerDontGuess/E5-jirgenson-model-blind-test) and [Kaggle](https://www.kaggle.com/datasets/martinjirgenson/e5-blind-test-jirgenson-model-ai-prompt). A copy without the bulky input packs is in `experiments/E5-blind-test-2026-10/`; start with `STUDY.md` there. The book's prompt v1.1 corresponds to the tested version v1.3-c (three small differences, listed in `STUDY.md`); the results above are for the latest tested version, v1.5-c.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23964934.svg)](https://doi.org/10.5281/zenodo.23964934)

## Licence

CC BY-ND 4.0, see `LICENSE`. The experiment folder has its own licence file (`experiments/E5-blind-test-2026-10/LICENSE.md`: data and documentation CC BY 4.0, scripts MIT, canon and prompts CC BY-ND 4.0). © Martin Jirgenson, 2026. This is not financial, legal or investment advice.
