import pickle
import numpy as np
import gradio as gr
from sentence_transformers import SentenceTransformer
from langdetect import detect
import traceback

print("🟢 Starting Dengue QA system...")

# ======== Load Model & Data ========
with open('dengue_qa_model (mpnet-base-v2).pkl', 'rb') as f:
    model_data = pickle.load(f)

# Load embeddings and QA data
questions_malay = model_data['training_questions_malay']
answers_malay = model_data['training_answers_malay']
embeddings_malay = model_data['embeddings_malay']

questions_english = model_data['training_questions_english']
answers_english = model_data['training_answers_english']
embeddings_english = model_data['embeddings_english']

categories = model_data['training_categories']

# Load sentence transformer model
model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

# ======== Chatbot Logic ========
def format_answer(answer):
    # Add line breaks for clarity if answer is long
    return answer.replace("~", "<br>~").strip("<br>")

def get_language(text):
    try:
        lang = detect(text)
        if lang == 'ms':
            return 'malay'
        elif lang == 'en':
            return 'english'
        # Optionally add 'id' for Indonesian as Malay
        elif lang == 'id':
            return 'malay'
        else:
            # Default to Malay if unsure
            return 'malay'
    except Exception:
        # Default fallback
        return 'malay'

def find_best_answer(query, language='malay', top_k=1, threshold=0.5):
    if language == 'malay':
        questions = questions_malay
        answers = answers_malay
        embeddings = embeddings_malay
    else:
        questions = questions_english
        answers = answers_english
        embeddings = embeddings_english

    # Get embedding for the query
    query_emb = model.encode([query], convert_to_numpy=True)
    # Compute cosine similarity
    sims = np.dot(embeddings, query_emb.T).flatten() / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_emb) + 1e-8)
    # Sort by similarity
    top_indices = np.argsort(sims)[-top_k:][::-1]
    results = []
    for idx in top_indices:
        if sims[idx] >= threshold:
            results.append({
                'question': questions[idx],
                'answer': answers[idx],
                'similarity': sims[idx]
            })
    return results

def chat_fn(message, history):
    try:
        # Detect query language
        lang = get_language(message)
        lang_code = "Malay" if lang == "malay" else "English"
        not_found_msg = "Maaf, tidak menemui jawapan yang sesuai." if lang == "malay" else "Sorry, could not find a suitable answer."

        # Search for the best answer (semantic retrieval)
        results = find_best_answer(message, language=lang, top_k=1, threshold=0.55)
        if results:
            matched_q = results[0]['question']
            answer = format_answer(results[0]['answer'])
            sim = f"{results[0]['similarity']:.3f}"
        else:
            matched_q = "(Tiada padanan)" if lang == "malay" else "(No match)"
            answer = not_found_msg
            sim = "0.000"

        response = f"""<div style='margin-bottom: 0.7em;'>
            <b style='color:#fff;'>Soalan serupa:</b> <span style='color:#7ec3ff'>{matched_q}</span><br>
            <b style='color:#fff;'>Jawapan:</b> <span style='color:#ffe066;'>{answer}</span><br>
            <span style='font-size:0.98em;color:#bfc9d1;'>[Similarity: {sim}] 
            <span style='background:#232c3b;color:#fff;padding:2px 8px;border-radius:8px;'>{lang_code}</span>
            </span>
        </div>"""
        return response

    except Exception as e:
        print("❌ ERROR:", e)
        traceback.print_exc()
        return f"❌ ERROR: {str(e)}"

# ======== Gradio Chat Interface ========
demo = gr.ChatInterface(
    fn=chat_fn,
    chatbot=gr.Chatbot(
        label="Chat Denggi",
        avatar_images=[
            "https://i.imgur.com/CyqjvKl.png",
            "https://i.imgur.com/G2222hg.png"
        ],
        type='messages'
    ),
    title="Sistem Soal Jawab Denggi",
    description=(
        '<div style="text-align:center;">'
        'Tanya apa saja berkaitan DENGGI dalam Malay atau English.<br>'
        '<b>Topik yang disokong:</b><br>'
        '&#8226; Apakah itu denggi<br>'
        '&#8226; Gejala/Simptom<br>'
        '&#8226; Rawatan dan penjagaan<br>'
        '&#8226; Cara pencegahan'
        '</div>'
    ),
    theme="Taithrah/Minimal",
    submit_btn="Hantar",
)

if __name__ == "__main__":
    print("✅ Ready. Launching Gradio interface...")
    demo.launch(share=True)