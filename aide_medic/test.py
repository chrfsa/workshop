from langchain_community.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()
print(search.run("Obama's first name?"))