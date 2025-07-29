import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResearchAgents
from data_loader import DataLoader

load_dotenv(override=True)

print("ok")
my_name = "Deep Dabhi"
linked_profile = "https://in.linkedin.com/in/deep-dabhi-aa9993223"
with st.sidebar:
    st.markdown(f"**{my_name}**")
    st.markdown(f"[LinkedIn]({linked_profile})")

st.title("AI-powered Research Assistant 📑")


st.markdown("""
This app helps researchers, students, and professionals quickly find and summarize research papers.

Simply enter a research query, and the app will fetch relevant papers from ArXiv and Google Scholar, providing concise summaries and insightful analyses.
""")

groq_api_key = os.getenv('GROQ_API_KEY')

if not groq_api_key:
    st.error("GROQ_API_KEY is missing. Please set it in your environment variables.")
    st.stop()

agents = ResearchAgents(groq_api_key)

data_loader = DataLoader()

query = st.text_input("Enter a research topic:")

if st.button("Search"):
    with st.spinner("Fetching research papers..."): 

        # Fetch research papers from ArXiv 
        arxiv_papers = data_loader.fetch_arxiv_papers(query)
        all_papers = arxiv_papers

        if not all_papers:
            st.error("Failed to fetch papers. Try again!")
        else:
            processed_papers = []

            
            for paper in all_papers:
                summary = agents.summarize_paper(paper['summary'])  
                adv_dis = agents.analyze_advantages_disadvantages(summary)  

                processed_papers.append({
                    "title": paper["title"],
                    "link": paper["link"],
                    "summary": summary,
                    "advantages_disadvantages": adv_dis,
                })

            st.subheader("Top Research Papers for the topic:")
            for i, paper in enumerate(processed_papers, 1):
                st.markdown(f"### {i}. {paper['title']}")  
                st.markdown(f"🔗 [Read Paper]({paper['link']})")  
                st.write(f"**Summary:** {paper['summary']}") 
                st.write(f"{paper['advantages_disadvantages']}")  
                st.markdown("---")  