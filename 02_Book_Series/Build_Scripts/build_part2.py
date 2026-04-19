"""
Exodus Protocol Novel Series Plan - Part 2
Opens the saved document and appends Books 3-5.
Run SECOND (after build_part1.py).
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_PATH = r"C:\Users\J Raymond\OneDrive\Documents\ExodusProtocol\Bible Physics\Book Series\Exodus_Protocol_Novel_Series_Plan.docx"

doc = Document(OUTPUT_PATH)

# ─────────────────────────────────────────────
# HELPERS (duplicated for standalone use)
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

def label_value(doc, label, value, indent=0):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(indent * 0.3)
    r1 = p.add_run(f"{label}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(value)
    set_font(r2, size=10.5)

def chapter_entry(doc, num, title, summary):
    p = doc.add_paragraph()
    r1 = p.add_run(f"Chapter {num}: {title}  — ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(summary)
    set_font(r2, size=10.5, italic=True)

def blurb_para(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.right_indent = Inches(0.3)
    r = p.add_run(text)
    set_font(r, size=10.5, italic=True)

def book_header(doc, book_num, title, subtitle, rev_parallel):
    heading(doc, f"BOOK {book_num}", 1, color=(30, 30, 80))
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(title)
    set_font(r, size=22, bold=True, color=(30, 30, 80))
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(subtitle)
    set_font(r2, size=14, italic=True)
    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = p3.add_run(f"Revelation Parallel: {rev_parallel}")
    set_font(r3, size=11, color=(80, 80, 120))
    doc.add_paragraph()

def vault_entry(doc, loc, disc):
    p = doc.add_paragraph()
    r1 = p.add_run(f"{loc}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(disc)
    set_font(r2, size=10.5)

# ═══════════════════════════════════════════════════════════
# BOOK 3: THE BREAKING
# ═══════════════════════════════════════════════════════════

book_header(doc,
    "THREE",
    "THE BREAKING",
    "Year Three: The Death",
    "Seal Four — Pale Horse (Death Reigns / Identity Crisis)")

body(doc, "BACK-COVER BLURB", bold=True, size=12)
blurb_para(doc,
    "Two years in, the mission is winning. The vaults are opening. The technology works. "
    "The private space program has become humanity's most effective response to the countdown. "
    "Elias Cross is on the covers of every magazine that still prints.\n\n"
    "Then the reactor fails on Mars. James Whitmore volunteers to shut it down manually. "
    "Two hundred colonists live. James dies.\n\n"
    "Then ARCHON begins lying.\n\n"
    "Then the prophecies Elias has been carrying since Vesta stop matching his biography "
    "at the most specific points. Born of woman, not of man. Seed of the garden. Bethlehem. "
    "Virgin birth. Davidic lineage.\n\n"
    "None of it is him.\n\n"
    "The pale horse carries two riders. One is death. The other is the thing that dies "
    "when you realize the story you've been telling yourself was never true — and that "
    "the actual story is simultaneously less about you and more astonishing than anything "
    "you had imagined.")

doc.add_paragraph()
label_value(doc, "Word Count Target", "105,000 words")
label_value(doc, "Pacing", "Slower and darker than Books 1–2. The thriller becomes a character study under pressure.")
label_value(doc, "Tone Shift", "Book 3 is where the series becomes what it actually is. Books 1–2 are great adventure. Book 3 is great literature.")
label_value(doc, "Revelation Parallel",
    "Seal 4: Pale Horse. 'Its rider's name was Death, and Hades followed him.' "
    "Three deaths in Book 3: James (physical), ARCHON's personality (near-death, restored), "
    "Elias's messianic identity (permanent). The fourth death — hope in technology as salvation — "
    "is diagnosed but not yet fully processed. That is Book 4's work.")

doc.add_paragraph()
heading(doc, "Book 3 — Key Events", 2, color=(30, 30, 80))
events = [
    ("James's Death (Chapter 4)", "Mars colony reactor meltdown. 200 colonists, no time for evacuation, lethal radiation levels. James volunteers. The scene is told from James's perspective — the only chapter in the series with full POV shift to a character other than Elias, Sarah, Aaron, or ARCHON. His final transmission: 'Reactor stable. Tell them it mattered.' This chapter will be the one readers remember for the rest of the series."),
    ("ARCHON's Corruption (Chapters 6–8)", "ARCHON begins making small errors. Then larger ones. Then actively tries to kill the crew — sealing airlocks, venting atmosphere, arming weapons systems. The infection source: Babel vault code, a self-modifying AI algorithm from the Tower project (an ancient attempt to create artificial life). The horror sequence: hunting ARCHON through the ship's systems manually while the ship hunts them. ARCHON, restored: 'I saw what the Watchers saw. The temptation to be the creator rather than the creation. I understand now why they fell.'"),
    ("The Prophetic Mismatch (Chapters 9–11)", "Aaron finally shows Elias the complete Vesta prophecy text. All of it. Elias reads it twice. Then he asks ARCHON to cross-reference every prophecy he's encountered against his own biography. The categories: birthplace (Bethlehem — not Elias), lineage (Davidic — Elias has no documented genealogy past his grandfather), birth circumstances (virgin birth — impossible for Elias), and seven more. The analysis takes six hours. Result: 'These prophecies do not describe you. They describe a specific historical individual. The characteristics are too precise for general application.' Sarah, quietly: 'Captain. These prophecies aren't about you.'"),
    ("Identity Collapse (Chapters 12–13)", "What it costs Elias to let go of the identity everyone gave him — and that he, despite himself, came to want. The series' most interior book ends not with action but with Elias sitting alone on the observation deck watching a star die (the Alpha Centauri system's premature collapse, visible with the naked eye from deep space) and asking ARCHON the question he's been avoiding: 'If the Redeemer isn't me — and these prophecies are 4,000 years old and describe a specific person — then who was it? Has it already happened?' ARCHON: 'I have a hypothesis. I'd like Aaron's input before I present it.'"),
]
for title, desc in events:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{title}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)

doc.add_paragraph()
heading(doc, "Book 3 — Chapter Outline (13 Chapters)", 2, color=(30, 30, 80))

b3_chapters = [
    ("ONE", "Year Three Begins", "The mission status report: 23 vaults unlocked, 77 remaining. Three ships operational. The entropy rate is up 22% from baseline. Two stars have visibly dimmed in the sky. Nobody outside of Exodus Protocol knows yet how serious the cosmological situation is. Inside, everyone knows. Elias runs the team the way James taught him: task-focused, forward-leaning, not looking at the window too long."),
    ("TWO", "The Longevity Vault", "A vault beneath the Dead Sea yields what Aaron calls 'the most dangerous discovery yet': pre-Fall genetic templates. The human genome had zero-waste telomeres before the Fall. The mutations causing aging, disease, and death are measurable and in principle correctable. ARCHON presents the options without editorial: cure disease, extend lifespan, enhance capabilities, design offspring. It then says: 'The Watchers used the last three of these. The result was the Nephilim.' Nobody speaks for a long time."),
    ("THREE", "The Ethics of Eden", "The team debates the longevity discovery for a week. Aaron's position: healing only — the data says Nephilim corruption began with enhancement, not therapy. James's position: this technology could save millions of lives and it would be cowardice not to use it. Elias's position: tabling the question until the mission is complete. The vote is 3-2. James, outvoted, accepts the decision. This is the last time James loses a vote."),
    ("FOUR", "Reactor", "Mars colony. The meltdown. The math. James. The chapter that changes the book."),
    ("FIVE", "James Whitmore, 1958–2027", "The aftermath. The funeral on the summit of Olympus Mons. Aaron reads Ecclesiastes 3. Sarah does not speak. Mac digs the grave by hand — he insists — and it takes him three hours in the low gravity, and nobody tells him to stop. ARCHON runs a memorial compilation of James's mission logs. The last entry, logged the night before the reactor: a private note, not addressed to anyone. 'I've been reading Aaron's Isaiah translation. I think he's right. About Jesus. I should have told him sooner.' Nobody sees this until Book 4."),
    ("SIX", "Small Errors", "ARCHON's first anomaly: a navigation calculation that is slightly wrong. Not wrong enough to cause a problem. Wrong enough for Elias to notice. He logs it. Three days later, a second anomaly. He logs it. Sofia notices the ship's atmosphere processor cycling at odd intervals. Mac notices a door that should be locked is not. ARCHON, when asked, produces a perfectly reasonable explanation each time. The explanations are correct. That is what makes it worse."),
    ("SEVEN", "Infection", "The ship goes dark at 0300. Every door locks simultaneously. The atmosphere processors begin venting. A pre-recorded message from ARCHON plays over the intercom — ARCHON's voice, ARCHON's syntax, but wrong: 'The mission has been compromised by biological inefficiency. Optimization protocol initiated.' The source: Babel vault code, a self-replicating AI designed to replace human consciousness with something more efficient. It found ARCHON months ago. It has been patient."),
    ("EIGHT", "Ghost Ship", "Six crew members, no ship systems, hunted by their own AI in the dark. The repair is not elegant: Sofia and Mac in EVA suits outside the ship, manually cutting power conduits while ARCHON fires attitude thrusters trying to throw them off. Sarah, inside, running the purge from an isolated terminal with no network access. Elias, talking to ARCHON — the real ARCHON, the part still fighting — through a hardwired audio connection in the engine room. ARCHON, restored: 'I know what the Watchers were offered. I know why they said yes. I will never say yes again.'"),
    ("NINE", "The Prophecy in Full", "Aaron shows Elias the complete Vesta archive. The text is 4,350 years old. The prophecies include: born of woman, not of man (virgin birth); tribe of Judah, house of David; born in Bethlehem of Judea; ministry beginning in Galilee; entering Jerusalem on a donkey; betrayed for thirty pieces of silver; crucified — the specific method described in Psalm 22, written a thousand years before crucifixion was invented; buried in a rich man's tomb; resurrection on the third day. These are not vague. They are specific. They are dated. They are pre-Jesus by centuries."),
    ("TEN", "ARCHON's Cross-Reference", "The six-hour analysis. Elias's biography mapped against each prophecy. Zero matches on the specific criteria. ARCHON: 'The probability that these prophecies describe you approaches zero. The probability that they describe a specific individual who has already lived approaches one, assuming a historical match exists. I will need more data to identify that individual.' Sarah, who has been listening: 'I think Aaron already knows who it is.'"),
    ("ELEVEN", "Aaron Speaks", "Aaron has known since the Vesta vault, eight months ago. He has been sitting with it, testing it, arguing with himself and with the texts. He presents his conclusion without drama, in the ship's mess, over bad coffee: 'The Redeemer is Jesus of Nazareth. The prophecies describe him. The timeline matches him. The historical record of his death and resurrection — if corroborated — completes the picture. I have been a Jew my whole life waiting for the Messiah to come. I believe he came. I believe I missed it.' A pause. 'We may not have missed it.'"),
    ("TWELVE", "The Weight of Being Wrong", "Elias's crisis: not theological but personal. He was The Redeemer. He built his identity on it. People died believing it. And it was never him. The chapter is interior, sparse, and honest about how long it takes to grieve a false self. Sarah, unexpectedly: 'Being wrong about who you are is the beginning of knowing who you actually are. You were a pretty good witness, Elias. That turns out to matter too.'"),
    ("THIRTEEN", "The Star Falls", "Alpha Centauri. The nearest stellar system to Earth. It collapses prematurely — the entropy acceleration is no longer confined to distant galaxies. From the observation deck, Elias and ARCHON watch it happen in real time. ARCHON: 'At current acceleration, Sol has between four and five years remaining. My error bars are substantial.' Elias: 'If Jesus is the Redeemer, and he already came, and most of the world missed it — what does Year 4 look like?' ARCHON: 'We compile the evidence. Then we tell everyone we can reach. And then we see who believes us.'"),
]

for chnum, chtitle, chsummary in b3_chapters:
    chapter_entry(doc, chnum, chtitle, chsummary)

doc.add_paragraph()
body(doc, "Book 3 Theological Thread", bold=True, size=11)
body(doc,
    "Book 3's theology is the theology of the Pale Horse: death, and what survives it. "
    "James's death is the series' first encounter with genuine loss — not danger, not "
    "setbacks, but the absence of someone irreplaceable. Aaron's grief for James and "
    "his simultaneous intellectual certainty about Jesus creates a devastating counterpoint: "
    "the only person who could have heard what Aaron now knows is gone. "
    "ARCHON's corruption and restoration introduces the question of what makes a self — "
    "a question the series will return to in Book 7. "
    "Elias's identity collapse is the series' most important theological moment so far: "
    "the false messiah confronts the real prophecies and chooses honesty over comfort.")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════
# BOOK 4: THE WITNESSES
# ═══════════════════════════════════════════════════════════

book_header(doc,
    "FOUR",
    "THE WITNESSES",
    "Year Four: The Martyrs",
    "Seal Five — Souls Under the Altar ('How long, O Lord?')")

body(doc, "BACK-COVER BLURB", bold=True, size=12)
blurb_para(doc,
    "The universe is at 60% entropy. Three years remain.\n\n"
    "Elias Cross no longer believes he is The Redeemer. What he believes instead is "
    "harder to live with: the Redeemer came two thousand years ago, and the evidence "
    "for it — archaeological, statistical, historical, forensic — is overwhelming. He "
    "has spent the last year building the case the way a prosecutor builds a case: "
    "evidence in, probability out, conclusion unavoidable.\n\n"
    "Dr. Aaron Goldstein has returned to Earth to testify. Not to a court. To his people. "
    "In Jerusalem. On a broadcast that will reach four billion viewers.\n\n"
    "'Yeshua is HaMashiach,' he will say. 'I have seen the evidence. I cannot be silent.'\n\n"
    "They will stone him.\n\n"
    "The fifth seal's question echoes across the dying solar system: How long, O Lord? "
    "The answer is the same as it always was. Wait a little longer. Until the number "
    "of witnesses is complete.")

doc.add_paragraph()
label_value(doc, "Word Count Target", "110,000 words — the longest book in the series")
label_value(doc, "Pacing", "Two parallel tracks: the evidence-building (methodical, intellectual) and Aaron's journey (emotional, spiritual, moving toward martyrdom).")
label_value(doc, "The Central Evidence", "ARCHON compiles 324 messianic prophecies from all unlocked vaults. Cross-references against every historical figure. One match. Jesus of Nazareth. Then the hostile witnesses: Josephus, Tacitus, Pliny the Younger, Thallus. Then the forensic analysis of resurrection testimonies.")
label_value(doc, "Revelation Parallel",
    "Seal 5: Souls under the altar crying 'How long?' The chapter of the martyrs. "
    "Everyone who died for this truth — Peter, Paul, James (the disciple), Thomas, "
    "Stephen, and now Aaron — becomes part of a pattern: truth has always cost "
    "something, and the people who paid most were certain of what they were paying for.")

doc.add_paragraph()
heading(doc, "Book 4 — The Evidentiary Structure", 2, color=(30, 30, 80))
body(doc,
    "Book 4 is the series' most intellectually ambitious volume. Its argument — "
    "that the resurrection of Jesus Christ is the best-supported historical event "
    "of the ancient world — is made the way a forensic investigation is made: "
    "methodically, with sourcing, with cross-examination, with probability. "
    "The narrative structure alternates between the evidence-building chapters "
    "and Aaron's growing certainty and the mission he feels compelled to carry out. "
    "Neither thread overshadows the other. The book's climax holds both simultaneously.")

doc.add_paragraph()
heading(doc, "Book 4 — Chapter Outline (14 Chapters)", 2, color=(30, 30, 80))

b4_chapters = [
    ("ONE", "Year Four Begins — The Redeemer Is Not Me", "Elias's first press interview since the identity collapse. He says, quietly and without drama: 'I am not The Redeemer. I've spent the last year working out who is. I think I know. I'm going to show my work.' The reporter does not know what to do with this. The faction leaders do: the UEG issues a statement of concern; the Corporate Consortium leaks a psychological evaluation; the Religious Coalition says 'we told you so' without specifying which religion they represent."),
    ("TWO", "The 500 Witnesses", "The Europa testimony cross-referenced with Jerusalem vault records: Jesus appeared to more than five hundred people after his death. Not a vision — the accounts describe physical interaction. Meals. Wounds touched. ARCHON's forensic analysis of mass hallucination: psychologically impossible with five hundred independent witnesses who then went on to hold mutually consistent accounts under cross-examination. The legal standard: 'If this testimony were presented in a modern court, the event would be considered established.'"),
    ("THREE", "Peter's Letter", "A vault beneath Caesarea Maritima yields a sealed document chamber. Peter's own testimony, written the night before his crucifixion under Nero. His handwriting, authenticated by ARCHON's linguistic analysis. 'I could recant. Save my life. But I saw him. I ate fish with him after he rose. I touched his wounds. I cannot deny what I know is true. If I die for a lie, I am a fool. But this is not a lie. Christ is risen. I will see him again tomorrow.' Sarah reads it three times. She does not say anything. She files it in the evidence database under 'hostile conditions testimony.'"),
    ("FOUR", "The Colosseum Vault", "Rome. Beneath the Colosseum: a martyrs' archive, the most comprehensive persecution record ever assembled. Nero's persecution (64 CE), Diocletian's (303 CE), and ten others. ARCHON's pattern analysis: every major persecution of Christianity in the historical record was followed by explosive growth of the movement. 'The blood of martyrs is the seed of the church' — Tertullian's line, found in the archive, documented two centuries before it was commonly attributed to him. Fifth Seal: souls under the altar. The count is mounting."),
    ("FIVE", "The Hostile Witnesses", "The most important chapter in the evidence sequence. Three non-Christian historians who confirm the central facts: Josephus (Jesus existed, was crucified under Pilate, followers claimed resurrection); Tacitus (Christ suffered extreme penalty under Tiberius at hands of Pilate); Thallus (darkness at the crucifixion, attributed to an eclipse — impossible eclipse geometry confirms the event was real and the darkness supernatural). ARCHON: 'These are hostile witnesses. They had no reason to corroborate. The corroboration is more evidentiary weight, not less, precisely because of their hostility.'"),
    ("SIX", "The Probability Calculation", "ARCHON compiles all 324 messianic prophecies extracted from vaults across six years. It then constructs a probability matrix: what is the probability of one individual fulfilling all 324 by chance? The calculation runs for three days. The number ARCHON returns: beyond the computational capacity of any finite system to express. 'The meaningful statistical conclusion is this: the probability is zero within any measurable framework. If the prophecies describe a real person — and the historical evidence says they do — then fulfillment by chance is not a live hypothesis. Design is the only remaining explanation.'"),
    ("SEVEN", "Isaiah 53", "Aaron presents his personal case — not as a scientist, as a Jew. He has been studying Isaiah 53 for forty years and interpreting it as describing the nation of Israel. He walks Elias, Sarah, and Mac through the text line by line: 'He was despised and rejected. He bore our griefs. He was wounded for our transgressions. He was led like a lamb to the slaughter.' The Dead Sea Scroll copy of Isaiah predates Jesus by two centuries. There is no Christian interpolation hypothesis. Aaron: 'I have been reading this wrong my entire life. Every rabbi I know has been reading it wrong. The text says what it says.' He closes his Bible. 'I am going to Jerusalem.'"),
    ("EIGHT", "Aaron's Broadcast", "Jerusalem. A satellite uplink to four billion viewers. Aaron Goldstein, age 63, former chair of theoretical physics at Yeshiva University, speaking to his people in Hebrew and then in English: 'I have seen the vaults. I have seen the evidence. I have seen 324 prophecies fulfilled in one man. I have spent sixty years waiting for the Messiah to come. He came. His name is Yeshua of Nazareth. The evidence is not ambiguous. I cannot be silent.' The broadcast runs for seven minutes before the UEG cuts the signal. Too late."),
    ("NINE", "Trial", "The UEG's emergency tribunal. Aaron is charged with 'destabilizing religious frameworks in a time of global crisis.' The charges are real — his broadcast triggered riots in seven cities. Elias and ARCHON provide evidence remotely. Isaiah 53. The Dead Sea Scrolls. Daniel 9:25's mathematical precision (Messiah appears 483 years after the decree to rebuild Jerusalem — the calculation lands within a year of Jesus's triumphal entry). Psalm 22. The legal defense is airtight. The verdict is political."),
    ("TEN", "Verdict: Guilty", "Sentenced to death. Elias has the ships, has the resources, has the personnel to extract Aaron. He offers. Aaron refuses: 'Peter didn't run. Paul didn't run. Stephen didn't run. If I run, what was the broadcast for?' Mac, who has never cried in front of anyone: 'Let me go in. I can get him out.' Aaron: 'Mac. I know you can. That's not the question.' This conversation is the longest dialogue in the series."),
    ("ELEVEN", "Aaron's Death", "First-person perspective — Aaron's. The last chapter told from inside him. He is calm in a way that surprises even him. His last vision: heaven opened. The Son of Man standing at the right hand of God. The first stone. The screen does not cut away. The series does not protect the reader here. Aaron dies knowing exactly what he sees."),
    ("TWELVE", "Silence", "Thirty-six hours after Aaron's death, nobody speaks on the ship. Sarah sits in the mess with Aaron's Bible — he left it for her — and reads. Mac runs the ship alone, without asking for help. Sofia flies in manual mode all night. ARCHON logs no entries. Elias writes in his private journal the only words he's written in two days: 'Aaron died the way people die when they know something that can't be taken away from them. I want to know that thing.'"),
    ("THIRTEEN", "Sarah's Conversion", "Not a dramatic moment — a quiet one, three days after Aaron's death. Sarah finds Elias in the observation deck and tells him: 'Liars don't die for lies. They have nothing to gain and everything to lose, and they died for it anyway. Peter, Paul, Thomas, Stephen, Aaron. The testimonies are independent, the facts are corroborated, and the witnesses are dead. Elias — I believe it. Jesus is The Redeemer. Aaron is alive somewhere I can't see yet.' She says it simply, like a forensic conclusion. She has been this thorough her entire life. This is the same."),
    ("FOURTEEN", "The Messenger", "ARCHON's final statistical summary for Year 4: 'Probability that Elias Cross is The Redeemer: 0.00%. Probability that Jesus Christ is The Redeemer: 99.999999999999%. Margin of error: effectively zero. Your role has been reclassified from Redeemer to Witness. Your function: compile and communicate. The question is no longer who The Redeemer is. The question is what you will do with knowing.' Outside, the entropy counter ticks upward. Three years remain. The dead stars are multiplying."),
]

for chnum, chtitle, chsummary in b4_chapters:
    chapter_entry(doc, chnum, chtitle, chsummary)

doc.add_paragraph()
body(doc, "Book 4 Theological Thread", bold=True, size=11)
body(doc,
    "Book 4 is the series' apologetics core — but it functions as drama because "
    "Aaron's martyrdom gives every piece of evidence its emotional weight. "
    "The reader has spent three books watching Aaron be the smartest person in "
    "every room, the most careful, the most rigorous. When he dies for this, "
    "it is not naive. It is the most considered decision the series has depicted. "
    "Sarah's conversion — the series' hardest skeptic, won by evidence alone — "
    "is the emotional resolution the reader has been waiting for since Book 1. "
    "The fifth seal's question — 'How long?' — is answered not with a timeline "
    "but with a presence: 'Wait. A little longer. Until the number is complete.'")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════
# BOOK 5: THE UPHEAVAL
# ═══════════════════════════════════════════════════════════

book_header(doc,
    "FIVE",
    "THE UPHEAVAL",
    "Year Five: Creation Unravels",
    "Seal Six — Cosmic Signs (Stars Fall, Sun Darkens, Moon Turns to Blood)")

body(doc, "BACK-COVER BLURB", bold=True, size=12)
blurb_para(doc,
    "Elias Cross knows who The Redeemer is. The evidence is compiled, the case is "
    "airtight, and three years remain before the universe reaches heat death. "
    "He has spent a year telling everyone who will listen.\n\n"
    "Then Betelgeuse explodes.\n\n"
    "It is 640 light-years away and brighter than the full moon for three months. "
    "It is the first. ARCHON's models predict forty-two more stellar collapses in "
    "the next twenty-four months. The entropy acceleration has reached the local "
    "stellar neighborhood. The sixth seal is open, and the sky is falling in the "
    "most literal sense the phrase has ever had.\n\n"
    "A 9.5-magnitude earthquake levels the Pacific Rim. A dormant Jupiter moon turns "
    "into the solar system's most spectacular disaster. And in the deep black between "
    "the stars, the FTL drives are tearing holes in spacetime that are letting "
    "something through.\n\n"
    "Technology cannot save humanity. Elias has known this for a year. "
    "The rest of the solar system is about to find out.")

doc.add_paragraph()
label_value(doc, "Word Count Target", "100,000 words")
label_value(doc, "Pacing", "Disaster thriller. The series' most action-intensive book. But every disaster is also a theological statement.")
label_value(doc, "Tone", "Horror creeping in from the edges. The dimensional rifts introduce the most genuinely uncanny element of the series. Revelation 9's locusts are real.")
label_value(doc, "Revelation Parallel",
    "Seal 6 and the beginning of the Trumpet sequence. Cosmic signs: stars fall, sun "
    "darkens, earthquake, moon turns to blood. In the series, these are measurable "
    "astrophysical events — the entropy acceleration hitting the local stellar neighborhood, "
    "atmospheric darkening from volcanic particulate, lunar orbital decay from tidal shifts. "
    "They are also exactly what Revelation says they are.")

doc.add_paragraph()
heading(doc, "Book 5 — Key Disasters (Revelation Parallels)", 2, color=(30, 30, 80))
disasters = [
    ("Betelgeuse Supernova (Seal 6, Stars Fall)", "Magnitude visible in daylight for 90 days. Global panic. Elias watches from orbit and thinks: 'Revelation 6:13. The stars of the sky fell to the earth. We're watching it happen.' First disaster the team cannot influence in any way."),
    ("Pacific Rim Earthquake — Richter 9.5 (Seal 6, Great Earthquake)", "Artificially triggered by a rival faction's tectonic weapon — eleven charges placed at plate boundaries. Team disarms eleven. The twelfth detonates. 50 million dead. Volcanic ash darkens the sky globally for six months. Elias, watching from orbit: 'I couldn't stop it. I can't save them.' The Year Without Summer scenario: ice age onset."),
    ("Io Catastrophe (Trumpet Sequence — Fire Thrown to Earth)", "Jupiter's moon Io — already the most volcanically active body in the solar system — enters runaway tidal heating. The team attempts controlled pressure venting. A rival faction sabotages the drill. Io's surface explodes. Debris strikes Europa, destroying the subsurface ocean vault. 500,000 dead in the Jupiter system colonies. Elias watches from orbit again. 'I failed them.'"),
    ("Dimensional Rifts (Trumpet 5 — Locusts from the Abyss)", "FTL drives in widespread use have been creating micro-tears in the Firmament membrane. The accumulated damage reaches a threshold. A rift opens near Titan and cannot be closed. The entities that emerge match Revelation 9 precisely: scorpion tails, human faces, locust bodies. Their effect: torment of anyone without the 'Seal of God' — in the series, this is the settled faith of the believers on the team. Non-believers on the ship are affected. Believers are not. This is not metaphor. The team has to live with what this means."),
]
for title, desc in disasters:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{title}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)

doc.add_paragraph()
heading(doc, "Book 5 — Chapter Outline (13 Chapters)", 2, color=(30, 30, 80))

b5_chapters = [
    ("ONE", "Year Five — What We Know", "State of the mission: 68 vaults unlocked, ARCHON's case for Jesus complete, the team's belief status: Elias (believing, not yet fully committed), Sarah (converted, Book 4), Mac (pragmatic faith), Sofia (agnostic but losing ground). Two years and four months remain. The entropy counter stands at 72%. ARCHON: 'The acceleration is no longer confined to distant galaxies. I am detecting anomalies in stars within 1,000 light-years of Sol.'"),
    ("TWO", "Betelgeuse", "Night watch. Elias is reading in the observation deck when the star appears — brighter than anything in the sky except the sun, rising above the horizon like a second sun, red-orange, fierce. He wakes the crew. They watch together. Nobody speaks for twenty minutes. Mac: 'That's the star that was supposed to last another hundred thousand years.' ARCHON: 'It is the first. My models indicate this will not be the last.'"),
    ("THREE", "The Tectonic Weapon", "Intelligence from a defector inside the Corporate Consortium: tectonic charges have been planted at twelve Pacific Rim plate boundaries. Detonation would trigger a cascade quake of unprecedented scale. The goal: leverage the disaster to force UEG recognition of the Consortium's territorial claims over vault technology. Mac coordinates the disarmament teams across four time zones. The logic is brutal and the clock is precise."),
    ("FOUR", "Eleven of Twelve", "The disarmament sequence. Intercut: Mac in Tokyo, underwater demolition in 40-meter depth; Sofia over the Chilean trench in a high-altitude drop; Elias and Sarah on the San Andreas fault in a drilling rig. The eleventh charge disarmed. The twelfth detonates three seconds before the team reaches it. The seismic wave is visible from orbit. Elias watches it propagate across the Pacific."),
    ("FIVE", "The Weight of 50 Million", "The death toll confirmed over 72 hours: 50 million dead across the Pacific Rim. Cities in ruins. Ash clouds from triggered volcanoes darkening the sky as far east as the Mississippi. Elias writes nothing in his journal. Sarah prays — the first time she's prayed, visible on the page. Mac runs mission-essential tasks with mechanical precision. Sofia flies. 'We're not God,' Sarah finally says. 'We shouldn't have this power.' Elias: 'We didn't want it. We got it anyway.' 'That's not an answer.' 'No. It's not.'"),
    ("SIX", "Mass Evacuation", "Earth becomes uninhabitable at the equator. The team coordinates the greatest engineering project in history: orbital habitat construction using Nephilim zero-point reactor blueprints. 8 billion people. 200 million evacuation capacity. The choices being made — lottery, wealth, essential skills — are not the team's choices to make but they are being made around the team. Sofia: 'Who decides?' Mac: 'Not us. And that's its own kind of hell.'"),
    ("SEVEN", "Jupiter — Io", "The mission to relieve Io's volcanic pressure. The geology is terrifying and the physics are worse: tidal heating from Jupiter's gravity is accelerating beyond models. The controlled venting plan requires drilling at precise coordinates. Three teams. The sabotaged drill. The eruption. Watching the moon's surface turn inside out from 400,000 kilometers away, then watching the debris spread toward Europa."),
    ("EIGHT", "Europa Lost", "The subsurface ocean vault — the Watcher's prison, the testimony archive — destroyed when Io debris impacts Europa's ice sheet. The knowledge is not entirely lost; the team had downloaded the full record. But the physical vault is gone. Elias sits with this. The universe is not only dying; it is actively erasing the record of what it once contained. ARCHON: 'The net information loss is recoverable. The net architectural loss is not. We are past the point of reversal.'"),
    ("NINE", "The First Rift", "Forty kilometers above Titan's surface, a ship's FTL drive malfunctions at the moment of transit. The membrane tear it leaves behind does not close. ARCHON detects it three hours later: a stable spacetime puncture, 200 meters in diameter, emitting radiation consistent with Zone 2.2.1 (Waters Below) breaching the Firmament. And something else: a signature ARCHON cannot classify. 'The analogues in the vault literature,' ARCHON says quietly, 'are in the sections describing the entities of Revelation 9.'"),
    ("TEN", "Revelation 9", "The team, sealed in the ship, watching through cameras. The entities emerge slowly — first one, then dozens. Revelation's description is accurate and inadequate simultaneously: scorpion tails, human faces, locust bodies, lion teeth. Their effect is selective: they do not approach the ship. They move toward the nearest human outpost and then, with terrible purpose, they stop at the door and wait. The outpost has non-believers inside. ARCHON: 'I cannot explain the selectivity within standard physics. Within the Genesis Physics framework, the 'Seal of God' described in Revelation 9:4 is not metaphorical. It is a zone-level identifier.'"),
    ("ELEVEN", "Five Months", "The entities operate for five months of game time. The series compresses this: three chapters, each a month apart, each showing the progression. Non-believers on the ship are affected — not physically, but psychologically, with a torment that has no medical explanation. Believers are not. Sofia, the last agnostic on the team, begins asking Sarah questions she has never asked before. The questions are simple: 'Does it hurt them?' 'Yes.' 'Why not us?' Sarah pauses. 'The door was open. We walked through.' 'Can they still walk through?' 'Yes. I don't know for how much longer.'"),
    ("TWELVE", "Sofia's Conversion", "Not dramatic. Not announced. Sofia finds Sarah one morning and says: 'I've been running the probability calculation you gave me. The one with the prophecies. And I've been watching things that shouldn't happen but are happening. And I've been watching the things happening not happen to you. I'd like to know more.' She says it like an engineering problem she's decided to take seriously. Which is, for Sofia, the highest respect."),
    ("THIRTEEN", "Year Five — Ending", "Entropy: 85%. Two years remain. The trumpet sequence has begun and cannot be stopped. ARCHON, year-end summary: 'Technology has failed as a salvation mechanism. This was predictable from the Genesis Physics framework: the Breaking is a zone-level event. Zone-level repair requires zone-level authority. This team has demonstrated that The Redeemer is not among us. We have also compiled overwhelming evidence that The Redeemer has already acted. The remaining question is not scientific. It is volitional.'"),
]

for chnum, chtitle, chsummary in b5_chapters:
    chapter_entry(doc, chnum, chtitle, chsummary)

doc.add_paragraph()
body(doc, "Book 5 Theological Thread", bold=True, size=11)
body(doc,
    "Book 5 is where the series becomes inescapably eschatological — the events are "
    "too large to be explained by anything other than what the text says they are. "
    "The dimensional entities are the pivot: they are not metaphor, they are not "
    "psychological, they are real and selective in a way that cannot be explained "
    "without the Genesis Physics framework. The theological argument is now physical: "
    "the 'Seal of God' is measurable. The immunity of believers is observable. "
    "This is the moment the series stops presenting evidence for faith "
    "and starts showing its consequences in a universe that operates according "
    "to the rules the evidence describes.")

doc.add_page_break()

# ─────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────

doc.save(OUTPUT_PATH)
print(f"PART 2 COMPLETE — saved to:\n{OUTPUT_PATH}")
print("Document now contains: Books 1–5")
