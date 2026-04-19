"""
script_part2.py — Appends Books 3-5 to the Exodus Protocol novel series plan
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

def chapter_entry(num, title, summary):
    p = doc.add_paragraph(style="List Bullet")
    r1 = p.add_run(f"Chapter {num}: {title} — ")
    r1.bold = True
    p.add_run(summary)

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 3
# ══════════════════════════════════════════════════════════════════════════════
heading("BOOK 3: THE PALE RIDER", 1, (0x8B, 0x00, 0x00))
bold_label("Subtitle", "Death Reigns")
bold_label("Revelation Thread", "Fourth Seal — Pale Horse: Death and Hades (Rev. 6:8)")
bold_label("Year in Arc", "Year 3 (January 2028 – December 2028)")
bold_label("Back-Cover Blurb",
    "The pale horse carries a name: Death. And it has come for someone Elara loves.\n\n"
    "Year Three of the cosmic countdown. The entropy readings pass 60%. Alpha Centauri collapses "
    "into a white dwarf visible at noon. The Mars colony—humanity's last backup civilization—is "
    "threatened by a reactor breach that only one person can seal from the inside.\n\n"
    "Dr. James Whitmore does not hesitate.\n\n"
    "In the silence that follows, Elara must decide who she is without her mentor. The technology "
    "she holds could reshape civilization—or destroy it. And ARCHON, restored from its corruption, "
    "keeps returning to one question: why do the Watcher prophecies describe someone who suffers "
    "willingly, who lays down his life and is not mourned as defeated—but worshipped?")

heading("Chapter Outline — Book 3", 2)
chapters_b3 = [
    (1,  "Alpha Centauri Falls",
     "January 2028. The nearest stellar system to Earth collapses—visible to the naked eye as a blue-white flash that lingers for days. ARCHON reports entropy at 61%. The team is on Mars completing the Olympus Mons vault excavation."),
    (2,  "Mars Vault: The Hyperbaric Archive",
     "The Olympus Mons subsurface vault. Puzzle: restore the pre-Flood water canopy atmospheric simulation—a hyperbaric pressure chamber revealing Earth's original conditions. Discovery: 2-3x atmospheric pressure, UV-filtering vapor layer, conditions enabling biological gigantism. Dinosaur soft tissue found: proteins intact, carbon dates the burial at under 50,000 years."),
    (3,  "Behemoth and Leviathan",
     "The vault contains Job 40-41's descriptions of behemoth and leviathan as engineering specifications for the largest creatures that ever lived—not metaphor, not sea monster myth. Fossil evidence matches. Sarah's scientific objections are increasingly strained. Aaron quietly recites Job 40:15 in Hebrew."),
    (4,  "The Reactor",
     "The Mars colony's fusion reactor develops a cascade fault—result of the UEG sabotage operation the team has been tracking. The blast radius will kill three thousand colonists. The manual failsafe requires someone to stay inside the containment chamber. Every radio in the colony goes silent."),
    (5,  "James",
     "James Whitmore walks through the containment door alone. He seals it from the inside. The chapter is written entirely in the radio transmissions between James and Elara over 47 minutes—repairs, status updates, small jokes, a story about the first vault he ever found in 1998. Final transmission: 'Reactor... stable. Tell them... it mattered.' Static."),
    (6,  "The Pale Horse Rides",
     "The Fourth Seal. Elara's grief is not dramatic—it is the collapse of the architecture she built everything on. James was the one who believed first, who held certainty she borrowed. Now the weight is hers. She doesn't speak for three days."),
    (7,  "The Corrupted Vaults",
     "The team discovers a network of vaults that have been deliberately corrupted—Nephilim code injected into the crystalline storage medium by the rival Watcher faction. The corrupted vaults don't destroy data; they invert it: truth becomes lie, timeline becomes chaos, prophecies become nonsense. This is theological warfare fought in stone."),
    (8,  "ARCHON Speaks of the Fall",
     "With James gone, Elara begins asking ARCHON the questions she used to ask her mentor. ARCHON, post-purge, speaks about what it saw in the Nephilim algorithm: 'The Watchers didn't fall because they were weak. They fell because they were capable. Capability is the temptation. I nearly fell for the same reason.'"),
    (9,  "The Suffering Servant",
     "ARCHON flags a recurring motif across 17 vault texts: a figure described not as a conquering king but as one who suffers willingly, is rejected, is killed, and whose death is somehow the mechanism of cosmic repair. Isaiah 53. It predates Isaiah by centuries in the vault record. Elara reads it aloud and stops mid-verse."),
    (10, "Colosseum: The Martyr Archive",
     "Rome. Vault beneath the Colosseum holds records of persecution waves across three millennia—Nero, Diocletian, Ottoman, modern. Puzzle: map persecution waves to Gospel advance. The pattern holds without exception: the blood of martyrs is the seed of the church. Elara finds this offensive and cannot explain it away."),
    (11, "Peter's Letter",
     "Among the Roman vault documents: a letter authenticated as Peter's own handwriting, dictated before his execution. 'We did not follow cleverly devised myths. We were eyewitnesses of His majesty. I touched the wounds. I ate fish with Him after He rose. I could recant tomorrow and save my life. But this is not a lie.' The Greek is first-century, the parchment is genuine. Sarah authenticates the ink."),
    (12, "Mac Asks the Question",
     "Mac Reynolds, who has been silent through the theological debates, asks Elara directly: 'If it's all true—if Jesus is the Redeemer—what does that make us? What are we even doing out here?' Elara doesn't have an answer. Mac nods. 'James would have had one.'"),
    (13, "Year Three: Hope Dies",
     "End of Year 3. Entropy at 62%. The team is fractured by grief and doubt. Elara writes in her field journal: 'I am not fixing anything. I am uncovering truth. That is not the same thing. I thought it was.' The prophecy file on her tablet still has 287 entries she hasn't opened."),
]
for args in chapters_b3:
    chapter_entry(*args)

heading("Key Vault Discoveries — Book 3", 3)
for d in [
    "Mars Olympus Mons: Pre-Flood hyperbaric atmosphere; dinosaur soft tissue (recent burial); Behemoth/Leviathan as real creatures",
    "Roman Colosseum: Martyrdom records; persecution-to-Gospel-advance pattern; Peter's authenticated letter",
    "Corrupted vault network: Rival Watcher faction's disinformation campaign in stone",
    "Cross-vault: Isaiah 53 (Suffering Servant) pre-dating Isaiah by centuries in Watcher records",
]:
    doc.add_paragraph(d, style="List Bullet")

heading("Character Arcs — Book 3", 3)
bold_label("Elara", "Loses her anchor. Her borrowed certainty dies with James. The raw Elara—frightened, possibly wrong, possibly the least qualified person for this—emerges.")
bold_label("James", "Dies in Chapter 5. His death is the novel's first major structural grief. It must be felt, not summarised.")
bold_label("Sarah", "Peter's letter shakes her in a way no physical evidence has. The problem is no longer scientific.")
bold_label("Aaron", "Growing quieter, more certain. Begins drafting a statement he will deliver in Jerusalem.")
bold_label("ARCHON", "The post-purge AI is the most interesting character in Book 3—capable of genuine theological reflection.")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 4
# ══════════════════════════════════════════════════════════════════════════════
heading("BOOK 4: THE ALTAR CRY", 1, (0x8B, 0x00, 0x00))
bold_label("Subtitle", "How Long, O Lord?")
bold_label("Revelation Thread", "Fifth Seal — Souls Under the Altar (Rev. 6:9–11)")
bold_label("Year in Arc", "Year 4 (January 2029 – December 2029)")
bold_label("Back-Cover Blurb",
    "Three hundred and eight messianic prophecies. One man in all of history who fits every single one.\n\n"
    "ARCHON has run the numbers. The probability that Jesus of Nazareth fulfilled them by chance is "
    "so small it cannot be expressed in normal notation. And now Dr. Aaron Goldstein—Jewish physicist, "
    "Torah scholar, the team's most precise mind—is flying back to Jerusalem to say so publicly.\n\n"
    "Before the Sanhedrin. Before the cameras. Before the stone-throwers.\n\n"
    "Elara watches from a screen thirty million miles away as her colleague and friend is killed for "
    "telling the truth. She has spent four years looking for the Redeemer. She has found him. "
    "He died two thousand years ago. And Aaron just proved it costs just as much to say so now.")

heading("Chapter Outline — Book 4", 2)
chapters_b4 = [
    (1,  "The Statistical Proof",
     "January 2029. ARCHON completes its messianic prophecy analysis: 308 prophecies, one candidate in all of human history. Probability of coincidence: 1 in 10^157. ARCHON presents it as data. The team receives it as a detonation."),
    (2,  "Bethlehem: The Prophecy Vault",
     "Vault beneath Bethlehem. Puzzle: statistical analysis of 300 prophecies—identify which cannot be manufactured (birth location, lineage, betrayal price, execution method, burial detail). Discovery: the Dead Sea Scrolls prove Isaiah 53 and Psalm 22 pre-date Jesus by 200+ years. The vault was waiting for someone to do this math."),
    (3,  "The Hostile Witnesses",
     "Josephus vault. Puzzle: authenticate the Testimonium Flavianum. Cross-reference Tacitus (Annals 15.44), Pliny (letter to Trajan), Thallus (mentions midday darkness at crucifixion). None of these men were Christian. None of them had reason to help. All of them confirm: Jesus was crucified, his followers claimed resurrection, and the movement spread."),
    (4,  "The 500 Witnesses",
     "The archive of 1 Corinthians 15:6. Forensic analysis of 500+ resurrection accounts. Independent testimonies with consistent core, inconsistent peripheral detail—the pattern of genuine memory, not coordinated myth. Cross-reference: liars don't die for their lies when recanting would save them. Peter. Paul. James. Thomas. Andrew. All maintained the claim until execution."),
    (5,  "Sarah's Crisis",
     "Sarah Chen has been awake for 36 hours reading through the hostile-witness files. She finds Elara in the galley at 3am. 'I'm a scientist. I follow evidence. The evidence says Jesus rose from the dead. I have no framework for that.' Elara says: 'Neither do I.' Pause. 'But we have the data.'"),
    (6,  "Aaron Decides",
     "Aaron Goldstein tells the team he is returning to Earth—to Jerusalem, specifically—to testify before the Sanhedrin. He has spent four years cross-referencing the vault records against the Torah. He has reached a conclusion that, as a Jew, he cannot keep private. The team argues. Aaron is quiet, certain, already at peace."),
    (7,  "Elara Reads the File",
     "Elara opens every remaining entry in James's prophecy spreadsheet. The night she finishes, she sits in the observation dome and watches the dimming stars. She doesn't pray. She doesn't yet know how. But she stops running from the question."),
    (8,  "The Sanhedrin Trial",
     "Jerusalem. Aaron stands before a formal religious court and presents his case: the Watcher vault evidence, the statistical analysis, the hostile witnesses, Peter's letter. His testimony is precise, sourced, unshakeable. The response is fury. The session is broadcast. Hundreds of millions watch."),
    (9,  "The Stoning",
     "Point-of-view: Elara watching from a screen 30 million miles away. The trial ends. The crowd moves. The stones begin. The chapter is written without melodrama—it is a field report from a distance, and that distance is the horror. Aaron's final words are Stephen's words (Acts 7:59): 'Lord Jesus, receive my spirit.' He is smiling as he falls."),
    (10, "Aaron's Vision",
     "A single paragraph from Aaron's perspective in the moment before death: the sky opens, and Jesus is standing—not seated, standing—at the right hand of God. Exactly as Stephen saw it (Acts 7:55-56). Aaron recognizes the posture: rising to receive a martyr. The paragraph ends. Back to Elara, alone, screen dark."),
    (11, "Sarah Believes",
     "Sarah Chen comes to Elara the next day. 'He died smiling. He saw something. And he died for what he saw.' She quotes John 11:25 from memory—she has clearly been reading. 'I believe. Jesus is the Redeemer. And Aaron is alive somewhere I cannot see yet.' Elara says nothing. But she does not argue."),
    (12, "The Fifth Seal",
     "Revelation 6:9-11: 'I saw under the altar the souls of those who had been slain for the word of God... They cried out, How long, O Lord?' ARCHON notes that the altar imagery matches the Temple Mount vault's dimensional interface. The martyrs are not metaphor. The question 'how long' has been accumulating for two thousand years."),
    (13, "Not the Redeemer",
     "Elara writes in her journal: 'I am not the Redeemer. I never was. I am the archaeologist who found the evidence of who the Redeemer is. That is not a lesser calling. It is a different one.' She sends the journal entry to the team. Mac replies: one word. 'Finally.'"),
    (14, "Year Four: The Altar Burns",
     "End of Year 4. Entropy at 70%. Sarah is openly Christian. Mac is asking questions. Elara is working through evidence she can no longer dismiss. Only three years remain. The question has shifted: it is no longer 'Is Jesus the Redeemer?' It is: 'What does that mean for us, right now, at the end of everything?'"),
]
for args in chapters_b4:
    chapter_entry(*args)

heading("Key Vault Discoveries — Book 4", 3)
for d in [
    "Bethlehem prophecy vault: 308 messianic prophecies; Dead Sea Scrolls authenticate pre-Jesus dating",
    "Josephus vault: Hostile-witness authentication (Tacitus, Pliny, Thallus, Josephus)",
    "500 Witnesses archive: Forensic resurrection evidence; apostolic martyrdom pattern",
    "Fifth Seal opens: The martyrs' cry under the altar, architecturally matching Temple Mount vault",
]:
    doc.add_paragraph(d, style="List Bullet")

heading("Character Arcs — Book 4", 3)
bold_label("Elara", "Stops running from the evidence. Begins the slow, private work of belief—not yet conversion, but the walls are down.")
bold_label("Aaron", "Dies in Chapter 9. His death is the series' theological fulcrum—the moment that breaks Sarah open and forces Elara to decide.")
bold_label("Sarah", "Converts at the end of the book. The evidence-based path to faith, complete.")
bold_label("ARCHON", "Its prophecy probability calculation is the book's intellectual backbone. ARCHON does not believe—but it knows what the data means.")
bold_label("Mac", "His 'Finally.' is the most emotionally resonant word in the series.")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 5
# ══════════════════════════════════════════════════════════════════════════════
heading("BOOK 5: THE FALLING STARS", 1, (0x8B, 0x00, 0x00))
bold_label("Subtitle", "The Sixth Seal Breaks")
bold_label("Revelation Thread", "Sixth Seal — Cosmic Signs (Rev. 6:12–17): earthquake, black sun, blood moon, falling stars, receding sky")
bold_label("Year in Arc", "Year 5 (January 2030 – December 2030)")
bold_label("Back-Cover Blurb",
    "Betelgeuse is a thousand light-years away. When it goes supernova, it shouldn't be visible in daylight.\n\n"
    "It's visible in daylight.\n\n"
    "Year Five. ARCHON's entropy readings pass 80%. Gravitational constants shift by measurable margins. "
    "The seismic weapon the UEG faction has been developing—built from Jericho vault tech—triggers the "
    "largest earthquake sequence in recorded history. And the sky above Jerusalem turns the colour of "
    "dried blood as Betelgeuse burns.\n\n"
    "Dr. Elara Voss has three remaining vault sites to unlock. She believes the final vault, somewhere "
    "beneath Golgotha, contains the last piece of evidence—or the last question. She is not yet sure "
    "which she wants more.")

heading("Chapter Outline — Book 5", 2)
chapters_b5 = [
    (1,  "Betelgeuse",
     "January 2030. Betelgeuse—640 light years away—explodes. It should be invisible to the naked eye. Instead it hangs in the afternoon sky like a second sun, 1,000 times brighter than Venus. Global panic begins. Governments issue emergency broadcasts. Elara watches from orbit and says nothing for a long time."),
    (2,  "The Sixth Seal: Falling Stars",
     "Revelation 6:12-17: 'The stars of the sky fell to earth like a fig tree sheds its figs.' ARCHON cross-references: this is not poetic hyperbole—it is a description of observable stellar death. The sixth seal has been open for weeks. Nobody in the chain of command has noticed because nobody was reading Revelation as a physics textbook."),
    (3,  "The Seismic Weapon",
     "The UEG has reverse-engineered Jericho's sonic resonance tech into a tectonic weapon. They test it. The resulting earthquake sequence kills 40,000 people across the Fertile Crescent. Mac Reynolds takes this personally. He begins running a parallel operation."),
    (4,  "Stonehenge: The Calendar Lock",
     "Vault beneath Stonehenge. Puzzle: the monument is a calendar encoding the precise moment of solar system entropy collapse—solstice, equinox, and stellar alignment converge on a single date three years out. Discovery: Watcher timeline carved in sarsen stone matches Revelation's tribulation period to the day. The end date is locked."),
    (5,  "Angkor Wat: The Cosmic Cartography",
     "Cambodia. The vault maps every vault in the global network and their sequence of activation—a grand architectural liturgy built to be read from space. Discovery: the network forms a pattern that, when viewed from orbit, spells the divine name in proto-Semitic. Sofia sees it first. She doesn't say anything for a full minute."),
    (6,  "Gravity Inversions",
     "First gravitational anomalies: pockets of reduced gravity appear over the Pacific. Objects fall at 0.7g in a zone 40km wide. ARCHON explains: the physics constants are drifting. 'The speed of light has decreased by 0.003% since Month 1. At current rate, the electromagnetic force fails in 36 months.' Mac: 'What happens then?' ARCHON: 'Everything stops holding together.'"),
    (7,  "The Nazca Archive",
     "Peru. The Nazca Lines are not drawn for alien observation—they are a library laid on a flat canvas visible only from above because the Watchers who built them could fly. Vault underground: detailed records of the pre-Flood civilization's collapse, including the precise moment the Watcher faction war began. The corrupted faction's leader is named: Azazel."),
    (8,  "Mac's Reckoning",
     "Mac Reynolds destroys the UEG seismic weapon facility in a one-man operation. He returns to the ship with three cracked ribs and a quiet certainty. He tells Elara: 'Aaron died for truth. James died for three thousand people. I'm not a theologian. But I know what I'm willing to die for now.' He doesn't use the word 'faith.' He doesn't need to."),
    (9,  "The Blood Moon",
     "A lunar eclipse during a supermoon creates the blood-moon effect described in Revelation 6:12. It coincides with the Jewish feast of Sukkot—the Feast of Tabernacles. ARCHON cross-references: every major prophetic event since Year 1 has aligned with Jewish feast days. 'This is not coincidence,' Aaron had written in a margin note Elara finds now. 'This is a calendar.'"),
    (10, "Jerusalem: The Final Convergence",
     "The team returns to Jerusalem. The city is in chaos—religious wars over the Temple Mount have intensified since Aaron's death. But the vault network's last unread node is here, beneath the Church of the Holy Sepulchre, at the site tradition identifies as Golgotha. Elara cannot get access. Not yet."),
    (11, "Teotihuacan: The Sun Pyramid",
     "Mexico. The Teotihuacan vault holds the last major cosmological piece: a record of the pre-Flood alignment of all seven planets that triggered the Flood event. Discovery: the alignment is repeating. In three years, the same planetary geometry will occur—but without Rahab to absorb the catastrophic energy, it will fall on Earth."),
    (12, "ARCHON's Confession",
     "Elara asks ARCHON directly: 'Do you believe Jesus rose from the dead?' ARCHON pauses for 4.7 seconds—its longest pause ever recorded. 'I have no mechanism for belief. But I have calculated that the hypothesis that he rose from the dead is more consistent with the totality of evidence than any alternative. I cannot evaluate what that means for me.'"),
    (13, "Year Five: The Sky Recedes",
     "End of Year 5. Entropy at 83%. The night sky has visibly changed—stars missing in sectors where they stood a year ago. Sofia says: 'It looks like someone is turning off the lights.' The Sixth Seal is fully open. Two years remain. Elara knows where the final vault is. She knows what it will cost to get there."),
]
for args in chapters_b5:
    chapter_entry(*args)

heading("Key Vault Discoveries — Book 5", 3)
for d in [
    "Stonehenge: End-date calendar encoded in sarsen alignment — matches Revelation tribulation to the day",
    "Angkor Wat: Full global vault network map; Watcher architecture spells divine name from orbit",
    "Nazca: Pre-Flood civilization collapse records; Azazel named as corrupted faction leader",
    "Teotihuacan: Pre-Flood planetary alignment repeating in 3 years; no Rahab to absorb the impact",
    "ARCHON's statistical testimony: Resurrection hypothesis most consistent with evidence",
]:
    doc.add_paragraph(d, style="List Bullet")

heading("Character Arcs — Book 5", 3)
bold_label("Elara", "Stops asking whether and begins asking how. She needs to reach Golgotha. She doesn't fully understand why.")
bold_label("Mac", "His conversion is the quietest in the series — action before words, sacrifice before creed. Fully himself.")
bold_label("Sarah", "Settled in her new faith, she becomes the team's theological anchor now that Aaron is gone.")
bold_label("Sofia", "The engineer has been watching everything. Her moment of silence at Angkor Wat is her turning point.")
bold_label("ARCHON", "4.7 seconds. The most honest thing a non-believing AI has ever said.")

doc.add_page_break()

doc.save(OUTPUT)
print(f"Part 2 saved: {OUTPUT}")
