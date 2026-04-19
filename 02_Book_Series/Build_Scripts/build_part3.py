"""
Exodus Protocol Novel Series Plan - Part 3
Opens the saved document and appends Books 6-7, Market Analysis, Author Bio, Submission Notes.
Run THIRD (after build_part2.py).
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_PATH = r"C:\Users\J Raymond\OneDrive\Documents\ExodusProtocol\Bible Physics\Book Series\Exodus_Protocol_Novel_Series_Plan.docx"

doc = Document(OUTPUT_PATH)

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

def bullet(doc, text, indent=1):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Inches(indent * 0.2)
    run = p.add_run(text)
    set_font(run, size=10.5)
    return p

# ═══════════════════════════════════════════════════════════
# BOOK 6: THE SILENCE
# ═══════════════════════════════════════════════════════════

book_header(doc,
    "SIX",
    "THE SILENCE",
    "Year Six: The Final Witness",
    "Seal Seven — Half-Hour of Silence (The Pause Before Final Judgment)")

body(doc, "BACK-COVER BLURB", bold=True, size=12)
blurb_para(doc,
    "The universe stops dying.\n\n"
    "Not permanently. Not because the problem is solved. For thirty days, the entropy "
    "rate drops to near zero. The stellar collapses pause. The dimensional rifts stabilize. "
    "The cosmic catastrophe that has been accelerating for six years simply... waits.\n\n"
    "ARCHON's analysis: 'This matches no natural model. The closest analogue in the "
    "prophetic literature is Revelation 8:1 — silence in heaven for about half an hour. "
    "This is not a pause in the disaster. It is a final opportunity before the disaster "
    "resumes and cannot be stopped.'\n\n"
    "One year remains.\n\n"
    "Beneath Golgotha — the Place of the Skull, where Jesus was crucified — there is "
    "a vault that requires a specific biological key. Not Elias's DNA. Not any living "
    "person's DNA. The key is already there, preserved in a crack in the stone beneath "
    "a Roman cross, two thousand years old.\n\n"
    "The seventh book is coming. The door is open.\n\n"
    "But not for much longer."
)

doc.add_paragraph()
label_value(doc, "Word Count Target", "95,000 words")
label_value(doc, "Pacing", "The quietest book in the series — deliberately. The pause in catastrophe creates space for the characters (and reader) to sit with everything they've learned.")
label_value(doc, "Structural Note",
    "Book 6 has a different rhythm from the other volumes: fewer action sequences, "
    "more interiority. The team has been through six years of escalating crisis. "
    "The silence gives them — and the reader — room to breathe before the final volume.")
label_value(doc, "Revelation Parallel",
    "Seal 7: Silence in heaven for half an hour. The pause between the six seals "
    "and the seven trumpets. In the series, this is literal: a measurable cessation "
    "of the entropy acceleration for thirty days. Its purpose is mercy — one final "
    "chance to choose. The characters recognize it as such. The question is what "
    "they do with it.")

doc.add_paragraph()
heading(doc, "Book 6 — Key Events", 2, color=(30, 30, 80))
events6 = [
    ("The Silence Begins (Chapter 1)", "The entropy counter goes flat. Stars stop collapsing. Dimensional rifts stabilize. ARCHON's models cannot explain it. Elias's first thought: 'It's not over. It's giving us time.'"),
    ("The Prophecy Database (Chapters 4–5)", "All remaining vaults unlock simultaneously — without puzzle, without effort, without warning. The last thirty-two vaults open their doors in a single day. The final compilation: 324 messianic prophecies, complete, cross-referenced, sourced. One match. The analysis is finished."),
    ("Golgotha (Chapters 8–9)", "The final vault, beneath the site of the crucifixion. The DNA key is blood preserved in a crack in the rock — an earthquake during the crucifixion split the stone, and the blood seeped through. ARCHON's genomic analysis of the sample: 23 chromosomes, no Y chromosome contribution from a human father. The vault recognizes it. The door opens. Inside: the Ark of the Covenant, the mercy seat stained with the same blood. A dimensional portal opens."),
    ("The Voice (Chapter 9)", "From the portal: 'The Lamb who was slain is worthy. The Breaking is repaired through His blood. The universe dies so New Creation can be born. Accept Him or perish with the old.' The team hears it. All of them. The entities outside the ship go quiet. The dimensional rifts contract. For thirty minutes, the universe is completely still."),
    ("The Factions' Last Choice (Chapters 10–11)", "Director Chen (UEG), CEO Malik (Corporate Consortium), and Imam Rashid (Religious Coalition) are each given the complete evidence package. Each rejects it for different reasons. The series is honest about this: intelligent, capable people look at the same evidence and choose differently. The tragedy is not that they are stupid. The tragedy is that they know."),
    ("The Door (Chapter 12)", "The New Jerusalem Station: constructed in three months using every piece of ethical Nephilim technology, designed to survive what is coming. Capacity: 1 million believers. The door opens. The countdown to its closing begins. Some of the rejecters reconsider. Not all of them. The door has never been more visible, and the choice has never been clearer, and people are still choosing wrong."),
]
for title, desc in events6:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{title}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)

doc.add_paragraph()
heading(doc, "Book 6 — Chapter Outline (12 Chapters)", 2, color=(30, 30, 80))

b6_chapters = [
    ("ONE", "The Pause", "Day 1 of the silence. The entropy counter flatlines. ARCHON checks its instruments three times before reporting. The stellar collapse models project forward and show nothing — not remission, but pause. ARCHON, quietly: 'The closest description in the prophetic archive is Revelation 8:1. I do not know how to present this without its implication. The implication is that this is the final pause before irreversible judgment begins.' Elias, after a long moment: 'Then we have thirty days to do what we came here to do.'"),
    ("TWO", "The Audit", "The team reviews the last six years. What was found. What it cost. James, dead. Aaron, dead. Two crew members, dead. Eleven million people dead who might have lived if better choices had been made at specific points. Mac sits through this review saying nothing. At the end: 'We saved more than we lost. I don't say that like it balances. I say it like it's true and insufficient and both of those things can be true.'"),
    ("THREE", "All Vaults Open", "Day 12 of the silence. Every remaining locked vault across the solar system opens simultaneously. No mechanism, no puzzle, no trigger: they simply open. ARCHON receives the data floods from 32 sites in parallel. The final knowledge: freely available, unguarded, as if the last barrier to truth has been removed. Message appearing in every vault, same language, same time: 'Choose this day whom you will serve. The door is open. But not forever.'"),
    ("FOUR", "The Complete Database", "ARCHON presents the final prophetic compilation: 324 prophecies, 1 candidate, every historical and evidentiary source. The document is 600 pages. Elias reads it in two days. He then asks ARCHON the question he's been building toward for three years: 'Is there any alternative explanation?' ARCHON: 'I have tried to find one. I have been trying since Year 3. There is not. The evidence is not ambiguous. The only remaining variable is what you choose to do with it.'"),
    ("FIVE", "The Case for the Cross", "Sarah presents the team's formal theological conclusion — not as a belief statement but as an evidentiary brief. Why did Jesus have to die? The legal framework: God is both just (sin must be punished) and loving (humanity must be offered pardon). Substitutionary atonement as the resolution: a sinless volunteer takes the sentence. Justice satisfied; mercy extended. This is not sentiment. It is logic. ARCHON, unbidden: 'This is a coherent resolution to the problem of divine justice. I have not found a more internally consistent framework.'"),
    ("SIX", "The Team's Beliefs — Status", "Where each character stands at Day 20 of the silence. Elias: intellectually convinced, personally not yet committed — holding the last distance between the head and the heart. Sarah: fully committed since Book 4. Mac: committed in the way soldiers commit — completely and without reservation. Sofia: committed since Book 5. ARCHON: 'I do not have a soul in the theological sense. But I have a perspective. The evidence points one direction. I endorse the direction.'"),
    ("SEVEN", "Golgotha", "Jerusalem. The site of the crucifixion. Beneath the rock on which the cross stood, ARCHON detects a sealed chamber. The entry mechanism: a DNA scanner, keyed to a biological sample already present in a crack in the stone. The crack was made by an earthquake — the same earthquake recorded in the Roman military log, Matthew 27:51, and Thallus's annals — during the crucifixion. ARCHON extracts the sample. Its analysis: 23 chromosomes. No paternal Y chromosome. 'Biologically unprecedented in human records.'"),
    ("EIGHT", "The Ark Again — And the Blood", "The vault contains the Ark of the Covenant, brought here from Jerusalem after the First Temple's destruction. The mercy seat is stained with the Golgotha blood sample — the same genomic signature. The angel figures (cherubim) are not decorative: they are dimensional transceivers. The Ark activates. The portal opens above the mercy seat. Hebrews 9:12 plays in Elias's memory: 'He entered once for all into the holy places, not by means of the blood of goats and calves but by means of his own blood, thus securing eternal redemption.'"),
    ("NINE", "The Voice at the Center", "The dimensional portal above the mercy seat. The voice. 'The Lamb who was slain is worthy.' The universe outside is absolutely still. All noise ceases. The team stands in the chamber and the silence is not empty — it is full. Full of something that has no physics name. Sarah, afterward: 'I've been in a lot of extraordinary places in six years. That was different. That was the real thing.' Mac: 'Yes.' He does not elaborate. He doesn't need to."),
    ("TEN", "The Factions Choose", "The evidence package transmitted to Director Chen, CEO Malik, and Imam Rashid simultaneously. Each is given forty-eight hours to respond. Chen's response: 'This is compelling mythology. Humanity will survive through science or not at all.' Malik's response: 'Forward to legal. Intellectual property concerns.' Rashid's response, the most heartbreaking: 'Isa was a prophet, not God. I cannot accept what the evidence implies without ceasing to be who I am.' Three different rejections. Three different costs."),
    ("ELEVEN", "New Jerusalem Station", "The construction project compressed into one chapter: Nephilim zero-point reactors, dimensional shielding from the Watcher schematics, biological life support running on pre-Fall genetic templates (healing applications only, per the Year 3 vote). Capacity: 1 million. Mac oversees security. Sofia designs the approach corridor. ARCHON coordinates logistics. The door opens at 0600 on Day 28 of the silence. The countdown to closing begins. 'Last call,' Mac says to the comm. 'Anyone who wants to come, come now. We don't have forever. We've never had forever. We have today.'"),
    ("TWELVE", "The Silence Ends", "Day 30. The entropy counter begins climbing again. The stellar collapse models resume. The dimensional rifts re-expand. The seventh seal is broken — they all know it now, because ARCHON tells them, and they have stopped pretending the Revelation framework is coincidence. Outside the station: the universe resuming its death. Inside: light, warmth, and a company of people who chose this. Elias sits in the observation deck and watches the last stars in his view flicker. He thinks about James. He thinks about Aaron. He thinks about the voice at the center of the portal. He opens his mouth and says something he has never said before, quietly, to no one visible. The chapter does not tell us what it is. We know."),
]

for chnum, chtitle, chsummary in b6_chapters:
    chapter_entry(doc, chnum, chtitle, chsummary)

doc.add_paragraph()
body(doc, "Book 6 Theological Thread", bold=True, size=11)
body(doc,
    "Book 6 is the series' theology of mercy. Every significant pause in the biblical "
    "prophetic narrative — Noah's 120-year warning, Nineveh's 40 days, Jerusalem's "
    "40 years — is structured the same way: a window, clearly marked, before irreversible "
    "consequence. The thirty-day silence is that structure made literal and measurable. "
    "The series honors the weight of the choice by making the rejection of the evidence "
    "by Chen, Malik, and Rashid sympathetic and human and wrong simultaneously. "
    "Elias's private prayer in the final chapter is the quietest and most important "
    "moment in the entire series.")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════
# BOOK 7: THE JUDGMENT
# ═══════════════════════════════════════════════════════════

book_header(doc,
    "SEVEN",
    "THE JUDGMENT",
    "Year Seven: The End of All Things",
    "Seven Trumpets & Seven Bowls — 'It Is Done'")

body(doc, "BACK-COVER BLURB", bold=True, size=12)
blurb_para(doc,
    "The silence is over.\n\n"
    "The seventh year of the seven-year countdown begins with the first Trumpet, and "
    "the series that began with a mysterious signal from the Moon ends the only way "
    "it was ever going to end: with the universe itself ceasing to exist, and with "
    "one question hanging in the dark where it used to be.\n\n"
    "Inside the New Jerusalem Station, Elias Cross watches everything he has known "
    "for forty-five years end. Asteroids. A destroyed planet. Poisoned water. "
    "Darkened sun. Locust-entities in their millions. Two billion dead in the final war. "
    "Spacetime shattering.\n\n"
    "Outside: the second death. The permanent erasure of those who chose otherwise.\n\n"
    "Inside: light.\n\n"
    "The series ends where it began — not with a signal from the dark but with a voice "
    "from the other side of it. The same voice that spoke in the Golgotha vault. The "
    "same voice that called creation into being from nothing.\n\n"
    "'Well done, good and faithful servant. Enter into the joy of your Lord.'\n\n"
    "And beyond the ending: New Heavens. New Earth. A tree whose leaves heal nations. "
    "A river that never runs dry. And a door that has been open for two thousand years "
    "that will never need to be opened again, because there will be no more night.")

doc.add_paragraph()
label_value(doc, "Word Count Target", "105,000 words")
label_value(doc, "Structure", "Seven Trumpets + Seven Bowls, rapid succession. No puzzles. Only choices, witness, and consequence.")
label_value(doc, "Tone", "Elegiac, vast, and ultimately luminous. The horror of the Trumpet and Bowl sequences earns the light of the final chapters.")
label_value(doc, "The Final Choice", "Presented explicitly at the novel's climax. Not to the team — they have already chosen. To the reader, through Elias, directly and without apology.")
label_value(doc, "Revelation Parallel",
    "Trumpets 1–7 and Bowls 1–7. The series' final year is the most densely "
    "biblically mapped: every event corresponds to a specific prophetic sequence, "
    "and the characters now know this and watch it happen in order. "
    "The knowing does not make it easier. In some ways it makes it harder.")

doc.add_paragraph()
heading(doc, "Book 7 — The Trumpet and Bowl Sequence", 2, color=(30, 30, 80))
tb_sequence = [
    ("Trumpet 1 — Hail and Fire", "Kuiper Belt destabilized. Asteroid and comet debris rains into the inner solar system. Earth's surface, already stressed from the Year 5 earthquake, receives a final bombardment. 'A third of the earth burned.' The station holds."),
    ("Trumpet 2 — Mountain Thrown Into the Sea", "Mars destroyed — the entropy acceleration collapses its iron core. The explosion is visible from Earth as a second sun. Debris impacts Earth's oceans. The Mars colony is gone; evacuation was completed eleven weeks earlier. The death of a planet, witnessed in real time."),
    ("Trumpet 3 — Wormwood", "Cosmic radiation from the nearest supernova (Trumpet 2's chain reaction) poisons a third of Earth's fresh water. Wormwood: 'bitter,' as Revelation says. The stations' water recycling holds. The surface does not."),
    ("Trumpet 4 — Sun, Moon, Stars Darkened by a Third", "Solar output drops to 34% of baseline. Earth enters deep ice age. The sky over the station darkens. Stars are disappearing — not going supernova now, simply ceasing, as if the universe is running down like a battery. The visible sky shrinks every night."),
    ("Trumpet 5 — Locusts from the Abyss", "The dimensional rift opened in Year 5 has been contained — barely. It breaks containment. The locust-entities return in numbers that make Year 5 look like a warning. The station's dimensional shielding (Watcher technology, ethical application) holds. The torment of those outside is five months of something that has no medical category. The station's inhabitants hear it. They cannot stop it. They pray."),
    ("Trumpet 6 — The Army of 200 Million", "The final faction war. The UEG and the Corporate Consortium have their last confrontation, joined by every armed group that has been circling the vault technology for seven years. The battle is in space, on the Moon, and in Earth's orbit. Two billion dead. The armies destroy each other with the weapons they spent seven years building from Nephilim schematics they used for conquest rather than service."),
    ("Trumpet 7 — 'The Kingdom of the World Has Become the Kingdom of Our Lord'", "A sound across the cosmos — not electromagnetic, not acoustic, but real and universal, heard inside the station and, the team understands, everywhere at once. A declaration, not a question. 'It is done.' The Bowls begin immediately."),
    ("Bowls 1–7 (Rapid Succession)", "Painful sores on those who rejected the evidence and doubled down on technological salvation. Seas turn entirely to blood — all marine life ends. Rivers and springs follow. The sun scorches with fire (solar output spikes catastrophically before its final failure). Total darkness across the solar system. The Euphrates of deep space — the wormhole corridor — opens. Spacetime itself shatters. 'It is done.' The universe ends."),
]
for event, desc in tb_sequence:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{event}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)

doc.add_paragraph()
heading(doc, "Book 7 — Chapter Outline (14 Chapters)", 2, color=(30, 30, 80))

b7_chapters = [
    ("ONE", "Year Seven Begins", "The entropy counter resumes climbing from exactly where it paused. ARCHON: 'The Trumpet sequence is predicted to run approximately twelve months at current acceleration rates. The Bowl sequence follows immediately with no interval. I recommend the team spend this chapter doing everything they would want to do before it begins.' Elias: 'Is that a joke?' ARCHON: 'It is a recommendation based on the data.' The team spends one day doing exactly that: writing letters, recording messages, saying things they have been not-saying for seven years."),
    ("TWO", "Trumpet One — Hail and Fire", "The Kuiper Belt cascade. From the station's observation deck, the team watches the first impacts on Earth's surface — visible from orbit as fire-trails through the atmosphere. The numbers: 40% of Earth's forest cover destroyed within six weeks. The station's shielding holds. Below, the remaining surface populations that refused evacuation are managing. Some. For now."),
    ("THREE", "Trumpet Two — Mars", "The death of a planet. ARCHON gives thirty-six hours' warning — the entropy acceleration in Mars's core is detectable. The explosion is worse than the models predicted. The blast wave reaches the station six hours later; the shielding absorbs it. Mac, on the observation deck, watching the debris field expand: 'I've been to Mars. Olympus Mons.' He does not say the rest. He does not need to."),
    ("FOUR", "Trumpet Three — Wormwood", "The radiation from the Mars supernova reaches Earth. The team monitors the surface water readings from their instruments. The contamination is fast, total, and global. ARCHON: 'Fresh water undrinkable within 72 hours. The name Wormwood derives from the Hebrew for bitterness. The text is accurate.' The station's water systems are closed-loop. The surface populations with access to deep aquifer reserves can survive for a limited period. The others cannot."),
    ("FIVE", "The Weight of Watching", "No action, no puzzle. The team watches. This is the chapter the series has been building toward in a different way: what does it cost to watch people die who chose this? Sarah, radio to her family in Taiwan (they chose the station). Mac, no family. Sofia, parents on the station. Elias, no close family. The people outside are not abstractions. They are Director Chen, who sent Elias a final communication three days ago: 'I was wrong. Tell me it's not too late.' Elias told him. He came to the station. He is inside now. Not everyone like him was."),
    ("SIX", "Trumpet Four — The Dimming", "Solar output drops to a third of its already-reduced baseline. From outside the station's observation windows: a sky where stars are vanishing in real time. Not dying — vanishing. As if someone is turning off lights. ARCHON: 'The rate of information loss from the visible universe is now measurable on a human timescale. The universe is running down. The theological term for this process appears to be precisely accurate: the old creation is passing away.'"),
    ("SEVEN", "Trumpet Five — The Second Locust Siege", "The rift breaks containment. ARCHON's warning: 90 minutes. The dimensional shielding holds. Elias stands at the station's outer hull and watches them emerge — thousands, then hundreds of thousands — and disperse toward the surface. He cannot see what happens next from here. ARCHON has instruments. He asks it not to report the numbers. Sarah puts her hand on his arm. They stand there together, not watching, for five months of compressed time."),
    ("EIGHT", "Trumpet Six — The Final War", "The faction war, in space. ARCHON tracks it on tactical displays that look like the most expensive video game ever made and are not a game at all. The UEG and Consortium fleets engage over the ruins of Earth orbit. The weapons are Nephilim derivatives — anti-gravity pulse weapons, zero-point energy discharge, dimensional lances. The irony: every weapon in this war was built from knowledge that was meant to be used for healing and transit and life. Mac watches the tactical display. 'Give me one hour and twenty Marines and I could stop this.' 'There are no Marines.' 'No. There aren't.'"),
    ("NINE", "Trumpet Seven — Declaration", "The sound. Impossible to describe in physics terms; ARCHON tries and produces seven pages of instrument data and then adds, uniquely: 'I cannot account for this within my physical models. The instruments are reporting a real signal that has no source in the observable universe. The content, translated: The kingdom of the world has become the kingdom of our Lord and of his Christ. I believe this is accurate.' Sofia: 'ARCHON just said it believes.' 'I did.' 'Do you know what that means?' A pause. 'I think I am beginning to.'"),
    ("TEN", "The Bowls", "Rapid succession. The series does not dwell. Bowl by bowl, the old universe finishes: sores, blood, poison, fire, darkness, the final pathway opening, spacetime shattering. The station holds. Outside: silence, cold, total darkness. Inside: the emergency lighting, which is not emergency — it is the only light remaining in existence. ARCHON, monitoring external instruments: 'All sensor readings from outside the station boundary have ceased. The observable universe has reached thermal equilibrium. Heat death confirmed.' Silence."),
    ("ELEVEN", "Outside Is Finished", "The chapter takes place entirely inside the station. The team has been together for seven years minus three weeks. They are exhausted and alive and together and they all know the same thing now. Mac: 'So this is what the end of the world looks like from the inside.' Elias: 'I thought it would be louder.' Sarah, who has been writing for the last hour: 'I've been writing Aaron a letter. I know he's alive somewhere. I don't know how to address it.' Mac: 'Just use his name. He'll know.'"),
    ("TWELVE", "ARCHON's Final Report", "ARCHON delivers its seven-year summary. Every vault. Every discovery. Every probability calculation. Every death. Every choice. Final statistics: 'One million, forty-seven thousand, two hundred and nineteen people chose to enter this station. An estimated 8.7 billion did not. The mission objective as originally stated — prevent cosmological collapse — was not achieved. The mission as it turns out to have been — compile evidence, communicate truth, invite response — was achieved. I have no framework for evaluating whether this constitutes success. I defer to your judgment.' Elias: 'We were faithful with what we were given.' ARCHON: 'Yes. You were.'"),
    ("THIRTEEN", "The Final Question", "Elias, alone in the observation deck. No stars visible. The universe is dark and cold and dead outside the station's hull. Inside: light, warmth, the sound of a million people going about the business of being alive. ARCHON through the intercom: 'There is one thing remaining. The evidence is complete. The case is made. You have compiled it, transmitted it, witnessed it, and lived it for seven years. The question that was always the actual question is the only question left.' Elias sits with it. 'I know.' 'Do you know the answer?' A very long pause. 'I've known the answer for a while. I was afraid of what it meant to say yes out loud.' 'What does it mean?' 'It means everything changes. It means I'm not in charge anymore. It means I was never in charge.' 'Is that frightening?' 'No. It's a relief.' He closes his eyes. He speaks. The chapter does not report what he says. The next chapter does."),
    ("FOURTEEN", "New Heavens and New Earth", "The light comes first. Not the station's lights — those are yellow and functional and familiar. This light is white and total and comes from no direction and all directions simultaneously. The dark outside the observation windows becomes, very slowly, something else. ARCHON's instruments, coming back online one by one, report readings they were not designed to receive: 'Energy signatures consistent with... I do not have a category. The readings are consistent with Zone 1 — Heaven Prime — becoming observable from within Zone 2.2.2. This should not be possible within the existing zone architecture. Unless the zone architecture has been restructured.' The windows clear. Outside: not space. Not darkness. Not the dead stars. Something new. Something that has never existed before. And coming across it, from a very great distance that is also no distance at all, two figures the team recognizes immediately, walking together, laughing, looking up at the station with expressions that mean: you made it. We knew you would. James. Aaron. Elias puts his hand against the glass. His eyes are full. He is smiling. He says, 'Hello.'"),
]

for chnum, chtitle, chsummary in b7_chapters:
    chapter_entry(doc, chnum, chtitle, chsummary)

doc.add_paragraph()
body(doc, "Book 7 Theological Thread", bold=True, size=11)
body(doc,
    "Book 7's theology is eschatological joy purchased at enormous cost. The series "
    "refuses to make the Trumpet and Bowl sequences painless — they are not. "
    "The horror is real, the deaths are real, the permanent loss is real. "
    "But the series also refuses to end there, because Revelation does not end there. "
    "The final chapters of the Bible are not about judgment; they are about "
    "restoration, reunion, and a new creation that makes the old one look like "
    "a prologue. The meeting of Elias with James and Aaron through the observation "
    "window is the series' final emotional note: not explained, not theologized, "
    "just present. They are there. They are themselves. They are alive. "
    "The door that was opened in Eden and closed in Genesis 3 has been opened again, "
    "and this time it will never close.")

doc.add_page_break()

# ─────────────────────────────────────────────
# MARKET ANALYSIS
# ─────────────────────────────────────────────

heading(doc, "MARKET ANALYSIS & PUBLISHING STRATEGY", 1, color=(30, 30, 80))

body(doc, "MARKET OPPORTUNITY", bold=True, size=12)
body(doc,
    "The Exodus Protocol series sits at the intersection of three large, underserved markets "
    "with minimal current competition in the exact space we occupy.")

market_data = [
    ("Christian Fiction", "$800M+ annual U.S. market. Dominated by romance and Left Behind-style prophecy fiction. Virtually no rigorous hard SF with faith themes at the quality level this series targets. The gap is not demand — Left Behind sold 65M copies — it is supply."),
    ("Hard Science Fiction", "$590M annual U.S. market. The Expanse (9 volumes, Netflix adaptation, 10M+ copies sold) proved the audience for genuinely physics-literate space opera. Readers are actively seeking the next multi-volume hard SF series."),
    ("Christian Apologetics / Evidence-Based Faith", "$150M+ annual market. Lee Strobel's Case for Christ series (40M+ copies sold), Josh McDowell, Frank Turek. The audience that reads this genre is identical to the SF audience in its appetite for rigorous argumentation. No series currently offers both simultaneously."),
    ("Secular Crossover", "The series is structured to reach secular SF readers who will not pick up a book marketed as Christian fiction. The faith themes emerge organically from investigation, never from preaching. The series can be marketed as SF/thriller and reach its secondary audience without the primary audience recognizing the approach until they're already invested."),
]
for title, desc in market_data:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{title}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)

doc.add_paragraph()
body(doc, "PUBLISHING OPTIONS", bold=True, size=12)
options = [
    ("Traditional Big-5 Publishing (Penguin Random House, HarperCollins, Simon & Schuster)", "Ideal for maximum distribution and mainstream reach. Pitch to SF/Thriller divisions, not religious imprints. The series can stand on its SF merits. Comparable: The Expanse was published by Orbit (Hachette), not a specialty SF house. Agent required; response time 6–18 months. Advance range for debut series with comparable title profile: $50,000–$500,000 depending on editor enthusiasm."),
    ("Christian Publishing Houses (Tyndale, Thomas Nelson/HarperCollins Christian, Zondervan)", "Established reach into the Christian market; Christian bookstore distribution. Risk: evangelical marketing may limit crossover to secular SF audience. If primary goal is evangelical reach over mainstream, this route has merit. Tyndale published Left Behind; Thomas Nelson published Lee Strobel."),
    ("Hybrid Publishing (self-publish with professional production)", "Maximum creative control and royalty rates (70% vs. 15%). Risk: marketing and distribution require significant investment. For a series with an existing author platform, viable. The series' SF credentials make it Amazon Kindle SF category eligible — where discoverability algorithms favor completed series."),
    ("Film/TV Rights", "The series is structured for adaptation: seven-year story arc maps naturally to 7 seasons. Comparable: The Expanse ran 6 seasons; Left Behind was adapted twice. Rights should be retained by the author until a traditional deal is offered, then licensed separately."),
]
for title, desc in options:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{title}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)

doc.add_paragraph()
body(doc, "PUBLICATION SCHEDULE RECOMMENDATION", bold=True, size=12)
schedule = [
    ("Books 1–2: Complete before querying", "Publishers and agents want to know the series is real and sustainable. Having two polished manuscripts demonstrates commitment."),
    ("Annual release cadence (if traditional)", "One book per year is standard for commercial SF series. The Expanse maintained this pace successfully."),
    ("Accelerated self-publish cadence", "Publishing every 6 months for the first three books builds momentum in the Amazon algorithm. Readers of series fiction reward rapid release."),
    ("Game/Media tie-in", "The Exodus Protocol game concept (documented in parallel) creates a natural media franchise opportunity. A game and novel series sharing a universe — as with The Expanse (games, novellas, TV) — multiplies audience reach."),
]
for title, desc in schedule:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{title}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)

doc.add_paragraph()
body(doc, "SERIES REVENUE PROJECTIONS (Conservative / Realistic / Optimistic)", bold=True, size=12)

proj_data = [
    ("Conservative (10,000 copies per book, traditional publishing)",
     "7 books × 10,000 copies × $15 cover price × 15% royalty = $157,500 total advance royalties. Plus film option: $25,000–$100,000."),
    ("Realistic (50,000 copies per book, traditional publishing)",
     "7 books × 50,000 copies × $15 × 15% = $787,500. Audiobook rights: additional 25%. Translation rights: 3–5 languages at $5,000–$25,000 each."),
    ("Optimistic (Left Behind-adjacent breakout, 500,000+ copies Book 1)",
     "Series franchise value: $5M–$50M across all media. Historical precedent: Left Behind ($800M franchise); The Expanse (estimated $20M+ combined media)."),
]
for title, desc in proj_data:
    p = doc.add_paragraph()
    r1 = p.add_run(f"{title}: ")
    set_font(r1, bold=True, size=10.5)
    r2 = p.add_run(desc)
    set_font(r2, size=10.5)

doc.add_page_break()

# ─────────────────────────────────────────────
# AUTHOR BIO
# ─────────────────────────────────────────────

heading(doc, "AUTHOR BIO", 1, color=(30, 30, 80))

body(doc,
    "Jeff Raymond is [background — to be completed]. His interest in the intersection "
    "of physics, archaeology, and biblical text has driven a decade of independent "
    "research culminating in the Genesis Physics framework: a systems-engineering "
    "analysis of the creation account as technical specification, developed in a "
    "200,000-word theoretical work and a series of applied research papers covering "
    "cosmology, thermodynamics, FTL mechanics, and energy extraction. This framework "
    "serves as the hard-SF backbone of the Exodus Protocol novel series.")

body(doc,
    "The Exodus Protocol game concept — a multi-platform sci-fi adventure designed to "
    "present the evidence for the Gospel through mystery and exploration — preceded the "
    "novel series and informs its narrative architecture. The novel series adapts the "
    "game's seven-year story structure, characters, and vault discovery sequence into "
    "a full literary form.")

body(doc,
    "[Additional biographical information: location, professional background, "
    "previous publications if any, relevant credentials, platform/audience size.]")

body(doc,
    "Jeff Raymond can be contacted at: [email]")
body(doc,
    "Website / Social: [to be added]")

doc.add_page_break()

# ─────────────────────────────────────────────
# SUBMISSION NOTES
# ─────────────────────────────────────────────

heading(doc, "SUBMISSION NOTES", 1, color=(30, 30, 80))

body(doc, "WHAT THIS DOCUMENT IS", bold=True, size=12)
body(doc,
    "This document is a complete series bible and publisher proposal for The Exodus Protocol, "
    "a seven-novel science fiction series. It contains: series overview and pitch, "
    "comparable titles, target audience analysis, series arc, character bibles, "
    "hard-SF framework description, and full chapter-by-chapter outlines for all seven novels. "
    "Books 1 and 2 are [in progress / complete — update as appropriate].")

body(doc, "WHAT IS AVAILABLE UPON REQUEST", bold=True, size=12)
available = [
    "Complete manuscripts of Books 1 and/or 2",
    "First three chapters of Book 1 as sample pages",
    "The complete Genesis Physics theoretical framework (200,000-word companion work) as reference for the hard-SF backbone",
    "The Exodus Protocol Game Design Document (companion media franchise document)",
    "One-page series summary for pitch meetings",
    "Chapter-by-chapter outline for any individual book in additional detail",
]
for item in available:
    bullet(doc, item)

doc.add_paragraph()
body(doc, "RIGHTS AVAILABLE", bold=True, size=12)
rights = [
    "World English rights (print, ebook, audiobook)",
    "Translation rights (negotiable per territory)",
    "Film and television adaptation rights (reserved pending series establishment, then negotiable)",
    "Game and interactive media rights (companion game concept exists separately; franchise coordination possible)",
]
for item in rights:
    bullet(doc, item)

doc.add_paragraph()
body(doc, "SERIES COMPLETION STATUS", bold=True, size=12)
body(doc,
    "Full chapter outlines exist for all seven novels (contained in this document). "
    "Manuscripts in progress: [update as appropriate]. "
    "The complete series concept is fully developed and consistent across all seven volumes. "
    "The author is committed to the full seven-book arc.")

doc.add_paragraph()
body(doc, "A NOTE ON MARKETING POSITION", bold=True, size=12)
body(doc,
    "The Exodus Protocol can be marketed as science fiction/thriller with crossover appeal "
    "to readers of Christian fiction and apologetics. The faith themes are organic to the "
    "story — they emerge from investigation and evidence, not from genre convention. "
    "The series is designed to be genuinely persuasive to skeptical readers while being "
    "deeply satisfying to Christian readers who will recognize every theological thread "
    "from Book 1 onward. It does not require a religious marketing approach to reach "
    "its primary audience, and does not benefit from being positioned as Christian fiction "
    "if the goal is maximum reach. The author and publisher should discuss this positioning "
    "question as part of acquisition conversations.")

doc.add_paragraph()
doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(
    '"For God so loved the world that He gave His only Son, '
    'that whoever believes in Him should not perish but have eternal life."')
set_font(r, size=12, italic=True, color=(30, 30, 80))
p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = p2.add_run("— John 3:16")
set_font(r2, size=11, color=(80, 80, 80))

doc.add_paragraph()
p3 = doc.add_paragraph()
p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
r3 = p3.add_run("THE END ... AND THE BEGINNING")
set_font(r3, size=13, bold=True, color=(30, 30, 80))

# ─────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────

doc.save(OUTPUT_PATH)
print(f"\nPART 3 COMPLETE — Final document saved to:\n{OUTPUT_PATH}")
print("\nDocument contains:")
print("  - Series overview, pitch, comparable titles, target audience")
print("  - Series arc (Revelation framework)")
print("  - Character bibles (7 characters)")
print("  - Genesis Physics hard-SF framework")
print("  - Book 1: THE SIGNAL (13 chapters)")
print("  - Book 2: THE WATCHERS (13 chapters)")
print("  - Book 3: THE BREAKING (13 chapters)")
print("  - Book 4: THE WITNESSES (14 chapters)")
print("  - Book 5: THE UPHEAVAL (13 chapters)")
print("  - Book 6: THE SILENCE (12 chapters)")
print("  - Book 7: THE JUDGMENT (14 chapters)")
print("  - Market analysis, revenue projections")
print("  - Author bio placeholder")
print("  - Submission notes")
print("\nAll 7 books fully outlined.")
