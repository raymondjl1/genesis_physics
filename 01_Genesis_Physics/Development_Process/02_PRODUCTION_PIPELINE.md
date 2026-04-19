# Production Pipeline — Manuscript to Amazon

**Date:** April 5, 2026
**Author:** Jeff Raymond
**Purpose:** The complete process for turning a validated manuscript into a published product on Amazon — Kindle, paperback, hardcover, and Audible.

---

## Overview

Once a manuscript passes validation (Phase 8 in the Process Overview), it enters production. This document covers everything from formatting through launch day.

**Publishing Platform:** Amazon KDP (Kindle Direct Publishing) for all print and ebook formats. ACX (Audiobook Creation Exchange) for audiobooks.

**Business Model:** Self-published, print-on-demand. Zero inventory. Jeff retains full rights and 60-70% royalties on ebooks, ~40-60% on print (minus printing costs).

```
Validated Manuscript
    │
    ├── 1. Interior Formatting ──→ Print PDF + EPUB
    ├── 2. Cover Design ──→ Print covers + Kindle cover
    ├── 3. ISBN Assignment ──→ Free KDP ISBNs or purchased
    ├── 4. KDP Upload ──→ Kindle ebook live
    ├── 5. KDP Print Upload ──→ Paperback + Hardcover live
    ├── 6. Proof Copies ──→ Jeff redlines hardcopy
    ├── 7. Revisions ──→ Incorporate redline edits
    ├── 8. Professional Copyedit ──→ Final polish
    ├── 9. Final Upload ──→ Updated files on KDP
    └── 10. Audiobook (ACX) ──→ Live on Audible
```

---

## Step 1: Interior Formatting

The manuscript must be professionally formatted for both print and digital.

### Tools by Product

| Product | Recommended Tool | Why |
|---------|-----------------|-----|
| **Foundations (Vols 1-6)** | **LaTeX** (texlive + custom class) | Heavy math, equations, derivations, problem sets. LaTeX is the only tool that handles this well. |
| **Book 1** | **LaTeX** | Significant math content. Same class as Foundations, lighter equation density. |
| **Book 2** | **Vellum** (macOS) or **InDesign** | Zero equations. Vellum produces beautiful ebook + print formatting with minimal effort. |
| **The Creator's Blueprint** | **Vellum** or **InDesign** | Scripture-heavy, discussion-focused. Vellum handles this well. |

### Print Formatting Requirements

- **Trim size:** 6×9 inches (standard for nonfiction). Foundations may use 7×10 for equation readability.
- **Margins:** KDP minimum margins apply (varies by page count). Build in at least 0.5" gutter.
- **Font:** Serif for body text (Garamond, Minion Pro, or similar). 10-11pt for standard, 9-10pt for Foundations.
- **Headers/footers:** Chapter title in header, page numbers in footer.
- **Front matter:** Half title, title page, copyright page, dedication, table of contents, preface.
- **Back matter:** Glossary, bibliography, index (Foundations), appendices, problem solutions (Foundations), about the author.
- **Bleed:** No bleed required for text-only books. If figures extend to page edge, enable bleed (add 0.125" on each side).

### Print Output

- **Paperback interior:** PDF, black-and-white interior (color only if figures require it — significantly increases print cost).
- **Hardcover interior:** Same PDF as paperback. KDP uses the same interior file for both.

### Ebook Formatting Requirements

- **Format:** EPUB (reflowable). KDP accepts EPUB or DOCX but EPUB gives far better results.
- **Equations in ebook:** For Foundations and Book 1, equations must be embedded as images (SVG preferred, PNG fallback) with alt text. MathML is partially supported but unreliable on older Kindles.
- **Table of contents:** Must be a navigable NCX/NAV TOC, not just a printed page. Most tools generate this automatically.
- **Cover image:** Embedded in EPUB front matter.
- **Testing:** Use Kindle Previewer (free from Amazon) to test on simulated devices before upload.

---

## Step 2: Cover Design

**Hire a professional cover designer.** The cover sells the book. Budget $500-1,500 per cover.

### What You Need

| Format | Specification |
|--------|--------------|
| **Kindle ebook** | Front cover only. 2560×1600 pixels (1.6:1 ratio). RGB color. JPEG or TIFF. |
| **Paperback** | Full wrap: front + spine + back. KDP provides a cover calculator tool — input your trim size and page count, it generates a template with exact spine width. 300 DPI. CMYK color. PDF. |
| **Hardcover** | Full wrap: front + spine + back. Case-laminate (no dust jacket — KDP doesn't offer dust jackets). KDP cover calculator generates template. 300 DPI. CMYK color. PDF. |

### Cover Design Brief (What to Tell the Designer)

- Series branding: all Genesis Physics books should be visually recognizable as a series
- Foundations volumes: academic feel, volume number prominent, consistent template across all 6
- Book 2 and The Creator's Blueprint: approachable, not intimidating, suggests wonder/discovery
- Book 1: professional, credible, suggests serious physics
- Back cover: brief description, author bio, barcode area (KDP places barcode automatically)

### Spine Width

KDP calculates spine width from page count and paper type:
- **White paper:** spine = page count × 0.002252"
- **Cream paper:** spine = page count × 0.002347"
- Minimum spine width for text on spine: 0.0625" (about 28 pages white / 27 pages cream)

All Genesis Physics books will exceed this minimum comfortably.

---

## Step 3: ISBN Assignment

**Options:**

| Option | Cost | Imprint |
|--------|------|---------|
| **Free KDP ISBN** | $0 | Lists "Independently Published" as publisher |
| **Purchased ISBN** (Bowker) | ~$125 each or $295 for 10 | Lists your own imprint name |

**Recommendation:** Purchase a block of ISBNs from Bowker and register a publisher imprint. Each format of each book needs its own ISBN (paperback, hardcover, and ebook each get separate ISBNs). For the full series (4 standalone books + 6 Foundations volumes = 10 titles × 3 formats = 30 ISBNs), a block of 100 ($575) provides room for future editions.

**Note:** Kindle ebooks don't require an ISBN (Amazon assigns an ASIN), but having one looks more professional and enables wider distribution later.

---

## Step 4: Kindle Ebook Upload (KDP)

### Process

1. Log into [kdp.amazon.com](https://kdp.amazon.com)
2. Click "Create New Title" → "Kindle eBook"
3. **Book Details:**
   - Title, subtitle, series name ("Genesis Physics Series" or "The Foundations of Genesis Physics")
   - Author: Jeff Raymond
   - Description (up to 4,000 characters, supports basic HTML)
   - Keywords (up to 7, each up to 50 characters — choose carefully for discoverability)
   - Categories (up to 3 BISAC categories)
4. **Content:**
   - Upload EPUB file
   - Upload cover image (2560×1600)
   - Enable DRM (recommended — prevents casual copying)
5. **Pricing:**
   - Select 70% royalty option (requires price between $2.99–$9.99)
   - For Foundations volumes priced above $9.99: 35% royalty applies
   - Set prices for each Amazon marketplace (US, UK, DE, etc.)
6. **Publish** → Live within 72 hours

### Pricing Strategy

| Product | Kindle Price | Royalty Rate |
|---------|-------------|-------------|
| The Creator's Blueprint | $9.99 | 70% |
| Book 2 | $9.99 | 70% |
| Book 1 | $14.99 | 35% (above $9.99 threshold) |
| Foundations (per volume) | $19.99 | 35% |

---

## Step 5: Print Upload (KDP Print-on-Demand)

### Paperback

1. In KDP, click "Create New Title" → "Paperback"
2. **Book Details:** Same as Kindle (link to Kindle edition by matching title/author)
3. **Content:**
   - Interior: Upload PDF (black-and-white or color)
   - Paper: White or cream (cream for narrative books, white for Foundations with figures)
   - Cover: Upload full-wrap PDF from cover designer
   - Trim size: 6×9 or 7×10
4. **Preview:** Use KDP Print Previewer to check for issues (margin violations, image quality, etc.)
5. **Pricing:**
   - Set list price. KDP shows printing cost and your royalty.
   - Printing cost = fixed charge + per-page charge (varies by page count, trim size, ink type)
   - Royalty = 60% × list price − printing cost
6. **Publish** → Live within 72 hours

### Hardcover

1. Same process as paperback, select "Hardcover" instead
2. **Cover type:** Case-laminate (the only option on KDP — no dust jacket)
3. **Trim sizes available:** 5.5×8.5, 6×9, 6.14×9.21, 7×10, 8.5×11
4. **Pricing:** Higher printing cost than paperback. Set list price accordingly.
5. **Note:** Hardcover is NOT available through KDP Expanded Distribution — Amazon only.

### Print Pricing Strategy

| Product | Paperback | Hardcover |
|---------|-----------|-----------|
| The Creator's Blueprint | $16.99–$19.99 | $24.99–$29.99 |
| Book 2 | $14.99–$16.99 | $24.99–$29.99 |
| Book 1 | $29.99–$34.99 | $44.99–$49.99 |
| Foundations (per volume) | $39.99–$59.99 | $54.99–$74.99 |

*Final pricing set after seeing actual printing costs and page counts.*

---

## Step 6: Proof Copies

**This is critical.** Before the book goes live (or immediately after uploading), order proof copies.

### How Proof Copies Work

- Available from KDP Bookshelf after uploading interior + cover files
- Order up to **5 proof copies per order**
- Printed with **"Not for Resale"** watermark on the last page
- Arrive in **5-7 business days** (standard shipping) or **2-3 business days** (expedited)
- Cost: **printing cost only** (no royalty charge, you just pay for printing + shipping)
- You do NOT need to publish the book first — proofs are available as soon as files are uploaded

### The Redline Process

1. Order 2 proof copies (one to read, one as backup)
2. **Jeff reads the physical book cover to cover** with a red pen
3. Mark every issue: typos, awkward phrasing, layout problems, figure placement, equation formatting
4. Transcribe redline notes into the digital manuscript
5. Re-upload corrected files to KDP
6. Order another proof to verify fixes (if changes were substantial)
7. Repeat until Jeff approves the hardcopy

### Why Physical Proofs Matter

You catch things on paper that you miss on screen — every time. Layout issues, font size problems, margin tightness, figure placement, the way equations break across pages. The physical proof is a non-negotiable step.

---

## Step 7: Author Copies (Jeff's Personal Hardcopies)

**After the book goes live on Amazon:**

- Order **author copies** from KDP Bookshelf
- Printed at **printing cost** (same as proof copies, but NO watermark)
- These are the final, retail-quality copies
- Order as many as you want — no minimum, no maximum
- Perfect for: Jeff's personal library, gifts, reference copies

**Important distinction:**
- **Proof copies** = before/during publication, "Not for Resale" watermark
- **Author copies** = after publication, no watermark, print cost only

---

## Step 8: Professional Copyedit

**After Jeff's redlines are incorporated but before final publication:**

Hire a professional copyeditor for final polish. This catches what the author and reviewer agents miss — subtle grammar issues, punctuation consistency, formatting micro-errors.

### What to Look For in a Copyeditor

- Experience with nonfiction, ideally science/technical writing
- For Foundations: must be comfortable with mathematical text (specialized skill — expect higher rates)
- Budget: $0.02–$0.04 per word for standard nonfiction. Technical/math content: $0.04–$0.06 per word.
- Turnaround: 2-4 weeks per book depending on length

### Cost Estimates

| Product | Words | Estimated Cost |
|---------|-------|---------------|
| The Creator's Blueprint | 60K–80K | $1,800–$4,800 |
| Book 2 | 55K–70K | $1,650–$4,200 |
| Book 1 | 80K–100K | $3,200–$6,000 |
| Foundations (per volume) | 90K–180K | $3,600–$10,800 |

*Foundations is the most expensive to copyedit due to volume and technical complexity.*

---

## Step 9: Final Upload and Launch

After all edits are incorporated:

1. Upload final interior files (PDF for print, EPUB for Kindle)
2. Upload final cover files
3. Verify in KDP Print Previewer and Kindle Previewer
4. If the book was already live, updates propagate within 72 hours
5. If not yet published, click Publish

### Amazon Listing Optimization

- **Title and subtitle:** Clear, descriptive, keyword-rich
- **Book description:** Up to 4,000 characters. Use basic HTML for formatting (bold, italics, line breaks). Lead with the hook.
- **Keywords:** 7 keyword phrases per listing. Research what readers search for. Include "zone architecture," "physics from first principles," etc.
- **Categories:** Up to 3 BISAC categories. Choose the most specific ones where the book can rank.
- **A+ Content:** Enhanced Brand Content available to brand-registered authors. Rich media product page with comparison charts, images, formatted text. Apply for Amazon Brand Registry to unlock this.

---

## Step 10: Audiobook Production (ACX)

**Applies to: Book 2 and The Creator's Blueprint.** (Foundations and Book 1 are too equation-heavy for audio.)

### Platform: ACX (Audiobook Creation Exchange)

ACX is Amazon's audiobook platform. Books produced through ACX are distributed on Audible, Amazon, and iTunes.

### Process

1. **Create an ACX account** at [acx.com](https://www.acx.com)
2. **Claim your title** — search for your book (must already be on Amazon/Kindle)
3. **Post an audition** — upload a short excerpt (2-3 pages) for narrators to audition
4. **Select a narrator** — listen to auditions, choose the best fit
5. **Negotiate terms** — see payment options below
6. **Production** — narrator records, edits, and masters the full audiobook
7. **Review** — listen to the full audiobook, request corrections
8. **Approve** — submit for Audible's quality review
9. **Live on Audible** — typically 10-14 business days after approval

### Payment Options

| Option | Upfront Cost | Royalty |
|--------|-------------|---------|
| **Per Finished Hour (PFH)** | $150–$400/hr | 40% exclusive, 25% non-exclusive |
| **Royalty Share** | $0 | 20% (narrator gets 20%, you get 20%) |
| **Royalty Share Plus** | Reduced PFH | Split royalties |

**Recommendation for Book 2 and The Creator's Blueprint:** Pay per finished hour for higher long-term royalties (40%). Budget $2,000–$6,000 per audiobook depending on length and narrator rates.

### Narrator Requirements

- **AI narration is NOT permitted on ACX** (as of 2026). Must be a human narrator.
- Look for experience with: nonfiction narration, science/faith content, warm/authoritative tone
- Book 2 narrator: engaging, conversational, sense of wonder
- The Creator's Blueprint narrator: warm, encouraging, family-friendly — possibly a different narrator than Book 2

### ACX Audio Requirements

- MP3 or WAV files, one per chapter
- Consistent volume (RMS between -23dB and -18dB, peak below -3dB)
- Sample rate: 44.1 kHz, 192 kbps or higher
- Room tone: max -60dB noise floor
- Each file must begin and end with 0.5–1 second of room tone

### Cost Estimates

| Product | Estimated Length | PFH Cost (at $250/hr) |
|---------|-----------------|----------------------|
| Book 2 | 7–9 finished hours | $1,750–$2,250 |
| The Creator's Blueprint | 8–10 finished hours | $2,000–$2,500 |

---

## Production Timeline

Each book's production phase takes approximately 2-4 months:

```
Week 1-2:    Interior formatting (LaTeX/Vellum)
Week 2-3:    Cover design (concurrent with formatting)
Week 3:      Upload to KDP + order proof copies
Week 4-5:    Jeff reads and redlines proofs
Week 5-6:    Incorporate redlines + re-upload
Week 6-8:    Professional copyedit
Week 8-9:    Final upload + launch
Week 4-12:   Audiobook production (concurrent, if applicable)
```

---

## Production Checklist

Use this checklist for each product as it enters production:

### Pre-Production
- [ ] Manuscript passes all validation (Phase 8)
- [ ] LaTeX/Vellum formatting tool selected and configured
- [ ] Cover designer contracted
- [ ] ISBN assigned
- [ ] Copyeditor identified (booked in advance — good editors have waitlists)

### Formatting
- [ ] Print interior PDF formatted and reviewed
- [ ] EPUB formatted and tested in Kindle Previewer
- [ ] Front matter complete (title, copyright, TOC, preface)
- [ ] Back matter complete (glossary, bibliography, index, about author)

### Cover
- [ ] Kindle cover received (2560×1600 JPEG)
- [ ] Paperback wrap received (PDF, 300 DPI, CMYK)
- [ ] Hardcover wrap received (PDF, 300 DPI, CMYK)
- [ ] Spine width verified against KDP calculator

### Upload and Proofing
- [ ] Kindle ebook uploaded to KDP
- [ ] Paperback uploaded to KDP
- [ ] Hardcover uploaded to KDP
- [ ] Proof copies ordered
- [ ] Jeff redlines complete
- [ ] Redline edits incorporated
- [ ] Second proof ordered (if needed)

### Copyedit and Final
- [ ] Professional copyedit complete
- [ ] Final files uploaded to KDP
- [ ] Final preview check passed (Kindle Previewer + Print Previewer)

### Launch
- [ ] Kindle ebook live
- [ ] Paperback live (print-on-demand)
- [ ] Hardcover live (print-on-demand)
- [ ] Author copies ordered for Jeff
- [ ] Categories and keywords optimized
- [ ] A+ Content created (if eligible)
- [ ] Audiobook production started (Book 2 and The Creator's Blueprint only)

### Post-Launch
- [ ] Audiobook live on Audible
- [ ] Amazon listing verified (correct categories, description, pricing)
- [ ] Launch email sent to subscriber list

---

## Cost Summary Per Product

| Cost Item | Family Ed | Book 2 | Book 1 | Foundations (per vol) |
|-----------|-----------|--------|--------|---------------------|
| Cover design | $500–$1,000 | $500–$1,000 | $500–$1,000 | $500–$1,000 |
| ISBNs (from block) | ~$18 × 3 | ~$18 × 3 | ~$18 × 3 | ~$18 × 3 |
| Copyedit | $1,800–$4,800 | $1,650–$4,200 | $3,200–$6,000 | $3,600–$10,800 |
| Proof copies | ~$20–$40 | ~$15–$30 | ~$30–$50 | ~$30–$60 |
| Audiobook | $2,000–$2,500 | $1,750–$2,250 | — | — |
| **Total** | **$4,400–$8,400** | **$4,000–$7,500** | **$3,800–$7,100** | **$4,200–$11,900** |

*Foundations total across all 6 volumes: $25,000–$71,000 (the largest investment by far).*

---

*This pipeline ensures every product reaches Amazon in professional quality — ebook, paperback, hardcover, and audiobook — without holding inventory and with Jeff maintaining full creative and financial control.*
