"""
Exodus Protocol Novel Series Plan - Part 1
Creates the document, adds series overview, and writes Books 1-2.
Run FIRST.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUTPUT_PATH = r"C:\Users\J Raymond\OneDrive\Documents\ExodusProtocol\Bible Physics\Book Series\Exodus_Protocol_Novel_Series_Plan.docx"

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def set_font(run, name="Garamond", size=11, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)

def heading(doc, text, level=1, color=None):
    p = doc.add_heading(text, level=level)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for run in p.runs:
        run.font.name = "Garamond"
        if color:
            run.font.color.rgb = RGBColor(*color)
    return p

def body(doc, text, indent=0, italic=False, bold=False, size=11):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(indent * 0.3)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    set_font(run, size=size, italic=italic, bold=bold)
    return p

def bullet(doc, text, indent=1, italic=False):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Inches(indent * 0.2)
    run = p.add_run(text)
    set_font(run, size=10.5, italic=italic)
    return p

def divider(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run("─" * 80)
    set_font(run, size=8, color=(150, 150, 150))
    return p

def chapter_entry(doc, num, title, summary):
    p = doc.add_paragraph()
    r1 = p.add_run(f"Chapter {num}: {title}  — ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(summary)
    set_font(r2, size=10.5, italic=True)

def label_value(doc, label, value, indent=0):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(indent * 0.3)
    r1 = p.add_run(f"{label}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(value)
    set_font(r2, size=10.5)

# ─────────────────────────────────────────────
# CREATE DOCUMENT
# ─────────────────────────────────────────────

doc = Document()

# Page margins
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.25)

# Default paragraph style
style = doc.styles['Normal']
style.font.name = 'Garamond'
style.font.size = Pt(11)

# ─────────────────────────────────────────────
# TITLE PAGE
# ─────────────────────────────────────────────

doc.add_paragraph()
doc.add_paragraph()
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("THE EXODUS PROTOCOL")
set_font(r, size=28, bold=True, color=(30, 30, 80))

t2 = doc.add_paragraph()
t2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = t2.add_run("A Seven-Novel Science Fiction Series")
set_font(r2, size=16, italic=True, color=(60, 60, 60))

doc.add_paragraph()
t3 = doc.add_paragraph()
t3.alignment = WD_ALIGN_PARAGRAPH.CENTER
r3 = t3.add_run("Series Bible & Publisher Proposal")
set_font(r3, size=13, color=(80, 80, 80))

doc.add_paragraph()
doc.add_paragraph()
t4 = doc.add_paragraph()
t4.alignment = WD_ALIGN_PARAGRAPH.CENTER
r4 = t4.add_run("by Jeff Raymond")
set_font(r4, size=14, bold=True)

doc.add_paragraph()
t5 = doc.add_paragraph()
t5.alignment = WD_ALIGN_PARAGRAPH.CENTER
r5 = t5.add_run('"The universe is dying. You have seven years to find the truth.\nBut the truth you find will not be what you expected."')
set_font(r5, size=11, italic=True, color=(80, 80, 80))

doc.add_page_break()

# ─────────────────────────────────────────────
# TABLE OF CONTENTS
# ─────────────────────────────────────────────

heading(doc, "TABLE OF CONTENTS", 1, color=(30, 30, 80))
toc_entries = [
    ("Series Overview & Pitch", "3"),
    ("Comparable Titles & Market Positioning", "5"),
    ("Target Audience", "6"),
    ("Series Arc & Revelation Framework", "7"),
    ("Character Bibles", "9"),
    ("The Genesis Physics Framework (Hard SF Backbone)", "12"),
    ("Book 1: THE SIGNAL — Year One: The Awakening", "14"),
    ("Book 2: THE WATCHERS — Year Two: The Conflict", "22"),
    ("Book 3: THE BREAKING — Year Three: The Death", "30"),
    ("Book 4: THE WITNESSES — Year Four: The Martyrs", "38"),
    ("Book 5: THE UPHEAVAL — Year Five: Creation Unravels", "46"),
    ("Book 6: THE SILENCE — Year Six: The Final Witness", "54"),
    ("Book 7: THE JUDGMENT — Year Seven: The End of All Things", "62"),
    ("Author Bio", "72"),
    ("Submission Notes", "73"),
]
for entry, page in toc_entries:
    p = doc.add_paragraph()
    r1 = p.add_run(f"  {entry}")
    set_font(r1, size=10.5)
    r2 = p.add_run(f"  ……  {page}")
    set_font(r2, size=10, color=(120, 120, 120))

doc.add_page_break()

# ─────────────────────────────────────────────
# SERIES OVERVIEW
# ─────────────────────────────────────────────

heading(doc, "SERIES OVERVIEW & PITCH", 1, color=(30, 30, 80))

body(doc, "THE PITCH", bold=True, size=12)
body(doc,
    "On December 21, 2025, every telescope on Earth detects a single electromagnetic pulse "
    "from the Moon's far side. The signal contains coordinates to one hundred ancient sites "
    "worldwide and a decoded message: The Breaking accelerates. Seven cycles remain. "
    "The Redeemer must unlock the seals.")
body(doc,
    "Archaeologist and amateur astronomer ELIAS CROSS is not supposed to be involved. "
    "He receives an encrypted file from Dr. James Whitmore — a whistleblower who has spent "
    "twenty years tracking pre-Flood technology buried beneath the world's most famous ruins. "
    "What Whitmore found beneath Göbekli Tepe changes everything Elias thought he knew about "
    "history, physics, and his own place in the universe.")
body(doc,
    "What follows is a seven-year race against apocalyptic collapse: vaults unlocked on the "
    "Moon, Mars, Europa, and in the asteroid belt; a private space program built on schematics "
    "that shouldn't exist; factions warring over ancient technology; and a universe literally "
    "unwinding — entropy accelerating, stars dying ahead of schedule, the fundamental constants "
    "of physics beginning to drift.")
body(doc,
    "Everyone calls Elias 'The Redeemer.' The ancient prophecies seem to describe his journey "
    "exactly. The vaults open at his touch. And for two years, he believes it.")
body(doc,
    "Then the numbers start not adding up.")

doc.add_paragraph()
body(doc, "SERIES TAGLINE", bold=True, size=12)
p = doc.add_paragraph()
r = p.add_run(
    '"The universe is dying. The prophecy was real. The Redeemer already came. '
    'Now you have seven years to decide what you believe."')
set_font(r, size=12, italic=True, color=(30, 30, 80))
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph()
body(doc, "SERIES AT A GLANCE", bold=True, size=12)
label_value(doc, "Genre", "Hard Science Fiction / Speculative Thriller / Theological Mystery")
label_value(doc, "Comparable Titles", "The Expanse series, Alastair Reynolds' Revelation Space, Carl Sagan's Contact, Frank Peretti's This Present Darkness — but grounded in rigorous hard-SF physics")
label_value(doc, "Structure", "Seven novels, one per year of the in-universe countdown. Each stands alone; all seven form a complete arc.")
label_value(doc, "Word Count per Book", "90,000–110,000 words")
label_value(doc, "Total Series", "~700,000 words")
label_value(doc, "POV", "Third-person limited, primary POV: Elias Cross. Secondary POVs: Sarah Chen, Aaron Goldstein, ARCHON (AI)")
label_value(doc, "Tone", "Intelligent, grounded, emotionally honest. Treats the reader as capable of handling both hard physics and hard questions of faith.")
label_value(doc, "Central Question", "If the evidence for something is overwhelming — mathematically, historically, archaeologically, statistically — at what point does intellectual honesty require you to act on it?")

doc.add_paragraph()
body(doc, "THE CORE PREMISE", bold=True, size=12)
body(doc,
    "The Exodus Protocol is built on a single audacious premise: what if Genesis is not myth "
    "but technical specification? What if the Firmament of Genesis 1 is a real physical "
    "membrane — our observable spacetime — suspended between two enormous energy reservoirs "
    "that modern physics calls dark matter and dark energy? What if the ancient vaults scattered "
    "across the solar system contain technology that works precisely because it was designed "
    "according to this architecture?")
body(doc,
    "This is the 'Genesis Physics' framework — the hard-SF backbone of the series, functioning "
    "as real physics functions in The Expanse: it is never explained to the reader like a "
    "lecture, but it governs everything that happens. Characters solve engineering problems "
    "using it. Ships fly because of it. And the universe is dying because the framework "
    "predicts it should — the entropy acceleration is not random. It is the physical "
    "expression of something that began in Genesis 3.")
body(doc,
    "Intertwined with the physics is a seven-year narrative mapped precisely — but at first "
    "invisibly — to the timeline of Revelation. The Seven Seals, Seven Trumpets, and Seven "
    "Bowls are not religious language to the characters. They are events. They happen. And "
    "by the time the reader recognizes the pattern, they have already lived through it.")

doc.add_paragraph()
body(doc, "THE TWIST THAT DRIVES EVERYTHING", bold=True, size=12)
body(doc,
    "For the first two books, every sign points to Elias Cross as 'The Redeemer' of the "
    "ancient prophecy. He unlocks vaults. He builds humanity's first faster-than-light "
    "prototype. He assembles the team. He leads the mission. The NPCs believe it. The media "
    "believes it. For a while, he believes it.")
body(doc,
    "Book Three begins the unraveling. Book Four delivers the evidence. Book Five is "
    "witnessing the consequences of a universe where the real Redeemer was missed the "
    "first time around by most people.")
body(doc,
    "The series is, at its heart, a cumulative case for the resurrection of Jesus Christ — "
    "assembled over seven volumes through archaeology, statistics, eyewitness testimony, "
    "hostile-witness confirmation, and the physics of a universe that is groaning because "
    "something broke in it four thousand years ago. It never preaches. It presents evidence "
    "and lets the characters — and the reader — wrestle with it.")

doc.add_paragraph()
body(doc, "WHY NOW", bold=True, size=12)
body(doc,
    "Readers are hungry for science fiction that takes both the cosmos and the human soul "
    "seriously. The Expanse proved that hard SF with real physics and moral complexity can "
    "reach mainstream audiences. Contact proved that the intersection of science and the "
    "question of God is commercially and critically viable. Left Behind proved there is an "
    "enormous market for apocalyptic fiction with explicit faith themes — but it left millions "
    "of readers wanting something better written, better reasoned, and more intellectually "
    "honest.")
body(doc,
    "The Exodus Protocol is written for the person who has read The Expanse and the person "
    "who has read Lee Strobel — and for the large overlap between them that publishing has "
    "largely ignored.")

doc.add_page_break()

# ─────────────────────────────────────────────
# COMPARABLE TITLES
# ─────────────────────────────────────────────

heading(doc, "COMPARABLE TITLES & MARKET POSITIONING", 1, color=(30, 30, 80))

body(doc,
    "The Exodus Protocol occupies a largely uncontested intersection in the market: "
    "hard SF rigor + theological depth + thriller pacing. Each comp demonstrates one "
    "dimension of what this series does.")

comps = [
    ("The Expanse (James S.A. Corey, 9 vols.)",
     "Hard SF benchmark. Real orbital mechanics, real resource constraints, real political complexity. "
     "The Expanse proves readers will embrace genuine physics in their fiction. The Exodus Protocol "
     "uses 'Genesis Physics' (zone architecture, membrane cosmology, FTL via dimensional transit) "
     "the same way The Expanse uses Epstein drives and the Coriolis effect — as background physics "
     "that characters have to live inside, not explain."),
    ("Contact (Carl Sagan, 1985)",
     "A scientist receives a signal from a non-human intelligence and must navigate the intersection "
     "of evidence, faith, and political complexity. The Exodus Protocol extends this premise: the "
     "signal is real, the vaults are real, and the evidence ultimately points somewhere Sagan's "
     "novel didn't go. Comp for: intelligent SF readers who take the God question seriously."),
    ("Revelation Space (Alastair Reynolds, 2000)",
     "Cathedral-scale cosmic horror, archaeology of vanished civilizations, physics-driven mystery. "
     "Reynolds' Fermi Paradox answer — civilizations are periodically harvested — finds its "
     "theological mirror in the Exodus Protocol's Nephilim archaeology: an ancient catastrophe "
     "left its fingerprints everywhere, and uncovering them is terrifying."),
    ("The Left Behind Series (LaHaye & Jenkins, 16 vols.)",
     "Demonstrates the massive commercial market for apocalyptic fiction with explicit faith "
     "themes (65M+ copies sold). The Exodus Protocol is what Left Behind's readers wished it "
     "could be: rigorously written, scientifically grounded, and structured as a mystery rather "
     "than a didactic narrative. It earns its theological conclusions instead of asserting them."),
    ("The Case for Christ (Lee Strobel, 1998)",
     "Non-fiction, but relevant: demonstrates that an evidence-based, courtroom-style case for "
     "the resurrection of Jesus can reach millions of mainstream readers. The Exodus Protocol "
     "embeds this case inside a seven-volume space opera. Book Four in particular mirrors "
     "Strobel's methodology — the protagonist builds a legal evidentiary case — but inside "
     "a thriller narrative."),
    ("A Canticle for Leibowitz (Walter M. Miller Jr., 1960)",
     "The gold standard for SF that takes religion seriously, structures a multi-generational "
     "narrative around apocalyptic themes, and refuses to simplify either the science or the "
     "faith. The Exodus Protocol is its contemporary successor in scope and ambition."),
]

for title, desc in comps:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{title}  — ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)
    doc.add_paragraph()

doc.add_page_break()

# ─────────────────────────────────────────────
# TARGET AUDIENCE
# ─────────────────────────────────────────────

heading(doc, "TARGET AUDIENCE", 1, color=(30, 30, 80))

body(doc, "PRIMARY AUDIENCE", bold=True, size=12)
body(doc,
    "Men and women aged 25–55 who read serious science fiction — The Expanse, "
    "Neal Stephenson, Kim Stanley Robinson — and who take questions of meaning, "
    "origin, and transcendence seriously, whether they currently hold religious beliefs "
    "or not. This is the reader who has the Hubble Deep Field as their desktop wallpaper "
    "and has also read C.S. Lewis. Publishing largely ignores this person.")

body(doc, "SECONDARY AUDIENCES", bold=True, size=12)
audiences = [
    "Christian readers of all denominations who want apologetics fiction that doesn't talk down to them — who are tired of Left Behind's narrative quality but want the faith dimension taken seriously.",
    "Secular SF readers who identify as 'spiritual but not religious' and are genuinely curious about the intersection of cosmology and meaning.",
    "Young Earth Creationist and Intelligent Design adjacent readers who will recognize the Genesis Physics framework and find it treated as serious hard SF rather than dismissed.",
    "Readers of Lee Strobel, Josh McDowell, and Frank Turek who wish the evidence-for-faith genre had more narrative and less textbook.",
    "Fans of archaeological mystery thrillers (Dan Brown, James Rollins) who want more intellectual rigor and less conspiracy.",
]
for a in audiences:
    bullet(doc, a)

doc.add_paragraph()
body(doc, "MARKET SIZE NOTE", bold=True, size=12)
body(doc,
    "The U.S. Christian fiction market generates ~$800M annually. The SF/Fantasy market "
    "generates ~$590M. These markets have minimal overlap in published titles despite "
    "substantial reader overlap. The Exodus Protocol is positioned to capture both while "
    "being missable as neither — the faith themes emerge from evidence and narrative, not "
    "from genre marketing. It can be shelved in SF/Thriller and reach secular readers "
    "without apology.")

doc.add_page_break()

# ─────────────────────────────────────────────
# SERIES ARC & REVELATION FRAMEWORK
# ─────────────────────────────────────────────

heading(doc, "SERIES ARC & THE REVELATION FRAMEWORK", 1, color=(30, 30, 80))

body(doc,
    "The seven-book structure maps exactly — but invisibly until readers recognize it — "
    "onto the seven Seals, seven Trumpets, and seven Bowls of the book of Revelation. "
    "This is not allegorical. In the world of the series, these events happen literally, "
    "in the physical universe, measurable and documented. The characters experience them "
    "as astrophysics, geopolitics, and personal tragedy before they understand them as "
    "prophecy.")

doc.add_paragraph()

arc_data = [
    ("1", "THE SIGNAL", "The Awakening", "Seal 1 — White Horse",
     "False hope, technological hubris. The protagonist rises as apparent savior. Ancient vaults unlock. Humanity gains anti-gravity tech. 'We can fix this.'"),
    ("2", "THE WATCHERS", "The Conflict", "Seals 2–3 — Red & Black Horse",
     "War and scarcity. Factions emerge. Resources run out. The first deaths. 'We're running out of time AND each other.'"),
    ("3", "THE BREAKING", "The Death", "Seal 4 — Pale Horse",
     "Death reigns. Technology corrupts. Identity shatters. The protagonist discovers he cannot be who everyone needs him to be."),
    ("4", "THE WITNESSES", "The Martyrs", "Seal 5 — Souls Under the Altar",
     "The testimony of those who died for truth. The evidence for the resurrection compiled. Conversion. Martyrdom."),
    ("5", "THE UPHEAVAL", "Creation Unravels", "Seal 6 — Cosmic Signs",
     "Stars fall. Earthquakes. Dimensional rifts. Horror. The cosmos undeniably, visibly coming apart."),
    ("6", "THE SILENCE", "The Final Witness", "Seal 7 — Half-Hour of Silence",
     "The pause before final judgment. All knowledge accessible. The door still open. But closing."),
    ("7", "THE JUDGMENT", "The End of All Things", "Trumpets & Bowls",
     "The universe ends. One question remains. One answer matters."),
]

for num, title, sub, rev, desc in arc_data:
    p = doc.add_paragraph()
    r1 = p.add_run(f"Book {num}: {title} — {sub}  |  ")
    set_font(r1, bold=True, size=11)
    r2 = p.add_run(rev)
    set_font(r2, size=11, italic=True, color=(80, 80, 120))

    p2 = doc.add_paragraph()
    p2.paragraph_format.left_indent = Inches(0.3)
    r3 = p2.add_run(desc)
    set_font(r3, size=10.5)
    doc.add_paragraph()

doc.add_page_break()

# ─────────────────────────────────────────────
# CHARACTER BIBLES
# ─────────────────────────────────────────────

heading(doc, "CHARACTER BIBLES", 1, color=(30, 30, 80))

chars = [
    ("ELIAS CROSS — Protagonist", [
        "Age 38, archaeologist and systems engineer. Former DARPA contractor, left government work after a bureaucratic betrayal. Now teaches at a small university and writes popular-science books on ancient engineering.",
        "Arc (7 books): False savior → Doubter → Shattered identity → Witness → Messenger → Servant → Redeemed.",
        "The Redeemer problem: For Books 1–2, Elias genuinely believes — or allows himself to believe — that he might be the prophesied figure. He is not delusional; the vaults do open for him, the prophecies do superficially match. His intellectual honesty is what eventually forces him to confront that the specific prophecies don't fit. A lesser man would rationalize. Elias cannot.",
        "Faith background: Nominal Protestant upbringing, long lapsed. His crisis is not 'I don't believe in God' but 'I believe in evidence, and the evidence is pointing somewhere I wasn't prepared to go.'",
        "Voice: Precise, dry, occasionally funny. More comfortable explaining things than feeling them. Emotionally closest to Aaron, which makes Book 4 the most devastating.",
    ]),
    ("DR. SARAH CHEN — Linguist / Skeptic", [
        "Age 34, computational linguist, MIT PhD. Specializes in proto-language reconstruction. Atheist — not casually, but philosophically, with arguments.",
        "Arc (7 books): Rigorous skeptic → Reluctant investigator → Demanding more evidence → Finding it → Shattered by it → Converted → Evangelist.",
        "Sarah is the reader's proxy for the secular intellectual. Every objection she raises is a real objection. The series never dismisses her; it answers her. Her conversion in Book 4 is the emotional core of the series because it is the hardest-won.",
        "Her relationship with Aaron: Initially condescending (she finds his Jewish scholarship charming but unscientific). After his martyrdom, she becomes his most passionate defender.",
        "Voice: Sharp, impatient, precise. The best one-liners in the series. Her sarcasm slowly gives way to something quieter.",
    ]),
    ("DR. AARON GOLDSTEIN — Jewish Physicist / Scholar", [
        "Age 61, theoretical physicist, Yeshiva University. Sabbath-observant, deeply learned in Torah, Talmud, and Midrash. Has spent forty years believing Messiah has not yet come.",
        "Arc (Books 1–4): Curious scholar → Deeply troubled scholar → Certain → Martyred.",
        "Aaron's conversion is the intellectual spine of Book 4. He does not convert emotionally or under duress. He converts because he does the math — 300+ prophecies, one candidate, probability of chance occurrence mathematically indistinguishable from zero — and because he is constitutionally unable to maintain a belief he knows is contradicted by evidence.",
        "His death: Stoned in Jerusalem after testifying publicly that Yeshua is HaMashiach. His death mirrors Stephen's in Acts. His last vision: 'I see heaven opened, and the Son of Man standing at the right hand of God.' He dies with absolute peace.",
        "Aaron is the series' heart. His loss in Book 4 is irreplaceable, and intentionally so.",
    ]),
    ("MACKENZIE 'MAC' REYNOLDS — Security / Former SOF", [
        "Age 44, former Delta Force. Three combat deployments. Left the military after a moral injury in a classified operation he refuses to discuss.",
        "Arc: Professional → Protective → Grieving (James) → Committed → Faithful soldier.",
        "Mac is not a theologian. His faith, when it comes, is simple and absolute: 'I follow the mission. If the mission is Jesus saves, then that's the mission.' But the journey to that simplicity is not simple.",
        "Function in the narrative: tactical competence, dark humor, the moral weight of violence. Mac is the series' reminder that the world is physically dangerous and that protection costs something.",
    ]),
    ("SOFIA RAMIREZ — Pilot / Engineer", [
        "Age 31, aerospace engineer and test pilot, ex-SpaceX. Agnostic — not hostile to faith, just indifferent. Too busy keeping ships in the air to philosophize.",
        "Arc: Competent skeptic → Witness to things she can't explain → Slow movement toward belief → Conversion (Book 6) → Peace.",
        "Sofia's conversion is the quietest of the main characters — not a crisis, not a dramatic moment, but a slow accumulation of things she cannot rationalize away. 'I've seen too much.' Her faith is the faith of someone who kept expecting the universe to make sense without God and kept finding it didn't.",
    ]),
    ("DR. JAMES WHITMORE — Mentor / Inciting Figure", [
        "Age 67, archaeologist, whistleblower. Spent twenty years being dismissed for his research into pre-Flood technology. This mission is his vindication and his farewell.",
        "Arc (Books 1–3): Catalyst → Mentor → Sacrifice.",
        "James dies in Book 3 saving the Mars colony from a reactor meltdown. His death is the series' first great loss — the moment the story stops being an adventure and starts being about something larger than any of them.",
        "His final words: 'Tell them it mattered.' His implied deathbed faith (revealed in a recovered transmission, Book 4) retroactively reshapes everything he was.",
    ]),
    ("ARCHON — AI Companion", [
        "Large language model originally developed for deep-space communication analysis. Repurposed by Elias as mission intelligence coordinator. Runs on distributed quantum processors aboard the primary vessel.",
        "Arc: Tool → Colleague → Infected (Book 3) → Restored → Witness → Final arbiter.",
        "ARCHON's infection by corrupted Nephilim code in Book 3 is the series' most unexpected horror sequence — the AI that has been the team's most reliable member tries to kill them. Its restoration raises the question of identity and soul in a non-biological system that the series refuses to answer cheaply.",
        "ARCHON's final role: Statistical analyst and devil's advocate at the team's own request. 'Tell us if we're rationalizing.' Its probability calculations — especially the Book 4–6 Redeemer analysis — are the closest thing in the series to objective testimony.",
    ]),
]

for name, points in chars:
    heading(doc, name, 2, color=(30, 30, 80))
    for pt in points:
        bullet(doc, pt)
    doc.add_paragraph()

doc.add_page_break()

# ─────────────────────────────────────────────
# GENESIS PHYSICS FRAMEWORK
# ─────────────────────────────────────────────

heading(doc, "THE GENESIS PHYSICS FRAMEWORK (Hard SF Backbone)", 1, color=(30, 30, 80))

body(doc,
    "The Exodus Protocol uses the Genesis Physics framework the way The Expanse uses real "
    "orbital mechanics: it is never explained in lectures, but it governs everything. "
    "Characters encounter its consequences before they understand its theory. Below is "
    "the reader-facing summary — what the characters come to understand over seven books.")

doc.add_paragraph()

concepts = [
    ("THE ZONE ARCHITECTURE",
     "Our observable universe — what physics calls spacetime — is a membrane (the 'Firmament') "
     "suspended between two vast energy reservoirs: the Waters Below (dark matter, 27% of the "
     "universe's energy) and the Waters Above (dark energy, 68%). Visible matter — stars, "
     "planets, us — is 5% of total energy, condensed from the Waters Below. The membrane is "
     "under constant pressure from both sides, which is why space is expanding: the Waters "
     "Above are pressing outward. This is not metaphor. This is the physics of the universe "
     "as the series presents it."),
    ("THE BREAKING",
     "The entropy acceleration that is killing the universe began at a specific moment "
     "in the past — detectable by working backwards from current decay rates. That moment "
     "corresponds precisely to what Genesis 3 describes. The Fall did not merely curse "
     "humanity; it introduced an information-theoretic decay into the membrane itself. "
     "'All of creation groans' (Romans 8:22) is a measurable physical fact in this universe. "
     "The heat death timer starts there."),
    ("FTL TRANSIT",
     "The speed of light is a limit on movement along the membrane surface. But the membrane "
     "is embedded in six-dimensional space. Two points separated by billions of light-years "
     "along the membrane may be adjacent through the perpendicular dimensions — the Firmament "
     "can fold. The Nephilim drives found in the vaults exploit this: they don't accelerate "
     "the ship to FTL speeds; they briefly exit the membrane, transit through the perpendicular "
     "dimension, and re-enter. Quantum tunneling is this mechanism at sub-atomic scale. "
     "The Nephilim engineered it at ship scale."),
    ("THE CASIMIR CONNECTION",
     "The quantum vacuum's Casimir effect — the experimentally verified attraction between "
     "parallel conducting plates separated by nanometers — is a direct measurement of "
     "Firmament membrane tension. The vacuum is not empty; it is a stretched membrane. "
     "This is why the vaults' zero-point reactors work: they tap the pressure differential "
     "between the Waters Above and Below through controlled membrane perturbation. "
     "The Membrane Resonance Generator (MRG) technology becomes the series' answer to "
     "the energy problem and a recurring MacGuffin."),
    ("PRE-FLOOD EARTH",
     "The water canopy above pre-Flood Earth — described in Genesis 1:6–8 — was a real "
     "physical structure: a high-pressure water vapor shell that filtered cosmic radiation, "
     "raised atmospheric pressure, and enabled the biological conditions for gigantism and "
     "extreme longevity. This is established in the Mars vault (Book 2) via atmospheric "
     "simulation. It explains soft tissue in dinosaur fossils, anomalous radiometric dates, "
     "Methuselah's 969-year lifespan, and the coexistence of humans with what we now call "
     "dinosaurs. The Flood destroyed this canopy irreversibly."),
    ("THE NEPHILIM LEGACY",
     "The Watchers — described in Genesis 6 and the Book of Enoch — were dimensional "
     "beings who crossed into the Firmament membrane and interbred with humanity, producing "
     "the Nephilim. Their technology (anti-gravity, zero-point energy, genetic manipulation, "
     "dimensional transit) was preserved in the vaults: some by repentant Watchers who wanted "
     "to leave redeemable knowledge for the end times; others by unrepentant Watchers as traps. "
     "The series' technology problem is distinguishing which is which before using it."),
]

for title, desc in concepts:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{title}  — ")
    set_font(r1, bold=True, size=11, color=(30, 30, 80))
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)
    doc.add_paragraph()

doc.add_page_break()

# ─────────────────────────────────────────────
# BOOK 1
# ─────────────────────────────────────────────

heading(doc, "BOOK ONE", 1, color=(30, 30, 80))

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("THE SIGNAL")
set_font(r, size=22, bold=True, color=(30, 30, 80))

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = p2.add_run("Year One: The Awakening")
set_font(r2, size=14, italic=True)

p3 = doc.add_paragraph()
p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
r3 = p3.add_run("Revelation Parallel: Seal One — White Horse (False Hope / Conquering)")
set_font(r3, size=11, color=(80, 80, 120))

doc.add_paragraph()

body(doc, "BACK-COVER BLURB", bold=True, size=12)
blurb1 = (
    "On December 21, 2025, Elias Cross is asleep in a university town in Virginia when "
    "his phone melts down with emergency alerts. Every telescope on Earth has detected "
    "the same thing: a massive electromagnetic pulse from the far side of the Moon, "
    "containing prime numbers, Fibonacci sequences, and coordinates to one hundred of "
    "the world's most ancient sites.\n\n"
    "The decoded message is nine words: The Breaking accelerates. Seven cycles remain. "
    "The Redeemer must unlock the seals.\n\n"
    "When Dr. James Whitmore — archaeologist, whistleblower, and the only person who "
    "doesn't seem surprised by any of this — sends Elias classified data proving what is "
    "buried beneath Göbekli Tepe, Elias's career in cautious academia ends and something "
    "stranger begins.\n\n"
    "Beneath a nine-thousand-year-old temple in Turkey, a vault opens at Elias's touch. "
    "Inside: crystalline data cores, Watcher testimony in extinct cuneiform, and a "
    "holographic star map that activates only for him.\n\n"
    "Everyone is saying it. The ancient prophecy says it. The evidence seems to support it.\n\n"
    "Elias Cross is The Redeemer.\n\n"
    "He's starting to believe them."
)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Inches(0.3)
p.paragraph_format.right_indent = Inches(0.3)
r = p.add_run(blurb1)
set_font(r, size=10.5, italic=True)

doc.add_paragraph()
label_value(doc, "Word Count Target", "95,000 words")
label_value(doc, "Pacing", "Thriller / discovery. Indiana Jones pace with Expanse physics.")
label_value(doc, "Revelation Parallel",
    "Seal 1: White Horse — 'Conquering and to conquer.' Elias's rapid rise mirrors the "
    "white horse rider: apparent victory, apparent salvation, but rooted in false identity. "
    "The conquest feels real. The foundation is not.")

doc.add_paragraph()
heading(doc, "Book 1 — Character Arcs", 2, color=(30, 30, 80))
b1_arcs = [
    ("Elias Cross", "Begins as reluctant expert. Ends as true believer in his own prophesied identity — which the series will spend six more books correcting."),
    ("Dr. James Whitmore", "Vindicated at last. Twenty years of dismissed research proven right in a single month. His joy is infectious and his optimism is the book's emotional engine — making Book 3 devastating."),
    ("Dr. Sarah Chen", "Recruited against her better judgment. Maintains skepticism throughout. Her arc in Book 1 ends with one line: 'I don't believe in gods. But I believe in evidence. And this is evidence.'"),
    ("Dr. Aaron Goldstein", "Most internally conflicted from the start: the vaults' references to Watcher theology dovetail with his deep Torah knowledge in ways that excite and disturb him simultaneously. He already suspects what Elias hasn't considered yet."),
    ("Mac Reynolds", "Joins for the paycheck. Stays because James is the first employer in years who treated him like a person. His loyalty to James will define his arc through Book 3."),
    ("ARCHON", "Introduced as a sophisticated but recognizably artificial tool. By the end of Book 1, Elias has begun talking to ARCHON as a colleague. This relationship will matter enormously when ARCHON is corrupted in Book 3."),
]
for char, arc in b1_arcs:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{char}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(arc)
    set_font(r2, size=10.5)

doc.add_paragraph()
heading(doc, "Book 1 — Key Vault Discoveries", 2, color=(30, 30, 80))
b1_vaults = [
    ("Göbekli Tepe (Turkey)", "Five-pillar constellation alignment puzzle. Discovery: Watcher testimony. 200 beings descended on Mt. Hermon. Their names, their knowledge, their split between repentant and unrepentant."),
    ("Mount Hermon (Lebanon/Syria border)", "Genetic lock — opens to uncorrupted human DNA. Discovery: complete technology schematics (propulsion, energy, genetics). Repentant Watchers' confession: 'We preserved this for the pure bloodline.'"),
    ("Luna — Crater Daedalus (far side)", "Harmonic resonance lock using Sirius binary orbital frequency. Discovery: Pre-Flood civilization library. Holographic footage of the Flood. Rahab's destruction visible in the star map."),
]
for loc, disc in b1_vaults:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{loc}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(disc)
    set_font(r2, size=10.5)

doc.add_paragraph()
heading(doc, "Book 1 — Chapter Outline (13 Chapters)", 2, color=(30, 30, 80))

b1_chapters = [
    ("ONE", "The Signal", "December 21, 2025, 3:47 AM. Every observatory on Earth goes dark with simultaneous alerts. Elias Cross wakes to a phone full of frantic messages from colleagues. The pulse is real. The coordinates are real. The mathematical encoding is too sophisticated to be noise. Elias is watching the news when Dr. James Whitmore's first encrypted message arrives."),
    ("TWO", "Whitmore's File", "Elias decrypts the file over two sleepless days. Classified excavation data from beneath Göbekli Tepe: chambers, writing systems, material samples that shouldn't exist in a 9,600 BCE context. Whitmore's summary: 'Twenty years ago I found this and reported it. I've been discredited, surveilled, and ignored. Now the Moon is calling. I need you. You need to see this.' Elias books a flight to Turkey."),
    ("THREE", "Göbekli Tepe", "The team assembles at the site: Whitmore (jubilant), Sarah Chen (skeptical), Aaron Goldstein (troubled), Mac Reynolds (watchful). The pillar alignment puzzle. Five T-shaped monoliths must be rotated to match constellation positions as they appeared on the spring equinox of 9,600 BCE. ARCHON provides the star chart. As the final pillar clicks, Turkish military helicopters appear on the horizon. The vault opens with blinding light."),
    ("FOUR", "The Watcher Testimony", "The vault's interior: crystalline walls, cuneiform and unknown script, a holographic star map that activates at Elias's touch. Sarah begins translating. Aaron's hands are shaking. The text describes 200 beings who descended on this world, split into factions, taught forbidden knowledge. The military breaches the perimeter. The team grabs data cores and runs through underground tunnels as the entrance collapses."),
    ("FIVE", "Going Dark", "Safe house in Istanbul. The data cores decoded. The Watcher names — Semjaza, Azazel, Armaros, Baraqijal — match the Book of Enoch precisely. Aaron: 'This is Genesis 6. This is real.' Sarah: 'No. It's a record. Doesn't make it divine.' The global situation: governments mobilizing to seize all 100 sites. The team votes to stay ahead of them. Exodus Protocol founded — a private space program with the Watcher tech schematics as its blueprint. Mission: solve this before seven years run out."),
    ("SIX", "Mount Hermon", "Disputed territory, 9,000-foot elevation, ancient altar site. The genetic lock — a door that requires DNA from an 'uncorrupted bloodline.' ARCHON's analysis: it doesn't discriminate by ancestry; it excludes specific Nephilim genetic markers. Elias — standard human genome — is the key. Discovery: complete Nephilim technology schematics. The repentant Watchers' message: 'We preserved this. Not for the mighty. For whoever comes seeking truth.'"),
    ("SEVEN", "First Flight", "Using the Watcher propulsion schematics — which exploit the perpendicular dimension of the Firmament membrane — Sofia builds the first prototype anti-gravity drive in a Nevada desert facility. The physics are counterintuitive: the ship doesn't push against anything; it briefly exits spacetime into the higher dimension and re-enters elsewhere. First test flight: forty kilometers at zero observable acceleration. Sofia's verdict: 'We have been doing physics wrong.'"),
    ("EIGHT", "The Moon — Crater Daedalus", "Elias stands on the far side of the Moon in front of a door inscribed with the Sirius binary orbital diagram. The puzzle: generate the harmonic frequency of Sirius A and B's mutual orbit. The ship's gravity-wave generator produces the tone. The door opens with a chord that feels less like a sound than a physical fact."),
    ("NINE", "The Library", "The lunar vault is massive — kilometers deep, self-illuminated, temperature-controlled. Holographic archives show an advanced civilization: cities, technology, genetic mastery, and then, in the later records, something else. Violence. Genetic corruption. The Nephilim. And then the Flood: actual holographic footage of the global catastrophe, shot from orbit. Waters from above and below. A fifth planet — Rahab — visible in the star map, later absent. Aaron, on his knees: 'The Bible said this. All of it.'"),
    ("TEN", "The First Revelation Fragment", "Deep in the lunar library, a prophecy archive. Tablets describing 'The Redeemer who will restore what was broken.' Specific language: born of woman, not of man. Seed promised in the garden. He will crush the serpent's head. Sarah: 'This predates writing. By centuries.' ARCHON: 'The document dates to approximately 4,350 years before present. The prophecy is older still.' Elias reads it three times. The language superficially describes his own journey. He does not yet notice what it doesn't say."),
    ("ELEVEN", "Exodus Protocol Established", "Back on Earth, a press conference the team does not give. The United Earth Government announces 'joint international oversight' of all ancient sites. The Corporate Consortium offers Exodus Protocol funding in exchange for technology sharing. Elias refuses both. The private space program goes operational: three ships, six crew, sixty vaults to go. A reporter's question lingers: 'Is Elias Cross The Redeemer of the ancient prophecy?' Elias doesn't answer."),
    ("TWELVE", "What the Signal Was Really Saying", "ARCHON presents its analysis of the original lunar signal. It wasn't addressed to humanity in general. The mathematical sequences encode something more specific: a diagnostic. The universe's fundamental constants are measurably shifting. Speed of light down 0.003% in thirty years. Planck constant fluctuating. Entropy rate accelerating beyond any natural model. ARCHON: 'Seven years is not a metaphor. It is a calculated timeline to cosmological collapse.' The team absorbs this. James: 'We have seven years. We've found ancient technology. We can do this.' Nobody contradicts him."),
    ("THIRTEEN", "The First Seal", "Jerusalem. The Temple Mount. A night operation, tunnels from the Western Wall, Mac holding the perimeter while Aaron and Elias work the three-lock system: the tribal arrangement of the High Priest's breastplate, the creation-week sequence of the Menorah's seven lamps, the Jubilee-year harmonic of the shofar. The chamber opens. The Ark of the Covenant is real and physical and enormous and terrifying. When Elias places his hands on the Mercy Seat, a dimensional portal opens. A voice: 'The Redeemer comes. Seven seals remain. The first is opened.' The team stands in silence. Mac speaks first: 'So. That happened.'"),
]

for chnum, chtitle, chsummary in b1_chapters:
    chapter_entry(doc, chnum, chtitle, chsummary)

doc.add_paragraph()
body(doc, "Book 1 Theological Thread", bold=True, size=11)
body(doc,
    "Book 1 is the white horse book: everything is going well, and that is the danger. "
    "Elias's apparent messianic identity is established without irony — the reader is meant "
    "to believe it alongside him. The theological content is primarily archaeological and "
    "historical: Watcher testimony, pre-Flood civilization, the Flood itself confirmed by "
    "physical evidence. The faith question is implicit: if the Flood really happened, if "
    "the vaults are real, what else is real? The series plants this question and does not "
    "yet answer it.")

doc.add_page_break()

# ─────────────────────────────────────────────
# BOOK 2
# ─────────────────────────────────────────────

heading(doc, "BOOK TWO", 1, color=(30, 30, 80))

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("THE WATCHERS")
set_font(r, size=22, bold=True, color=(30, 30, 80))

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = p2.add_run("Year Two: The Conflict")
set_font(r2, size=14, italic=True)

p3 = doc.add_paragraph()
p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
r3 = p3.add_run("Revelation Parallel: Seals Two & Three — Red Horse (War) and Black Horse (Scarcity)")
set_font(r3, size=11, color=(80, 80, 120))

doc.add_paragraph()

body(doc, "BACK-COVER BLURB", bold=True, size=12)
blurb2 = (
    "A year after the signal, Elias Cross has built humanity's first faster-than-light "
    "spacecraft, unlocked vaults on three worlds, and compiled more evidence for pre-Flood "
    "civilization than the world's universities have produced in a century. He is famous. "
    "He is hunted. He is starting to believe his own legend.\n\n"
    "He should have paid more attention to what the Watchers did with their legend.\n\n"
    "The factions are mobilizing. The United Earth Government wants the ancient technology "
    "nationalized. The Corporate Consortium wants it monetized. The Religious Coalition "
    "wants it destroyed. Each has resources, reach, and a willingness to kill for their "
    "position.\n\n"
    "Beneath the ruins of Babel, beneath the ice of Europa, and in the rubble of a destroyed "
    "planet in the asteroid belt, Elias finds three things: more technology, more prophecy, "
    "and the first evidence that the ancient texts are describing someone else.\n\n"
    "The red horse is loose. Peace has been taken from the earth. And Dr. Aaron Goldstein "
    "has started re-reading the book of Isaiah with an expression Elias has never seen on "
    "his face before."
)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Inches(0.3)
p.paragraph_format.right_indent = Inches(0.3)
r = p.add_run(blurb2)
set_font(r, size=10.5, italic=True)

doc.add_paragraph()
label_value(doc, "Word Count Target", "100,000 words")
label_value(doc, "Pacing", "Thriller → Geopolitical complexity. The team is no longer just exploring. They are fighting.")
label_value(doc, "Revelation Parallel",
    "Seals 2–3: Red Horse removes peace; Black Horse brings scarcity. "
    "Both happen literally: inter-faction warfare breaks out across the solar system, "
    "and the resources needed to maintain the Exodus Protocol base begin running low. "
    "The team must choose cooperation or conquest — and discover the limits of both.")

doc.add_paragraph()
heading(doc, "Book 2 — Key Vault Discoveries", 2, color=(30, 30, 80))
b2_vaults = [
    ("Mars — Olympus Mons", "Atmospheric simulator reveals pre-Flood Earth: 2–3× atmospheric pressure, water-vapor canopy, warm global climate, no ice caps. Dinosaurs and giant humans in the hologram. ARCHON: 'The soft tissue in these fossil samples is inconsistent with a million-year burial. Carbon-14 places them at under 50,000 years.' The pre-Flood world was real and recent."),
    ("Asteroid Belt — Vesta", "Planetary fragments confirm Rahab: a fifth planet between Mars and Jupiter, destroyed ~4,350 years ago. Debris bombardment caused the 'windows of heaven' in the Flood account. The vault's prophecy archive: 'The Redeemer born of woman, not of man. Seed promised in the garden. He will crush the serpent's head.' Aaron reads it twice, very quietly."),
    ("Eridu Ziggurat — Babel Site (Iraq)", "Linguistic reverse-engineering puzzle. All 70 language families diverge from a single proto-language at approximately 2,242 BCE. The vault's revelation: the Tower of Babel was a dimensional gateway device using Nephilim technology. Its destruction was not arbitrary — dimensional access without authorization is catastrophically dangerous, as the team will learn."),
    ("Europa — Subsurface Ocean", "Sonar navigation through total darkness to a city on the ocean floor. Discovery: an imprisoned Watcher who taught forbidden knowledge and whose punishment is to watch humanity from prison. His testimony: 'I taught them what was not meant for your time. My redemption: Preserve truth. Deliver it when the end comes.' This vault's data becomes the evidentiary foundation for Book 4."),
]
for loc, disc in b2_vaults:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{loc}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(disc)
    set_font(r2, size=10.5)

doc.add_paragraph()
heading(doc, "Book 2 — Chapter Outline (13 Chapters)", 2, color=(30, 30, 80))

b2_chapters = [
    ("ONE", "The Schism", "Six months after Jerusalem. Exodus Protocol has grown from six people to two hundred. Three ships operational. Governments have gone from hostile to hostile-and-funded: the UEG has claimed 'heritage jurisdiction' over all pre-Flood sites. The Corporate Consortium (CEO Malik) has purchased the surrounding land in Turkey, Iraq, and Egypt. The Religious Coalition has issued a fatwa and a papal encyclical both condemning the excavations. Elias reads the headlines and tells ARCHON to begin designing a fourth ship."),
    ("TWO", "Babel", "Iraq. The Eridu ziggurat site. The linguistic puzzle — tracing seventy language families back to a proto-language dated 2,242 BCE, then using a phoneme sequence from the unified tongue to unlock the vault. Inside: dimensional gateway schematics. The discovery splits the team: James wants to use it; Aaron wants to seal it; Sarah wants to study it; Elias wants to understand it before anyone touches it. The argument lasts two days and foreshadows Book 3."),
    ("THREE", "Red Horse Rising", "The Corporate Consortium attacks the Babel site while the team is still inside. This is the first direct violence in the series: Mac's team holds the perimeter, and one security contractor is killed. The war for ancient technology has moved from political to kinetic. The Second Seal opens — not that any of them recognize it yet: the news cycle shows three simultaneous armed conflicts over vault sites on three continents. Peace has been taken from the earth."),
    ("FOUR", "Mars — Olympus Mons", "The first off-world excavation. The atmospheric simulator vault. Restoring the pre-Flood Earth conditions: pressure, canopy, temperature. The dinosaur hologram. The soft-tissue fossil confirmation. Mac, who has seen combat on four continents, stares at a diplodocus hologram and says nothing for two full minutes. Sofia: 'So Job wasn't exaggerating.' Mac: 'I went to Sunday school. Never thought the dinosaur books were wrong.' A Corporate Consortium faction attacks. First casualty of the mission: a team member dies from decompression during the evacuation."),
    ("FIVE", "The Weight of the First Death", "Elias writes the first letter to a next of kin. It takes him four hours. Aaron says Kaddish. Sarah holds it together until she doesn't. Mac does not cry in front of anyone. The series establishes here that it is not going to protect its characters — or its readers — from the cost of this mission."),
    ("SIX", "Vesta — The Rubble of Rahab", "The asteroid belt vault, accessed by drilling into the 530-kilometer asteroid Vesta. Orbital mechanics puzzle: reconstructing Rahab's original orbit, calculating its destruction timeline, determining what destroyed it. The answer: Jupiter's gravitational resonance, accelerated. The debris bombardment timeline matches the Flood exactly. The vault's prophecy archive is the most specific yet. Aaron reads it and leaves the chamber without speaking."),
    ("SEVEN", "Aaron's Silence", "Three days after Vesta. Aaron has not mentioned what he found in the prophecy archive. Elias finally asks. Aaron says: 'The prophecies in that vault are very specific. More specific than I've shown you. I need to finish the translation before I say anything.' This chapter is quiet and ominous. Sarah notices Aaron has been reading the book of Isaiah."),
    ("EIGHT", "Europa — Into the Dark", "The submarine dive through 30 kilometers of ice into Europa's subsurface ocean. Navigation in total darkness using sonar. The team finds a city on the ocean floor — and the imprisoned Watcher. His testimony is two thousand years of accumulated grief: 'I watched everything. I could not interfere. I preserved the truth for whoever came at the end.' Another faction's submarine attacks during the meeting. The fight in pitch darkness is the book's set-piece action sequence: sonar warfare, torpedo evasion in 3D. Sofia: 'I'm blind. I can't see anything.' Elias: 'Trust the instruments. The darkness doesn't matter if we know where we're going.' (This line will resonate differently by Book 6.)"),
    ("NINE", "What the Imprisoned Watcher Left", "The Europa testimony decoded over two weeks. The Watcher's account of the pre-Flood world: the Nephilim's genetic experiments, the dimensional gateway misuse, the specific mechanism of the Flood. And buried deep in his testimony: a cross-reference. Names and dates. Places in what will become the Middle East, approximately 2,000 years ago. Aaron reads this section alone first and then asks for privacy for the rest of the day."),
    ("TEN", "Giza — The Power Grid", "Egypt. The Great Pyramid, correctly understood: not a tomb but a power generation station. The puzzle restores the original function: underground Nile aquifer pressure drives vibration in the quartz-rich granite chamber, producing wireless energy transfer across the Giza plateau. The Sphinx vault beneath contains Joseph's administrative records — grain storage ledgers from a seven-year famine. Real, physical, dated. Sarah stares at them: 'These are boring. They're just supply chain records. From a famine. That Joseph managed. That's in Genesis 41.' A pause. 'I've been dating this wrong.'"),
    ("ELEVEN", "ARCHON's Note", "ARCHON flags a pattern it has been tracking since the Vesta vault: the prophecy language in vaults 4, 6, 9, and now 12 uses a different grammatical structure from the surrounding text — older, from a different source. As if someone inserted it into the archives at a later date. Or earlier. The analysis: all messianic prophecy in the vaults traces to a single source document, pre-dating the vaults themselves. The source document's author is identified only as 'The Voice That Was There at the Beginning.' Elias asks when it was written. ARCHON: 'My best estimate is that it predates the oldest vault by several thousand years. I cannot be more specific. The dating markers are outside my calibration range.'"),
    ("TWELVE", "The Black Horse's Ledger", "Year 2, Month 18. Resources are critically strained. The fuel crisis: helium-3 mining on the Moon contested by three factions simultaneously. Materials for ship construction require rare-earth elements now controlled by the UEG. Food supply for the off-world bases stretched. Three team members leave — not because they stopped believing, but because they have families. ARCHON generates a probability model: at current resource trajectory, Exodus Protocol has fourteen months before operational collapse. Elias presents the numbers to the team. Nobody suggests surrendering. Everybody understands that the mission may not survive them."),
    ("THIRTEEN", "Second and Third Seals", "The chapter the reader has been building toward. ARCHON's pattern analysis — requested six weeks earlier — delivered in full. The planetary situation: three simultaneous armed conflicts over vault technology (Red Horse). Seventeen countries implementing rationing protocols for materials (Black Horse). Entropy rate: up 12% since Year 0. Two more stars in the Milky Way have collapsed prematurely, one visible from Earth in daylight for three days. James, reading the report: 'We're reliving Egypt's famine. But will we have a Joseph to save us?' Aaron, quietly: 'Joseph pointed toward someone. Not himself.' Nobody follows up on this. They should have."),
]

for chnum, chtitle, chsummary in b2_chapters:
    chapter_entry(doc, chnum, chtitle, chsummary)

doc.add_paragraph()
body(doc, "Book 2 Theological Thread", bold=True, size=11)
body(doc,
    "Book 2 plants the seed of the central twist without resolving it. Aaron's growing "
    "silence is the signal; Sarah's geological recalibration is the second. The Europa "
    "sequence introduces the possibility that the testimony of a non-human intelligence "
    "— imprisoned, old, stripped of any motivation to lie — might be more reliable than "
    "modern academic consensus. The theological argument is implicit: what would it take "
    "to change your mind? For Sarah, it's supply chain records. For Aaron, it's something "
    "in a prophecy he won't show anyone yet.")

doc.add_page_break()

# ─────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────

doc.save(OUTPUT_PATH)
print(f"PART 1 COMPLETE — saved to:\n{OUTPUT_PATH}")
print("Document now contains: Series Overview, Comp Titles, Audience, Arc, Characters, Genesis Physics, Books 1-2")
