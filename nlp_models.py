"""
Module: nlp_models.py
Purpose: Load HuggingFace transformer models
"""

from transformers import pipeline

def load_qa_pipeline():
    return pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_question(pipeline, question, context):
    result = pipeline(question=question, context=context)
    return result["answer"]
