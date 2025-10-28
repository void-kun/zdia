# zdia Web UI (Vue 3 + Vite)

This is a minimal Vue 3 + Vite frontend to preview the JSON output produced by `pyan`.

Quick start

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 and enter the URL or path to a JSON file produced by `pyan` (for example, run `python3 -m pyan --json --file out.json path/to/*.py` and then load `/out.json` from the UI).

Notes

- The app is intentionally minimal. It fetches JSON and renders it in a <pre> block.
- You can extend it to visualize nodes/edges with a graphing library (e.g., cytoscape.js, vis-network, d3).
