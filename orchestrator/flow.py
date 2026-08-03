"""Research -> Decide -> Approve -> Execute flow."""
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class Decision:
    ticker: str
    action: str
    size: float
    rationale: str

class TradingFlow:
    def __init__(self, research: Callable, risk: Callable, execute: Callable, approve: Optional[Callable] = None):
        self.research = research
        self.risk = risk
        self.execute = execute
        self.approve = approve

    def run(self, ticker: str) -> dict:
        brief = self.research(ticker)
        decision = Decision(ticker, brief["action"], brief["size"], brief["rationale"])
        if not self.risk(decision):
            return {"status": "blocked_by_risk"}
        if self.approve and not self.approve(decision):
            return {"status": "awaiting_approval"}
        return {"status": "executed", "tx": self.execute(decision)}
