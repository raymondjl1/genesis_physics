from docx import Document
from docx.shared import Pt, RGBColor

OUT = r"C:\Users\J Raymond\OneDrive\Documents\ExodusProtocol\Bible Physics\Book Series\Exodus_Protocol_Novel_Series_Plan.docx"
doc = Document(OUT)

def h1(t): p = doc.add_heading(t, 1); p.runs[0].font.color.rgb = RGBColor(0x1F,0x38,0x64); return p
def h2(t): p = doc.add_heading(t, 2); p.runs[0].font.color.rgb = RGBColor(0x2E,0x50,0x90); return p
def h3(t): p = doc.add_heading(t, 3); p.runs[0].font.color.rgb = RGBColor(0x1F,0x38,0x64); return p
def add(t): p = doc.add_paragraph(); p.add_run(t).font.size = Pt(10.5); p.paragraph_format.space_after = Pt(4); return p
def label(k, v): p = doc.add_paragraph(); r1 = p.add_run(k+": "); r1.bold = True; r1.font.size = Pt(10.5); p.add_run(v).font.size = Pt(10.5); return p
def bullet(t): p = doc.add_paragraph(style='List Bullet'); p.add_run(t).font.size = Pt(10.5); p.paragraph_format.space_after = Pt(2); return p

doc.add_page_break()
h1("WORLD-BUILDING & SCIENCE FRAMEWORK")
h2("The Genesis Physics Framework")
add("All science in the series draws from the Genesis Physics theoretical framework: treating the biblical creation account as precision cosmological description. The series does not argue Genesis Physics is true — it assumes it as the operating physics of its universe, the same way Star Trek assumes warp drive.")
for t in ["Firmament (raqia) = spacetime membrane — the boundary layer between dark energy (Waters Above) and dark matter (Waters Below)",
           "Pre-Flood hyperbaric atmosphere: 2-3x pressure, UV-filtering vapor canopy, warm global climate enabling dinosaur gigantism and human lifespans",
           "Flood mechanism: Rahab (fifth planet) destroyed ~2350 BCE; debris bombarded Earth ('windows of heaven'); Waters Above canopy collapsed ('fountains of the deep')",
           "Watcher technology: Anti-gravity (gravitational wave manipulation), wireless power (piezoelectric resonance), dimensional rifts (zone-boundary traversal)",
           "Entropy acceleration: Physics constants measurably decreasing — the universe runs down per Romans 8:22, measurable and on schedule",
           "Casimir-effect energy (MRG): Harvested from quantum vacuum at zone boundaries — the power source for all Watcher-derived technology",
           "Resurrection physics: A biological entity crossing from Zone 2.2.2 (Firmament) into Zone 1 (Heaven Prime) and returning — unique, unrepeatable, evidenced"]: bullet(t)

h2("Vault Network Master List — Key Sites")
vaults = [("Gobekli Tepe", "Turkey", "Watcher names, star map, pre-Flood chronology"), ("Mount Hermon", "Lebanon/Syria", "Tech schematics, genetic lock, repentant Watcher testimony"),
    ("Moon (Crater Daedalus)", "Far Side", "Pre-Flood library, Flood footage, Rahab evidence"), ("Temple Mount", "Jerusalem", "Ark of the Covenant, First Seal, mercy-seat gateway"),
    ("Babel/Eridu", "Iraq", "Dimensional gateway device, language confusion physics"), ("Jericho", "Israel", "Sonic resonance weapon, Nephilim quarantine records"),
    ("Giza/Sphinx", "Egypt", "Pyramid power grid, Joseph's records, plague vault"), ("Vesta", "Asteroid Belt", "Rahab fragments, first messianic prophecy"),
    ("Europa", "Jupiter system", "Oannes testimony — Redeemer already came; first extraterrestrial life"), ("Olympus Mons", "Mars", "Hyperbaric archive, dinosaur/human coexistence"),
    ("Colosseum", "Rome", "Martyr archive, Peter's letter, Tacitus/Pliny evidence"), ("Bethlehem", "Israel", "Prophecy probability vault, Daniel 9:25 calculation"),
    ("Golgotha", "Jerusalem", "Jesus's blood, resurrection recording, Ark of the Covenant — final vault")]
for site, loc, desc in vaults: label(f"{site} ({loc})", desc)

doc.add_page_break()
h1("MARKETING & PUBLISHING NOTES")
h2("Comparable Titles")
for t in ["The Martian (Andy Weir): Hard sci-fi with rigorous science, first-person voice, survival stakes — same register",
           "The Da Vinci Code (Dan Brown): Archaeological mystery, conspiracy, global locations, theological revelation — same structure",
           "This Present Darkness (Frank Peretti): Spiritual warfare, supernatural stakes, evangelical fiction — same audience overlap",
           "The Left Behind Series (LaHaye/Jenkins): End-times framework — Exodus Protocol offers literary quality Left Behind lacks",
           "Recursion (Blake Crouch): High-concept sci-fi with philosophical stakes — same ambition, different theology"]: bullet(t)

h2("Target Audiences")
for t in ["Christian readers (evangelical/messianic): 40M+ in US. Hungry for scientifically credible fiction that takes their beliefs seriously",
           "Hard sci-fi readers: Andy Weir / Blake Crouch crossover — readers who want rigorous physics with their fiction",
           "Archaeological thriller readers: James Rollins, Steve Berry, Dan Brown audience — global locations, ancient mysteries, conspiracies",
           "Skeptics and seekers: Sarah Chen's arc is written for this reader. The evidence-based path to faith is the series' main road",
           "Jewish readers: Aaron Goldstein's arc — a Jewish physicist accepting Jesus as Messiah — is rare and significant"]: bullet(t)

h2("Series Commercial Structure")
add("Seven books at approximately 80,000 words each (~567,000 words total). Books 1-2 accessible to new readers; Books 3-7 reward series loyalty. Books 1-2 can be marketed as a duology standalone. The theological content escalates gradually — non-Christian readers have 80,000 words to invest before the argument becomes explicit.")
add("Unique selling proposition: Exodus Protocol does not require the reader to be Christian. It requires only that the reader follow evidence. The series makes the same case Sarah Chen makes — through archaeology, mathematics, forensic history, and physics. It does not preach. It prosecutes.")

h2("What the Series Does Not Do")
for t in ["Does not portray Christians as naive or anti-intellectual — Sarah's conversion is evidence-based",
           "Does not portray non-Christians as villains — the antagonists are misguided, not evil",
           "Does not use the Rapture framework (Left Behind) — this is not rapture fiction",
           "Does not fictionalize Jesus — he appears only in documented historical record and the vault's resurrection recording",
           "Does not resolve the theological question for the reader — the final chapter offers evidence, not verdict"]: bullet(t)

doc.add_page_break()
h1("SERIES AT A GLANCE")
books = [("1","SIGNAL: The Awakening Seal","Year 1 (2026)","~80,000","First Seal — White Horse"),
         ("2","FRACTURE: The Red and Black Horses","Year 2 (2027)","~80,000","Second & Third Seals"),
         ("3","THE PALE RIDER: Death Reigns","Year 3 (2028)","~82,000","Fourth Seal — Pale Horse"),
         ("4","THE ALTAR CRY: How Long, O Lord?","Year 4 (2029)","~85,000","Fifth Seal — Martyrs"),
         ("5","THE FALLING STARS: The Sixth Seal","Year 5 (2030)","~80,000","Sixth Seal — Cosmic Signs"),
         ("6","THE SEVENTH SEAL: Silence in Heaven","Year 6 (2031)","~78,000","Seventh Seal + Trumpets"),
         ("7","THE REDEEMER: The Final Choice","Year 7 (2032)","~82,000","Seven Bowls + New Creation")]
for num, title, year, words, thread in books:
    p = doc.add_paragraph()
    p.add_run(f"Book {num}: ").bold = True
    p.add_run(f"{title} | {year} | {words} | {thread}").font.size = Pt(10.5)
    p.paragraph_format.space_after = Pt(4)

add("")
p2 = doc.add_paragraph()
r = p2.add_run("Total Series: ~567,000 words | Genre: Hard Sci-Fi / Archaeological Thriller / Speculative Theology")
r.bold = True; r.font.size = Pt(11)

doc.add_page_break()
h1("AUTHOR'S NOTE")
add("This series grew from a single question: What if the archaeological and scientific evidence for the events of the Bible was not scattered and disputed — but comprehensive, coordinated, and hidden, waiting to be found at the exact moment humanity needed it most?")
add("The Genesis Physics framework, the vault network, the 324 prophecies, the hostile witnesses, Peter's letter, the blood at Golgotha — none of these are invented from nothing. Each one is rooted in real archaeology, real historical documents, real scientific data points, and real theological argument. The series dramatizes an investigation that anyone could conduct. It simply gives that investigation a deadline.")
add("The deadline is the point. The evidence has always been available. The door has always been open. But in this story — as perhaps in this world — it will not be open forever.")
p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(24)
r = p.add_run("For the ones who followed the evidence all the way to the end of it.")
r.italic = True; r.bold = True; r.font.size = Pt(12)

doc.save(OUT); print("Appendices and back matter appended. Document complete.")
