from flask import Blueprint
from flask_caching import Cache
from transformers import LlamaTokenizer, LlamaForCausalLM, pipeline
import torch

#app
bp = Blueprint('main', __name__)

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 0
}

cache = Cache(config=config)
cache.init_app(bp)

tokenizer = LlamaTokenizer.from_pretrained("../../llama_converted")
model = LlamaForCausalLM.from_pretrained(pretrained_model_name_or_path="../../llama_converted",
                                         low_cpu_mem_usage=True, torch_dtype="auto")
llama_pipeline = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    device_map="auto"
)

from app.main import routes
