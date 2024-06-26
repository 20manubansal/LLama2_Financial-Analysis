# -*- coding: utf-8 -*-
"""FINAL CODE LLama 33p snp500 : e2-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EXYrTn0rFz7X95btfCzlN7s8i9wen558
"""

# @title
!pip install transformers
!pip install -q datasets

!pip install autotrain-advanced

!pip install huggingface_hub

"""########
RESTART BEFORE FURTHER EXECUTION (wait for pop up)
"""

# @title Update autotrain (GPU Required)
!autotrain setup --update-torch

# Hugging Face Login Credentials
# ID:     LLama2-test1
# Access: Write
# Token:  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20

from huggingface_hub import notebook_login
notebook_login()

!autotrain llm --train --project_name LLama2_fin_test1 \
--model TinyPixel/Llama-2-7B-bf16-sharded \
--data_path ManuBansal/33param_snp500_dataSet \
--train-split train \
--valid-split test \
--text_column text \
--use_peft\
--use_int4 \
--learning_rate 2e-2 \
--train_batch_size 2 \
--num_train_epochs 3 \
--evaluation-strategy epoch \
--trainer sft \
--model_max_length 1024 \
--push_to_hub \
--repo_id ManuBansal/33p_snp-3epoch_2e-2 \
--token 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20 \
--block_size 1024 > training.log

from transformers import BasicTokenizer

"""sharded version used because of compute unit constraints

"""

## torch.cuda.is_available()

"""Testing Text generation

"""

from transformers import pipeline

generator = pipeline('text-generation', model = 'ManuBansal/33p_snp-3epoch')
generator("What is DCF", max_length = 30, num_return_sequences=3)

from transformers import AutoTokenizer
import transformers
import torch

model = "ManuBansal/33p_snp-3epoch"
#model = "meta-llama/Llama-2-7b-chat-hf"
model = "ManuBansal/33p_snp-3epoch_2e-2"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

sequences = pipeline(
    "### instruction:  This array contains the change in a certain company's 33 unique financial parameters observed in an undisclosed year. Taking -1 as decrease from the previous year, 1 as increase and 0 as unavailable, estimate how the company's valuation will change in the same year. Give your answer only as either -1 or 1. ### input: [1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1]",
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

from IPython.display import HTML, display

def set_css():
  display(HTML('''
  <style>
    pre {
        white-space: pre-wrap;
    }
  </style>
  '''))
get_ipython().events.register('pre_run_cell', set_css)

model = "ManuBansal/33p_snp-3epoch"
#model = "meta-llama/Llama-2-7b-chat-hf"
model = "ManuBansal/33p_snp-3epoch_2e-2"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

sequences = pipeline(
    "### instruction:  This array contains the change in a certain company's 33 unique financial parameters observed in an undisclosed year. Taking -1 as decrease from the previous year, 1 as increase and 0 as unavailable, estimate how the company's valuation will change in the same year. Give your answer only as either -1 or 1. ### input: [1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1]",
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

model = "ManuBansal/33p_snp-3epoch"
#model = "meta-llama/Llama-2-7b-chat-hf"
model = "ManuBansal/33p_snp-3epoch_2e-2"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

sequences = pipeline(
    "### instruction:  This array contains the change in a certain company's 33 unique financial parameters observed in an undisclosed year. Taking -1 as decrease from the previous year, 1 as increase and 0 as unavailable, estimate how the company's valuation will change in the same year. Give your answer only as either -1 or 1. ### input: [1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1]",
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

