# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
TOKENIZER_PATH = '/'
LLAMA_PATH = '/'

tokenizer = None
model_pipeline = None
# tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
# model = AutoModelForCausalLM.from_pretrained(LLAMA_PATH, torch_dtype="auto")
# model_pipeline = pipeline(
#     task="text-generation",
#     model=model,
#     tokenizer=tokenizer,
#     torch_dtype=torch.float16,
#     device_map="auto"
# )
