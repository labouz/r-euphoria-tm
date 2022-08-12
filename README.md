## Analyzing discourse on HBO's euphoria from Reddit commentary
### CAA apprenticeship Jul 16 - Aug 12, 2022

**Files:**  

- `py/` : notebooks and scripts for anlaysis
  - `dev/` : deprecated scripts
  - `analysis.ipynb` : setting scope of analysis and data cleaning
  - `eda.ipynb` : exploratory analysis, creating term-document matrix, frequencies and similarity scores
  - `lda_general.ipynb` : topic modeling with LDA on first set of comments pulled form reddit, not for a specific date range
  - `tm-bert.ipynb` : topic modeling with pre-trained language models using `BERTopic` library plus sentiment analysis 
- `dat/` : S1 and S2 sub ids & comments in `.pkl` format
- `img/` : images created by notebooks and other sources for presentation
- `plots/' : plots created from scripts like word clouds, bar charts, etc.

**Data:**

- Reddit comments from 'r/euphoria' using `psaw` library
  - S1: June 16 - Aug 4 , 2019
  - S2: Jan 9 - Feb 27, 2022
  



