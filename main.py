import streamlit as st
from rag_pipeline import get_answer
from feedback import save_feedback, display_feedback_summary
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Math Agent", page_icon="📘")
st.title("🧠 Math Professor Agent")
st.subheader("Ask any math-related question!")

question = st.text_input("📌 Enter your math question here:")

if question:
    with st.spinner("🔍 Processing..."):
        ai_answer = get_answer(question)

    st.markdown("### ✅ AI-generated Answer:")
    st.success(ai_answer)

    with st.form("feedback_form"):
        st.markdown("### 📝 Provide Feedback:")
        feedback_text = st.radio("Was the answer helpful?", ["Yes", "No"])
        user_correction = st.text_area("Suggest a better answer (optional):")
        submitted = st.form_submit_button("Submit Feedback")

        if submitted:
            save_feedback(question, ai_answer, feedback_text, user_correction)
            st.success("✅ Feedback submitted successfully!")

    with st.expander("📚 Recent Feedback History"):
        history = display_feedback_summary()
        for i, item in enumerate(history, 1):
            st.markdown(f"**{i}.** Question: `{item['question']}`")
            st.markdown(f"  _AI Answer:_ {item['ai_answer']}")
            st.markdown(f"  _Feedback:_ {item['feedback']}")
            if item['user_correction']:
                st.markdown(f"  _Correction:_ {item['user_correction']}")
            st.markdown("---")
