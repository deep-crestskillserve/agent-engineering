from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List

@CrewBase
class FinancialResearcherMine():
    """FinancialResearcherMine crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config['researcher'], verbose = True, tools = [SerperDevTool()])

    @agent
    def analyst(self) -> Agent:
        return Agent(config=self.agents_config['analyst'], verbose = True, tools = [SerperDevTool()])

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])

    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_task'])
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            # here, self.agents and self.tasks is poppulated because of putting @agent and @task decorator above it
            agents = self.agents,
            tasks = self.tasks,
            Process = Process.sequential,
            verbose = True
        )