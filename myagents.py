import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 1. Streamlit UI Setup
st.set_page_config(page_title="3-Agent Multi-Agent System", layout="wide")
st.title("🤖 Multi-Agent Workflow: Plan, Execute, Verify")
st.caption("Powered by LangChain & Hugging Face Models")

# Sidebar for API Configuration
st.sidebar.header("Configuration")
hf_token = st.sidebar.text_input("Enter Hugging Face API Token", type="password")
model_repo = st.sidebar.selectbox(
    "Select LLM Model",
    ["mistralai/Mistral-7B-Instruct-v0.3", "meta-llama/Meta-Llama-3-8B-Instruct"]
)

# 2. Main Logic Function
def run_agent_workflow(task_input, token, model):
    try:
        # Initialize the Hugging Face Endpoint
        llm = HuggingFaceEndpoint(
            repo_id=model,
            huggingfacehub_api_token=token,
            temperature=0.5,
            max_new_tokens=512
        )

        # ---- AGENT 1: THE PLANNER ----
        planner_template = """
        You are the PLANNER Agent. 
        Your job is to take a high-level task and break it down into a clear, step-by-step execution plan.
        Do not execute the task. Only provide the steps.

        Task: {task}

        Step-by-Step Plan:
        """
        planner_prompt = PromptTemplate(template=planner_template, input_variables=["task"])
        planner_chain = planner_prompt | llm

        # ---- AGENT 2: THE EXECUTOR ----
        executor_template = """
        You are the EXECUTOR Agent.
        Your job is to take the plan provided by the Planner and generate the actual content, code, or answer required.

        Plan to follow: {plan}

        Executed Output:
        """
        executor_prompt = PromptTemplate(template=executor_template, input_variables=["plan"])
        executor_chain = executor_prompt | llm

        # ---- AGENT 3: THE VERIFIER ----
        verifier_template = """
        You are the VERIFIER Agent.
        Your job is to review the Executor's output against the original task and the plan. 
        Check for accuracy, completeness, and formatting. Provide a final stamp of approval or constructive feedback.

        Original Task: {task}
        Executor's Output: {output}

        Verification Report:
        """
        verifier_prompt = PromptTemplate(template=verifier_template, input_variables=["task", "output"])
        verifier_chain = verifier_prompt | llm

        # ---- Execution Pipeline ----
        with st.status("Agents are working...", expanded=True) as status:
            
            status.update(label="🧠 Agent 1: Planning the task...")
            plan_result = planner_chain.invoke({"task": task_input})
            st.subheader("📋 Planner's Action Steps")
            st.info(plan_result)

            status.update(label="⚙️ Agent 2: Executing the plan...")
            execution_result = executor_chain.invoke({"plan": plan_result})
            st.subheader("🛠️ Executor's Output")
            st.code(execution_result, language="text")

            status.update(label="🔍 Agent 3: Verifying the results...")
            verification_result = verifier_chain.invoke({"task": task_input, "output": execution_result})
            st.subheader("✅ Verifier's Final Report")
            st.success(verification_result)

            status.update(label="Workflow Complete!", state="complete")

    except Exception as e:
        st.error(f"An error occurred: {e}")

# 3. User Input Layout
user_task = st.text_area("What task should the agents perform?", placeholder="e.g., Write a python script to scrape weather data, or write a marketing email for a new shoe line.")

if st.button("Start Agents", type="primary"):
    if not hf_token:
        st.warning("Please enter your Hugging Face API Token in the sidebar.")
    elif not user_task.strip():
        st.warning("Please enter a task for the agents.")
    else:
        run_agent_workflow(user_task, hf_token, model_repo)
