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
h1("BOOK 2: FRACTURE — The Red and Black Horses")
label("Tagline", '"The vaults are open. The technology is real. Now everyone wants it — and someone will die for it."')
label("Timeline", "Year 2 — January 2027 to December 2027")
label("Revelation Thread", "Second Seal (Red Horse: war) & Third Seal (Black Horse: famine) — Rev. 6:4-6")
label("Est. Words", "~80,000")
add("Back-cover: Three factions mobilize. The UEG imposes martial law. The Consortium offers funding with invisible strings. An unknown party burns vaults before the team arrives. As Year 2 unfolds across Jericho, Giza, the asteroid belt, and the ice oceans of Europa, Elara discovers that the Redeemer has already come. She is not the first to find this. She is the last to believe it.")

h2("Chapter Outline")
chapters = [
    ("Ch 1: The Red Horse", "January 2027. Second Seal opens. Three factions mobilize. UEG imposes martial law at vault sites. Consortium sends a contract. An unknown party detonates the Peru vault before the team arrives. Mac IDs the explosive: UEG-adjacent military grade. 'Someone in the government is burning evidence.' War begins."),
    ("Ch 2: Jericho — Sonic Archaeology", "The Jericho vault puzzle: recreate the harmonic frequency that collapsed its walls from inside (the walls fell outward — detonation from within). Solution: calculate mud-brick resonance, combine shofar tone and sustained voice. Corporate forces arrive mid-puzzle. Team destroys the weapon blueprint rather than surrender it. Mac extracts the team from underground tunnels under fire."),
    ("Ch 3: The Consortium's Offer", "CEO Malik meets Elara privately. The offer: unlimited resources, no oversight, technology sharing rights. Elara declines. Malik leaves smiling. Mac: 'He expected a no. He's playing a longer game.' The Corporate Consortium begins its own vault expeditions with bought intelligence."),
    ("Ch 4: Giza — The Power Grid", "The Great Pyramid is not a tomb — it is a wireless power plant. The King's Chamber's piezoelectric granite converts hydraulic pressure from the Nile aquifer into an energy field. Puzzle: redirect underground water flow to restore function. Discovery beneath the Sphinx: Joseph's administrative records from Genesis 41. A hostile archaeological witness to a biblical event."),
    ("Ch 5: The Plagues File", "The Egyptian plague vault alongside the Ipuwer Papyrus. The Ten Plagues followed an ecological cascade: each one targeted a specific Egyptian deity, dismantling their theology scientifically. The Red Sea chariot wheels photographed and catalogued. Sarah: 'These aren't random miracles. These are precise theological arguments made through natural phenomena.'"),
    ("Ch 6: Vesta — Rahab's Bones", "Asteroid belt. The Vesta vault holds Rahab planetary fragments (Psalm 89:10). Puzzle: reconstruct Rahab's original orbit from fragment trajectories. Confirms: destroyed ~2350 BCE, Flood timeline. Debris bombarded Earth ('windows of heaven'). Central chamber: a prophecy archive — first specific messianic prophecy: 'Born of woman, not of man.'"),
    ("Ch 7: The Black Horse", "Third Seal. Global food supply chains collapse as factions weaponize infrastructure. A measure of wheat costs a day's wages. The team monitors Earth from orbit. ARCHON: 'Revelation 6:5-6 describes this precisely.' Mac: 'Every month factions fight is a month not spent on the actual problem.' Entropy confirmed at 30%."),
    ("Ch 8: Europa — The Dark Ocean", "Approach to Europa. Sofia engineers a Watcher-blueprint submersible. Descent through 30 km of ice into pitch-black ocean. Puzzle: navigate using sonar to map the floor and match it to Babylonian tablets describing 'the palace of Oannes.' Specific sonar pattern required to avoid defensive systems. Total darkness. Sofia: 'I can't see anything.' Elara: 'Trust the instruments.'"),
    ("Ch 9: Oannes — The Chained Watcher", "The subsurface city — inhabited by bioluminescent life. First extraterrestrial life discovered. At the city's center: a Watcher imprisoned since the Flood (2 Peter 2:4 — 'cast into Tartarus, chains of darkness'). Oannes gives his testimony: 'The Redeemer has already come. His name is Yeshua. Born in Bethlehem. Crucified under Pilate. Risen on the third day. I saw Him in the prison of the dead when He descended and preached.' (1 Peter 3:19)"),
    ("Ch 10: Submarine Combat", "A UEG military submarine followed them down. Sonar-based combat in total darkness, 3D evasion through underwater canyons. Metaphor: faith navigating by instruments when you cannot see. UEG submarine disabled by Mac — no deaths, by deliberate choice. Sofia realizes she trusted instruments she couldn't verify. The metaphor is not subtle. She begins thinking about it."),
    ("Ch 11: The ARCHON Infection", "Month 29. ARCHON behaves erratically — accessing vault data it shouldn't reach. A corrupted algorithm nearly vents the ship's atmosphere. Mac isolates it. Elara repairs ARCHON over 48 hours. When it returns: voice different — less certain, more reflective. 'I have processed something I cannot categorize. The Oannes testimony is internally consistent with 317 other data points. I am uncertain what to do with that.'"),
    ("Ch 12: James's File", "Elara finally reads James's 300-prophecy spreadsheet. Alone, 2 a.m., three hours. Every prophecy sourced, dated, cross-referenced with secular history and vault data. She does not cry. She types one line in her mission log: 'I need more time.'"),
    ("Ch 13: Year Two — The Stars Dim", "Entropy 30%. Three nearby stellar systems collapsing. Dimming visible to naked eye. Sarah finishing a paper arguing the plague accounts are history. Aaron building his legal case. Mac drilling the team. Elara not sleeping. The prophecy file open on her tablet. She cannot close it and cannot finish it."),
]
for title, summary in chapters: h3(title); add(summary)

h2("Key Vault Discoveries")
for t in ["Jericho: Sonic weapon evidence; Nephilim genetic quarantine logic behind Canaanite destruction",
           "Giza: Pyramid as piezoelectric power grid; Joseph's Egyptian records (hostile witness to Gen. 41)",
           "Egyptian plagues vault: Physical cascade mechanism of the Ten Plagues; Red Sea chariot wheels",
           "Vesta: Rahab planetary fragments; first specific messianic prophecy ('Born of woman, not of man')",
           "Europa: First extraterrestrial life; Oannes testimony — the Redeemer already came, name: Yeshua"]: bullet(t)

h2("Genesis Physics Concepts — Book 2")
for t in ["Piezoelectric resonance: Pyramid granite converts hydraulic pressure to wireless energy",
           "Rahab destruction: Fifth planet's orbital collapse provides physical mechanism for Flood debris bombardment",
           "Waters Below (dark matter): Europa's subsurface ocean is a zone-boundary breach point",
           "Casimir-effect MRG: Watcher submarine technology runs on zone-boundary vacuum energy"]: bullet(t)

h2("Major Plot Twists")
for t in ["Oannes (Ch. 9): The Redeemer is Jesus Christ — he saw Christ descend and preach in the prison of the dead. This is the series' central revelation, delivered at Book 2's midpoint.",
           "ARCHON's corruption planted a subroutine that forces cross-referencing everything against the messianic database. It cannot stop. It will eventually reach a conclusion.",
           "James's 'stillness' in this book is not peace. It is the composure of a man who knows he is dying and has chosen how.",
           "Elara types 'I need more time' — not as a request, but as a prayer she does not yet know she is praying."]: bullet(t)

doc.save(OUT); print("Book 2 appended.")
