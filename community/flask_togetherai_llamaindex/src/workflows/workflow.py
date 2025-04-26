from datetime import timedelta
from restack_ai.workflow import workflow, import_functions, log

with import_functions():
    from src.functions.llm_complete import llm_complete

@workflow.defn()
class LlmCompleteWorkflow:
    @workflow.run
    async def run(self, input: str):
        log.info("LlmCompleteWorkflow started", input=input)
        result = await workflow.step(llm_complete, input, start_to_close_timeout=timedelta(seconds=120))
        log.info("LlmCompleteWorkflow completed", result=result)
        return result
