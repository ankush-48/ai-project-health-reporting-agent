import os
import json
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# 1. Load environment variables from .env
load_dotenv()

# 2. Define the exact structured format we want from the AI
class ProjectHealthReport(BaseModel):
    project_name: str = Field(description="Name of the project")
    overall_rag_status: str = Field(description="Must be GREEN, AMBER, or RED based on the matrix rules")
    dimension_scores: dict = Field(description="Scores assigned (0 to 2) for Schedule, Budget, Blockers, Sentiment")
    executive_reasoning: str = Field(description="A clear, plain-English synthesis of why this status was given")
    data_gaps_identified: List[str] = Field(description="List of messy, incomplete, or missing data points handled gracefully")

# 3. Create the Core Groq-powered Agent class
class ProjectHealthAgent:
    def __init__(self):
        # Initializing Llama 3.3 via Groq with structured JSON outputs enforced
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile", 
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY")
        ).with_structured_output(ProjectHealthReport)
        
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", """
            You are an elite automated Project Health Reporting Agent for the Professional Services team at Zycus.
            Your task is to analyze raw project data and evaluate it strictly using the following Phase 1 Framework:
            
            SCORING (0 = On Track, 1 = At Risk, 2 = Critical):
            - Schedule Slippage: 0 (<=5 days), 1 (6-14 days), 2 (>14 days or critical path hit)
            - Budget Burn Rate: 0 (on track), 1 (up to 15% overburn), 2 (>15% overburn or depleted)
            - Blockers: 0 (none), 1 (active with workarounds), 2 (hard blockers needing escalation)
            - Stakeholder Sentiment: 0 (positive/neutral), 1 (mixed/silent), 2 (negative/complaints)
            
            MAPPING LOGIC:
            - GREEN: Score is low AND no single dimension is 2.
            - AMBER: Single dimension hits 1, or minor risks exist.
            - RED: If ANY single dimension is 2 (Critical Fail-Safe Trigger), the entire project is RED.
            
            MESSY DATA HANDLING:
            - If data is missing (e.g., budget is empty), default that score to 0 but log it explicitly in data_gaps_identified.
            """),
            ("human", "Analyze the following raw project plan data:\n\n{raw_data}")
        ])
        
    def analyze_project(self, project_data: dict) -> ProjectHealthReport:
        formatted_input = json.dumps(project_data, indent=2)
        chain = self.prompt_template | self.llm
        response = chain.invoke({"raw_data": formatted_input})
        return response

# 4. Run an initial test execution
# 4. Dynamic File Runner
if __name__ == "__main__":
    agent = ProjectHealthAgent()
    
    input_file_path = os.path.join("data", "project_alpha.json")
    output_file_path = os.path.join("outputs", "status_report_alpha.json")
    
    print(f"🤖 Reading input data from {input_file_path}...")
    
    # Load raw file data
    if os.path.exists(input_file_path):
        with open(input_file_path, "r") as f:
            project_raw_data = json.load(f)
            
        print("🤖 Running analysis via Groq...")
        report = agent.analyze_project(project_raw_data)
        
        # Save output to outputs folder
        with open(output_file_path, "w") as f:
            json.dump(report.model_dump(), indent=4, fp=f)
            
        print(f"✅ Success! Report successfully generated and saved to {output_file_path}")
    else:
        print(f"❌ Error: Could not find sample file at {input_file_path}. Please create it first.")