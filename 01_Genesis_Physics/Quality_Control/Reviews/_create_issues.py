"""Create GitHub issues from the 0516_Rev master task lists.

Resumable: re-running skips tasks already marked OK in the log.
Logs every action to 0516_Rev_issue_creation_log.csv next to this script.
"""
import csv
import json
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = "raymondjl1/genesis_physics"
PROJECT_ID = "PVT_kwHOB1aXSc4BTuXV"
STATUS_FIELD_ID = "PVTSSF_lAHOB1aXSc4BTuXVzhA7W4Y"
TODO_OPTION_ID = "f75ad846"

ROOT = Path(__file__).resolve().parent
MASTERS = [
    ROOT / "0516_Rev_Book_0_TASKS.md",
    ROOT / "0516_Rev_Book_1_TASKS.md",
    ROOT / "0516_Rev_Book_2_TASKS.md",
]
LOG_FILE = ROOT / "0516_Rev_issue_creation_log.csv"

LABEL_DEFS = {
    "review:0516":    ("FEF2C0", "2026-05-16 comprehensive review"),
    "sev:P0":         ("B60205", "P0 blocker"),
    "sev:P1":         ("D93F0B", "P1 critical"),
    "sev:P2":         ("FBCA04", "P2 important"),
    "sev:P3":         ("0E8A16", "P3 polish"),
    "sev:PRESERVE":   ("0052CC", "Strength to protect"),
    "concern:C1":     ("5319E7", "C1 flow/consistency"),
    "concern:C2":     ("5319E7", "C2 no conflicts"),
    "concern:C3":     ("5319E7", "C3 cross-references"),
    "concern:C4":     ("5319E7", "C4 biblical derivation"),
    "unit:Vol1":      ("C5DEF5", "Book 0 Vol 1"),
    "unit:Vol2":      ("C5DEF5", "Book 0 Vol 2"),
    "unit:Vol3":      ("C5DEF5", "Book 0 Vol 3"),
    "unit:Vol4":      ("C5DEF5", "Book 0 Vol 4"),
    "unit:Vol5":      ("C5DEF5", "Book 0 Vol 5"),
    "unit:Vol6":      ("C5DEF5", "Book 0 Vol 6"),
    "unit:Book1":     ("BFDADC", "Book 1 Hidden Architecture"),
    "unit:Book2":     ("BFDADC", "Book 2 Creator's Blueprint"),
    "unit:CrossCut":  ("F9D0C4", "Cross-cutting"),
}


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")


def ensure_labels():
    # gh CLI account lacks label admin on this repo; skip label creation.
    # All severity / concern / unit metadata is embedded in each issue body.
    return


def split_row(line):
    # leading | and trailing | produce empty cells; drop them
    cells = [c.strip() for c in line.split("|")]
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def parse_tasks():
    tasks = []
    row_re = re.compile(r"^\|\s*0516_Rev_(\d{3,4})\s*\|")
    for path in MASTERS:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not row_re.match(line):
                continue
            cells = split_row(line)
            # cells[0] = id, then severity, concern, unit, chapter, description, fix, owner, effort, source, raw_id, [notes]
            while len(cells) < 12:
                cells.append("")
            rev_num = int(re.search(r"0516_Rev_(\d+)", cells[0]).group(1))
            tasks.append({
                "id": rev_num,
                "id_str": f"0516_Rev_{rev_num:03d}",
                "severity":  cells[1],
                "concern":   cells[2],
                "unit":      cells[3],
                "chapter":   cells[4],
                "description": cells[5],
                "fix":       cells[6],
                "owner":     cells[7],
                "effort":    cells[8],
                "source":    cells[9],
                "raw_id":    cells[10],
                "notes":     cells[11],
            })
    tasks.sort(key=lambda t: t["id"])
    return tasks


def title_for(task):
    desc = task["description"].replace("\n", " ")
    desc = re.sub(r"\s+", " ", desc)
    # Strip bold markers for cleaner title
    desc = desc.replace("**", "")
    cap = 130
    short = desc[:cap].rstrip()
    if len(desc) > cap:
        short = short.rsplit(" ", 1)[0] + "…"
    return f"[{task['id_str']}] {short}"


def body_for(task):
    notes_line = f"- **Notes:** {task['notes']}\n" if task.get("notes") else ""
    return f"""**Task ID:** `{task['id_str']}`
**Severity:** {task['severity']}
**Concern(s):** {task['concern']}
**Unit:** {task['unit']}
**Chapter / Location:** {task['chapter']}

## Description
{task['description']}

## Suggested Fix
{task['fix']}

## Metadata
- **Owner (suggested):** {task['owner'] or '_unassigned_'}
- **Effort:** {task['effort']}
- **Source reviewer(s):** {task['source']}
- **Raw task ID(s):** `{task['raw_id']}`
{notes_line}
---
_Generated from the 2026-05-16 comprehensive review pass (96 reviewer sub-agents × 8 units). See `Quality_Control/Reviews/BOOK_SERIES_MASTER_REVIEW_2026-05-16.md`._
"""


def labels_for(task):
    labels = ["review:0516"]
    sev = task["severity"].upper()
    if "PRESERVE" in sev:    labels.append("sev:PRESERVE")
    elif "P0" in sev:        labels.append("sev:P0")
    elif "P1" in sev:        labels.append("sev:P1")
    elif "P2" in sev:        labels.append("sev:P2")
    elif "P3" in sev:        labels.append("sev:P3")
    concern = task["concern"].upper()
    for c in ["C1", "C2", "C3", "C4"]:
        if c in concern:
            labels.append(f"concern:{c}")
    unit = task["unit"]
    mapping = [("Vol 1", "unit:Vol1"), ("Vol 2", "unit:Vol2"),
               ("Vol 3", "unit:Vol3"), ("Vol 4", "unit:Vol4"),
               ("Vol 5", "unit:Vol5"), ("Vol 6", "unit:Vol6"),
               ("Book 1", "unit:Book1"), ("Book 2", "unit:Book2")]
    for tag, label in mapping:
        if tag in unit:
            labels.append(label)
    # Cross-cut detection
    if unit.count(",") >= 2 or "Book 0 cascade" in unit or "Multi-chapter" in unit:
        labels.append("unit:CrossCut")
    return labels


import tempfile

def create_issue(task):
    title = title_for(task)
    body = body_for(task)
    labels = labels_for(task)
    # Write body to a UTF-8 temp file so Unicode (σ, ξ, η, etc.) survives Windows console.
    tf = tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8")
    tf.write(body); tf.close()
    cmd = ["gh", "issue", "create",
           "--repo", REPO,
           "--title", title,
           "--body-file", tf.name]
    # Labels not attached: gh CLI account lacks label admin scope on this repo.
    # _ = labels  # retained for future use
    # Retry create up to 3 times on transient failures
    last_err = None
    for attempt in range(3):
        r = run(cmd)
        if r.returncode == 0 and r.stdout.strip():
            break
        last_err = (r.stderr or "").strip() or (r.stdout or "").strip() or f"empty output, rc={r.returncode}"
        time.sleep(2.0 * (attempt + 1))
    try:
        Path(tf.name).unlink()
    except Exception:
        pass
    if r.returncode != 0 or not r.stdout.strip():
        return None, last_err or r.stderr.strip() or "empty output"
    lines = r.stdout.strip().splitlines()
    if not lines:
        return None, "empty stdout after success"
    url = lines[-1]
    issue_num = url.rsplit("/", 1)[-1]
    r2 = run(["gh", "api", f"repos/{REPO}/issues/{issue_num}", "--jq", ".node_id"])
    if r2.returncode != 0:
        return None, r2.stderr.strip()
    return (issue_num, r2.stdout.strip(), url), None


def add_to_project(content_id):
    mut = (
        'mutation{addProjectV2ItemById(input:{'
        f'projectId:"{PROJECT_ID}",contentId:"{content_id}"'
        '}){item{id}}}'
    )
    r = run(["gh", "api", "graphql", "-f", f"query={mut}"])
    if r.returncode != 0:
        return None, r.stderr.strip()
    try:
        data = json.loads(r.stdout)
        return data["data"]["addProjectV2ItemById"]["item"]["id"], None
    except Exception as e:
        return None, f"{e}: {r.stdout[:200]}"


def set_status_todo(item_id):
    mut = (
        'mutation{updateProjectV2ItemFieldValue(input:{'
        f'projectId:"{PROJECT_ID}",itemId:"{item_id}",'
        f'fieldId:"{STATUS_FIELD_ID}",'
        f'value:{{singleSelectOptionId:"{TODO_OPTION_ID}"}}'
        '}){projectV2Item{id}}}'
    )
    r = run(["gh", "api", "graphql", "-f", f"query={mut}"])
    return r.returncode == 0, (r.stderr.strip() if r.returncode != 0 else "")


def main():
    print(f"Ensuring labels exist...", flush=True)
    ensure_labels()
    tasks = parse_tasks()
    print(f"Parsed {len(tasks)} tasks.", flush=True)

    done = set()
    if LOG_FILE.exists():
        with LOG_FILE.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("status") == "OK":
                    done.add(row["id"])
        print(f"Resuming: {len(done)} tasks already OK.", flush=True)

    log_exists = LOG_FILE.exists()
    log_f = LOG_FILE.open("a", newline="", encoding="utf-8")
    fields = ["id", "issue_num", "node_id", "item_id", "status", "error", "ts"]
    writer = csv.DictWriter(log_f, fieldnames=fields)
    if not log_exists:
        writer.writeheader()

    ok_count = 0
    fail_count = 0
    for i, task in enumerate(tasks, 1):
        if task["id_str"] in done:
            continue
        try:
            res, err = create_issue(task)
            if err:
                writer.writerow({"id": task["id_str"], "issue_num": "", "node_id": "", "item_id": "",
                                 "status": "CREATE_FAIL", "error": err[:300], "ts": int(time.time())})
                log_f.flush(); fail_count += 1
                print(f"[{i}/{len(tasks)}] {task['id_str']} CREATE FAIL: {err[:100]}", flush=True)
                time.sleep(2.0)
                continue
            issue_num, node_id, url = res
            item_id, err = add_to_project(node_id)
            if err:
                writer.writerow({"id": task["id_str"], "issue_num": issue_num, "node_id": node_id, "item_id": "",
                                 "status": "PROJECT_FAIL", "error": err[:300], "ts": int(time.time())})
                log_f.flush(); fail_count += 1
                print(f"[{i}/{len(tasks)}] {task['id_str']} #{issue_num} PROJECT FAIL", flush=True)
                time.sleep(2.0)
                continue
            ok, err = set_status_todo(item_id)
            status = "OK" if ok else "STATUS_FAIL"
            writer.writerow({"id": task["id_str"], "issue_num": issue_num, "node_id": node_id, "item_id": item_id,
                             "status": status, "error": err[:300] if err else "", "ts": int(time.time())})
            log_f.flush()
            if ok:
                ok_count += 1
            else:
                fail_count += 1
            if i % 10 == 0 or i == len(tasks):
                print(f"[{i}/{len(tasks)}] {task['id_str']} -> #{issue_num} {status}  (OK={ok_count} FAIL={fail_count})", flush=True)
        except Exception as e:
            writer.writerow({"id": task["id_str"], "issue_num": "", "node_id": "", "item_id": "",
                             "status": "EXCEPTION", "error": str(e)[:300], "ts": int(time.time())})
            log_f.flush(); fail_count += 1
            print(f"[{i}/{len(tasks)}] {task['id_str']} EXCEPTION: {e}", flush=True)
        time.sleep(0.7)

    log_f.close()
    print(f"Complete. OK={ok_count} FAIL={fail_count} log={LOG_FILE}", flush=True)


if __name__ == "__main__":
    main()
