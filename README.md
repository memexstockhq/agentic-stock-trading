# Agentic Stock Trading

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Chains](https://img.shields.io/badge/Chains-RH%20%7C%20BSC%20%7C%20EVM-lightgrey)](configs/)

**Agents that research, decide and execute**

Multi-agent trading framework for stock tokens: research agent, risk agent, execution agent — with an approval gate between decision and execution.

## Quick start

```bash
git clone https://github.com/cervemone/agentic-stock-trading.git
cd agentic-stock-trading
pip install -r requirements.txt
python -m src.main --help
```

## Layout

```
  orchestrator/
  agents/
  decisions/
  execution/
  risk/
  tests/
  docs/
  scripts/
  configs/
  examples/
  backtesting/
  integrations/
```

## Related

- `stock-token-index` — registry of tokenized equities
- `stock-analyst-agent` — the agent that consumes this repo
- `rh-stock-token-sdk` — SDK for BNB Chain stock tokens

## License

MIT
