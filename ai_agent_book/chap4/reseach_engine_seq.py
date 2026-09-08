from web_scraping import web_scrape
from web_searching import web_search
from llm_models import get_llm
from utilities import to_json
from prompts import (
    ASSISTANT_SELECTION_PROMPT_TEMPLATE,
    WEB_SEARCH_PROMPT_TEMPLATE,
    SUMMARY_PROMPT_TEMPLATE,
    RESEARCH_REPORT_PROMPT_TEMPLATE
)


NUM_SEARCH_QUERIES = 2
NUM_SEARCH_RESULTS_PER_QUERY= 3
RESULT_TEXT_MAX_CHARACTERS = 10000

question = 'What can I see and do in the Spanish town of Astorga?'

llm= get_llm()

assistant_selection_prompt = ASSISTANT_SELECTION_PROMPT_TEMPLATE.format(user_question=question)
assistant_instructions= llm.invoke(assistant_selection_prompt)


