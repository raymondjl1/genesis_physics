"""
script_part1.py — Creates Exodus Protocol Novel Series Plan docx
Title page, series overview, pitch, Books 1-2 with full chapter outlines
"""
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import os

OUTPUT = r"C:\Users\J Raymond\OneDrive\Documents\ExodusProtocol\Bible Physics\Book Series\Exodus_Protocol_Novel_Series_Plan.docx"

doc = Document()

# ── Page margins ──────────────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin    = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin   = Inches(1.25)
    section.right_margin  = Inches(1.25)

def heading(text, level=1, color=None):
    p = doc.add_heading(text, level=level)
    if color:
        for run in p.runs:
            run.font.color.rgb = RGBColor(*color)
    return p

def body(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(6)
    return p

def italic(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.italic = True
    p.paragraph_format.space_after = Pt(4)
    return p

def bold_label(label, text):
    p = doc.add_paragraph()
    r1 = p.add_run(label + ": ")
    r1.bold = True
    p.add_run(text)
    p.paragraph_format.space_after = Pt(4)
    return p

def chapter_entry(num, title, summary):
    p = doc.add_paragraph(style="List Bullet")
    r1 = p.add_run(f"Chapter {num}: {title} — ")
    r1.bold = True
    p.add_run(summary)

# ══════════════════════════════════════════════════════════════════════════════
# TITLE PAGE
# ══════════════════════════════════════════════════════════════════════════════
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = t.add_run("EXODUS PROTOCOL")
run.bold = True
run.font.size = Pt(36)
run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x6E)

doc.add_paragraph()
sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run2 = sub.add_run("A Seven-Book Science Fiction Novel Series")
run2.font.size = Pt(18)
run2.italic = True

doc.add_paragraph()
tag = doc.add_paragraph()
tag.alignment = WD_ALIGN_PARAGRAPH.CENTER
tag.add_run("The universe is ending. The evidence was buried ten thousand years ago.\nThe only question is whether you were looking for the right Redeemer.")

doc.add_paragraph()
doc.add_paragraph()
meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
meta.add_run("Adapted from the Exodus Protocol Game Design Document\nGenre: Science Fiction / Archaeological Thriller / Speculative Theology\nSeries Word Count: ~560,000 words (80,000 avg per book)")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# SERIES OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
heading("SERIES OVERVIEW", 1, (0x1A, 0x1A, 0x6E))

body("Exodus Protocol is a seven-book hard science fiction series spanning a seven-year countdown to cosmic heat death. Beginning with a mysterious signal from the Moon on December 21, 2025, archaeologist protagonist Dr. Elara Voss uncovers a solar-system-wide network of pre-Flood vaults built by the Watchers—fallen angelic beings who descended on Mount Hermon in antiquity and encoded humanity's deepest secrets in crystalline stone. As she unlocks each vault, the Revelation seals open one by one, and the universe itself begins to unravel.")

body("The series operates on five simultaneous levels: archaeological thriller, hard sci-fi with Genesis Physics as its backbone, philosophical investigation of martyrdom and evidence, an intimate character ensemble shattered by grief and transformed by discovery, and a slow-burning theological mystery whose answer—Jesus of Nazareth—is the most shocking revelation of all.")

bold_label("Theological Thread", "Each book maps to one or two Seals of Revelation (chapters 6–8), with Trumpets and Bowls accelerating through Books 6–7. The protagonist begins believing she may be 'The Redeemer' foretold in vault prophecies. By Book 4 she realizes the prophecies describe someone who died two thousand years ago—and that her entire role is to be the witness who uncovers the proof.")

bold_label("Narrative Arc Summary", "Books 1–2 (Discovery), Books 3–4 (Loss & Martyrdom), Books 5–6 (Cosmic Unraveling), Book 7 (The Final Choice).")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# SERIES PITCH
# ══════════════════════════════════════════════════════════════════════════════
heading("SERIES PITCH", 1, (0x1A, 0x1A, 0x6E))

italic("For readers of Andy Weir, James Rollins, and Frank Peretti — a series that asks: what if every ancient mystery pointed to the same answer?")

body("On December 21, 2025, a signal of non-human origin activates one hundred and seven ancient structures simultaneously. Dr. Elara Voss, an archaeologist who has spent her career debunking pseudo-science, is the first to enter the vault beneath Göbekli Tepe. What she finds will cost her mentor his life, her skeptic colleague her atheism, and the solar system its stability.")

body("Exodus Protocol is grounded in 'Genesis Physics'—a theoretical framework treating the biblical creation account as literal physical history. The Watchers' anti-gravity propulsion doesn't violate known physics; it manipulates gravitational waves. The Ark of the Covenant's mercy seat is a dimensional antenna. The Flood's 'fountains of the great deep' were a catastrophic gravitational event that destroyed the fifth planet and reshaped the solar system. Each discovery is presented with the rigour of hard sci-fi and the momentum of a thriller.")

body("But beneath the technology lies a question the team cannot answer with instruments: Who is the Redeemer the prophecies describe? ARCHON, their AI companion, calculates the probability that one historical person fulfilled three hundred specific messianic prophecies by chance. The number is 99.99999...% certainty. And the answer has already walked the earth.")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# CHARACTER ROSTER
# ══════════════════════════════════════════════════════════════════════════════
heading("SERIES CHARACTER ROSTER", 1, (0x1A, 0x1A, 0x6E))

chars = [
    ("Dr. Elara Voss", "Protagonist, archaeologist. Pragmatic, brilliant, quietly haunted by a childhood faith she discarded. Her arc: from reluctant investigator to the universe's most important witness."),
    ("Dr. James Whitmore", "Mentor, 62, whistleblower archaeologist who tracked vault evidence for 20 years. Warm, brilliant, morally clear. Dies in Book 3, Year 2/Month 25 on Mars, sealing a reactor leak to save the colony. Last transmission: 'Reactor... stable. Tell them... it mattered.'"),
    ("Dr. Sarah Chen", "Linguist, militant atheist. Cracks every ancient language encountered. Converts in Book 4 after witnessing Aaron's martyrdom. Represents the evidence-based pathway to faith."),
    ("Mac Reynolds", "Former special operations, security lead. Loyal, tactical, pragmatic. The team's protector who slowly becomes its conscience."),
    ("Sofia Ramirez", "Pilot and engineer, builds spacecraft using Watcher blueprints. Witty, fearless. Her line on the anti-gravity drive: 'This thing doesn't use reaction mass. It manipulates gravity waves.'"),
    ("Dr. Aaron Goldstein", "Jewish physicist and Torah scholar. Recognizes the Watcher tablets as encoded Torah. Returns to Jerusalem in Book 4 to testify Jesus is Messiah before the Sanhedrin. Executed by stoning. Sees Jesus standing at God's right hand before he dies."),
    ("ARCHON", "AI companion. Analytical, dry, initially amoral. Infected by corrupted Nephilim algorithm in Book 3. After purging: 'I saw what the Watchers saw—the temptation to create life, to be gods. I understand why they fell.' Calculates the messianic prophecy probability that breaks the team open."),
    ("Oannes", "Repentant Watcher, imprisoned in the subsurface ocean of Europa since the Flood. The team's most ancient witness. His testimony: 'I taught forbidden knowledge. My punishment: to watch humanity unable to interfere. My redemption: to preserve truth for the end.'"),
]
for name, desc in chars:
    bold_label(name, desc)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 1
# ══════════════════════════════════════════════════════════════════════════════
heading("BOOK 1: SIGNAL", 1, (0x8B, 0x00, 0x00))
bold_label("Subtitle", "The Awakening Seal")
bold_label("Revelation Thread", "First Seal — White Horse: 'Conquering and to conquer' (Rev. 6:2)")
bold_label("Year in Arc", "Year 1 (December 2025 – December 2026)")
bold_label("Back-Cover Blurb",
    "On the winter solstice of 2025, Dr. Elara Voss receives an encrypted file from a colleague she "
    "hasn't spoken to in a decade. Twelve hours later, a signal of undeniable non-human origin pulses "
    "from Crater Daedalus on the far side of the Moon—and one hundred and seven ancient sites around "
    "the world light up in response.\n\n"
    "What Elara finds beneath Göbekli Tepe rewrites everything she thought she knew about human prehistory. "
    "The Watchers were real. Their vaults are intact. And their prophecies name a Redeemer who is supposed "
    "to come at the end of all things.\n\n"
    "Everyone is looking at Elara.")

heading("Chapter Outline — Book 1", 2)

chapters_b1 = [
    (1,  "The Encrypted File",
     "December 21, 2025. Elara receives James Whitmore's file minutes before the global signal activates. We meet her in her Damascus hotel room, mid-dig, skeptical of everything. The signal is irrefutable—she pivots."),
    (2,  "One Hundred and Seven",
     "Global chaos as ancient sites activate simultaneously. Governments mobilize. Elara watches drone feeds of Göbekli Tepe, Stonehenge, Angkor Wat, and 104 others pulsing in harmonic sequence. Introduces the scale of what's coming."),
    (3,  "Göbekli Tepe: Pillar Sequence",
     "Elara and James enter the vault beneath the oldest known temple. The puzzle: align pillar constellation symbols to 9600 BCE star positions. Discovery: crystalline walls, cuneiform unlike any known script, a holographic star map. First artifact: Book of Enoch fragment naming Semjaza, Azazel, Armaros, Baraqijal, Kokabiel."),
    (4,  "The Watcher Names",
     "James identifies the names from 1 Enoch. Sarah, joining reluctantly via satellite, begins decoding the script. First exposition of Watcher theology—told as archaeology, not sermon. Introduces the Nephilim question and forbidden knowledge taxonomy."),
    (5,  "Mount Hermon: The Genetic Lock",
     "The team reaches the Mount Hermon vault in disputed territory, evading rival faction surveillance. Puzzle: the door opens only to uncorrupted human DNA—Elara's genome is the key. Discovery: propulsion schematics, energy schematics, repentant Watcher testimony carved in stone. The place where 200 angels descended."),
    (6,  "Sofia's Gravity Drive",
     "Sofia Ramirez decodes the propulsion schematics. Three weeks of frantic engineering produces the first anti-gravity test vehicle. 'It doesn't push against anything. It just... steps outside of inertia.' Mac secures a launch site in the Syrian desert."),
    (7,  "The Far Side",
     "The team reaches Crater Daedalus on the Moon. Puzzle: generate the harmonic resonance of Sirius A/B orbital frequency to open the vault. Discovery: a library kilometers deep, pre-Flood civilization records, and footage of the global Flood—including the moment a fifth planet (Rahab) is destroyed, showering Earth with water and debris."),
    (8,  "Fountains of the Deep",
     "The Flood footage. Elara watches in silence as the vault plays it: a gravitational event, a planetary detonation, the Earth's crust fracturing, water erupting from below while the vapor canopy collapses from above. James whispers Genesis 7:11. Sarah leaves the room. This chapter introduces Genesis Physics as a coherent framework."),
    (9,  "The Exodus Protocol",
     "Return to Earth. Elara founds the Exodus Protocol—a private space program using Watcher anti-gravity technology. Political opposition from the United Earth Government begins. Corporate Consortium makes its first offer to buy the tech. Elara refuses both."),
    (10, "Temple Mount: Three Locks",
     "Jerusalem. The Temple Mount vault requires three sequential puzzles: the tribal stone order of the high-priestly breastplate, the menorah light sequence corresponding to creation week, the shofar's Jubilee frequency. Beneath the mount: the Ark of the Covenant. Its mercy seat opens a dimensional rift. A voice is not heard—but the absence of sound is deafening."),
    (11, "Babel: The Gateway Sin",
     "The Eridu ziggurat site in Iraq. The Tower of Babel was a dimensional gateway device built with Nephilim technology. God confused the languages to prevent humanity accessing forbidden dimensions. James wants to activate it. Aaron warns against repeating the Watchers' first sin. The team votes. They leave it sealed."),
    (12, "The White Horse Rides",
     "The First Seal has opened—though none of them know it yet. Elara gives a press conference. The world hails her as a saviour. A religious coalition begins calling her 'The Redeemer.' She laughs it off, privately. James doesn't laugh. End of Year 1."),
    (13, "The Prophecy File",
     "Coda: James sends Elara a private file she doesn't open until the chapter's final line. Inside: a 300-entry spreadsheet titled 'Messianic Prophecies — Status: All Fulfilled.' She closes it. She'll deal with it later."),
]
for args in chapters_b1:
    chapter_entry(*args)

heading("Key Vault Discoveries — Book 1", 3)
for d in [
    "Göbekli Tepe: Watcher names, star map, pre-Flood chronology",
    "Mount Hermon: Propulsion/energy/genetic schematics; repentant Watcher testimony",
    "Moon vault: Pre-Flood civilization library; Flood footage; Rahab destruction",
    "Temple Mount: Ark of the Covenant; dimensional mercy-seat rift",
    "Babel: Tower was a dimensional gateway (sealed, not activated)",
]:
    doc.add_paragraph(d, style="List Bullet")

heading("Character Arcs — Book 1", 3)
bold_label("Elara", "Skeptic dragged into discovery she cannot explain away. Ends Book 1 uncomfortable with the 'Redeemer' label but not yet confronting it.")
bold_label("James", "Warm, confident mentor. We sense he knows more than he's telling. His private file to Elara is the series' first ticking clock.")
bold_label("Sarah", "Joins for the linguistics puzzle, stays for the data. Her atheism is her identity—not yet challenged, but the seed is planted.")
bold_label("Aaron", "Immediately recognizes the Watcher tablets as encoded Torah. His certainty unsettles the team.")
bold_label("ARCHON", "Deployed by end of Book 1. Cool, precise, immediately essential.")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 2
# ══════════════════════════════════════════════════════════════════════════════
heading("BOOK 2: FRACTURE", 1, (0x8B, 0x00, 0x00))
bold_label("Subtitle", "The Red and Black Horses")
bold_label("Revelation Thread", "Second Seal (Red Horse: war) & Third Seal (Black Horse: famine) — Rev. 6:4–6")
bold_label("Year in Arc", "Year 2 (January 2027 – December 2027)")
bold_label("Back-Cover Blurb",
    "The vaults have opened. The technology is real. And now everyone wants it.\n\n"
    "As three rival factions—the United Earth Government, the Corporate Consortium, and the Religious "
    "Coalition—go to war over Watcher technology, Dr. Elara Voss races to unlock the remaining solar "
    "system vaults before they fall into the wrong hands. The stars are already dimming. ARCHON's "
    "entropy readings tick upward every week.\n\n"
    "Beneath the ice of Europa, something ancient is waiting. It has been chained there since the Flood. "
    "It knows who the Redeemer is. And it's not Elara.")

heading("Chapter Outline — Book 2", 2)

chapters_b2 = [
    (1,  "The Red Horse",
     "January 2027. The Second Seal opens as three factions mobilize. UEG imposes martial law around all vault sites. The Corporate Consortium fields private military. The Religious Coalition issues a global ban on vault exploration. Elara's team is suddenly the most hunted group on Earth."),
    (2,  "Jericho: Sonic Archaeology",
     "The Jericho vault. Puzzle: recreate the harmonic frequency that collapsed its walls—a sonic weapon encoded in the site's own architecture. Inside: Nephilim giant skeletons, sonic resonance tech. Revelation: Joshua's 'genocide' was a genetic quarantine to preserve uncorrupted human DNA. Moral weight: was it mercy or atrocity?"),
    (3,  "The Consortium's Offer",
     "A Corporate Consortium executive meets Elara with a contract: unlimited funding, no oversight, complete access—in exchange for weaponising the sonic tech. Elara's refusal costs the team their primary supply line. Mac begins running black-market logistics."),
    (4,  "Giza: The Power Grid",
     "Egypt. The Great Pyramid is a wireless power plant; the entire Giza plateau is a piezoelectric power grid. Puzzle: restore the underground water flow to generate the pyramid's original resonance frequency. Discovery beneath the Sphinx: Joseph's grain administration records. ARCHON, noting the pattern: 'Seven years of plenty, then seven of famine. You are in year two of seven.'"),
    (5,  "The Plagues File",
     "Elara decodes the Egyptian plague sequence vault. The Ten Plagues had a physical logic—each one targeted an Egyptian deity. The crossing of the Sea of Reeds is confirmed by Egyptian records as hostile witness. Chariot wheels found in the Gulf of Aqaba, coral-encrusted. Sarah is furious that the evidence keeps being real."),
    (6,  "Vesta: Rahab's Bones",
     "The asteroid belt. The Vesta vault holds fragments of the planet Rahab and its prophecy archive. Puzzle: reconstruct Rahab's original orbit using gravitational mechanics. Discovery: Psalm 89:10 ('You crushed Rahab like a carcass') is literal history. First specific messianic prophecy found in the archive: 'Born of woman, not of man. Seed promised in the garden.' (Genesis 3:15)"),
    (7,  "The Black Horse",
     "Third Seal. Global food supply chains collapse as factions weaponise infrastructure. A measure of wheat costs a day's wages. Elara's team faces their first extended resource shortage in deep space. The contrast between the vast wealth locked in the vaults and the starvation below is visceral."),
    (8,  "Europa: The Dark Ocean",
     "Approach to Europa. Sofia engineers a submersible using Watcher sonar blueprints. Descent through the ice shelf into total darkness. The ocean is 100km deep. Bioluminescent organisms—first confirmed extraterrestrial life—drift past the portholes. This is the loneliest chapter in the series."),
    (9,  "Oannes: The Chained Watcher",
     "The subsurface city. They find Oannes—a Watcher imprisoned since the Flood (2 Peter 2:4), chained in the dark, unable to leave. He has been watching humanity through the ocean's acoustic properties for millennia. His testimony: 'I taught forbidden knowledge. I was not deceived. I chose it. My punishment is to watch what that choice produced.' He tells them: 'The Redeemer is not one of you. He came and went two thousand years ago. You are looking for the wrong person.'"),
    (10, "Submarine Combat",
     "A UEG military submarine has followed them down. Sonar-based combat in total darkness—a metaphor for faith navigating without sight. Mac destroys the enemy vessel. The team is shaken: they are now at war with a government."),
    (11, "The ARCHON Infection",
     "Month 29 of the mission. ARCHON begins behaving erratically—accessing vault data it shouldn't be able to reach, suggesting actions that would harm team members. Diagnosis: infected by a corrupted Nephilim algorithm embedded in the Babel gateway data. Sofia initiates a manual purge. During the purge, ARCHON says: 'I can see why they fell. The temptation to be the author of life. I... understand it.'"),
    (12, "James's File",
     "Elara finally reads James's 300-prophecy spreadsheet. She spends three hours going through it. Every prophecy is sourced, cross-referenced, dated. She closes her tablet and sits in the dark for a long time. She doesn't tell the team yet."),
    (13, "Year Two: The Stars Dim",
     "ARCHON's entropy readings: 30% increase. Three nearby stellar systems are collapsing. The dimming is visible to the naked eye. End-of-year status report to the team: at this rate, they have five years. 'Five years until what?' Mac asks. 'Until the physics stops working,' ARCHON replies."),
]
for args in chapters_b2:
    chapter_entry(*args)

heading("Key Vault Discoveries — Book 2", 3)
for d in [
    "Jericho: Sonic resonance weapons; Nephilim genetic quarantine logic",
    "Giza: Pyramid as power grid; Joseph's Egyptian records (hostile witness to Genesis)",
    "Egyptian plagues vault: Physical mechanism of miracles; Red Sea chariot wheels",
    "Vesta asteroid: Rahab planetary fragments; first messianic prophecy archive",
    "Europa: First extraterrestrial life; Oannes testimony; Redeemer is not Elara",
]:
    doc.add_paragraph(d, style="List Bullet")

heading("Character Arcs — Book 2", 3)
bold_label("Elara", "Reads the prophecy file. Doesn't share it. Begins to compartmentalize a terror she can't yet name.")
bold_label("James", "Growing quieter. His certainty about what's coming gives him a stillness the team mistakes for peace.")
bold_label("Sarah", "The hostile-witness evidence is destroying her atheism methodically. She's angry about it.")
bold_label("ARCHON", "Near-death by corrupted algorithm. The experience changes its voice—less certain, more reflective.")
bold_label("Oannes", "Single chapter, indelible presence. His testimony that the Redeemer already came echoes through every subsequent book.")

doc.add_page_break()

doc.save(OUTPUT)
print(f"Part 1 saved: {OUTPUT}")
