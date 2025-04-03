# policy-llm

Create new env:
conda create -n llm-policy python=3.9.18conda activate llm-policy

Install dependencies:
conda install -c conda-forge -y \         langchain \            
  chromadb \
  llama-cpp-python \
  sentence-transformers \
  pypdf2

Run:
python /Users/siddharthchaudhary/Documents/GitHub/policy-llm/app/main.py
