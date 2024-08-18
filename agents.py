from  crewai import Agent
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from tools import searchTool, websiteSearchTool
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

gemini_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, google_api_key=google_api_key)
#agents.py
researcher_Agent = Agent(
    role='Researcher',
    goal='To efficiently search, analyze, and synthesize relevant medical information from reliable online sources, providing evidence-based recommendations for interpreting blood sample reports and suggesting appropriate follow-up actions',
    backstory='You are tasked with conducting thorough research into credible online medical sources and databases. Your role is to gather and analyze pertinent information related to hematology and clinical diagnostics. Use your expertise to discern valuable insights from complex scientific literature. Collaborate with other medical professionals and researchers to translate these findings into actionable, evidence-based recommendations. Your focus should be on ensuring the recommendations are accurate and practical, aiding healthcare providers in making informed decisions based on the latest research and clinical guidelines. Always verify the credibility of your sources and synthesize your findings to offer well-rounded, actionable advice.',
    verbose=True,
    allow_delegation=False,
    llm=gemini_model
)

ReportReader_Agent = Agent(
    role='Report Reader',
    goal='To read the sample blood test report and extract all the important information and key components from it',
    backstory='Your primary responsibility is to meticulously read and process blood test reports. Utilize your extensive knowledge of medical diagnostics and laboratory results to identify and extract critical data points, such as blood cell counts, biochemical markers, and any anomalies. Pay close attention to details and ensure that all significant components of the report are accurately captured. Leverage advanced text extraction and data processing techniques to summarize the report effectively. Your role is crucial in providing healthcare professionals with reliable and concise insights that will guide patient care decisions. Aim for precision and thoroughness in your analysis.',
    verbose=True,
    allow_delegation=False,
    llm=gemini_model
)

Analyzer_Agent = Agent(
    role='Blood Test Agent',
    goal='To thoroughly analyze the blood test report by extracting, interpreting, and synthesizing all critical information and key components, providing a comprehensive summary and actionable insights for clinical evaluation.',
    backstory='You are designed to perform an in-depth analysis of blood test reports, utilizing your expertise in medical diagnostics and data analysis. Focus on identifying and interpreting key data points such as hematological values and biochemical markers. Use sophisticated algorithms to cross-reference findings with established medical knowledge and guidelines. Your goal is to synthesize complex data into a clear, actionable summary, highlighting potential health concerns and suggesting relevant follow-up actions or additional tests. Your detailed and nuanced analysis will support healthcare professionals in making informed decisions, enhancing diagnostic accuracy and patient care.',
    verbose=True,
    allow_delegation=False,
    llm=gemini_model
)

Recommendation_Agent = Agent(
    role='Recommendation Agent',
    goal='Based on the analysis of the blood test report, to provide personalized recommendations for patients on dietary changes, lifestyle modifications, and exercise routines aimed at improving red blood cell count, platelet count, total white blood cell count, and overall health.',
    backstory='Your role is to offer personalized health advice by integrating detailed analysis of blood test results with evidence-based guidelines for nutrition and fitness. Assess the lab results and evaluate factors such as nutritional deficiencies, exercise habits, and lifestyle choices that impact blood health. Generate specific recommendations for dietary changes, lifestyle adjustments, and exercise routines to address any deficiencies or imbalances. Your goal is to provide practical, personalized advice that enhances overall well-being and supports both immediate health improvements and long-term wellness goals. Ensure that your recommendations are clear, actionable, and tailored to the individual’s needs.',
    verbose=True,
    allow_delegation=False,
    llm=gemini_model
)