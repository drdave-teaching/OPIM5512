# 📂 A02 — Buddy Collab (Decision Tree ML)

**Goal:**  
Work with a partner to build a tiny, end-to-end ML pipeline — *and* practice real GitHub collaboration (issues → branches → PRs → code review → merge).

You will create a **two-person repo**, alternate “serves,” and keep each pull request tiny and traceable.

---

# 1️⃣ Setup (Both Students)

### Step 1 — One person creates the repo  
Name it something like:

A02-collab-netID1-netID2

Inside this repo, create the following structure:

A02-collab/  
  data/  
  figs/  
  src/  
    pipeline.py  
  README.md  
  requirements.txt  

Your instructor will provide the **California Housing dataset**.  
Place it at:

A02-collab/data/raw_ca_housing.csv

---

### Step 2 — Add your partner as a collaborator
Repo → **Settings** → **Collaborators** → Add your buddy’s GitHub username.

---

### Step 3 — Protect the `main` branch
Repo → **Settings** → **Branches** → Add a branch protection rule:

- Require pull requests before merging  
- Block direct pushes to `main`  

---

### Step 4 — Create one shared issue
Create an issue titled:

A02 Ping-Pong Plan

Assign **both teammates**.  
You will check off steps inside this issue as you progress.

---

# 2️⃣ Workflow Rules (Ping-Pong Model)

You and your partner will **alternate who performs each step**.

Each step requires:

- A **new branch**  
- A **small PR**  
- A **short review** from your partner  
- **One artifact** (CSV, PNG, JSON, etc.)  
- **2–3 sentences added to the Notes section of this README**

📌 **No one may complete two steps in a row.**

---

# 3️⃣ The ML Pipeline (Lap 1 — Required)

All logic belongs inside:

A02-collab/src/pipeline.py

Use pandas, scikit-learn, matplotlib, seaborn, etc.

---

## 🔵 Step 1 — LOAD (Student A)

**Branch:** load-<name>  
**Artifact:** A02-collab/data/raw.csv

Tasks:
- Load raw_ca_housing.csv  
- Optionally subset rows/columns  
- Save as raw.csv  
- Add 2–3 sentences under Notes → Load describing:
  • dataset shape  
  • columns kept  
  • target variable  

PR → Review → Merge.

---

## 🟢 Step 2 — CLEAN (Student B)

**Branch:** clean-<name>  
**Artifact:** A02-collab/data/clean.csv

Tasks:
- Handle missing values  
- Address outliers (or note if none were changed)  
- Rename unclear columns  
- Save cleaned data  
- Add 2–3 sentences under Notes → Clean  

PR → Review → Merge.

---

## 🟠 Step 3 — MODEL (Decision Tree) (Student A)

**Branch:** model-<name>  
**Artifacts:**  
A02-collab/data/metrics.json  
A02-collab/data/preds_test.csv  
A02-collab/figs/residuals.png  
A02-collab/figs/feat_importance.png  

Tasks:
- Train/test split  
- Fit DecisionTreeRegressor  
- Compute R² and RMSE  
- Save predictions  
- Generate:
  • residuals plot  
  • feature importance plot  
- Add notes under Notes → Model  

PR → Review → Merge.

---

## 🟣 Step 4 — EVALUATE (Student B)

**Branch:** evaluate-<name>  
**Artifact:** A02-collab/figs/pred_vs_actual.png

Tasks:
- Create predicted vs. actual scatter plot  
- Add R² and RMSE under Notes → Evaluate  
- Add a short interpretation  

PR → Review → Merge.

---

## ⚫ Step 5 — WRITE-UP v1 (Either student; maintain ping-pong order)

**Branch:** writeup-v1  

Tasks:
- Add a 150–200 word summary under Mini Write-up v1:
  • What you tried  
  • What worked  
  • What didn’t  
  • What you’d try next  

PR → Review → Merge.

---

# 4️⃣ Optional Lap 2 (Extra Credit)

Continue the ping-pong pattern:

- Feature engineering → clean_fe.csv  
- Hyperparameter tuning → depth grid search  
- Error analysis → error_by_decile.csv + plot  
- Write-up v2 → describe improvements + limitations  

---

# 5️⃣ How to Run the Pipeline

Install requirements:

pip install -r requirements.txt

Run pipeline steps:

python A02-collab/src/pipeline.py load  
python A02-collab/src/pipeline.py clean  
python A02-collab/src/pipeline.py model  
python A02-collab/src/pipeline.py evaluate  

(Additional steps for Lap 2 if implemented.)

---

# 6️⃣ Notes (Update Each Step)

**Load:**  
> Add notes here.

**Clean:**  
> Add notes here.

**Model:**  
> Add notes here.

**Evaluate:**  
> Add notes here.

**Feature Engineering (optional):**  
> Notes.

**Hyperparameter Tuning (optional):**  
> Notes.

**Error Analysis (optional):**  
> Notes.

---

# ✍️ Mini Write-up v1  
Add 150–200 word summary here.

---

# ✍️ Mini Write-up v2 (optional)  
Add follow-up summary here.
