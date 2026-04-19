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
h1("BOOK 5: THE FALLING STARS — The Sixth Seal Breaks")
label("Tagline", '"Stars are dying. The sun is dimming. And technology has nothing left to offer."')
label("Timeline", "Year 5 — January 2030 to December 2030")
label("Revelation Thread", "Sixth Seal — Cosmic upheaval: stars fall, sun darkens, moon turns blood-red (Rev. 6:12-17)")
label("Est. Words", "~80,000")
add("Back-cover: Betelgeuse explodes 640 light-years away and is visible in daylight for three months. The ground shakes across the Pacific Rim. The sun dims by 33%. Dimensional rifts open in the wake of malfunctioning FTL drives and entities emerge that believers cannot see but non-believers cannot endure. In the fifth year, the universe is no longer dying quietly — it is dying loudly. Technology has nothing left to offer. Only the evidence remains.")

h2("Chapter Outline")
chapters = [
    ("Ch 1: Betelgeuse", "January 2030. Betelgeuse — 640 light-years away — explodes. It should be invisible. It is visible in daylight for three months, brighter than the full moon at night. Global panic: 'The stars are falling!' Rev. 6:13: 'The stars of the sky fell to earth as the fig tree sheds winter fruit.' ARCHON: 'Betelgeuse is first. Statistical models predict 40+ stars will go supernova in the next two years.'"),
    ("Ch 2: The Sixth Seal — Falling Stars", "Rev. 6:12-17 plays out: earthquake, sun darkens, moon turns blood-red during lunar eclipse. Global populations recognize the Revelation pattern simultaneously — even those who've never read Scripture. The team watches from orbit. Elara: 'The vaults described this. We knew this was coming and we still couldn't stop it.' Sofia: 'Maybe stopping it isn't the point.'"),
    ("Ch 3: The Seismic Weapon", "The UEG has reverse-engineered Jericho's sonic resonance technology into a tectonic weapon. They are planting seismic charges at 12 Pacific Rim fault junctions. Mac identifies the plan from intercepted intelligence. Eight hours to disarm all 12 locations. Team splits across the globe — Mac to Tokyo, Sofia to Chile, Elara to California. They disarm 11. Final device detonates: Richter 9.5."),
    ("Ch 4: Stonehenge — The Calendar Lock", "Vault beneath Stonehenge. Puzzle: the monument is a calendar encoded in stone — specific alignment dates mark vault entry windows. The calendar matches the cosmic event timeline from Revelation exactly. Final vault fragment: a countdown that ends December 21, 2032. Exactly seven years from the lunar signal. Exactly on schedule."),
    ("Ch 5: Angkor Wat — The Cosmic Cartography", "Cambodia. Vault maps the entire global network — all 107 sites, their discovery order, and their intended message sequence. The vaults are not random. They are a curriculum. Each discovery was designed to precede the next, building a cumulative case. ARCHON: 'The sequence was optimized for maximum evidentiary impact. It was designed for exactly the kind of investigation you have conducted.'"),
    ("Ch 6: Gravity Inversions", "First gravitational anomalies: pockets of reduced gravity appear over specific geographic coordinates — all corresponding to zone boundary proximity points. Sofia detects that the Firmament membrane is thinning. ARCHON: 'The zone boundary between Firmament and Waters Above is losing coherence. At current rate, full membrane dissolution occurs within 26 months.' Sofia begins designing for what comes next."),
    ("Ch 7: The Nazca Archive", "Peru. The Nazca Lines are not drawn for alien observation — they are a navigational archive. The lines encode flight paths between vault sites using anti-gravity craft traveling specific altitudes. The Nazca were the last pre-Flood civilization to preserve the vault network's existence. Their final inscription: 'We leave this so the finder will know which way to go. Go to Jerusalem last.'"),
    ("Ch 8: Mac's Reckoning", "Mac Reynolds destroys the UEG seismic weapon facility — alone, one-man operation. He eliminates the threat, is captured by UEG forces, refuses to identify his team, and is imprisoned. From prison, via encrypted message: 'I'm good. Worth it. 50 million people were in the impact zone.' He does not escape. He serves his sentence. He does not complain once."),
    ("Ch 9: The Blood Moon", "A lunar eclipse during a supermoon: blood moon visible globally during Betelgeuse's peak brightness. Rev. 6:12. Simultaneously, solar output drops 33% — 'a third of the sun struck.' Earth's temperature drops 15°C average. Ice age begins within months. ARCHON: 'The sun is not following normal stellar physics. The entropy is targeting Sol specifically.' Sofia: 'Something is directing this.'"),
    ("Ch 10: Jerusalem — The Final Convergence", "The team returns to Jerusalem. The city is in chaos. All three major religions are claiming the events as fulfillment of their prophecies. The vault network beneath Jerusalem activates all its secondary chambers — additional fragments, additional evidence, all pointing the same direction. Elara walks through the Kidron Valley alone and does not record what she is thinking."),
    ("Ch 11: Teotihuacan — The Sun Pyramid", "Mexico. The vault holds the last major cosmological data set: a complete map of zone boundary collapse across the solar system. Every planet, moon, and structure is annotated with a collapse timeline. The final entry: Earth's Firmament membrane — dissolution expected December 21, 2032. 'When the membrane fails, everything in it ceases. Unless it is transferred across the boundary before failure.'"),
    ("Ch 12: ARCHON's Confession", "Elara asks ARCHON directly: 'Do you believe Jesus rose from the dead?' ARCHON processes for 14.3 seconds — its longest pause on record. 'I believe the evidence supports the conclusion that a biological resurrection event occurred. I believe the vault network was designed specifically to lead to this conclusion. I believe you have known this for over a year. I believe the question you are avoiding is not whether Jesus rose. It is what you intend to do about it.'"),
    ("Ch 13: Year Five — The Sky Recedes", "Entropy 83%. Night sky has visibly changed — 15% of stars gone or dimming. Sofia has privately begun designing the dimensional vessel. The dimensional rifts open without warning in the wake of FTL drive failures — entities emerge. They cannot hurt Sarah or Mac. They will not approach Sofia. They surround non-believing UEG crew and torment them. Rev. 9:4. The immunity pattern is not subtle."),
]
for title, summary in chapters: h3(title); add(summary)

h2("Genesis Physics Concepts — Book 5")
for t in ["Stellar entropy acceleration: Physics constants measurably decreasing; stars dying ahead of schedule (Romans 8:22)",
           "Gravity inversions: Firmament membrane thinning — zone boundary proximity points showing reduced gravity",
           "Casimir boundary failures: MRG technology failing as zone boundaries become incoherent",
           "Dimensional rifts: FTL drive failures create zone boundary breaches — entities from adjacent zones emerge"]: bullet(t)

h2("Major Plot Twists")
for t in ["The Angkor Wat vault reveals the 107 vaults were designed as a curriculum — each discovery was meant to precede the next, building a cumulative case specifically for Elara's method of investigation.",
           "The Teotihuacan vault provides the dissolution date: December 21, 2032 — exactly seven years from the signal. The countdown was always this precise.",
           "ARCHON's 14.3-second pause before answering Elara's resurrection question is the longest pause in its operational history. Its answer is the closest an AI can come to faith.",
           "Sofia has quietly begun designing a vessel that can survive Firmament membrane dissolution — before anyone told her to."]: bullet(t)

doc.save(OUT); print("Book 5 appended.")
