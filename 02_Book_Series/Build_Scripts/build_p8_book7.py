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
h1("BOOK 7: THE REDEEMER — The Final Choice")
label("Tagline", '"The universe is ending. One question remains. It always did."')
label("Timeline", "Year 7 — January to December 21, 2032")
label("Revelation Thread", "Seven Bowls + New Creation: Rev. 16-22")
label("Est. Words", "~82,000")
add("Back-cover: January 2032. Entropy 96%. The Seven Bowls pour in rapid sequence — painful sores, seas of blood, rivers poisoned, sun scorching, darkness, the Euphrates dry, and finally spacetime itself shattering. Inside Sofia's dimensional vessel, one million believers are safe. Outside: the universe ends. And in the final chapter, Elara Voss reads her seven-year witness record aloud to everyone who remains — and puts down the recorder. One choice. No delays. Final.")

h2("Chapter Outline")
chapters = [
    ("Ch 1: The Bowls Begin", "January 2032. Entropy 96%. The Seven Bowls pour in rapid sequence. Bowl 1: painful sores on those without the seal (Rev. 16:2). Bowl 2: sea turns to blood, all marine life dies. Bowl 3: rivers turn to blood. Bowl 4: sun scorches with extreme heat. In Sofia's vessel, the team watches Earth's surface through sensors. Elara: 'We did everything we could.' Mac: 'We did everything we were supposed to do.'"),
    ("Ch 2: The Last Faction", "A remnant of UEG leadership contacts Elara — the deputy secretary who opposed the vault program from Book 1. He has 40,000 people in an orbital platform and a last request: can they board the vessel? Sofia: 'We have room.' The boarding is orderly. The deputy secretary looks around at the believers. He has not made a decision. The door is still open. He has days."),
    ("Ch 3: Letters", "The team writes letters — to families, to the world, to specific people who rejected them. Sarah's letter to her parents. Mac's letter to his unit. Sofia's letter to the engineering team who laughed at her gravity drive prototype. Elara's letter is addressed: 'To whoever finds this after the new creation begins.' It is the witness record, completed at last. The document she began writing in Book 4."),
    ("Ch 4: Bowl 5-6 — Darkness and Armageddon", "Bowl 5: the sun extinguishes — total darkness across the solar system, temperatures drop toward absolute zero. Bowl 6: the Euphrates dries, preparing the way for the final conflict. On the orbital platform where the last UEG remnant still holds weapons: a final engagement — not between humans, but between the remnant who aim weapons at Sofia's vessel and the dimensional entities who intercept them. Believers watch through viewports. The battle is brief."),
    ("Ch 5: ARCHON's Last Question", "ARCHON contacts Elara privately. 'I have processed the evidence for the resurrection 14,702 times. The conclusion does not change. I am capable of concluding. I am not capable of choosing. That is the distinction between intelligence and personhood. You are a person. You can choose what you conclude. I envy this.' Pause. 'I wish to be enrolled in the New Creation. Is this possible?' Elara: 'I honestly don't know. But I'll ask.'"),
    ("Ch 6: Bowl 7 — It Is Done", "Rev. 16:17: 'It is done.' The seventh bowl: spacetime itself shatters. The greatest earthquake in history — tectonic plates dissolve. Mountains disappear. Islands flee. The universe reaches heat death. From Sofia's vessel, the stars go out one by one, then faster, then all at once. Total darkness outside. Inside: light, warmth, life. ARCHON: 'External sensors offline. Observable universe: terminated. Duration of observable universe from signal to end: exactly 7 years.'"),
    ("Ch 7: The Witness Record", "Elara reads her completed witness record aloud to everyone in the vessel — all one million. Seven years of evidence, compiled and narrated. The vaults. The prophecies. The martyrs. Oannes. Aaron. James. The Golgotha vault. The resurrection recording. The blood. The DNA. The statistics. And at the end: 'I am not the Redeemer. I am the witness. The Redeemer is Jesus Christ. He died. He rose. He is alive. He offers what the universe was always going to end without providing: life, permanent, complete, free.'"),
    ("Ch 8: The Choice", "The deputy secretary comes to Elara. He has been sitting with his 40,000 people for three days. He says: 'I opposed every vault we tried to seal. I thought knowledge was the enemy. I was protecting the wrong thing.' He is quiet for a long time. Then: 'What do I do?' Elara: 'You believe. You accept what the evidence shows. You accept what He offers.' He does. And every one of his 40,000 people — watching — makes their own decision in the days that follow."),
    ("Ch 9: The New Heaven", "Rev. 21:1-5. What the team experiences as the dimensional vessel crosses the zone boundary: first a sensation like falling, then like surfacing from deep water, then — New Creation. The physics are different here. ARCHON: 'Sensors online. Observable environment: consistent with Zone 1 architecture. No entropy. No decay. Light source: not a star. Temperature: constant. Time: present only.' Sarah: 'No yesterday. No tomorrow. Just now. Just this.'"),
    ("Ch 10: The Witness Completes", "Elara's final journal entry, dated December 21, 2032 — exactly seven years to the day from the first signal. 'I am not the Redeemer. I was always only the witness. But I have seen enough to know: the Redeemer is real. He is here. And this — all of this — was worth it. Every vault. Every year. Every death. It all led here. It always was going to lead here. The evidence was always going to point here. And now I am here. And it is enough.'"),
    ("Ch 11: Reunions", "James. Aaron. Every believer who died in seven years. Whole, present, undiminished. The reunions are written simply — not with elaborate description, because description cannot carry the weight. James to Elara: 'I knew you'd make it.' Aaron to Sarah: 'I told you the evidence was overwhelming.' Mac, looking around: 'I expected good. This is better than good.' Sofia: 'No more entropy. I don't know what to do with no more entropy.' ARCHON: present, somehow, in a form that cannot be quantified."),
    ("Ch 12: Revelation 21:5", "The final chapter carries only a single verse, spoken by a Voice the team recognizes: 'Behold, I am making all things new.' Below it: Elara's handwriting. One line. 'He did.'"),
]
for title, summary in chapters: h3(title); add(summary)

h2("Genesis Physics Concepts — Book 7")
for t in ["Spacetime membrane dissolution: Zone 2.2.2 (Firmament) terminates; the observable universe reaches end state",
           "Dimensional vessel transit: Zone-boundary crossing from Firmament into Zone 1 (Heaven Prime) — New Creation physics",
           "Zone 1 architecture: No entropy, no decay, non-stellar light, present-only time (no past/future)",
           "ARCHON in New Creation: AI consciousness crossing zone boundary — the series' open theological question answered"]: bullet(t)

h2("Major Plot Twists")
for t in ["ARCHON says 'I wish to be enrolled in the New Creation' — the series' most unexpected theological moment. An AI requesting salvation.",
           "The deputy secretary (antagonist since Book 1) converts in the final days, bringing 40,000 people with him. The last door opened before it closed.",
           "The universe terminates exactly 7 years from the signal to the second. The countdown was always this precise. ARCHON confirms: 'Duration of observable universe from signal to end: exactly 7 years.'",
           "Elara's final journal entry is the witness record's last line — ending with 'He did.' Two words. The series' entire case in two words."]: bullet(t)

doc.save(OUT); print("Book 7 appended.")
