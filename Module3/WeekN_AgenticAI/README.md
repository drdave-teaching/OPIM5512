# Welcome to Week N!

Now that you are comfortable writing some basic scrapers on GCP, let's see if we can translate messy .txt files into something actionable. We can do it locally in Colab, then try to scale in GCP.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/284233bd-4e7f-4b94-a641-6592326263e2" />

Architecture (keeps your current scraper)
1. Keep your Cloud Function exactly as-is (writes index.csv + txt/ per run).
2. Add a lightweight extractor worker (Cloud Run job or another Function) that:
  * Watches a Pub/Sub topic or scans the txt/ folder for new files
  * Loads the raw text
  * Calls an LLM on Vertex AI (Gemini) to extract fields to a JSON schema
  * Validates with Pydantic; if invalid or low-confidence → repairs by prompting again with validator errors
  * Normalizes fields (e.g., standardize makes, parse mileage/price)
  * Writes one JSONL per run (or streams to BigQuery later)

You can trigger the extractor right after you upload each .txt (publish a message with gs://bucket/path/to/file.txt), or run it on a schedule.
