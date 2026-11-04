# Chapter 8, pages 8.4 to 8.7. Coordinates are [longitude, latitude].
from common import c, q

BG = "https://www.biblegateway.com/passage/?search="
S = {
 # 8.4
 'brit-philip2': ("Encyclopaedia Britannica, \"Philip II\" (king of Macedonia)", "https://www.britannica.com/biography/Philip-II-king-of-Macedonia"),
 'brit-alexander': ("Encyclopaedia Britannica, \"Alexander the Great\"", "https://www.britannica.com/biography/Alexander-the-Great"),
 'brit-gaugamela': ("Encyclopaedia Britannica, \"Battle of Gaugamela\"", "https://www.britannica.com/event/Battle-of-Gaugamela"),
 'brit-alexandria': ("Encyclopaedia Britannica, \"Alexandria\"", "https://www.britannica.com/place/Alexandria-Egypt"),
 'brit-hydaspes': ("Encyclopaedia Britannica, \"Battle of the Hydaspes\"", "https://www.britannica.com/event/Battle-of-the-Hydaspes"),
 'met-hellenistic': ("The Met, \"Art of the Hellenistic Age and the Hellenistic tradition\"", "https://www.metmuseum.org/essays/art-of-the-hellenistic-age-and-the-hellenistic-tradition"),
 'brit-library': ("Encyclopaedia Britannica, \"Library of Alexandria\"", "https://www.britannica.com/topic/Library-of-Alexandria"),
 'bagnall2002': ("Roger Bagnall, \"Alexandria: library of dreams\", Proceedings of the American Philosophical Society 146.4 (2002)", "https://www.open.edu/openlearn/pluginfile.php/437863/mod_resource/content/2/Bagnall%20article.pdf"),
 'ou-library': ("The Open University, OpenLearn, \"The Library of Alexandria\"", "https://www.open.edu/openlearn/history-the-arts/library-alexandria/content-section-2.1"),
 'brit-septuagint': ("Encyclopaedia Britannica, \"Septuagint\"", "https://www.britannica.com/topic/Septuagint"),
 'iranica-aikhanoum': ("Paul Bernard, \"Āy Ḵānom\", Encyclopaedia Iranica (1987)", "https://www.iranicaonline.org/articles/ay-kanom-or-a-khanum-tepe-a-local-uzbek-name-lit"),
 'met-afghan2009': ("The Met, press release for \"Afghanistan: Hidden Treasures from the National Museum, Kabul\" (2009)", "https://www.metmuseum.org/press-releases/afghanistans-dazzling-national-treasureshidden-for-25-yearspresented-at-metropolitan-museum-2009-exhibitions"),
 # 8.5
 'brit-antiochus4': ("Encyclopaedia Britannica, \"Antiochus IV Epiphanes\"", "https://www.britannica.com/biography/Antiochus-IV-Epiphanes"),
 'brit-maccabees': ("Encyclopaedia Britannica, \"Maccabees\"", "https://www.britannica.com/topic/Maccabees"),
 'bg-1macc1': ("1 Maccabees 1:54-61 (NRSVUE)", BG + "1%20Maccabees%201%3A54-61&version=NRSVUE"),
 'bg-1macc4': ("1 Maccabees 4:52-59 (NRSVUE)", BG + "1%20Maccabees%204%3A52-59&version=NRSVUE"),
 'bg-2macc10': ("2 Maccabees 10:5-8 and 1 Maccabees 13:41-42 (NRSVUE)", BG + "2%20Maccabees%2010%3A5-8%3B1%20Maccabees%2013%3A41-42&version=NRSVUE"),
 'sefaria-shabbat21b': ("Babylonian Talmud, Shabbat 21b (Sefaria, English)", "https://www.sefaria.org/Shabbat.21b"),
 'brit-jerusalem-roman': ("Encyclopaedia Britannica, \"Jerusalem: Roman rule\"", "https://www.britannica.com/place/Jerusalem/Roman-rule"),
 'brit-sadducee': ("Encyclopaedia Britannica, \"Sadducee\"", "https://www.britannica.com/topic/Sadducee"),
 'brit-essene': ("Encyclopaedia Britannica, \"Essene\"", "https://www.britannica.com/topic/Essene"),
 'cojs-pliny-essenes': ("Center for Online Judaic Studies, Pliny, Natural History 5.15, 'the solitary Essenes'", "https://cojs.org/pliny-_natural_history_v-_xv-_the_solitary_essenes/"),
 'upenn-essenes': ("R. A. Kraft (University of Pennsylvania), ancient texts on the Essenes: Philo, Josephus and Pliny", "https://ccat.sas.upenn.edu/rak/courses/225/texts/ESSENES"),
 'brit-dss': ("Encyclopaedia Britannica, \"Dead Sea Scrolls\"", "https://www.britannica.com/topic/Dead-Sea-Scrolls"),
 'benami2004': ("Yaakov Ben-Ami, \"The enigma of Qumran\", The Bible and Interpretation (2004)", "https://bibleinterp.arizona.edu/node/2891"),
 'popovic2025': ("Popović et al., \"Dating ancient manuscripts using radiocarbon and AI-based writing style analysis\", PLOS ONE 20.6 (2025)", "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0323185"),
 'eurekalert-enoch': ("EurekAlert, University of Groningen release on the 'Enoch' dating model (2025)", "https://www.eurekalert.org/news-releases/1085589"),
 'bg-dan11': ("Daniel 11:31 and 12:11 (NRSVUE)", BG + "Daniel%2011%3A31%3BDaniel%2012%3A11&version=NRSVUE"),
 # 8.6
 'met-romr': ("The Met, \"The Roman Republic\"", "https://www.metmuseum.org/toah/hd/romr/hd_romr.htm"),
 'jobin-lapis': ("N. V. Jobin, Ancient Rome: Sourcebook and Historical Atlas (open textbook, 2022), on the Lapis Niger", "https://colorado.pressbooks.pub/ancientrome/?p=55"),
 'carlsberg-sauer': ("Carlsberg Foundation grant CF22-0141 (Cambridge project on archaic Rome)", "https://www.carlsbergfondet.dk/det-har-vi-stoettet/CF22-0141"),
 'sd-gabii2025': ("ScienceDaily / University of Missouri, on the Gabii basin (2 December 2025)", "https://www.sciencedaily.com/releases/2025/12/251202052222.htm"),
 'brit-republic': ("Encyclopaedia Britannica, \"Roman Republic\"", "https://www.britannica.com/place/Roman-Republic"),
 'brit-orders': ("Encyclopaedia Britannica, \"Conflict of the Orders\"", "https://www.britannica.com/topic/Conflict-of-the-Orders"),
 'brit-hortensia': ("Encyclopaedia Britannica, \"Lex Hortensia\"", "https://www.britannica.com/topic/Lex-Hortensia"),
 'polyb6': ("Polybius, Histories, Book 6 (Loeb translation on LacusCurtius)", "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Polybius/6*.html"),
 'brit-pyrrhus': ("Encyclopaedia Britannica, \"Pyrrhus\"", "https://www.britannica.com/biography/Pyrrhus"),
 'ebsco-julian': ("Pepe and Watkins, \"Julian Law\", EBSCO Research Starters (2022)", "https://www.ebsco.com/research-starters/history/julian-law/"),
 # 8.7
 'brit-punic': ("Encyclopaedia Britannica, \"Punic Wars\"", "https://www.britannica.com/event/Punic-Wars"),
 'met-iberia': ("The Met, Heilbrunn Timeline, \"Iberian Peninsula, 1000 B.C.-1 A.D.\"", "https://www.metmuseum.org/toah/ht/04/eusi.html"),
 'brit-cartagena': ("Encyclopaedia Britannica, \"Cartagena\" (Spain)", "https://www.britannica.com/place/Cartagena-Spain"),
 'brit-hannibal': ("Encyclopaedia Britannica, \"Hannibal\"", "https://www.britannica.com/biography/Hannibal-Carthaginian-general-247-183-BC"),
 'brit-nearer-spain': ("Encyclopaedia Britannica, \"Nearer Spain\"", "https://www.britannica.com/place/Nearer-Spain"),
 'brit-numantia': ("Encyclopaedia Britannica, \"Numantia\"", "https://www.britannica.com/place/Numantia"),
 'grout-numantia': ("James Grout, \"The Celtiberian War\", Encyclopaedia Romana (University of Chicago)", "https://penelope.uchicago.edu/encyclopaedia_romana/hispania/celtiberianwar.html"),
 'brit-cantabrian': ("Encyclopaedia Britannica, \"Cantabrian War\"", "https://www.britannica.com/topic/Cantabrian-War"),
 'ebsco-spanish': ("Rydgren, \"Spanish language\", EBSCO Research Starters (2023)", "https://ebsco.com/research-starters/language-and-linguistics/spanish-language"),
 'brit-spanish': ("Encyclopaedia Britannica, \"Spanish language\"", "https://www.britannica.com/topic/Spanish-language"),
 'unesco-medulas': ("UNESCO World Heritage Centre, \"Las Médulas\"", "https://whc.unesco.org/en/list/803/"),
 'jones1980': ("G. D. B. Jones, \"The Roman mines at Riotinto\", Journal of Roman Studies 70 (1980)", "https://www.cambridge.org/core/journals/journal-of-roman-studies/article/abs/roman-mines-at-riotinto/8C596A65C572C330A1F121E4423957A9"),
 'ku-mcconnell2018': ("McConnell et al., \"Lead pollution recorded in Greenland ice...\", PNAS 115 (2018), University of Copenhagen record", "https://researchprofiles.ku.dk/en/publications/lead-pollution-recorded-in-greenland-ice-indicates-european-emiss/"),
}

C = {
 # 8.4
 'c-philip': c("Philip II of Macedon (ruled 359-336 BCE) made his kingdom the dominant power in Greece, by war and diplomacy, by 339.", 'consensus', ['brit-philip2'], show=False),
 'c-alexander': c("Alexander, born at Pella in 356 BCE, became king in 336 and died at Babylon in June 323, aged 32.", 'consensus', ['brit-alexander'], show=False),
 'c-gaugamela': c("At Gaugamela, on 1 October 331 BCE, Alexander defeated Darius III's larger army; Darius was later killed by one of his own governors, and the Persian empire passed to Alexander.", 'consensus', ['brit-gaugamela'], show=False),
 'c-alexandria-found': c("Alexander founded Alexandria in Egypt in 332 or 331 BCE.", 'approx', ['brit-alexandria'], "Sources differ by a year."),
 'c-hydaspes': c("On the Hydaspes (Jhelum) in 326 BCE Alexander defeated the Indian king Porus and kept him on as ruler; soon after, at the Beas, his army refused to go further.", 'consensus', ['brit-hydaspes'], show=False),
 'c-hellenistic': c("Historians call the period from Alexander's death (323 BCE) to the battle of Actium (31 BCE) 'Hellenistic'; his empire split among dynasties founded by his generals, chiefly the Ptolemies in Egypt, the Seleucids in Asia and the Antigonids in Macedonia, with the Attalids at Pergamon.", 'consensus', ['met-hellenistic'], show=False),
 'c-library': c("The Ptolemies built the Library of Alexandria from the early 3rd century BCE, with a 'daughter' collection at the Serapeum; where exactly it stood and how it was laid out are unknown.", 'consensus', ['brit-library'], show=False),
 'c-library-size': c("Ancient writers credit the Library with 40,000, about 490,000 or 700,000 book-rolls.", 'debated', ['bagnall2002', 'ou-library'], "Roger Bagnall argues the figures 'do not deserve any credence' and the real holdings were probably smaller 'by as much as one order of magnitude'; popular accounts repeat the big numbers."),
 'c-library-end': c("How the Library ended is uncertain: one account blames the fighting in Alexandria under the emperor Aurelian in the 270s CE, another a Christian attack on the Serapeum in 391 CE.", 'debated', ['brit-library'], "Many scholars doubt any great library still existed by 391; the decline was probably gradual."),
 'c-septuagint': c("Linguistic study dates the Greek translation of the Torah, the core of the Septuagint, to the mid-3rd century BCE, and most other books to the 2nd century BCE.", 'approx', ['brit-septuagint'], "The dates come from the language of the translation itself."),
 'c-aristeas': c("The Letter of Aristeas says Ptolemy II asked for the translation and 72 elders, six from each tribe, produced it.", 'tradition', ['brit-septuagint', 'ou-library'], "Scholars treat the story as legend, widely read as Jewish writing aimed at Greek readers."),
 'c-aikhanoum': c("Aï Khanoum, a Greek city on the Oxus in northern Afghanistan, had a huge gymnasium, a theatre and a copy of the moral maxims of Delphi; steppe nomads destroyed it about 150 BCE.", 'approx', ['iranica-aikhanoum', 'met-afghan2009'], "The destruction date is approximate; Bactria broke away from the Seleucids about 250 BCE."),
 # 8.5
 'c-antiochus-egypt': c("In 168 BCE the Seleucid king Antiochus IV was invading Egypt when a Roman envoy drew a circle in the sand around him and demanded an answer before he stepped out of it; he withdrew.", 'consensus', ['brit-antiochus4'], show=False),
 'c-antiochus-ban': c("In 167 BCE Antiochus IV garrisoned Jerusalem, banned Jewish worship, the Sabbath and circumcision, and set up an altar to Zeus in the Temple.", 'consensus', ['brit-antiochus4', 'brit-maccabees'], show=False),
 'c-desolating': c("1 Maccabees calls the new altar 'a desolating sacrilege' (1:54) and tells of women put to death for having their children circumcised (1:60-61).", 'tradition', ['bg-1macc1'], "1 Maccabees was written about a generation after the events, from the Hasmonean side."),
 'c-rededication': c("Judas Maccabeus' rebels retook the Temple and rededicated it in December 164 BCE.", 'consensus', ['brit-antiochus4'], show=False),
 'c-eight-days': c("1 Maccabees says the altar's dedication was celebrated 'for eight days' and decreed an annual festival (4:56-59); 2 Maccabees compares it to the festival of Booths (10:6).", 'tradition', ['bg-1macc4', 'bg-2macc10'], "This is the origin of Hanukkah as the texts give it."),
 'c-oil': c("The story of one jar of oil that burned for eight days is not in Maccabees; it first appears in the Babylonian Talmud (Shabbat 21b), compiled centuries later.", 'consensus', ['sefaria-shabbat21b'], show=False),
 'c-hasmonean': c("1 Maccabees dates Judea's independence to the year when 'the yoke of the nations was removed from Israel' and documents began to be dated by Simon, 'the great high priest and commander and leader of the Jews' (13:41-42), that is, 142 BCE.", 'tradition', ['bg-2macc10'], "The years in Maccabees are counted in the Seleucid era; year 170 corresponds to 143/142 BCE."),
 'c-pompey': c("The Roman general Pompey captured Jerusalem in 63 BCE.", 'consensus', ['brit-jerusalem-roman'], show=False),
 'c-herod': c("Rome's Senate named Herod king of Judea in 40 BCE; he died in 4 BCE. He enlarged the Temple platform with huge retaining walls, of which the Western Wall is part, and the rebuilt Temple took more than a generation to finish.", 'consensus', ['brit-jerusalem-roman'], show=False),
 'c-sadducees': c("The Sadducees, a priestly and aristocratic party, accepted only the written Torah and denied resurrection; the Pharisees also treated an oral tradition as going back to Moses.", 'consensus', ['brit-sadducee'], show=False),
 'c-essenes': c("Josephus, Philo and Pliny the Elder all describe a third group, the Essenes; Philo and Josephus each put their number at about 4,000. Their accounts differ in details, and the New Testament never names them.", 'consensus', ['brit-essene', 'upenn-essenes', 'cojs-pliny-essenes'], show=False),
 'c-dss': c("From 1947, eleven caves near Qumran yielded about 15,000 fragments from some 800 to 900 manuscripts, mostly in Hebrew; every book of the Hebrew Bible except Esther is represented.", 'approx', ['brit-dss'], "Counts depend on how fragments are grouped into manuscripts."),
 'c-qumran': c("Who lived at Qumran, and whether they wrote the scrolls, is disputed.", 'debated', ['brit-essene', 'benami2004'], "Most scholars, following the excavator Roland de Vaux, see an Essene community. Yizhar Hirschfeld argued for a wealthy estate; Yitzhak Magen and Yuval Peleg for a fort turned pottery workshop, with scrolls hidden by refugees from Jerusalem."),
 'c-enoch': c("In 2025 a team radiocarbon-dated 27 scroll samples and used them to train an AI model of handwriting called 'Enoch'; many manuscripts came out older than handwriting experts had thought.", 'debated', ['popovic2025', 'eurekalert-enoch'], "New. Experts judged about 79 percent of the model's estimates realistic; the result challenges the standard sequence of scripts."),
 'c-daniel-frag': c("One Daniel manuscript from Qumran (4Q114) was radiocarbon-dated to 230-160 BCE, close to the 160s BCE in which most critical scholars date the book's visions.", 'debated', ['popovic2025', 'bg-dan11'], "New. The authors call it possibly the first biblical fragment from about its author's lifetime; traditional readers instead date Daniel to the 6th century BCE."),
 # 8.6
 'c-early-rome': c("Rome began as a small cluster of huts on its hills in the 10th century BCE.", 'approx', ['met-romr'], "An archaeological date; the traditional founding date of 753 BCE is a later calculation."),
 'c-lapis': c("An inscription of the 6th century BCE in the Forum, under the black stone called the Lapis Niger, contains the word for 'king', supporting the tradition that early Rome had kings.", 'tradition', ['jobin-lapis'], "The names and dates of the seven kings in Livy are 'traditional but impossible to verify'."),
 'c-sauer': c("A current Cambridge project argues that archaeology, not Livy, should set the outline of early Rome, and that the old picture of a rich 6th-century monarchy followed by a poorer early republic is outdated.", 'debated', ['carlsberg-sauer'], "The traditional outline follows Livy's chronology."),
 'c-gabii': c("In 2025 excavators at Gabii, east of Rome, reported a large stone-lined basin of about 250 BCE at the city centre, perhaps a monumental pool in a forum-like square built on Greek models.", 'approx', ['sd-gabii2025'], "New. The use of the basin is an interpretation."),
 'c-509': c("By tradition the Romans expelled their last king in 509 BCE and replaced him with two consuls elected each year.", 'tradition', ['brit-republic'], "The date and story come from later Roman writers."),
 'c-institutions': c("The Senate was formally an advisory body but held enormous power; the centuriate assembly declared war and elected the senior magistrates, and the tribal assemblies passed most laws.", 'consensus', ['brit-republic'], show=False),
 'c-orders': c("In the 'Conflict of the Orders' the plebeians won their own tribunes and a written law code, the Twelve Tables, partly by walking out of the city en masse; the Lex Hortensia of 287 BCE made the plebeian assembly's decisions binding on all citizens.", 'consensus', ['brit-orders', 'brit-hortensia'], show=False),
 'c-polybius-mixed': c("Polybius described Rome's constitution as a mix of monarchy (the consuls), aristocracy (the Senate) and democracy (the people), each able to block the others, so that even a Roman could not say which it was (6.11-18).", 'debated', ['polyb6'], "That is what Polybius says; how far his model describes how Rome actually worked is a matter of interpretation."),
 'c-pyrrhus': c("Pyrrhus of Epirus, invited by Tarentum, beat Roman armies in 280 and 279 BCE at such a cost to his own army that 'Pyrrhic victory' became a phrase; he left Italy after 275, and Rome was master of the peninsula.", 'consensus', ['brit-pyrrhus', 'brit-republic'], show=False),
 'c-social-war': c("Rome's Italian allies, refused citizenship, revolted in 91 BCE; the Lex Julia of 90 granted it to communities that stayed loyal or quickly laid down their arms, and it was extended across Italy over the following decades.", 'consensus', ['ebsco-julian'], show=False),
 # 8.7
 'c-punic1': c("The First Punic War (264-241 BCE) began over Messana in Sicily and ended, after a Roman naval victory at the Aegates Islands, with Carthage giving up Sicily.", 'consensus', ['brit-punic'], show=False),
 'c-barcids': c("After that defeat Hamilcar Barca built a Carthaginian domain in Spain from 237 BCE, gaining what the Met calls 'the richest silver mines in the ancient world'.", 'consensus', ['brit-punic', 'met-iberia'], show=False),
 'c-cartagena': c("Hasdrubal founded Qart Hadasht, 'New Town' (Cartagena), whose silver mines helped pay for the war against Rome; Scipio captured it in 209 BCE.", 'consensus', ['brit-cartagena'], show=False),
 'c-saguntum': c("Hannibal's siege of Saguntum in 219 BCE set off the Second Punic War (218-201).", 'consensus', ['brit-punic'], show=False),
 'c-hannibal': c("In 218 BCE Hannibal marched from Spain over the Alps into Italy with about 25,000 infantry and 6,000 cavalry, and won at the Trebia (218), Lake Trasimene (217) and Cannae (216).", 'approx', ['brit-hannibal'], "The army figures are Polybius'; many more set out from Spain."),
 'c-cannae': c("At Cannae perhaps 55,000 to 70,000 Romans were killed in a single day.", 'approx', ['brit-hannibal'], "Livy gives 55,000, Polybius 70,000; both may be high."),
 'c-zama': c("Scipio, later called Africanus, carried the war to Africa and defeated Hannibal at Zama in 202 BCE; Rome destroyed Carthage itself in 146.", 'consensus', ['brit-hannibal', 'brit-republic'], show=False),
 'c-provinces': c("Rome organised its Spanish lands as two provinces, Nearer and Further Spain, in 197 BCE; Augustus later divided them into Tarraconensis, Lusitania and Baetica.", 'consensus', ['brit-nearer-spain'], show=False),
 'c-numantia': c("Numantia, near modern Soria, led Celtiberian resistance; Scipio Aemilianus ringed it with about 10 km of walls, and after some eight months of starvation it surrendered in 133 BCE and was razed.", 'approx', ['brit-numantia', 'grout-numantia'], "The siege's size (perhaps 60,000 Romans against about 4,000 defenders) comes from the ancient historian Appian."),
 'c-cantabrian': c("The conquest of Iberia took nearly 200 years; it ended only with the Cantabrian Wars in the north, where Augustus campaigned in person, in 19 BCE.", 'consensus', ['brit-cantabrian', 'met-iberia'], show=False),
 'c-latin-spanish': c("Spanish grew from the spoken Latin of Roman Hispania; Castilian emerged in Cantabria around the 9th century CE, and its first written traces are notes in 10th-century manuscripts.", 'consensus', ['ebsco-spanish', 'brit-spanish'], show=False),
 'c-medulas': c("At Las Médulas in León, Roman engineers mined gold for about two centuries from the 1st century CE by channelling water to bring down whole hillsides.", 'consensus', ['unesco-medulas'], show=False),
 'c-riotinto': c("Roman miners at Riotinto (Huelva) left vast heaps of slag, mostly from silver; modern open-cast mining has destroyed much of the ancient workings.", 'approx', ['jones1980'], "Estimates of total Roman output rest on slag that has partly disappeared."),
 'c-iberian-lead': c("The Greenland lead record accelerates with Carthaginian and Roman mining, which its authors place mainly in the Iberian Peninsula.", 'debated', ['ku-mcconnell2018', 'mcconnell2018'], "The record itself is secure; reading lead as a measure of the whole economy is debated."),
}

# ---------------------------------------------------------------- 8.4
P4 = {
 'title': "Alexander and the Hellenistic world", 'sub': "336 to 31 BCE",
 'lede': "In eleven years a Macedonian king conquered the Persian empire and marched to India. He left no working state behind him, but the kingdoms his generals carved out spread Greek language and cities from Egypt to Afghanistan for three centuries.",
 'body': [
  "Macedonia, on the northern edge of the Greek world, became its master under Philip II. [[c-philip]] His son Alexander inherited the army and a planned war on Persia in 336 BCE. [[c-alexander]] He crossed into Asia in 334, took Egypt, where he founded Alexandria, [[c-alexandria-found]] and broke Darius III at Gaugamela in 331. [[c-gaugamela]] He pushed on through Iran and Central Asia to the Indus, where his army finally refused to go further. [[c-hydaspes]]",
  "He died at Babylon in 323, and his generals fought over the empire for a generation. What emerged was a world of Greek-speaking dynasties ruling non-Greek majorities: the Ptolemies in Egypt, the Seleucids in Syria, Mesopotamia and Iran, the Antigonids in Macedonia. [[c-hellenistic]] Greek cities were planted as far east as the Oxus, where the French excavators of Aï Khanoum found a gymnasium, a theatre and the maxims of Delphi carved in stone. [[c-aikhanoum]]",
  "The Ptolemies made Alexandria the intellectual capital of the age. Their Library is the most famous lost institution of antiquity, [[c-library]] but the figures for its size come from late writers, and one leading papyrologist thinks they are ten times too large. [[c-library-size]] Its end is equally uncertain. [[c-library-end]]",
  "For readers of the Bible, the great Hellenistic event is the Septuagint. Alexandria had a large Jewish community whose language was Greek, and in the mid-3rd century BCE the Torah was translated for them. [[c-septuagint]] A later legend has 72 elders do it at the king's request. [[c-aristeas]] The Septuagint became the Bible of the early Christians, which is why the Old Testament of many churches follows its order and contents.",
  {'table': {'head': ["Dynasty", "Heartland", "Capital", "Taken by Rome"], 'rows': [
    ["Antigonids", "Macedonia", "Pella", "168 BCE"],
    ["Attalids", "western Anatolia", "Pergamon", "133 BCE, by bequest"],
    ["Seleucids", "Syria, Mesopotamia, Iran", "Antioch", "64 BCE"],
    ["Ptolemies", "Egypt", "Alexandria", "30 BCE, the last"]], 'note': "[[c-hellenistic]]"}},
  {'compare': "The Septuagint's books and order differ from the Hebrew Bible: it includes works such as 1 and 2 Maccabees, Tobit and Judith. Catholic and Orthodox Old Testaments keep many of them; Protestant Bibles follow the shorter Hebrew canon and print them, if at all, as the Apocrypha."}],
 'figure': {'kind': 'map', 'view': {'lon': 48.5, 'lat': 33.0, 'zoom': 6.2}, 'caption': "Alexander's campaigns, 334-323 BCE, and the kingdoms after him", 'hint': "Click a place",
  'legend': [['acc dash', 'march out, 334-326 (simplified)'], ['dash', 'return, 325-323'], ['dot', 'battle or key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'route', 'items': [{'path': [[22.52, 40.76], [26.4, 40.2], [27.3, 40.2], [32.0, 39.65], [36.2, 36.85], [35.2, 33.27], [34.45, 31.5], [31.25, 29.85], [29.92, 31.2], [34.45, 31.5], [35.6, 33.8], [38.2, 36.0], [43.48, 36.59], [44.42, 32.54], [48.25, 32.19], [52.89, 29.94], [48.5, 34.8], [52.0, 35.5], [58.0, 37.0], [62.2, 34.35], [62.1, 32.4], [65.7, 31.6], [69.2, 34.9], [66.9, 36.76], [66.97, 39.65], [66.9, 36.76], [69.2, 34.5], [72.0, 33.9], [73.73, 32.93], [75.3, 31.5]], 'label': 'Alexander', 'lab': [58.0, 37.0], 'ldy': -10, 'acc': True, 'head': True}]},
   {'type': 'route', 'items': [{'path': [[75.3, 31.5], [72.5, 30.5], [71.0, 28.5], [68.4, 25.4], [64.5, 25.6], [61.0, 26.4], [57.0, 28.5], [52.89, 29.94], [48.25, 32.19], [44.42, 32.54]], 'label': 'return through Gedrosia', 'lab': [62.0, 26.2], 'ldy': 16, 'head': True}]},
   {'type': 'region', 'items': [{'ll': [22.0, 41.8], 'label': 'MACEDONIA', 'size': 9}, {'ll': [30.0, 26.5], 'label': 'EGYPT', 'size': 11}, {'ll': [54.5, 31.5], 'label': 'PERSIA', 'size': 11}, {'ll': [65.5, 40.8], 'label': 'BACTRIA', 'size': 10}, {'ll': [72.5, 28.0], 'label': 'INDUS', 'size': 9}, {'ll': [43.5, 34.5], 'label': 'MESOPOTAMIA', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [22.52, 40.76], 'label': 'Pella', 'date': 'born 356', 'acc': True, 'big': True, 'anchor': 'end', 'plate': {'kicker': '8.4 · Macedonia', 'title': 'Philip and Alexander', 'sub': '359 to 323 BCE', 'text': "[[c-philip]] [[c-alexander]]", 'sources': ['brit-philip2', 'brit-alexander']}},
    {'ll': [27.18, 39.13], 'label': 'Pergamon', 'date': 'Attalids', 'dy': 16},
    {'ll': [29.92, 31.2], 'label': 'Alexandria', 'date': 'founded 332/331', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 4, 'plate': {'kicker': '8.4 · Alexandria', 'title': 'Alexandria', 'sub': 'the Library and the Septuagint', 'text': "[[c-alexandria-found]] [[c-library]] [[c-library-size]] [[c-septuagint]] [[c-aristeas]]", 'sources': ['brit-alexandria', 'brit-library', 'bagnall2002', 'brit-septuagint']}},
    {'ll': [36.16, 36.2], 'label': 'Antioch', 'date': 'Seleucids', 'dy': -8},
    {'ll': [43.48, 36.59], 'label': 'Gaugamela', 'date': '331', 'acc': True, 'big': True, 'plate': {'kicker': '8.4 · battle', 'title': 'Gaugamela', 'sub': '1 October 331 BCE', 'text': "[[c-gaugamela]]", 'sources': ['brit-gaugamela']}},
    {'ll': [44.42, 32.54], 'label': 'Babylon', 'date': 'died 323', 'acc': True, 'dy': 16, 'anchor': 'end'},
    {'ll': [52.89, 29.94], 'label': 'Persepolis', 'dy': 16},
    {'ll': [69.41, 37.17], 'label': 'Aï Khanoum', 'date': 'Greek city on the Oxus', 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '8.4 · Bactria', 'title': 'Aï Khanoum', 'sub': 'destroyed about 150 BCE', 'text': "[[c-aikhanoum]]", 'sources': ['iranica-aikhanoum', 'met-afghan2009']}},
    {'ll': [73.73, 32.93], 'label': 'Hydaspes', 'date': '326', 'acc': True, 'anchor': 'end', 'dy': -6, 'plate': {'kicker': '8.4 · India', 'title': 'The Hydaspes', 'sub': '326 BCE', 'text': "[[c-hydaspes]]", 'sources': ['brit-hydaspes']}},
    {'ll': [75.3, 31.5], 'label': 'Beas', 'date': 'army turns back', 'anchor': 'end', 'dy': 18}]}]},
 'practice': [
  q("Why does Roger Bagnall reject the large ancient figures, up to 700,000 rolls, for the Library of Alexandria?",
    ["Excavators found the building and measured its many shelves", "The numbers come from late writers and look far too big", "He accepts 700,000 but thinks most were duplicate copies", "The ancient sources agree on one figure, suggesting copying"], 1,
    "Bagnall argues the figures 'do not deserve any credence' and that the real holdings were probably smaller 'by as much as one order of magnitude'.",
    {0: "Where the Library stood and how it was laid out are unknown.", 2: "He argues the figures 'do not deserve any credence'.", 3: "The ancient figures differ widely: 40,000, about 490,000 or 700,000."}),
  q("What do the Greek inscriptions and buildings of Aï Khanoum show best?",
    ["That Bactria stayed loyal to the Seleucids until about 150 BCE", "That Greek civic life took root far to the east, on the Oxus", "That the city survived into the Roman imperial period", "That Persian rather than Greek culture shaped its public life"], 1,
    "A gymnasium, a theatre and the maxims of Delphi in northern Afghanistan show a Greek city far from Greece, kept up until about 150 BCE.",
    {0: "Bactria broke away from the Seleucids about 250 BCE.", 2: "Steppe nomads destroyed it about 150 BCE.", 3: "It had a gymnasium, a theatre and the maxims of Delphi carved in stone."})]}

# ---------------------------------------------------------------- 8.5
P5 = {
 'title': "Judea between empires", 'sub': "from the Maccabees to Herod",
 'lede': "Under Alexander's successors the small temple-state of Judea was fought over by Egypt and Syria, revolted against a king who outlawed its religion, won some eighty years of independence, and fell to Rome. In these centuries Judaism took the forms, and split into the parties, that the New Testament knows.",
 'body': [
  "After Antiochus III's victory at Panium in 200 BCE, Judea belonged to the Seleucid kings in Antioch. In 168 Antiochus IV was turned back from Egypt by a Roman envoy, [[c-antiochus-egypt]] and the next year he garrisoned Jerusalem, outlawed the Sabbath and circumcision and set up an altar to Zeus in the Temple. [[c-antiochus-ban]] 1 Maccabees, written from the rebels' side, calls it 'a desolating sacrilege'. [[c-desolating]]",
  "A priestly family, the Maccabees, led a guerrilla revolt. In December 164 BCE they retook and rededicated the Temple, [[c-rededication]] and the eight-day festival they founded is Hanukkah. [[c-eight-days]] The familiar story of the oil comes from a much later source. [[c-oil]] Judas' brother Simon won full independence in 142, [[c-hasmonean]] and his descendants, the Hasmoneans, ruled as high priests and then kings until the Roman general Pompey took Jerusalem in 63. [[c-pompey]] Rome then ruled through Herod, who rebuilt the Temple on a vast new platform. [[c-herod]]",
  "Josephus describes three 'philosophies' among the Jews. The Sadducees were the priestly elite; the Pharisees, ancestors of rabbinic Judaism, added an oral law to the written one; [[c-sadducees]] the Essenes lived apart under strict rules. [[c-essenes]]",
  "In 1947 shepherds found the first of the Dead Sea Scrolls near Qumran: the oldest surviving manuscripts of the Hebrew Bible, along with rules, hymns and commentaries of a separatist group. [[c-dss]] Most scholars think that group was Essene, but not all. [[c-qumran]] A 2025 study combining radiocarbon with AI analysis of handwriting has pushed many dates earlier, [[c-enoch]] including a copy of Daniel made perhaps within a lifetime of the book's composition. [[c-daniel-frag]]",
  {'table': {'head': ["Group", "What our sources say", "Caution"], 'rows': [
    ["Sadducees", "priestly elite; written Torah only; no resurrection", "known mainly from opponents; vanish after 70 CE"],
    ["Pharisees", "oral tradition alongside the Torah; resurrection", "described by Josephus, a Pharisee sympathiser, and by the Gospels"],
    ["Essenes", "communal life, strict purity; about 4,000 (Philo, Josephus)", "never named in the New Testament"],
    ["Qumran community", "the scrolls' rule books", "Essene identity is the majority view, not certain"]], 'note': "[[c-sadducees]] [[c-essenes]] [[c-qumran]]"}},
  {'compare': "1 Maccabees 1:54 calls Antiochus' altar 'a desolating sacrilege', and Daniel uses the same words for what is set up in the Temple: 'the desolating sacrilege' (Daniel 11:31; 12:11). The echo is one reason critical scholars date Daniel's visions to these years, 167-164 BCE; traditional readers take them as prophecy from the 6th century."}],
 'figure': {'kind': 'map', 'view': {'lon': 35.25, 'lat': 31.85, 'zoom': 110}, 'caption': "Judea, 2nd to 1st century BCE", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [35.05, 31.6], 'label': 'JUDEA', 'size': 12}, {'ll': [35.25, 32.3], 'label': 'SAMARIA', 'size': 10}, {'ll': [35.4, 32.85], 'label': 'GALILEE', 'size': 10}, {'ll': [34.85, 31.25], 'label': 'IDUMEA', 'size': 9}, {'ll': [35.75, 31.5], 'label': 'DEAD SEA', 'size': 8}]},
   {'type': 'points', 'items': [
    {'ll': [35.235, 31.778], 'label': 'Jerusalem', 'date': 'Temple rededicated 164', 'acc': True, 'big': True, 'anchor': 'end', 'plate': {'kicker': '8.5 · Jerusalem', 'title': 'The Temple', 'sub': '167 BCE to 4 BCE', 'text': "[[c-antiochus-ban]] [[c-rededication]] [[c-eight-days]] [[c-pompey]] [[c-herod]]", 'sources': ['brit-antiochus4', 'bg-1macc4', 'brit-jerusalem-roman']}},
    {'ll': [35.0, 31.93], 'label': 'Modein', 'date': 'home of the Maccabees', 'anchor': 'end', 'dy': -8},
    {'ll': [35.459, 31.741], 'label': 'Qumran', 'date': 'scrolls found 1947', 'acc': True, 'big': True, 'plate': {'kicker': '8.5 · the scrolls', 'title': 'Qumran', 'sub': 'the Dead Sea Scrolls', 'text': "[[c-dss]] [[c-qumran]] [[c-enoch]] [[c-daniel-frag]]", 'sources': ['brit-dss', 'benami2004', 'popovic2025']}},
    {'ll': [35.354, 31.316], 'label': 'Masada', 'date': "Herod's fortress", 'acc': True},
    {'ll': [34.89, 32.5], 'label': 'Caesarea', 'date': "Herod's port", 'anchor': 'end'}]}]},
 'practice': [
  q("A friend says: '1 Maccabees tells us Hanukkah lasts eight days because the oil lasted eight days.' What is the best correction?",
    ["1 Maccabees mentions no eight-day festival of any kind", "The eight days were for the altar; the oil story came later", "The oil story comes from Josephus, not from the books of Maccabees", "2 Maccabees links the eight days to the Passover festival"], 1,
    "1 Maccabees gives eight days for the altar's dedication. The oil story first appears centuries later, in the Babylonian Talmud. Keep the text and the later tradition apart.",
    {0: "1 Maccabees 4:56-59 describes eight days and an annual festival.", 2: "The oil story first appears in the Babylonian Talmud, Shabbat 21b.", 3: "2 Maccabees 10:6 compares the festival to Booths."}),
  q("What does the 2025 'Enoch' study chiefly change?",
    ["It proves the Essenes, not refugees, wrote the scrolls", "Many manuscripts came out older than experts had thought", "It moves most of the scroll dates later, to after 70 CE", "It relies on handwriting alone, with no laboratory dating"], 1,
    "Dates anchored by radiocarbon came out older than handwriting experts had assigned, which challenges the standard sequence of scripts.",
    {0: "It dates manuscripts; who wrote them is a separate debate.", 2: "Many came out older, and its Daniel fragment dates to 230-160 BCE.", 3: "27 radiocarbon-dated samples were used to train the model."})]}

# ---------------------------------------------------------------- 8.6
P6 = {
 'title': "The Roman Republic", 'sub': "a constitution of checks",
 'lede': "Rome began as a village of huts and became master of Italy under a constitution with no single ruler. A Greek hostage who watched it work thought its secret was that every part of the state could block every other, and the framers of the American Constitution read him.",
 'body': [
  "Archaeology finds a cluster of huts on Rome's hills by the 10th century BCE. [[c-early-rome]] The Romans' own story, of seven kings and a republic founded in 509, survives in writers of the 1st century BCE, and only scraps of early evidence back it. [[c-lapis]] [[c-509]] Historians now argue about how much of Livy's early Rome to keep at all, [[c-sauer]] and new excavations, such as the city centre of nearby Gabii, keep adding to the picture. [[c-gabii]]",
  "By the 3rd century BCE the system had a clear shape. Two consuls, elected for a year, commanded the armies. The Senate of former magistrates had no formal power to legislate, but controlled money and foreign policy. Assemblies of citizens elected magistrates, declared war and passed laws. [[c-institutions]] The plebeians, the mass of ordinary citizens, had won their own officers, the tribunes, and a written code by a long struggle that ended in 287 BCE. [[c-orders]]",
  "Polybius, writing in the 2nd century BCE, explained Rome's success by its 'mixed constitution'. [[c-polybius-mixed]] It is the ancestor of the idea of checks and balances; whether it describes how Rome really worked, where wealthy families dominated every office, is another question.",
  "The Republic conquered Italy by war and by alliance. A Greek king, Pyrrhus, came to stop it and won battles he could not afford. [[c-pyrrhus]] Rome bound the defeated as allies who supplied soldiers but could not vote. When they demanded citizenship and were refused, they rebelled in 91 BCE, and Rome conceded what they had asked for. [[c-social-war]]",
  {'table': {'head': ["Office or body", "Who", "Term", "Main powers"], 'rows': [
    ["Consuls", "2, elected", "1 year", "command armies; preside over Senate and assemblies"],
    ["Senate", "about 300 former magistrates", "for life", "finance, foreign policy, advice"],
    ["Tribunes of the plebs", "10, elected by plebeians", "1 year", "veto; protect citizens; propose laws"],
    ["Assemblies", "adult male citizens", "-", "elect magistrates, declare war, pass laws"]], 'note': "[[c-institutions]] [[c-orders]] [[c-polybius-mixed]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ledger', 'signs': False, 'caption': "Polybius' mixed constitution", 'title': "How each part of the Roman state could check the others (Polybius, Histories 6)",
  'left': {'h': 'Each part held power...', 'items': [
   {'t': 'Consuls: supreme command in war', 's': 'Polybius 6.12 (the monarchic part)'},
   {'t': 'Senate: the treasury and embassies', 's': 'Polybius 6.13 (the aristocratic part)'},
   {'t': 'People: honours, punishments, laws, war and peace', 's': 'Polybius 6.14 (the democratic part)'}]},
  'right': {'h': '...and depended on the others', 'items': [
   {'t': 'Consuls need Senate funds and popular votes', 's': 'Polybius 6.15'},
   {'t': "Senate's decrees can be blocked by a tribune's veto", 's': 'Polybius 6.16'},
   {'t': 'People depend on the Senate for contracts and judges', 's': 'Polybius 6.17'}]},
  'notes': ["Polybius 6.18: when one part grows too strong, the others hold it back. This is his model, not a legal text."]},
 'practice': [
  q("According to Polybius, why was the Roman Republic stable?",
    ["The Senate held absolute power, so there was no rivalry", "Consuls, Senate and people could each check the others", "Its consuls were elected for life, giving continuity", "Even a Roman could tell at once that it was a democracy"], 1,
    "Polybius saw a mix of monarchy (the consuls), aristocracy (the Senate) and democracy (the people), each able to block the others.",
    {0: "He says each part could block the others.", 2: "Consuls were elected for one-year terms, two at a time.", 3: "He says even a Roman could not say which kind of constitution it was."}),
  q("What did the Lex Hortensia of 287 BCE change?",
    ["It created the consulship and the system of two consuls", "It gave Roman citizenship to the Italian allies", "It made plebeian assembly decisions bind every citizen", "It took control of finance away from the Senate"], 2,
    "It made the plebeian assembly's decisions binding on all citizens, and is usually taken as the end of the Conflict of the Orders.",
    {0: "By tradition, two consuls replaced the kings in 509 BCE.", 1: "That came after the allies' revolt of 91 BCE, from 90 BCE.", 3: "The Senate still controlled money and foreign policy."})]}

# ---------------------------------------------------------------- 8.7
P7 = {
 'title': "Rome, Carthage and Hispania", 'sub': "264 BCE to 19 BCE",
 'lede': "Rome and Carthage fought three wars over a century for the western Mediterranean, and much of the second was fought in and for Spain. Rome needed nearly two centuries to conquer the peninsula; in the process it left Spain its language, its towns and a layer of lead in the Greenland ice.",
 'body': [
  "The first war, fought over Sicily, ended in 241 BCE with Carthage's defeat at sea. [[c-punic1]] Carthage looked west for compensation. The Barcid family built a power base in southern and eastern Spain, with silver mines that paid for armies, [[c-barcids]] and a new capital at Cartagena, still called after Carthage today. [[c-cartagena]]",
  "From Spain Hannibal launched the second war. He besieged Saguntum in 219, [[c-saguntum]] crossed the Pyrenees and the Alps with elephants, and destroyed three Roman armies in three years. [[c-hannibal]] At Cannae in 216 more Romans died in one afternoon than in almost any battle in history. [[c-cannae]] Rome refused to make peace. Scipio cut off Hannibal's Spanish base by taking Cartagena in 209 and beat him in Africa at Zama in 202. Half a century later, in 146, Rome razed Carthage. [[c-zama]]",
  "Rome stayed in Spain, organising two provinces in 197 BCE. [[c-provinces]] The conquest was long and brutal: the Celtiberian town of Numantia held out until 133, when its starving people surrendered, [[c-numantia]] and the north was subdued only under Augustus. [[c-cantabrian]] By then southern Spain was among the most Roman places outside Italy. Spanish descends from the Latin spoken there. [[c-latin-spanish]]",
  "The Romans also mined Spain on an industrial scale: gold at Las Médulas, where they washed away mountains, [[c-medulas]] and silver at Riotinto. [[c-riotinto]] Smelting released lead that drifted to Greenland and fell in the snow, so the ice cores carry a year-by-year record of Iberian mining. [[c-iberian-lead]] [[c-lead-ice]]",
  {'table': {'head': ["Year (BCE)", "Event"], 'rows': [
    ["264-241", "First Punic War; Carthage loses Sicily"],
    ["237", "Hamilcar Barca begins a Carthaginian domain in Spain"],
    ["218-201", "Second Punic War: Hannibal in Italy, Scipio in Spain and Africa"],
    ["209", "Scipio takes Cartagena"],
    ["197", "Nearer and Further Spain become Roman provinces"],
    ["146", "Carthage destroyed"],
    ["133", "Numantia falls"],
    ["19", "Cantabrian Wars end the conquest of Iberia"]], 'note': "[[c-punic1]] [[c-barcids]] [[c-cartagena]] [[c-provinces]] [[c-zama]] [[c-numantia]] [[c-cantabrian]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 3.2, 'lat': 40.0, 'zoom': 11}, 'caption': "Rome and Carthage in the west, 264-19 BCE", 'hint': "Click a place",
  'legend': [['acc dash', "Hannibal's march, 218-216 (simplified)"], ['dot', 'battle, siege or key place'], ['pt', 'other place or mine']], 'seas': False,
  'layers': [
   {'type': 'route', 'items': [{'path': [[-0.98, 37.6], [-0.3, 39.5], [0.8, 41.0], [2.5, 42.0], [3.0, 42.8], [4.0, 43.7], [4.8, 44.0], [5.8, 44.8], [6.8, 45.2], [7.7, 45.1], [9.6, 45.05], [11.0, 44.4], [12.1, 43.13], [13.5, 42.3], [16.13, 41.31]], 'label': 'Hannibal, 218', 'lab': [4.8, 44.0], 'ldy': -14, 'acc': True, 'head': True}]},
   {'type': 'region', 'items': [{'ll': [-2.8, 41.2], 'label': 'CELTIBERIA', 'size': 9}, {'ll': [-5.2, 43.2], 'label': 'CANTABRIA', 'size': 8}, {'ll': [2.5, 46.5], 'label': 'GAUL', 'size': 10}, {'ll': [5.6, 35.4], 'label': 'NUMIDIA', 'size': 9}, {'ll': [-5.0, 38.4], 'label': 'BAETICA', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [12.49, 41.89], 'label': 'Rome', 'acc': True, 'big': True, 'dy': -10},
    {'ll': [10.323, 36.853], 'label': 'Carthage', 'date': 'destroyed 146', 'acc': True, 'big': True, 'dy': -12, 'plate': {'kicker': '8.7 · Carthage', 'title': 'Carthage', 'sub': 'destroyed 146 BCE', 'text': "[[c-punic1]] [[c-zama]]", 'sources': ['brit-punic', 'brit-hannibal']}},
    {'ll': [-0.98, 37.6], 'label': 'Cartagena', 'date': 'Qart Hadasht; taken 209', 'acc': True, 'big': True, 'dy': 14, 'plate': {'kicker': '8.7 · Spain', 'title': 'Qart Hadasht', 'sub': 'Cartagena', 'text': "[[c-barcids]] [[c-cartagena]]", 'sources': ['met-iberia', 'brit-cartagena']}},
    {'ll': [-0.28, 39.68], 'label': 'Saguntum', 'date': '219', 'acc': True},
    {'ll': [3.12, 42.13], 'label': 'Emporion', 'date': 'Romans land 218', 'dy': 14},
    {'ll': [9.6, 45.05], 'label': 'Trebia', 'date': '218', 'acc': True, 'dy': -8},
    {'ll': [12.1, 43.13], 'label': 'Trasimene', 'date': '217', 'acc': True, 'anchor': 'end'},
    {'ll': [16.13, 41.31], 'label': 'Cannae', 'date': '216', 'acc': True, 'big': True, 'dy': 14, 'plate': {'kicker': '8.7 · battle', 'title': 'Cannae', 'sub': '216 BCE', 'text': "[[c-hannibal]] [[c-cannae]]", 'sources': ['brit-hannibal']}},
    {'ll': [9.4, 36.3], 'label': 'Zama', 'date': '202', 'acc': True, 'anchor': 'end', 'dy': 16},
    {'ll': [-2.44, 41.81], 'label': 'Numantia', 'date': 'falls 133', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '8.7 · Hispania', 'title': 'Numantia', 'sub': '133 BCE', 'text': "[[c-numantia]] [[c-cantabrian]]", 'sources': ['brit-numantia', 'grout-numantia', 'brit-cantabrian']}},
    {'ll': [-6.77, 42.46], 'label': 'Las Médulas', 'date': 'gold, 1st-2nd century CE', 'anchor': 'end', 'plate': {'kicker': '8.7 · mining', 'title': 'Las Médulas', 'sub': 'Roman gold mines', 'text': "[[c-medulas]] [[c-iberian-lead]]", 'sources': ['unesco-medulas', 'ku-mcconnell2018']}},
    {'ll': [-6.59, 37.69], 'label': 'Riotinto', 'date': 'silver', 'anchor': 'end', 'plate': {'kicker': '8.7 · mining', 'title': 'Riotinto', 'sub': 'Roman silver mines', 'text': "[[c-riotinto]] [[c-iberian-lead]]", 'sources': ['jones1980', 'ku-mcconnell2018']}}]}]},
 'practice': [
  q("Why does ice from Greenland record the history of Roman Spain?",
    ["Romans shipped Spanish ore north to smelters in Greenland", "Smelting sent lead north on the wind, into the snow", "The ice records volcanic eruptions, not human activity", "Lead peaked under the Republic and vanished under Augustus"], 1,
    "Smelting lead-silver ore released lead that drifted to Greenland and fell in the snow, leaving a year-by-year record of Iberian mining.",
    {0: "The ore was smelted in Spain; the lead reached Greenland through the air.", 2: "It records European mining and smelting year by year.", 3: "Lead in the ice peaks under the Roman empire."}),
  q("Why did Carthage's presence in Spain matter so much to Rome?",
    ["Spain was Carthage's oldest and most loyal overseas colony", "Its silver paid for armies, and Hannibal marched from there", "Rome had already conquered the whole of Spain before 218 BCE", "Hannibal sailed from Cartagena to invade Italy by sea"], 1,
    "Spanish silver paid for Carthage's war, and Hannibal launched his invasion from Spain. That is why Scipio struck at Cartagena in 209 BCE.",
    {0: "The Barcid domain in Spain dates from 237 BCE, after the First Punic War.", 2: "The conquest of Iberia was completed only in 19 BCE.", 3: "He marched overland, across the Pyrenees and the Alps."})]}

PAGES = [P4, P5, P6, P7]
