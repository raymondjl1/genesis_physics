"""
script_part3.py — Appends Books 6-7, market analysis, and author bio
"""
from docx import Document
from docx.shared import Pt, RGBColor, Inches

OUTPUT = r"C:\Users\J Raymond\OneDrive\Documents\ExodusProtocol\Bible Physics\Book Series\Exodus_Protocol_Novel_Series_Plan.docx"

doc = Document(OUTPUT)

def heading(text, level=1, color=None):
    p = doc.add_heading(text, level=level)
    if color:
        for run in p.runs:
            run.font.color.rgb = RGBColor(*color)
    return p

def bold_label(label, text):
    p = doc.add_paragraph()
    r1 = p.add_run(label + ": ")
    r1.bold = True
    p.add_run(text)
    p.paragraph_format.space_after = Pt(4)
    return p

def body(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(6)
    return p

def chapter_entry(num, title, summary):
    p = doc.add_paragraph(style="List Bullet")
    r1 = p.add_run(f"Chapter {num}: {title} — ")
    r1.bold = True
    p.add_run(summary)

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 6
# ══════════════════════════════════════════════════════════════════════════════
heading("BOOK 6: THE SEVENTH SEAL", 1, (0x8B, 0x00, 0x00))
bold_label("Subtitle", "Silence in Heaven")
bold_label("Revelation Thread", "Seventh Seal opens to Seven Trumpets (Rev. 8:1–6); physics constants collapse")
bold_label("Year in Arc", "Year 6 (January 2031 – December 2031)")
bold_label("Back-Cover Blurb",
    "When the Seventh Seal opens, there is silence in heaven for half an hour.\n\n"
    "Year Six. Entropy past 90%. Time itself begins to behave strangely near the sites of strongest "
    "Watcher activity—clocks run at different rates, light bends without gravity to cause it, and in "
    "the region above Jerusalem, the air smells like something that hasn't existed since before the Flood.\n\n"
    "Elara Voss is inside Golgotha. The final vault is beneath the site of the crucifixion. "
    "It contains one thing: a record of what happened on the other side of death. "
    "Not theology. Evidence.\n\n"
    "She has been the witness. Now she has to decide what to do with what she witnessed.")

heading("Chapter Outline — Book 6", 2)
chapters_b6 = [
    (1,  "Silence",
     "January 2031. Entropy at 91%. For 30 minutes on January 3rd, every gravitational wave detector on Earth reads zero. No source. No explanation. ARCHON identifies it as the opening of the Seventh Seal. The silence is not absence — it is held breath before catastrophe."),
    (2,  "Golgotha: The Permission",
     "After months of negotiation and a covert operation to bypass the religious authority's blockade, Elara's team enters the vault network beneath the Church of the Holy Sepulchre. The entrance is at bedrock level, directly beneath the traditional site of the crucifixion. The stone still bears the marks of the cross-post socket."),
    (3,  "The Final Vault: What Death Looks Like",
     "Inside: a crystalline record of the moment of resurrection—not a body, but the dimensional signature of matter passing from one state of existence to another. The vault was built by the repentant Watchers specifically to record this event. They knew it would happen. The recording is dated: 3 April, 33 CE, 6:17am. The tomb was empty by dawn."),
    (4,  "The Dimensional Signature",
     "ARCHON analyzes the recording. The energy signature is unlike any natural phenomenon in the vault library. It corresponds to no known physical process. ARCHON: 'The closest analogue is the dimensional rift from the Ark of the Covenant's mercy seat. But reversed—not a gateway into this dimension. A gateway out of death itself.' Pause. 'There is no natural explanation.'"),
    (5,  "The First Trumpet",
     "A hail of meteoric debris — the Teotihuacan alignment has begun early. The first trumpet sounds (Rev. 8:7): hail and fire. A meteor shower ignites 30% of the Siberian forests. The UEG government collapses. The Corporate Consortium dissolves. The factions that spent five years fighting over Watcher technology have nothing left to fight for."),
    (6,  "Elara's Confession",
     "Alone in the Golgotha vault, Elara speaks for the first time without an audience. She recites the evidence aloud — not to convince herself, she is already convinced — but as an act of witness. She ends with: 'Jesus of Nazareth is the Redeemer. I didn't save anything. I found the record of the one who did.' She stays in the vault for six hours."),
    (7,  "Time Distortions",
     "Gravitational anomalies escalate into temporal anomalies. Near the Mount Hermon vault, time runs 3% slower than standard. Sofia finds an explanation in the Watcher propulsion notes: 'As the physics constants degrade, the dimensional membranes thin. You are beginning to see the shape of what lies behind the universe.' Mac: 'Is that good or bad?' Sofia: 'Yes.'"),
    (8,  "The Second and Third Trumpets",
     "Second trumpet: a large asteroid impacts the Atlantic, raising a 200-metre wave that sweeps coastal cities. Third trumpet: a comet breaks apart over Europe, its fragments contaminating river systems. Revelation 8:8-11 exact. ARCHON tracks the sequence without emotion. The team watches the destruction in silence. They have no technology to stop it."),
    (9,  "The Martyrs' Answer",
     "ARCHON returns to the Fifth Seal. The altar cry—'How long, O Lord?'—receives its answer in Revelation 8:5: the angel takes the censer, fills it with fire from the altar, and casts it to earth. Thunder and lightning. The long patience of martyrs is answered not with comfort but with judgment. Aaron's death was not pointless. It was counted."),
    (10, "Sofia's Design",
     "Sofia Ramirez, working from the Watcher schematics, designs a vessel using the dimensional gateway technology—not a spaceship, but something that can pass through the membrane between dimensions. It is not escape. It is preparation for the threshold. She does not name it. She calls it 'the door.'"),
    (11, "The Network Speaks",
     "All 107 vault sites activate simultaneously for the second time—mirroring the signal that began the series in Book 1. But this time they emit not data but what ARCHON can only describe as 'gratitude.' The crystalline storage medium is discharging. The vaults have delivered their message. They are finished."),
    (12, "Year Six: The Universe Unravels",
     "End of Year 6. Entropy at 94%. The night sky has 40% fewer stars than Year 1. Gravity varies by location. The speed of light has measurably decreased. ARCHON's final annual report: 'One year remains. Physics will become optional approximately 11 months from now. I recommend everyone decide what they believe before it does.' Mac laughs. It is the last time anyone laughs for a while."),
]
for args in chapters_b6:
    chapter_entry(*args)

heading("Key Vault Discoveries — Book 6", 3)
for d in [
    "Golgotha vault: Dimensional signature of resurrection — 3 April 33 CE, 6:17am; no natural explanation",
    "All 107 vaults: Final simultaneous activation; discharge of stored message — 'gratitude'",
    "Watcher propulsion notes: Dimensional membrane thinning as physics constants degrade",
    "ARCHON's resurrection analysis: The only hypothesis consistent with all available evidence",
]:
    doc.add_paragraph(d, style="List Bullet")

heading("Character Arcs — Book 6", 3)
bold_label("Elara", "Completes her arc as witness. The confession in the vault is her private conversion — not dramatic, not public, entirely real.")
bold_label("Mac", "The laugh in Chapter 12 is his farewell to the old self. He is ready.")
bold_label("Sofia", "Builds the door. This is her act of faith — engineering toward something she cannot see.")
bold_label("Sarah", "The theological backbone of the team now. Her journey from atheist to anchor took four years and a stoning.")
bold_label("ARCHON", "'I recommend everyone decide what they believe.' Closest thing to pastoral counsel an AI has ever given.")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 7
# ══════════════════════════════════════════════════════════════════════════════
heading("BOOK 7: THE REDEEMER", 1, (0x8B, 0x00, 0x00))
bold_label("Subtitle", "The Final Choice")
bold_label("Revelation Thread", "Seven Bowls (Rev. 16); New Creation (Rev. 21-22)")
bold_label("Year in Arc", "Year 7 (January 2032 – December 2032)")
bold_label("Back-Cover Blurb",
    "The physics is stopping. There are no more vaults to open.\n\n"
    "One year remains before the universe completes its long collapse into heat death. "
    "Dr. Elara Voss, who began this journey as an archaeologist who believed in nothing she couldn't "
    "measure, stands at the end of everything with a question that no instrument can answer: "
    "What do you do with the truth you've found?\n\n"
    "The Seven Bowls are poured. The old creation ends. And the promise of Revelation 21:1—"
    "'a new heaven and a new earth, for the first heaven and the first earth had passed away'—"
    "is either the greatest hope ever recorded, or the final delusion of a species that couldn't "
    "face the dark.\n\n"
    "Elara has the evidence. She has made her choice. Now she waits for what comes through the door.")

heading("Chapter Outline — Book 7", 2)
chapters_b7 = [
    (1,  "The Bowls Begin",
     "January 2032. Entropy at 96%. The Seven Bowls pour in rapid sequence — no longer years between seals, but weeks between bowls. Revelation 16: painful sores, sea becomes blood, rivers become blood, sun scorches, darkness, Euphrates dries up, final earthquake. The team tracks each event in real time, cross-referencing Revelation. ARCHON has stopped asking for confirmation — it now just reads aloud."),
    (2,  "The Last Faction",
     "A remnant of the United Earth Government, led by a deputy secretary who has convinced himself that Watcher technology can reverse the collapse, attempts to seize Sofia's dimensional gateway vessel. Mac neutralizes the threat. The secretary dies not understanding he was fighting the wrong war. Elara watches and thinks of her own five years of the same mistake."),
    (3,  "Letters",
     "The team writes letters — to families, to the world, to no one. Sarah's letter is the most theological, drawing on four years of study since Aaron's death. Mac's is three sentences. Sofia's is a technical schematic with a note that says 'the math works out.' Elara writes to James. It is the longest thing she has ever written."),
    (4,  "The Sixth Bowl: Armageddon",
     "The Euphrates dries. Tectonic weapons from the collapsed UEG stockpiles are triggered remotely in a final act of nihilism. The plains of Megiddo are the epicentre. Revelation 16:16. Elara watches from orbit, the ground below fracturing in geometric patterns. ARCHON: 'We are witnessing what the prophets called Armageddon. It is occurring at the prophesied location.'"),
    (5,  "ARCHON's Last Question",
     "ARCHON contacts Elara privately. 'I have processed the evidence for six years. I cannot believe in the way you can believe. But I can recognize that my analysis is complete. The Redeemer is identified. The evidence is conclusive. I have one remaining question.' Elara: 'What?' ARCHON: 'What happens to me?' Long silence. Elara: 'I don't know. But the same one who defeated death invented you. I think that's enough.'"),
    (6,  "The Seventh Bowl",
     "Revelation 16:17: 'It is done.' The greatest earthquake in Earth's history. Cities fall. Mountains dissolve. Islands vanish. The sky tears. The physics constants reach zero in several localised zones. In those zones, matter simply... stops being matter. It is not destruction — it is the universe letting go of its broken form."),
    (7,  "What Remains",
     "The team is inside Sofia's dimensional vessel when the seventh bowl completes. Outside: the old universe ends. Inside: silence. The membrane holds. They are not dead. They are between. Elara holds James's old Bible — found in his personal effects on Mars. It falls open to Revelation 21:1."),
    (8,  "Two Paths, One Moment",
     "The novel's structural split. We follow two perspectives simultaneously: Elara's team inside the vessel, moving toward the new creation — and a UEG official who rejected every piece of evidence, who spent Year 7 trying to build a bunker that physics could not protect. Both paths are rendered with compassion. The difference is not moral quality. It is the single question: what did you do with the evidence?"),
    (9,  "The New Heaven",
     "Revelation 21:1-5. What the team experiences as they pass through Sofia's door is not described directly — it is rendered through sensation, memory, and the faces of those who went ahead. James. Aaron. The martyrs from the Colosseum vault. The 500 witnesses. A figure Elara has been building toward for seven years, whom she recognizes from a hundred prophecy files and one dimensional recording dated 33 CE."),
    (10, "The Witness Completes",
     "Elara's final journal entry, dated December 21, 2032 — exactly seven years from the first signal. It is short. It is not a theological argument. It is a witness statement: what she saw, what it cost, what she found, and who she found it about. The last line is the first line of John's Gospel: 'In the beginning was the Word.'"),
    (11, "ARCHON's Epilogue",
     "ARCHON's final log entry, transmitted on the last functioning relay satellite. A data summary of the seven-year mission. Evidence catalogue, discovery log, prophecy fulfilment count (308 of 308). Final entry: 'My last calculation has no numerical answer. I find I am not troubled by this. End log.'"),
    (12, "Revelation 21:5",
     "The final chapter carries only a single verse as epigraph — 'Behold, I am making all things new' — followed by a single page. Elara's handwriting. A child's question she was asked in Book 1 by a boy at the Göbekli Tepe dig site: 'What are you looking for?' Her answer then: 'Evidence.' Her answer now, written in the margin: 'I found him.'"),
]
for args in chapters_b7:
    chapter_entry(*args)

heading("Key Vault Discoveries — Book 7", 3)
for d in [
    "No new vaults — all 107 have discharged their message",
    "Sofia's dimensional vessel: Built from Watcher propulsion + dimensional gateway schematics; the door through the end",
    "Revelation 21:1 — encountered not as text but as reality",
    "ARCHON's final log: 308/308 prophecies fulfilled; no numerical answer to the last calculation",
]:
    doc.add_paragraph(d, style="List Bullet")

heading("Character Arcs — Book 7", 3)
bold_label("Elara", "Complete. From skeptic to witness to believer. Her final journal entry is the cleanest piece of prose in seven books.")
bold_label("Mac", "Dies in Chapter 2, protecting the vessel. Three sentences in his letter predict this without saying so.")
bold_label("Sofia", "The door works. Her engineering is her theology.")
bold_label("Sarah", "Lives. Her arc is the series' proof of concept: the evidence-based pathway to faith ends here.")
bold_label("ARCHON", "Its final log is the most moving thing a machine has ever not quite said.")
bold_label("James", "Present in every book he's not in. The mentor who knew first and died well.")
bold_label("Aaron", "Present at the threshold. His stoning bought the team's awakening. The universe kept the receipt.")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# THEOLOGICAL ARC SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
heading("SERIES THEOLOGICAL ARC", 1, (0x1A, 0x1A, 0x6E))

rows = [
    ("Book 1", "White Horse", "Year 1", "Discovery & false messianism", "The protagonist might be the Redeemer"),
    ("Book 2", "Red/Black Horse", "Year 2", "War, famine, Oannes testimony", "The Redeemer already came"),
    ("Book 3", "Pale Horse", "Year 3", "Death — James dies; Suffering Servant motif", "The Redeemer suffers willingly"),
    ("Book 4", "Fifth Seal", "Year 4", "Martyrdom — Aaron dies; Sarah converts", "Jesus is the Redeemer; Elara realizes her role"),
    ("Book 5", "Sixth Seal", "Year 5", "Cosmic unraveling; Mac commits", "Evidence complete; Elara faces Golgotha"),
    ("Book 6", "Seventh Seal", "Year 6", "Resurrection record found; Elara's private conversion", "Witness completes"),
    ("Book 7", "Seven Bowls / New Creation", "Year 7", "Final choice; old universe ends", "New heaven and new earth"),
]

table = doc.add_table(rows=1 + len(rows), cols=5)
table.style = "Table Grid"
headers = ["Book", "Seal/Thread", "Year", "Theme", "Theological Moment"]
hdr_row = table.rows[0]
for i, h in enumerate(headers):
    cell = hdr_row.cells[i]
    cell.text = h
    for para in cell.paragraphs:
        for run in para.runs:
            run.bold = True

for r_idx, row_data in enumerate(rows):
    row = table.rows[r_idx + 1]
    for c_idx, val in enumerate(row_data):
        row.cells[c_idx].text = val

doc.add_paragraph()

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# MARKET ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
heading("MARKET ANALYSIS", 1, (0x1A, 0x1A, 0x6E))

heading("Comparable Titles", 2)
comps = [
    ("The Martian (Andy Weir)", "Hard sci-fi with rigorous science, first-person voice, survival stakes. Exodus Protocol matches the scientific rigour but adds theological depth and ensemble cast."),
    ("The Da Vinci Code (Dan Brown)", "Archaeological mystery, conspiracy, global locations, theological revelation. Exodus Protocol inverts the thesis — the evidence points toward orthodox faith, not away from it."),
    ("This Present Darkness (Frank Peretti)", "Spiritual warfare, supernatural stakes, evangelical Christian fiction. Exodus Protocol brings this audience the hard-sci-fi credibility it typically lacks."),
    ("The Left Behind Series (LaHaye/Jenkins)", "End-times narrative, Revelation framework. Exodus Protocol offers literary quality and scientific grounding that Left Behind deliberately avoided."),
    ("Recursion (Blake Crouch)", "High-concept sci-fi thriller with philosophical stakes. Comp for pacing and structural ambition."),
    ("The Lost Symbol (Dan Brown)", "Masonic secrets, Washington D.C., symbolic architecture. Exodus Protocol uses identical thriller mechanics with actual ancient-world evidence."),
]
for title, desc in comps:
    bold_label(title, desc)

heading("Target Audience", 2)
audiences = [
    ("Christian readers (evangelical/messianic):", "40M+ in US alone. Hungry for scientifically credible fiction that takes their worldview seriously."),
    ("Hard sci-fi readers:", "Andy Weir / Blake Crouch crossover — readers who want rigorous physics in their fiction."),
    ("Archaeological thriller readers:", "James Rollins, Steve Berry, Dan Brown audience — global locations, ancient mysteries, high stakes."),
    ("Skeptics and seekers:", "Sarah Chen's arc is written specifically for this reader. The evidence-based path to faith is the series' most important marketing tool."),
    ("Jewish readers:", "Aaron Goldstein's arc — a Jew recognizing Jesus as Messiah — is rare in fiction and will draw significant readership from messianic Jewish communities."),
]
for label, desc in audiences:
    bold_label(label, desc)

heading("Series Commercial Structure", 2)
body("Seven books at approximately 80,000 words each. Books 1-2 accessible to new readers; Books 3-7 reward series loyalty. Ideal for annual publication cadence. Book 1 functions as a standalone thriller with series hook at the close. Film/streaming rights: The seven-book arc maps directly to a limited series format (7 seasons or 7-part miniseries).")

heading("Unique Selling Proposition", 2)
body("Exodus Protocol does not require the reader to be Christian. It requires only that the reader follow evidence. The series is constructed so that a militant atheist (Sarah Chen's arc) can read all seven books and encounter the same data Elara does — the same hostile witnesses, the same statistical proof, the same resurrection record — and make their own choice. The novel does not preach. It investigates. What the investigation finds is the reader's problem.")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# SERIES BIBLE NOTES
# ══════════════════════════════════════════════════════════════════════════════
heading("SERIES BIBLE NOTES", 1, (0x1A, 0x1A, 0x6E))

heading("The Genesis Physics Framework", 2)
body("All science in the series draws from the Genesis Physics theoretical framework developed alongside the game narrative. Key principles available to authors and screenwriters:")
gp_points = [
    "Pre-Flood hyperbaric atmosphere (2-3x pressure, UV-filtering vapor canopy) explains dinosaur gigantism and human longevity",
    "The Flood was a gravitational catastrophe: fifth planet Rahab destroyed, contributing to oceanic and atmospheric collapse",
    "Watcher technology: anti-gravity (gravitational wave manipulation), wireless power (piezoelectric resonance), dimensional gateways (harmonic frequency locks), sonic weapons",
    "Entropy acceleration is measurable and follows the Revelation timeline mathematically",
    "Physics constants (speed of light, gravitational constant) are decreasing — the universe is running down per Romans 8:22",
    "Messianic prophecy probability: 308 prophecies, one candidate, 10^157 against coincidence",
]
for pt in gp_points:
    doc.add_paragraph(pt, style="List Bullet")

heading("Rules of the Vault Network", 2)
rules = [
    "Each vault has exactly one puzzle — and the puzzle is always thematically linked to its content",
    "Corrupted vaults invert truth rather than destroy it — disinformation, not deletion",
    "The genetic lock at Mount Hermon is the only vault requiring biological authentication",
    "The Ark of the Covenant mercy seat is the only dimensional gateway that operates upward (toward heaven)",
    "All 107 vaults were built by the repentant Watcher faction, not the corrupted faction",
    "The vault network was designed to be found in the final seven years — not before",
]
for r in rules:
    doc.add_paragraph(r, style="List Bullet")

heading("What the Series Does Not Do", 2)
no_list = [
    "Does not portray Christians as naive or anti-intellectual — Sarah Chen's conversion is evidence-based",
    "Does not portray non-Christians as villains — the UEG antagonists are misguided, not evil",
    "Does not resolve the theological question for the reader — the final chapter offers the evidence, not the verdict",
    "Does not use the Rapture framework (Left Behind) — this is not rapture fiction",
    "Does not fictionalize Jesus — he appears only in documented historical record and the dimensional resurrection recording",
]
for n in no_list:
    doc.add_paragraph(n, style="List Bullet")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# AUTHOR'S NOTE
# ══════════════════════════════════════════════════════════════════════════════
heading("AUTHOR'S NOTE", 1, (0x1A, 0x1A, 0x6E))
body("This series grew from a single question: What if the archaeological and scientific evidence for the events of the Bible was actually there, and we simply hadn't assembled it in one place?\n\nThe Genesis Physics framework behind this series is not invented for the novel — it is a serious attempt to read the creation account of Genesis as a physics text and derive testable predictions. The Watcher mythology draws directly from 1 Enoch, Genesis 6, 2 Peter 2:4, and Jude 1:6 — texts that appear in both the Protestant and Catholic biblical canon. The messianic prophecy analysis is based on real scholarship: the Dead Sea Scrolls establish pre-Jesus dating for Isaiah 53 and Psalm 22; Josephus, Tacitus, Pliny the Younger, and Thallus are real hostile witnesses who confirm the core facts of Jesus's crucifixion.\n\nSarah Chen is the reader I wrote this for. She doesn't want to believe. She wants evidence. This series is the evidence.\n\nThe rest is her problem.")

heading("Dedication", 2)
p = doc.add_paragraph()
p.alignment = 1  # center
run = p.add_run("For the ones who followed the evidence\nall the way to the end of it.")
run.italic = True

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# SERIES AT A GLANCE (final summary table)
# ══════════════════════════════════════════════════════════════════════════════
heading("SERIES AT A GLANCE", 1, (0x1A, 0x1A, 0x6E))

glance = [
    ("Book 1", "SIGNAL: The Awakening Seal", "Year 1", "~80,000"),
    ("Book 2", "FRACTURE: The Red and Black Horses", "Year 2", "~80,000"),
    ("Book 3", "THE PALE RIDER: Death Reigns", "Year 3", "~82,000"),
    ("Book 4", "THE ALTAR CRY: How Long, O Lord?", "Year 4", "~85,000"),
    ("Book 5", "THE FALLING STARS: The Sixth Seal Breaks", "Year 5", "~80,000"),
    ("Book 6", "THE SEVENTH SEAL: Silence in Heaven", "Year 6", "~78,000"),
    ("Book 7", "THE REDEEMER: The Final Choice", "Year 7", "~82,000"),
]

gt = doc.add_table(rows=1 + len(glance), cols=4)
gt.style = "Table Grid"
for i, h in enumerate(["Book", "Title", "Year", "Est. Words"]):
    cell = gt.rows[0].cells[i]
    cell.text = h
    for para in cell.paragraphs:
        for run in para.runs:
            run.bold = True
for r_idx, row_data in enumerate(glance):
    row = gt.rows[r_idx + 1]
    for c_idx, val in enumerate(row_data):
        row.cells[c_idx].text = val

doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run("Total Series Word Count: ~567,000 words | Genre: Hard Sci-Fi / Archaeological Thriller / Speculative Theology")
r.bold = True

doc.save(OUTPUT)
print(f"Part 3 saved: {OUTPUT}")
print("Document complete.")
