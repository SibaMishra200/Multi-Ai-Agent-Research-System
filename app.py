import streamlit as st

from src.pipelines.pipeline import run_research_pipeline


st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 AI Research Agent")

st.write(
    "Enter a research topic and let the multi-agent system "
    "search, read, write, and critique the research."
)

topic = st.text_area(
    "Research Topic",
    placeholder="Example: Latest approaches for improving RAG systems",
    height=120
)


if st.button("🚀 Start Research", type="primary"):

    if not topic.strip():
        st.warning("Please enter a research topic.")

    else:

        with st.spinner("Research pipeline is running..."):

            try:
                result = run_research_pipeline(
                    topic.strip()
                )

                st.success("Research completed successfully!")

                # -----------------------------
                # FINAL REPORT
                # -----------------------------

                st.header("📄 Research Report")

                st.markdown(result["report"])


                # -----------------------------
                # CRITIC
                # -----------------------------

                st.header("🧐 Critic Review")

                st.markdown(result["feedback"])


                # -----------------------------
                # RESEARCH EVIDENCE
                # -----------------------------

                st.header("🔍 Research Evidence")

                with st.expander("Search Results"):
                    st.markdown(result["search_results"])

                with st.expander("Scraped Content"):
                    st.markdown(result["scraped_content"])


            except Exception as e:

                st.error(
                    "Something went wrong while running the research pipeline."
                )

                with st.expander("Technical Details"):
                    st.exception(e)