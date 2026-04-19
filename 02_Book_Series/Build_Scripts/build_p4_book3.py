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
h1("BOOK 3: THE PALE RIDER — Death Reigns")
label("Tagline", '"The mentor is gone. The universe is bleeding. And the evidence points somewhere Elara cannot follow. Yet."')
label("Timeline", "Year 3 — January 2028 to December 2028")
label("Revelation Thread", "Fourth Seal — Pale Horse: 'Death, and Hades followed with him' (Rev. 6:8)")
label("Est. Words", "~82,000")
add("Back-cover: Alpha Centauri is collapsing. James Whitmore is dying — though only he knows it. And the vaults are showing evidence of a figure who suffered willingly for others across seventeen archaeological sites from six civilizations over four millennia. In the third year, Elara Voss loses her mentor, her certainty, and her working theory of who she is. What she gains is a question she cannot unask.")

h2("Chapter Outline")
chapters = [
    ("Ch 1: Alpha Centauri Falls", "January 2028. The nearest stellar system collapses — visible as a new dark patch in the southern sky. Entropy at 62%. ARCHON: 'This was not predicted by stellar models. The decay rate is inconsistent with known physics.' The team watches from orbit. It takes eight minutes for light to travel from Alpha Centauri. They are watching a death that happened eight years ago."),
    ("Ch 2: Mars Vault — The Hyperbaric Archive", "Olympus Mons subsurface vault. Puzzle: restore the atmospheric simulator to pre-Flood conditions — 2-3x pressure, water vapor canopy, warm global climate. Simulator activates: holographic pre-Flood Earth. Dinosaurs and giant humans in the same ecosystem. ARCHON: 'Fossil soft tissue proteins degrade in thousands of years, not millions. Carbon-14 confirms less than 50,000 years. This is biology.'"),
    ("Ch 3: Behemoth and Leviathan", "The vault contains Job 40-41's creature descriptions. Aaron: 'Job is the oldest biblical book. These descriptions match sauropod and mosasaur morphology precisely — Job described real animals.' Elara cross-references with soft-tissue fossil data. Match is anatomical. Sarah refuses comment for 72 hours. Then: 'Fine. Dinosaurs and humans. Same time. What else did I decide was mythology?'"),
    ("Ch 4: The Reactor", "The Mars colony's fusion reactor develops cascade fault — result of UEG sabotage of Exodus supply chains. Fault will breach in 11 hours, killing 4,000 colonists unless contained. Mac coordinates evacuation. Sofia reroutes power. James disappears from comms for two hours. When he returns, his voice is wrong — calm in a way that is not calm."),
    ("Ch 5: James", "James Whitmore walks through the reactor containment door alone. Seals it from inside. In 4 minutes before shielding blocks comms, he says three things: 'Tell Aaron he was right.' 'Tell Elara to open the file — the whole file this time.' 'I am not afraid.' The door seals. The reactor stabilizes. He is gone. This chapter is three pages."),
    ("Ch 6: The Pale Horse Rides", "The Fourth Seal opens. Elara's grief is not dramatic — it is the collapse of her operating framework. James was proof the destination was reachable. Without him the evidence is orphaned. Mac handles logistics. Aaron handles Aaron. Sofia handles the ship. Elara handles nothing for eleven days. Then she opens the file. The whole file."),
    ("Ch 7: The Corrupted Vaults", "Discovery: a network of vaults deliberately corrupted — not by UEG, but by the rival Watcher faction. These contain false prophecies, inverted histories, disinformation designed to redirect toward a false Redeemer candidate. ARCHON: 'These were built to confuse. The corruption is architectural, not accidental.' The rival faction feared the real evidence would be found."),
    ("Ch 8: ARCHON Speaks of the Fall", "Elara begins asking ARCHON the questions she never asked James. ARCHON processes vault data and produces a chronological account of Genesis 3 as a physics event: 'The Breaking began with a choice violating zone boundary protocols. Entropy is the physical expression of that violation. The universe has been winding down since Genesis 3. At current rate: seven years from December 2025.' Elara: 'That's the exact vault countdown duration.' ARCHON: 'Yes.'"),
    ("Ch 9: The Suffering Servant", "ARCHON flags a motif across 17 vault texts from 6 civilizations spanning 4,000 years: a figure who suffers willingly for others, absorbs punishment meant for someone else, and is vindicated afterward. Egypt, Babylon, Persia, Israel, Rome, pre-Flood archive. ARCHON: 'The probability this motif describes the same historical event, converging from independent traditions, exceeds 10^47.' The texts call him: 'The One Who Takes the Blow.'"),
    ("Ch 10: Colosseum — The Martyr Archive", "Rome. Vault beneath the Colosseum holds persecution records. Tacitus Annals 15:44: 'Christ suffered extreme penalty during the reign of Tiberius at the hands of Pontius Pilate.' Forensic analysis of people who died maintaining they witnessed Jesus risen — each had nothing to gain, everything to lose. Mac: 'Liars don't die for lies when they have nothing to gain.'"),
    ("Ch 11: Peter's Letter", "Among the Colosseum documents: a letter authenticated by ink composition, papyrus carbon dating, and linguistic analysis as Peter's own — written the night before his crucifixion. 'I could recant. Save my life. But I saw Him. I ate fish with Him after He rose. I touched His wounds. I cannot deny what I know to be true. I am not afraid of tomorrow.' Sarah reads it aloud. She cannot finish it."),
    ("Ch 12: Mac Asks the Question", "Mac Reynolds, silent through three chapters of evidence, asks one question: 'How many people die for something they know is a lie?' No one answers. Mac: 'None. You might die for something you think is true. But if you know it's a lie — you don't die for it. Peter knew. They died anyway.' He goes back to his post. He does not ask another theological question for six months."),
    ("Ch 13: Year Three — Hope Dies", "Entropy 62%. Team fractured by grief. ARCHON has processed 289 of 324 messianic prophecies and is building toward a conclusion it has not announced. Aaron is writing a document he will not share. Sarah is sleeping badly. Mac is still. And Elara has read the full prophecy file. She writes: 'The evidence goes somewhere. I know where. I am not ready to go there.'"),
]
for title, summary in chapters: h3(title); add(summary)

h2("Genesis Physics Concepts — Book 3")
for t in ["Pre-Flood hyperbaric atmosphere: 2-3x pressure; vapor canopy enabled gigantism and extended lifespans",
           "Fossil chronology: Soft tissue preservation = rapid catastrophic burial, not millions of years of gradual deposition",
           "Entropy as Genesis 3 physics: The Fall introduced thermodynamic decay with a calculable start date",
           "Zone boundary violation: The Breaking is a physics event with start (Genesis 3) and end (7 years) dates"]: bullet(t)

h2("Major Plot Twists")
for t in ["James's death is not surprising to James. His 'stillness' in Book 2 was preparation. He chose this.",
           "The 17-vault 'Suffering Servant' motif from 6 civilizations spanning 4,000 years is statistically impossible as coincidence.",
           "Corrupted vaults reveal an organized rival-Watcher disinformation campaign still active — the team's adversary is not just human factions.",
           "ARCHON has been running a messianic probability calculation since the Vesta infection. At 289 of 324 data points. Will announce in Book 4."]: bullet(t)

doc.save(OUT); print("Book 3 appended.")
