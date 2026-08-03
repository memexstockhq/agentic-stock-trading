"""Research agent — consumes the analyst stack."""
def make_research_agent(analyst):
    def research(ticker: str) -> dict:
        brief = analyst.analyze(ticker)
        return {"action": brief.verdict.lower(), "size": 10.0, "rationale": f"{brief.sentiment} sentiment, RSI {brief.rsi:.1f}"}
    return research
