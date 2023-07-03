## Celeberity Detais

The target of this create a streamlit application that will display the imformation about the celebrity, his DOB and the main events that took place in INDIA during his birth date.

## Output

![langchain](https://github.com/akash-soni/langchain_hands_on/assets/37892453/f4fb5ec5-afb1-45b8-81c4-3788c10f3d7f)


### Tech Stack
- OpenAI
- Langchain
- Streamlit


# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/akash-soni/langchain_hands_on
```


### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summary python=3.8 -y
```

```bash
conda activate summary
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```
### STEP 03- Get OpenAI API key

- Create a OpenAI API Key and  copy it.
- Create a .env work directory and copy the key in variable as:
  OPENAI_API_KEY=sk-*******************************


```bash
# Finally run the following command
streamlit run main.py
```
