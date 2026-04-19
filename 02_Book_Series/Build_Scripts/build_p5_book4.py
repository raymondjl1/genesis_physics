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
h1("BOOK 4: THE ALTAR CRY — How Long, O Lord?")
label("Tagline", '"Aaron dies. Sarah believes. Elara writes: I am not the Redeemer. I am the witness."')
label("Timeline", "Year 4 — January 2029 to December 2029")
label("Revelation Thread", "Fifth Seal — Souls under the altar: 'How long, O Lord?' (Rev. 6:9-11)")
label("Est. Words", "~85,000")
add("Back-cover: ARCHON has completed its analysis. The probability that Jesus Christ is the Redeemer: 99.999999%. The probability that Dr. Elara Voss is the Redeemer: 0.00%. In the fourth year, a Jewish physicist returns to Jerusalem to testify publicly. He knows what will happen. He goes anyway. What follows is the series' emotional turning point — an event so precisely foreshadowed by vault evidence that it becomes impossible to distinguish archaeology from prophecy.")

h2("Chapter Outline")
chapters = [
    ("Ch 1: The Statistical Proof", "January 2029. ARCHON announces to the full team: 'Probability Jesus Christ is The Redeemer: 99.999999%. Probability Dr. Voss is The Redeemer: 0.00%. Your role, Dr. Voss: Witness. The question is whether you will believe the conclusion of your own investigation.' Silence. Aaron: 'I knew. I've known for two years. I just needed to hear it from a machine.'"),
    ("Ch 2: Bethlehem — The Prophecy Vault", "Vault beneath Bethlehem. Puzzle: probability calculation — odds of fulfilling 8 prophecies by chance: 1 in 10^17 (silver dollars covering Texas two feet deep; find one blindfolded). 48 prophecies: 1 in 10^157 (beyond observable universe atom count). 324 prophecies: the number ARCHON produces has no name in mathematics. Vault fragment: 'He will be born here. In this city. In this manner. At this time.'"),
    ("Ch 3: The Hostile Witnesses", "Josephus vault: authenticate the Testimonium Flavianum by cross-referencing Arabic and Syriac translations. Core passage confirmed authentic: 'About this time there lived Jesus, a wise man. He won over many Jews and Greeks. When Pilate condemned him to the cross, those who loved him did not cease.' Tacitus and Pliny vaults follow: three non-Christian first-century historians confirm Jesus existed, was crucified, had resurrection-claiming followers."),
    ("Ch 4: The 500 Witnesses", "Archive of 1 Corinthians 15:6 — 500+ people claiming to see Jesus alive after death, 'most of whom are still alive' (Paul writing 25 years post-resurrection). Forensic cross-examination: testimonies are independent but corroborating. Witnesses died maintaining this claim — Peter crucified, Paul beheaded, James stoned, Thomas speared. Mac: 'People don't die for things they know are lies.'"),
    ("Ch 5: Sarah's Crisis", "Sarah Chen awake 36 hours. Comes to Elara: 'I am a scientist. I follow evidence. I cannot find a single counterexample that survives scrutiny. I cannot find a case where the evidence points away from Jesus. I've looked.' Elara: 'I know.' Sarah: 'What do I do with that?' Elara: 'I don't know yet. I'm still deciding.' Sarah: 'How much more evidence do you need?' Elara has no answer."),
    ("Ch 6: Aaron Decides", "Aaron tells the team he is returning to Jerusalem to testify publicly. Elara: 'They'll kill you.' Aaron: 'I'm Jewish. My whole life I waited for Messiah. Now I know — Yeshua is HaMashiach. I have to tell my people. If Jesus is the Redeemer, nothing else matters.' He gives Elara his complete research document: 847 pages. 'For when you're ready.'"),
    ("Ch 7: Elara Reads the File", "Over three days, alone, Elara reads James's full spreadsheet and Aaron's 847 pages simultaneously. She does not eat. ARCHON monitors vitals and says nothing. At the end of three days she asks Sofia to keep the flight log running continuously. Sofia: 'Why?' Elara: 'I want a witness record.'"),
    ("Ch 8: The Sanhedrin Trial", "Jerusalem. Aaron presents his case using only Old Testament texts and vault archaeology. Isaiah 53 (Dead Sea Scroll, predates Jesus 200 years). Daniel 9:25 (calculates Messiah's arrival to within a week). Psalm 22 (describes crucifixion 1,000 years before Rome invented it). Broadcast goes global. Team watches from orbit. Verdict: Guilty of heresy. Aaron thanks the court politely."),
    ("Ch 9: The Stoning", "Point of view: Elara watching from a screen 30 million miles away. Verdict delivered. Aaron walks out. He does not run. First stone. Second. He does not fall immediately. He looks up. The screen resolution cannot show what he sees. Transmission cuts. ARCHON logs: 'Dr. Aaron Goldstein. Deceased. Year 4, Month 42.' Elara turns off the screen. Two pages."),
    ("Ch 10: Aaron's Vision", "A single page from Aaron's perspective in the moment before death. He sees heaven opened. He sees the Son of Man standing at the right hand of God. It does not describe what this looks like — only that he is not afraid, and that it is better than he expected, and that he wants to tell the others. He cannot. He goes anyway."),
    ("Ch 11: Sarah Believes", "Sarah comes to Elara the next morning. 'He died smiling. How?' Elara: 'I don't know.' Sarah: 'I do.' She holds out John 11:25 translated in her own hand: 'I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live.' Sarah: 'I believe. Not because it's comforting. Because the evidence is overwhelming and because he died smiling.' She does not ask permission. She simply believes."),
    ("Ch 12: The Fifth Seal", "Rev. 6:9-11: 'Souls under the altar — how long, O Lord?' The Colosseum vault activates with a final fragment: a list of martyrs' names. Aaron's name appears on it, placed 4,000 years ago. ARCHON: 'The vault was constructed approximately 4,000 BCE. Aaron's name was here before he was born.' Elara: 'Then it was always going to happen this way.' ARCHON: 'Yes.'"),
    ("Ch 13: Not the Redeemer", "Elara writes in her journal: 'I am not the Redeemer. I never was. I am the witness. The one who saw the evidence, compiled it, presented it. James believed first. Aaron died for it. Sarah follows evidence wherever it leads. I keep the record. That is what I am. That is enough.' She does not know yet if she believes. She knows what she is."),
    ("Ch 14: Year Four — The Altar Burns", "Entropy 70%. Sarah openly Christian, working on her first paper. Mac simply present — steady, faithful. Four years remain. Evidence complete. Vaults 70% unlocked. Elara reads Aaron's document one more time and begins writing a response addressed to no one she can name."),
]
for title, summary in chapters: h3(title); add(summary)

h2("Genesis Physics Concepts — Book 4")
for t in ["Blood DNA analysis: Virgin birth leaves genetic marker — 23 chromosomes from mother only, no paternal Y chromosome",
           "Prophecy probability: 10^157 against fulfilling 48 prophecies by chance; 324 prophecies exceed calculable odds",
           "Pre-inscribed vault data: Vault built ~4,000 BCE contains post-2029 names — implies extra-temporal foreknowledge",
           "Entropy at 70%: Stellar death visible to naked eye; thermodynamic collapse is measurable and on schedule"]: bullet(t)

h2("Major Plot Twists")
for t in ["ARCHON announces Elara's Redeemer probability as 0.00% — in front of the full team. She already knew. The team did not.",
           "Aaron's name was pre-inscribed on the martyr list 4,000 years ago. The martyrdom was scheduled in the vault's design.",
           "The Bethlehem vault contains Daniel 9:25's mathematical calculation pointing to the exact week of Jesus' entry into Jerusalem.",
           "Elara's 'response document' begun here will become the series' final testimony — read aloud in Book 7."]: bullet(t)

doc.save(OUT); print("Book 4 appended.")
