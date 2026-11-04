# Chapter 8, pages 8.0 to 8.3. Coordinates are [longitude, latitude].
from common import c, q

MIT = "https://classics.mit.edu/"
S = {
 'brit-herodotus': ("Encyclopaedia Britannica, \"Herodotus\"", "https://www.britannica.com/biography/Herodotus-Greek-historian"),
 'thuc1': ("Thucydides, History of the Peloponnesian War, Book 1, tr. Crawley (MIT Internet Classics Archive)", MIT + "Thucydides/pelopwar.1.first.html"),
 'thuc2': ("Thucydides, History of the Peloponnesian War, Book 2, tr. Crawley (MIT Internet Classics Archive)", MIT + "Thucydides/pelopwar.2.second.html"),
 'thuc5': ("Thucydides, History of the Peloponnesian War, Book 5, tr. Crawley (MIT Internet Classics Archive)", MIT + "Thucydides/pelopwar.5.fifth.html"),
 'brit-polybius': ("Encyclopaedia Britannica, \"Polybius\"", "https://www.britannica.com/biography/Polybius"),
 'polyb1': ("Polybius, Histories, Book 1 (Loeb translation on LacusCurtius)", "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Polybius/1*.html"),
 'brit-livy': ("Encyclopaedia Britannica, \"Livy\"", "https://www.britannica.com/biography/Livy"),
 'brit-josephus': ("Encyclopaedia Britannica, \"Flavius Josephus\"", "https://www.britannica.com/biography/Flavius-Josephus"),
 'aio-ig259': ("Attic Inscriptions Online, IG I³ 259: the first Athenian tribute quota list, 454/3 BCE", "https://atticinscriptions.com/inscription/IGI3/259"),
 'gr-2500': ("Hellenic Ministry of Culture, \"2500 Years Since Thermopylae and Salamis: excavations\"", "https://2500years.culture.gov.gr/en/chapters/anaskafes"),
 'wilson2011': ("Andrew Wilson, \"Developments in Mediterranean shipping and maritime trade from the Hellenistic period to AD 1000\" (Oxford, 2011)", "https://www.ancientportsantiques.com/wp-content/uploads/Documents/AUTHORS/Wilson2011-MedShipping.pdf"),
 'oxrep-wrecks': ("Oxford Roman Economy Project, shipwrecks database", "https://oxrep.web.ox.ac.uk/shipwrecks-database"),
 'mcconnell2018': ("EurekAlert, on McConnell et al., \"Lead pollution recorded in Greenland ice indicates European emissions tracked plagues, wars, and imperial expansion during antiquity\", PNAS (2018)", "https://www.eurekalert.org/news-releases/866148"),
 'mcconnell2025': ("McConnell et al., \"Pan-European atmospheric lead pollution, enhanced blood lead levels, and cognitive decline from Roman-era mining and smelting\", PNAS 122 (2025), Oxford record", "https://ora.ox.ac.uk/objects/uuid:286d749d-5295-4ac1-be27-5161d167ba54"),
 'nbc-lead2025': ("NBC News, on the 2025 Roman lead and IQ study, with comments by Bruce Lanphear and Joseph Manning", "https://www.nbcnews.com/news/amp/rcna186200"),
 'cnn-herculaneum': ("CNN, on the Herculaneum scroll PHerc. 172 identified as Philodemus' On Vices (May 2025)", "https://edition.cnn.com/2025/05/06/science/herculaneum-scroll-title-author-decoded-intl-scli"),
 # 8.1
 'brit-grecopersian': ("Encyclopaedia Britannica, \"Greco-Persian Wars\"", "https://www.britannica.com/event/Greco-Persian-Wars"),
 'brit-salamis': ("Encyclopaedia Britannica, \"Battle of Salamis\"", "https://www.britannica.com/event/Battle-of-Salamis"),
 'livius-salamis': ("Livius, \"Salamis (480 BCE)\"", "https://www.livius.org/articles/battle/salamis-480-bce/"),
 'tarn1908': ("W. W. Tarn, \"The fleet of Xerxes\", Journal of Hellenic Studies 28 (1908)", "https://www.cambridge.org/core/journals/journal-of-hellenic-studies/article/abs/fleet-of-xerxes/F9124D82E10B775A1CBF2D583244479A"),
 'bmcr-2021-09-04': ("Bryn Mawr Classical Review 2021.09.04 (S. Hirsch, review)", "https://bmcr.brynmawr.edu/?p=63178"),
 'isserlin2003': ("Isserlin, Jones, Karastathis et al., \"The canal of Xerxes: summary of investigations 1991-2001\", Annual of the British School at Athens 98 (2003)", "https://www.cambridge.org/core/journals/annual-of-the-british-school-at-athens/article/canal-of-xerxes-summary-of-investigations-19912001/35C2DDE7525BB541A8C97C8A6AAA8CC8"),
 'isac-pfa': ("Institute for the Study of Ancient Cultures, University of Chicago, Persepolis Fortification Archive project", "https://isac.uchicago.edu/node/2474"),
 'livius-pft': ("Livius, \"Persepolis Fortification Tablets\"", "https://www.livius.org/sources/about/persepolis-fortification-tablets/"),
 'livius-datis': ("Livius, \"Datis\"", "https://www.livius.org/articles/person/datis/"),
 'almonitor2024': ("Al-Monitor, \"US returns to Iran latest batch of ancient clay tablets\" (27 September 2024)", "https://www.al-monitor.com/originals/2024/09/us-returns-iran-latest-batch-ancient-clay-tablets"),
 'eie-yauna': ("National Hellenic Research Foundation, \"Greeks in Iran\" (Iranohellenica)", "https://iranohellenica.eie.gr/node/11"),
 # 8.2
 'athpol': ("Aristotle (school of), The Athenian Constitution, tr. Kenyon (MIT Internet Classics Archive)", MIT + "Aristotle/athenian_const.mb.txt"),
 'demos': ("C. W. Blackwell, \"The development of Athenian democracy\", Dēmos: Classical Athenian Democracy (Stoa, 2003)", "https://www.stoa.org/demos/article_democracy_overview@page=all&greekEncoding=UnicodeC.html"),
 'brit-ostracism': ("Encyclopaedia Britannica, \"Ostracism\"", "https://www.britannica.com/topic/ostracism"),
 'agora25': ("Mabel Lang, Ostraka, The Athenian Agora XXV (1990)", "https://ambrosia.ascsa.net/id/agora/publication/agora%2025"),
 'sickinger2017': ("James Sickinger, \"New ostraka from the Athenian Agora\", Hesperia 86.3 (2017)", "https://ascsa.edu.gr/publications/hesperia/article/86/3/443-508"),
 'brit-pelwar-sum': ("Encyclopaedia Britannica, \"Peloponnesian War\" summary", "https://www.britannica.com/summary/Peloponnesian-War"),
 'sehepunkte-akrigg': ("Review of Ben Akrigg, Population and Economy in Classical Athens (2019), sehepunkte 21 (2021)", "https://www.sehepunkte.de/2021/01/33368.html"),
 'cfa-akrigg': ("Classics for All, review of Akrigg, Population and Economy in Classical Athens", "https://classicsforall.org.uk/reading-room/book-reviews/population-and-economy-classical-athens"),
 'bmcr-akrigg': ("Matthew Simonton, review of Akrigg, Population and Economy in Classical Athens, Bryn Mawr Classical Review 2020.10.40", "https://bmcr.brynmawr.edu/?p=49324"),
 'akrigg-ch4': ("Ben Akrigg, Population and Economy in Classical Athens (Cambridge, 2019), ch. 4, \"Population size 2: non-citizens\"", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5B4418529EDF6E9DC300F43190ECDF6E/9781107027091c4_89-138.pdf/population_size_2_noncitizens.pdf"),
 # 8.3
 'sd-typhoid2006': ("ScienceDaily, on Papagrigorakis et al., DNA from the Kerameikos mass grave (2006)", "https://www.sciencedaily.com/releases/2006/01/060123163827.htm"),
 'ijid-noproof': ("\"No proof that typhoid caused the Plague of Athens\", International Journal of Infectious Diseases 10.4 (2006), record", "https://www.scilit.net/publications/4f2c923baf3d3b532d91b14f866d916b"),
 'nature-plague': ("Nature news, on candidate diseases for the plague of Athens", "https://www.nature.com/articles/4813343"),
 'apology': ("Plato, Apology, tr. Jowett (MIT Internet Classics Archive)", MIT + "Plato/apology.html"),
 'sep-socrates': ("Stanford Encyclopedia of Philosophy, \"Socrates\"", "https://plato.stanford.edu/entries/socrates/"),
 'brit-socrates': ("Encyclopaedia Britannica, \"Socrates\"", "https://www.britannica.com/biography/Socrates"),
}

C = {
 # 8.0: how we know
 'c-herodotus': c("Herodotus came from Halicarnassus (modern Bodrum), a Greek city under Persian rule; his Histories are 'the first great narrative history produced in the ancient world'.", 'approx', ['brit-herodotus'], "He was born about 484 BCE and died between about 430 and 420; neither date is secure."),
 'c-thuc-speeches': c("Thucydides says he wrote his speeches 'adhering as closely as possible to the general sense of what they really said', and called his book 'a possession for all time' (1.22).", 'consensus', ['thuc1'], show=False),
 'c-polybius': c("Polybius, a Greek hostage in Rome, set out to explain how the Romans 'in less than fifty-three years' had brought nearly the whole inhabited world under their rule (1.1).", 'approx', ['brit-polybius', 'polyb1'], "His own dates, about 200 to about 118 BCE, are approximate; the fifty-three years run from 220 to the fall of Macedon in 168/167 BCE."),
 'c-livy': c("Livy (died 17 CE) wrote 142 books of Roman history; only 35 survive (Books 1-10 and 21-45), and the rest are known from short summaries.", 'consensus', ['brit-livy'], show=False),
 'c-josephus': c("Josephus (born 37/38 CE, died about 100) wrote the Jewish War in the 70s and the Jewish Antiquities in 93/94 CE; he is the main narrative source for Judea in this period.", 'consensus', ['brit-josephus'], show=False),
 'c-inscriptions': c("Inscriptions preserve state records that no historian quotes: from 454/3 BCE Athens carved on stone the sixtieth of each ally's tribute dedicated to Athena.", 'consensus', ['aio-ig259'], show=False),
 'c-wrecks': c("Counts of dated shipwrecks rise steeply in the late Republic and peak in the 1st century CE; in the 2nd and 3rd centuries they fall below a third of that peak.", 'debated', ['wilson2011', 'oxrep-wrecks'], "Andrew Wilson, who compiled the counts, warns that wrecks are not a direct measure of trade: amphora cargoes are easy to find, barrels and perishable goods are not, and some coasts are barely surveyed."),
 'c-lead-ice': c("Lead in Greenland ice records European mining and smelting year by year from 1100 BCE to 800 CE: it rises with Phoenician expansion, peaks under the Roman empire, and dips during wars and after the Antonine plague.", 'approx', ['mcconnell2018'], "The measurements are secure; matching individual dips to particular wars and plagues is interpretation."),
 'c-lead-iq': c("A 2025 study estimates that Roman-era airborne lead raised children's blood lead across Europe enough to lower average IQ by about 2.5 to 3 points.", 'debated', ['mcconnell2025', 'nbc-lead2025', 'univie-lead'], "New and model-based, not measured in people. Bruce Lanphear calls it 'likely to be an underestimate', since it counts only airborne lead and not sources such as lead-sweetened wine or pipes, and says 'it's never just one thing'; Joseph Manning notes that the lead came 'on top of really horrible sanitary conditions'."),
 'c-herculaneum': c("Scrolls carbonised at Herculaneum by Vesuvius in 79 CE are now being read without unrolling them: the first word was read in 2023, and in 2025 one scroll was identified as a work of the philosopher Philodemus, On Vices.", 'approx', ['cnn-herculaneum'], "New. The method combines X-ray scans with machine learning; only small parts of a few scrolls have been read so far."),
 # 8.1
 'c-ionian': c("The Ionian Revolt was a failed rising of the Greek cities of western Anatolia against Persia; Athens and Eretria sent a small fleet to help.", 'approx', ['brit-grecopersian'], "Usually dated 499-494 BCE; Britannica gives 500-494."),
 'c-marathon': c("At Marathon in 490 BCE about 10,000 Athenians and 1,000 Plataeans defeated a Persian landing force; Herodotus gives the dead as 192 Greeks and 6,400 Persians.", 'approx', ['brit-grecopersian'], "The outcome is certain; the figures come from Herodotus, and the size of the Persian force (Britannica says about 25,000) is an estimate."),
 'c-thermopylae': c("In August 480 BCE Leonidas of Sparta held the pass at Thermopylae for two days, until a local man guided Persian troops around it; the Greek fleet fought at Artemisium at the same time.", 'consensus', ['brit-grecopersian'], show=False),
 'c-athens-burned': c("The Persians burned the evacuated city of Athens in 480 BCE; excavators have found burned monuments on the Acropolis and destroyed buildings in the Agora.", 'consensus', ['gr-2500'], show=False),
 'c-salamis': c("At Salamis in September 480 BCE about 370 Greek triremes defeated a Persian fleet perhaps twice as large in the narrow strait.", 'approx', ['brit-salamis', 'livius-salamis'], "Britannica gives about 800 Persian ships; the exact day is also uncertain (Livius suggests 29 September)."),
 'c-plataea': c("In 479 BCE a Spartan-led army won at Plataea, and the Greeks destroyed the beached Persian fleet at Mycale, ending the invasion.", 'consensus', ['brit-grecopersian'], show=False),
 'c-xerxes-army': c("Herodotus gives Xerxes an army of millions; modern historians reject that figure but disagree about the real size.", 'debated', ['brit-grecopersian', 'tarn1908', 'bmcr-2021-09-04'], "For the fleet alone, scholars already ranged in 1908 from Delbrück's 300 ships at most to Herodotus' 1,207; one recent estimate puts about 200,000 fighting men at Plataea, on both sides together."),
 'c-herodotus-court': c("Herodotus' speeches and scenes at Xerxes' court are literary reconstructions; one reviewer calls it 'virtually inconceivable' that he knew what the king said in private.", 'consensus', ['bmcr-2021-09-04'], show=False),
 'c-athos': c("Geophysical survey and boreholes across the Athos peninsula (1991-2001) found a buried channel about 30 m wide, most likely the canal Herodotus says Xerxes dug for his fleet.", 'approx', ['isserlin2003'], "'Most likely' is the investigators' own judgement; the canal's course is reconstructed from cores and survey."),
 'c-pfa': c("The Persepolis Fortification Archive, found in 1933, holds some 15,000 to 18,000 inscribed tablets, mostly in Elamite, recording food stores and rations around 500 BCE.", 'approx', ['isac-pfa', 'livius-pft'], "Counts vary because so many tablets are fragments; the dated texts run from about 509 to 494 BCE on most reckonings (Livius gives 506-497)."),
 'c-datis': c("A Persepolis tablet of 494 BCE issues wine to 'Datiya', who was carrying a sealed royal document from Sardis to the king; he is probably Datis, a commander at Marathon four years later.", 'debated', ['livius-datis'], "The identification is widely accepted but not proven. Jona Lendering also argues that, for Persia, Marathon was a minor setback rather than the decisive defeat of Greek tradition."),
 'c-pfa-return': c("The University of Chicago returned more than 3,500 of the tablets to Iran in 2023 and another 1,100 in 2024.", 'consensus', ['almonitor2024'], show=False),
 'c-yauna': c("Darius's inscriptions call Greeks Yaunā, a word related to 'Ionians'.", 'debated', ['eie-yauna'], "Whether Persians meant all Greeks or chiefly those of Asia Minor is debated."),
 # 8.2
 'c-cleisthenes': c("Cleisthenes (508/7 BCE) replaced Athens' four old tribes with ten new ones and enlarged the Council from 400 to 500 members.", 'consensus', ['athpol'], show=False),
 'c-council': c("The Council of 500 was chosen by lot, 50 from each tribe, from citizens over 30; the Assembly met on the Pnyx hill four times in each tenth of the year and usually voted by show of hands.", 'consensus', ['demos'], show=False),
 'c-generals': c("Generals (strategoi) were elected, not chosen by lot: the one job where Athenians thought skill mattered more than equal chances.", 'consensus', ['demos'], show=False),
 'c-quorum': c("Some decisions, taken by secret ballot, needed at least 6,000 citizens present.", 'consensus', ['demos'], show=False),
 'c-ostracism': c("Ostracism, credited to Cleisthenes, sent a leading citizen out of Attica for ten years without any charge, though he kept his property; it was first used in 488/7 BCE and last probably in 417.", 'approx', ['brit-ostracism'], "The last date is uncertain (417 or 416)."),
 'c-ostraka': c("The potsherd ballots survive: the Agora excavations published 1,145 from the Agora itself and 191 from one well, most naming Themistocles; more than 150 from the 480s, published in 2017, mostly name Xanthippos, Pericles' father.", 'consensus', ['agora25', 'sickinger2017'], show=False),
 'c-pay': c("Pericles 'was the first to institute pay for service in the law-courts'; later, pay for attending the Assembly began at one obol and rose to three.", 'tradition', ['athpol', 'demos'], "Both statements come from the Athenian Constitution (27, 41); jurors were paid three obols a day."),
 'c-juries': c("Athenian juries were very large and chosen by lot: 201 or 401 citizens for private suits, and 501 or more, up to 1,500, for public cases.", 'consensus', ['demos', 'athpol'], show=False),
 'c-citizen-law': c("A law proposed by Pericles limited citizenship to those 'of citizen birth by both parents'.", 'tradition', ['athpol'], "Conventionally dated 451/0 BCE from the Athenian Constitution (26)."),
 'c-excluded': c("Only adult male citizens could speak and vote; women, slaves and resident foreigners (metics) had no political rights. Pericles' funeral speech praises the woman who is 'least talked of among the men'.", 'consensus', ['demos', 'thuc2'], show=False),
 'c-delian': c("The Delian League was founded in 478 BCE under Athenian leadership with its treasury on Delos; the treasury moved to Athens in 454/3, and the allies' payments became, in effect, tribute.", 'consensus', ['brit-pelwar-sum', 'aio-ig259'], show=False),
 'c-first-stele': c("The 'first stele' of the tribute lists, about 3.8 m tall and rebuilt from 184 fragments, records payments from 454/3 to 440/39 BCE.", 'consensus', ['aio-ig259'], show=False),
 'c-athens-pop': c("Attica in 431 BCE may have held about 250,000 people, of whom about 60,000 were adult male citizens.", 'debated', ['sehepunkte-akrigg', 'cfa-akrigg', 'bmcr-akrigg'], "This follows Mogens Hansen and Ben Akrigg; reviewers of Akrigg's book report his totals differently (one reads him as allowing 400,000 or more), and every figure is a reconstruction."),
 'c-slaves': c("Estimates of the number of slaves in Athens differ more than fivefold, from about 20,000 to about 100,000.", 'debated', ['akrigg-ch4'], "Low: A. H. M. Jones and Victor Hanson (20,000-30,000). High: Mogens Hansen (66,000-93,000), Peter Rhodes (about 100,000). An ancient 'census' of 400,000 slaves is generally rejected. Akrigg sets a floor of more than 30,000 enslaved men in 431."),
 'c-empire-gain': c("Who gained most from the Athenian empire is disputed.", 'debated', ['bmcr-akrigg'], "Akrigg, following Moses Finley, argues the rich gained most; his reviewer Matthew Simonton finds the evidence too thin to say."),
 # 8.3
 'c-truest-cause': c("Thucydides named the war's real cause as 'the growth of the power of Athens, and the alarm which this inspired in Lacedaemon' (1.23).", 'debated', ['thuc1'], "The words are certain; whether they are the right explanation is a long-running argument (the modern 'Thucydides trap' idea builds on them)."),
 'c-resources431': c("In 431 BCE, Pericles reckoned, Athens took in about 600 talents a year from its allies, held 6,000 talents of coined silver on the Acropolis, and had 13,000 hoplites, 16,000 garrison troops and 300 seaworthy triremes (2.13).", 'approx', ['thuc2'], "These are figures Thucydides puts in Pericles' mouth; modern scholars broadly accept their scale."),
 'c-war-course': c("The war ran from 431 to 404 BCE: a first decade ended by the Peace of Nicias (421), the disaster in Sicily (415-413), a brief oligarchy at Athens (411), and Sparta's victory at Aegospotami (405), paid for with Persian money.", 'consensus', ['brit-pelwar-sum'], show=False),
 'c-thuc-exile': c("Thucydides was himself an Athenian general; after losing Amphipolis in 424 BCE he spent twenty years in exile (5.26).", 'consensus', ['thuc5'], show=False),
 'c-plague': c("A plague reached Athens through its port in 430 BCE; Thucydides, who 'had the disease myself', describes fever, inflamed eyes, coughing, pustules and unbearable thirst (2.48-49). It killed Pericles.", 'consensus', ['thuc2', 'brit-pelwar-sum'], show=False),
 'c-plague-toll': c("Perhaps up to a third of the people of Athens died.", 'approx', ['sd-typhoid2006'], "No count survives; this is a modern estimate."),
 'c-typhoid': c("DNA from teeth in a mass grave of 430-426 BCE in the Kerameikos cemetery matched sequences similar to typhoid fever, which the team called 'the probable cause'.", 'debated', ['sd-typhoid2006', 'ijid-noproof', 'nature-plague'], "Challenged at once in a reply titled 'No proof that typhoid caused the Plague of Athens'. Earlier candidates include smallpox, measles and bubonic plague; no newer study has settled it."),
 'c-melos': c("In 416 BCE Athens demanded that neutral Melos submit; in Thucydides' dialogue the Athenians say 'the strong do what they can and the weak suffer what they must' (5.89). When Melos fell, Athens killed its men and enslaved its women and children (5.116).", 'debated', ['thuc5'], "The killing is narrated as fact; the dialogue is Thucydides' own composition, read by some as a lesson in realism and by others as an indictment of Athenian arrogance."),
 'c-socrates-trial': c("In 399 BCE Socrates, aged 70, was tried for impiety and corrupting the young, found guilty and sentenced to death; in Plato's Apology he says that if thirty votes had gone the other way he would have been acquitted.", 'consensus', ['apology', 'sep-socrates'], show=False),
 'c-socrates-politics': c("The trial came four years after the oligarchy of the Thirty, among them Socrates' associate Critias, had been overthrown.", 'debated', ['sep-socrates', 'brit-socrates'], "Many scholars think his links to the Thirty mattered, though an amnesty barred charges for their crimes; our accounts of the trial come from his admirers Plato and Xenophon."),
}


# ---------------------------------------------------------------- 8.0
P0 = {
 'title': "Persia, Greece and Rome", 'sub': "the classical Mediterranean, c. 500 BCE to 250 CE",
 'lede': "In 500 BCE the largest state on earth was Persia, and the Greeks were a scatter of quarrelling cities on its western edge. By 150 CE one empire, Rome, ruled every shore of the Mediterranean. This chapter follows that shift, and the ideas that came out of it: democracy, the republic, history-writing, rabbinic Judaism and Christianity.",
 'body': [
  "The story has four acts. First the Greek cities beat off Persia, [[c-salamis]] and Athens built a democracy and an empire. Then Alexander of Macedon conquered Persia itself, [[c-alexander]] and his generals' kingdoms spread Greek language and cities from Egypt to Afghanistan. [[c-hellenistic]] Meanwhile Rome conquered Italy, destroyed Carthage [[c-zama]] and absorbed the Greek kingdoms one by one. Finally the Roman Republic gave way to emperors, [[c-augustus]] whose peace lasted, with interruptions, into the 2nd century CE. [[c-five-good]]",
  "This is the first period in this book for which we have real historians. Herodotus wrote the history of the Persian Wars a generation after them; [[c-herodotus]] Thucydides wrote about a war he fought in, and told his readers how he composed his speeches. [[c-thuc-speeches]] Polybius explained Rome's rise to the Greeks, [[c-polybius]] Livy told Rome's story to the Romans, [[c-livy]] and Josephus, a Jewish general who changed sides, wrote the history of his own people's war with Rome. [[c-josephus]] All of them had views and loyalties, and all of them made up speeches.",
  "So historians test the texts against other evidence. Inscriptions preserve official records that the writers never quote. [[c-inscriptions]] Shipwrecks map the rise and fall of seaborne trade, though not perfectly. [[c-wrecks]] And the Greenland ice sheet holds a year-by-year record of Roman mining and smelting, written in lead. [[c-lead-ice]] [[c-lead-iq]] And new texts are still appearing: scrolls burned by Vesuvius are being read by X-ray and machine learning. [[c-herculaneum]]",
  {'table': {'head': ["Witness", "Wrote", "About", "Caution"], 'rows': [
    ["Herodotus", "c. 430s-420s BCE", "the Persian Wars", "numbers inflated; speeches invented"],
    ["Thucydides", "from 431 BCE", "the Peloponnesian War", "speeches give 'the general sense'"],
    ["Polybius", "2nd century BCE", "Rome's rise, 220-146 BCE", "admirer of Rome and of his patrons"],
    ["Livy", "late 1st century BCE", "Rome from its founding", "early books mostly legend; 35 of 142 books survive"],
    ["Josephus", "70s-90s CE", "Judea and the Jewish War", "a participant, writing under Roman patrons"],
    ["Greenland ice", "1100 BCE-800 CE, year by year", "lead from mining and smelting", "a proxy, not a measure of the whole economy"]], 'note': "[[c-herodotus]] [[c-thuc-speeches]] [[c-polybius]] [[c-livy]] [[c-josephus]] [[c-lead-ice]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "Who tells us, and when they wrote", 'title': "The main ancient historians, with five turning points",
  'max': 500, 'min': -130, 'unit': 'ka', 'ticks': [500, 400, 300, 200, 100, 0, -100], 'tickLabels': ['500 BCE', '400', '300', '200', '100 BCE', '1 CE', '100 CE'],
  'axis': "years BCE and CE; lifetimes approximate", 'hint': "Hover or click a row",
  'marks': [{'ya': 480, 't': 'Salamis, 480'}, {'ya': 323, 't': 'Alexander dies, 323'}, {'ya': 146, 't': 'Carthage destroyed, 146'}, {'ya': 31, 't': 'Actium, 31 BCE'}, {'ya': -70, 't': 'Temple destroyed, 70 CE', 'anchor': 'end'}],
  'rows': [
   {'t': 'Herodotus', 'sub': 'of Halicarnassus', 'from': 484, 'to': 425, 'lab': 'c. 484-425', 'acc': True, 'plate': {'kicker': '8.0 · how we know', 'title': 'Herodotus', 'sub': 'the Persian Wars', 'text': "[[c-herodotus]] [[c-xerxes-army]]", 'sources': ['brit-herodotus', 'tarn1908']}},
   {'t': 'Thucydides', 'sub': 'of Athens', 'from': 431, 'to': 400, 'lab': 'wrote from 431', 'acc': True, 'plate': {'kicker': '8.0 · how we know', 'title': 'Thucydides', 'sub': 'the Peloponnesian War', 'text': "[[c-thuc-speeches]] [[c-thuc-exile]]", 'sources': ['thuc1', 'thuc5']}},
   {'t': 'Polybius', 'sub': 'of Megalopolis', 'from': 200, 'to': 118, 'lab': 'c. 200-118', 'acc': True, 'plate': {'kicker': '8.0 · how we know', 'title': 'Polybius', 'sub': "Rome's rise", 'text': "[[c-polybius]] [[c-polybius-mixed]]", 'sources': ['brit-polybius', 'polyb1', 'polyb6']}},
   {'t': 'Livy', 'sub': 'of Patavium', 'from': 59, 'to': -17, 'lab': 'c. 59 BCE-17 CE', 'acc': True, 'plate': {'kicker': '8.0 · how we know', 'title': 'Livy', 'sub': 'History of Rome', 'text': "[[c-livy]] [[c-lapis]]", 'sources': ['brit-livy', 'jobin-lapis']}},
   {'t': 'Josephus', 'sub': 'of Jerusalem', 'from': -37, 'to': -100, 'lab': '37-c. 100 CE', 'acc': True, 'plate': {'kicker': '8.0 · how we know', 'title': 'Josephus', 'sub': 'the Jewish War and Antiquities', 'text': "[[c-josephus]] [[c-testimonium]]", 'sources': ['brit-josephus', 'goldberg-tf']}},
   {'t': 'Greenland lead record', 'sub': 'NGRIP ice core: 1100 BCE-800 CE', 'from': 500, 'to': -130, 'open': True, 'plate': {'kicker': '8.0 · how we know', 'title': 'Lead in the ice', 'sub': '1100 BCE to 800 CE', 'text': "[[c-lead-ice]] [[c-lead-iq]] [[c-iberian-lead]]", 'sources': ['mcconnell2018', 'mcconnell2025', 'nbc-lead2025']}}]},
 'practice': [
  q("Why do historians value the Greenland lead record alongside writers like Livy and Polybius?",
    ["It records the names of Roman mine owners year by year", "It is a yearly physical record no author could slant", "It proves that lead poisoning brought about the fall of Rome", "It confirms the battle figures given by Herodotus and Livy"], 1,
    "Greenland ice records European mining and smelting year by year from 1100 BCE to 800 CE, so it can be checked against the texts.",
    {0: "The ice holds traces of lead, not names.", 2: "The 2025 IQ estimate is new and model-based, and Lanphear notes 'it's never just one thing'.", 3: "The ice records mining and smelting, not battles; matching its dips to particular wars is interpretation."}),
  q("Shipwreck counts peak in the 1st century CE. What is the most important caution in reading that peak?",
    ["Barrels are easier to find than amphorae, inflating some counts", "Wilson, who compiled the counts, treats them as a direct measure", "Amphora cargoes are easy to find; barrels and perishables are not", "Greenland lead shows trade in fact fell during the 1st century CE"], 2,
    "Andrew Wilson, who compiled the figures, warns that wrecks are not a direct measure of trade: the counts partly reflect what survives and which coasts have been surveyed.",
    {0: "It is the other way round: amphora cargoes are easy to find, and barrels are not.", 1: "Wilson warns that wrecks are not a direct measure of trade.", 3: "Lead in the Greenland ice peaks under the Roman empire."})]}

# ---------------------------------------------------------------- 8.1
P1 = {
 'title': "The Persian Wars", 'sub': "499 to 479 BCE",
 'lede': "Twice in ten years the largest empire on earth sent forces against a scatter of small Greek cities, and twice it went home. The Greeks made the story into the founding legend of the West; the Persian records show how small a frontier war it was from the other side.",
 'body': [
  "The Greek cities of the Anatolian coast had lived under Persia since Cyrus (see 7.8). Around 499 BCE they rose in revolt, and Athens and Eretria sent ships to help. [[c-ionian]] The revolt was crushed by 494, and Darius sent a punitive force across the Aegean. At Marathon in 490 the Athenians and their Plataean allies beat it on the beach. [[c-marathon]] A Persian administrative tablet places a man named Datiya, probably the Persian commander Datis, carrying royal documents in the west four years earlier. [[c-datis]]",
  "Ten years later Xerxes came himself, with an army that crossed the Hellespont on a bridge of boats and a fleet that was spared the storms off Mount Athos by a canal cut across the peninsula. [[c-athos]] Leonidas held Thermopylae for two days in August 480, [[c-thermopylae]] the Persians burned an empty Athens, [[c-athens-burned]] and in September the Greek fleet trapped the Persian ships in the strait of Salamis. [[c-salamis]] In 479 the Greeks won on land at Plataea and destroyed the remaining Persian fleet at Mycale. [[c-plataea]]",
  "Almost all we know comes from Herodotus, writing a generation later. [[c-herodotus]] His numbers cannot be right: an army of millions could not have been fed. [[c-xerxes-army]] His speeches and his scenes at the Persian court are reconstructions. [[c-herodotus-court]] Yet the Athos canal is real, and so are the burned layers of Athens. The Persian side survives only in administrative tablets from Persepolis, [[c-pfa]] [[c-pfa-return]] and in royal inscriptions that call the Greeks Yaunā, the Ionians. [[c-yauna]]",
  {'table': {'head': ["Battle", "Date", "Result", "Numbers, and where they come from"], 'rows': [
    ["Marathon", "490 BCE", "Athenian victory", "Herodotus: 192 Greek and 6,400 Persian dead"],
    ["Thermopylae", "August 480", "Persians force the pass", "300 Spartans among several thousand Greeks"],
    ["Salamis", "September 480", "Greek naval victory", "about 370 Greek ships against perhaps 800"],
    ["Plataea", "479", "Greek victory on land", "one modern estimate: 200,000 men in all"],
    ["Mycale", "479", "Persian fleet destroyed", "-"]], 'note': "[[c-marathon]] [[c-thermopylae]] [[c-salamis]] [[c-plataea]] [[c-xerxes-army]]"}},
  {'compare': "The Book of Esther is set in Susa at the court of King Ahasuerus (Esther 1:1-2), the Hebrew form of the name the Greeks wrote as Xerxes. Most scholars read it as a story rather than a chronicle. No Persian record mentions Esther; Persepolis tablets name officials called Marduka, but whether one of them is Mordecai is disputed."}],
 'figure': {'kind': 'map', 'view': {'lon': 25.6, 'lat': 38.6, 'zoom': 36}, 'caption': "The Persian Wars, 490 and 480-479 BCE", 'hint': "Click a place",
  'legend': [['acc dash', "Xerxes' march, 480 (simplified)"], ['acc', 'Persian fleet, 490'], ['dot', 'battle or key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'route', 'items': [{'path': [[28.04, 38.49], [27.4, 39.3], [26.4, 40.15], [26.1, 40.6], [25.3, 40.9], [24.4, 40.95], [23.4, 40.75], [22.9, 40.6], [22.5, 40.0], [22.4, 39.3], [22.54, 38.8], [23.2, 38.35], [23.72, 37.97]], 'label': 'Xerxes, 480', 'lab': [24.4, 40.95], 'ldy': -10, 'acc': True, 'head': True}]},
   {'type': 'arrow', 'items': [{'path': [[26.9, 37.7], [25.4, 37.1], [25.27, 37.4], [24.3, 38.2], [23.79, 38.39], [23.97, 38.15]], 'label': 'Datis, 490', 'lab': [25.4, 37.1], 'ldy': 16}]},
   {'type': 'region', 'items': [{'ll': [28.6, 39.4], 'label': 'LYDIA', 'size': 10}, {'ll': [28.5, 37.95], 'label': 'IONIA', 'size': 10}, {'ll': [22.1, 37.3], 'label': 'PELOPONNESE', 'size': 9}, {'ll': [22.2, 39.6], 'label': 'THESSALY', 'size': 9}, {'ll': [25.0, 41.3], 'label': 'THRACE', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [28.0403, 38.4883], 'label': 'Sardis', 'date': 'Persian capital of the west', 'acc': True, 'big': True, 'dy': 14, 'plate': {'kicker': '8.1 · Persia', 'title': 'Sardis', 'sub': "the satrap's seat", 'text': "[[c-ionian]] [[c-datis]] [[c-pfa]]", 'sources': ['brit-grecopersian', 'livius-datis', 'isac-pfa']}},
    {'ll': [27.2775, 37.5292], 'label': 'Miletus', 'date': 'revolt crushed 494', 'dy': 16},
    {'ll': [27.42, 37.04], 'label': 'Halicarnassus', 'date': 'home of Herodotus', 'dy': 14, 'plate': {'kicker': '8.1 · the historian', 'title': 'Herodotus', 'sub': 'of Halicarnassus', 'text': "[[c-herodotus]] [[c-herodotus-court]] [[c-xerxes-army]]", 'sources': ['brit-herodotus', 'bmcr-2021-09-04', 'tarn1908']}},
    {'ll': [27.15, 37.66], 'label': 'Mycale', 'date': '479', 'acc': True, 'anchor': 'end', 'dy': -10},
    {'ll': [23.92, 40.38], 'label': 'Athos canal', 'date': 'dug c. 483-480', 'dy': 16, 'plate': {'kicker': '8.1 · evidence', 'title': "Xerxes' canal", 'sub': 'Athos peninsula', 'text': "[[c-athos]]", 'sources': ['isserlin2003']}},
    {'ll': [22.5436, 38.7960], 'label': 'Thermopylae', 'date': 'August 480', 'acc': True, 'big': True, 'anchor': 'end', 'plate': {'kicker': '8.1 · battle', 'title': 'Thermopylae', 'sub': 'August 480 BCE', 'text': "[[c-thermopylae]]", 'sources': ['brit-grecopersian']}},
    {'ll': [23.9701, 38.1466], 'label': 'Marathon', 'date': '490', 'acc': True, 'big': True, 'plate': {'kicker': '8.1 · battle', 'title': 'Marathon', 'sub': '490 BCE', 'text': "[[c-marathon]] [[c-datis]]", 'sources': ['brit-grecopersian', 'livius-datis']}},
    {'ll': [23.2735, 38.2211], 'label': 'Plataea', 'date': '479', 'acc': True, 'anchor': 'end', 'dy': -6},
    {'ll': [23.72, 37.97], 'label': 'Athens', 'date': 'burned 480', 'acc': True, 'big': True, 'dy': 22, 'plate': {'kicker': '8.1 · Athens', 'title': 'Athens burned', 'sub': '480 BCE', 'text': "[[c-athens-burned]]", 'sources': ['gr-2500']}},
    {'ll': [23.5303, 37.9488], 'label': 'Salamis', 'date': 'September 480', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 18, 'plate': {'kicker': '8.1 · battle', 'title': 'Salamis', 'sub': 'September 480 BCE', 'text': "[[c-salamis]]", 'sources': ['brit-salamis', 'livius-salamis']}},
    {'ll': [22.4247, 37.0818], 'label': 'Sparta', 'acc': True, 'dy': 14}]}]},
 'practice': [
  q("What does the Persepolis tablet naming 'Datiya' add that Herodotus cannot?",
    ["The likely number of Persians killed in the battle at Marathon", "A Persian record probably placing Datis in the west in 494", "Darius's own words ordering Datis to invade Greece by sea", "Proof that, for Persia, Marathon was the decisive defeat"], 1,
    "It is a ration record of 494 BCE, written for bookkeeping rather than for glory. Identifying Datiya with Datis is widely accepted but not proven.",
    {0: "The 6,400 figure comes from Herodotus; the tablet issues wine to a traveller.", 2: "The archive records food stores and rations, not royal speeches.", 3: "Jona Lendering argues that, for Persia, Marathon was a minor setback."}),
  q("Why do historians reject Herodotus' army figures yet still rely on him?",
    ["He was born after the wars had ended and met no witnesses", "An army of millions is impossible, but finds confirm key details", "Persian tablets give exact army totals that replace his", "He wrote in Persian, so his numbers suffered badly in translation"], 1,
    "Historians test each kind of statement separately: an army of millions could not have been fed, but the Athos canal and the burned layers of Athens are real.",
    {0: "He was born about 484 BCE and wrote a generation after the wars.", 2: "The Persepolis archive records food stores and rations, not army totals.", 3: "He came from a Greek city, Halicarnassus, and wrote his Histories in Greek."})]}

# ---------------------------------------------------------------- 8.2
P2 = {
 'title': "Athenian democracy", 'sub': "how it worked, and who it left out",
 'lede': "For almost two centuries the citizens of one Greek city governed themselves directly: they voted on war and peace in person, filled most offices by lottery and sat by the hundred on juries. It was the most radical democracy in history, and most of the people who lived under it had no vote.",
 'body': [
  "The system began with Cleisthenes, who in 508/7 BCE broke the power of the old aristocratic clans by mixing the population into ten new tribes. [[c-cleisthenes]] Each tribe sent 50 men, chosen by lot, to a Council of 500, which prepared business for the Assembly of all citizens on the Pnyx hill. [[c-council]] [[c-quorum]] The lottery was the point: it gave every citizen an equal chance at office. The great exception was the generals, who were elected, because a city at war could not leave command to luck. [[c-generals]]",
  "The Athenians invented ostracism to guard against tyranny. Each year they could vote to send one leading man into exile for ten years, without a trial; he kept his property and came back afterwards. [[c-ostracism]] Thousands of the potsherd ballots survive, many of them with the names of famous politicians scratched on them. [[c-ostraka]] Under Pericles, from the 450s, Athens began to pay citizens for jury service, so that poor men could afford to take part; [[c-pay]] juries of hundreds of citizens, 201 for small private suits and 501 or more for public cases, decided them with no professional judges. [[c-juries]]",
  "The same Pericles narrowed who counted as a citizen: from about 451 BCE, both parents had to be Athenian. [[c-citizen-law]] Women, slaves and resident foreigners could not vote at all. [[c-excluded]] A rough reconstruction makes the voters about a quarter of the population. [[c-athens-pop]] The number of slaves is one of the most disputed figures in ancient history. [[c-slaves]]",
  "Democracy at home went with empire abroad. The Delian League, formed in 478 to keep fighting Persia, turned into an Athenian empire; in 454/3 its treasury moved to Athens, and the allies' contributions became tribute recorded on stone. [[c-delian]] [[c-first-stele]] [[c-inscriptions]] Some of that money paid for the Parthenon and for the jurors' wages. Historians still argue over which Athenians gained most. [[c-empire-gain]]",
  {'table': {'head': ["Body", "How chosen", "Size", "Pay"], 'rows': [
    ["Assembly", "every adult male citizen who came", "6,000 needed for some votes", "1 obol, then 2, then 3, in the 390s"],
    ["Council", "lot, 50 per tribe, aged 30 or more", "500", "paid"],
    ["Law courts", "lot", "juries of 201 to 1,500", "3 obols a day"],
    ["Generals", "election", "10", "-"],
    ["Ostracism", "Assembly vote with potsherds", "one man exiled for 10 years", "-"]], 'note': "[[c-council]] [[c-quorum]] [[c-pay]] [[c-juries]] [[c-generals]] [[c-ostracism]]"}}],
 'figure': {'kind': 'chart', 'chart': 'split', 'caption': "Who could vote in Athens?", 'title': "People of Attica: adult male citizens and everyone else (one reconstruction)",
  'hint': "Hover a bar",
  'rows': [
   {'t': 'About 470 BCE', 'parts': [{'v': 30000, 'lab': 'citizens: c. 30,000', 'name': 'adult male citizens', 'acc': True, 'tip': 'could speak and vote in the Assembly'}, {'v': 110000, 'lab': 'everyone else: c. 110,000', 'name': 'women, children, metics, slaves', 'tip': 'no political rights'}]},
   {'t': '431 BCE', 'parts': [{'v': 60000, 'lab': 'citizens: c. 60,000', 'name': 'adult male citizens', 'acc': True, 'tip': 'could speak and vote in the Assembly'}, {'v': 190000, 'lab': 'everyone else: c. 190,000', 'name': 'women, children, metics, slaves', 'tip': 'no political rights'}]}],
  'notes': ["After Ben Akrigg (2019). Other reconstructions differ widely."]},
 'practice': [
  q("Which Athenian office was filled by election rather than by lot?",
    ["Member of the Council", "General (strategos)", "Juror in the law courts", "Member of the Assembly"], 1,
    "Athenians trusted the lottery for most jobs, but not for command in war, where skill mattered more than equal chances.",
    {0: "Councillors were chosen by lot, 50 from each tribe.", 2: "Juries were chosen by lot.", 3: "Every adult male citizen who came could take part; there was no selection."}),
  q("Why do estimates of the number of slaves in Athens range from about 20,000 to about 100,000?",
    ["The tribute lists record slaves, but the stones are damaged", "No reliable count survives, and estimates rest on assumptions", "Slaves hid from census takers, so the counts run low", "Hansen trusts the ancient census, while Jones and Hanson do not"], 1,
    "Low estimates (Jones, Hanson) and high ones (Hansen, Rhodes) rest on different assumptions, not different counts.",
    {0: "The tribute lists record the allies' payments, not slaves.", 2: "The one ancient 'census', of 400,000 slaves, is generally rejected as too high, not too low.", 3: "The ancient 'census' of 400,000 is generally rejected; Hansen's own estimate is 66,000-93,000."})]}

# ---------------------------------------------------------------- 8.3
P3 = {
 'title': "The Peloponnesian War", 'sub': "431 to 404 BCE, and Thucydides",
 'lede': "For twenty-seven years the two greatest Greek powers, Athens at sea and Sparta on land, fought a war that neither could win quickly. Its historian, an Athenian general exiled for failing to save a city, wrote the first analysis of power politics, and students of international relations still read him.",
 'body': [
  "Thucydides looked past the quarrels that started the war to a deeper cause: Athens was growing, and Sparta was afraid. [[c-truest-cause]] Athens had money, a navy and walls that ran down to its harbour; [[c-resources431]] Pericles' plan was to abandon the countryside to Spartan raids, shelter the people inside the walls and fight at sea.",
  "The plan collided with disease. In 430 BCE a plague broke out in the crowded city. Thucydides caught it and survived, and his description of the symptoms is the earliest of its kind; [[c-plague]] perhaps up to a third of the people died, Pericles among them. [[c-plague-toll]] DNA from a mass grave of the plague years pointed to typhoid fever, but the result was challenged at once and the disease is still unidentified. [[c-typhoid]]",
  "The war went on through a peace in 421, a catastrophic invasion of Sicily that destroyed an Athenian army and fleet in 413, and Sparta's final naval victory in 405, won with Persian gold. [[c-war-course]] Its most famous passage concerns the small island of Melos, which wanted to stay neutral. Thucydides gives the Athenian envoys the bluntest statement of power politics in ancient literature, and then records what Athens did to Melos. [[c-melos]] He wrote as an exile, having lost Amphipolis as a general in 424. [[c-thuc-exile]]",
  "Defeat brought a pro-Spartan oligarchy, the Thirty, and a year of terror before the democracy was restored in 403. [[c-socrates-politics]] Four years later a jury of citizens condemned the philosopher Socrates to death for impiety and for corrupting the young. [[c-socrates-trial]] His pupil Plato drew the lesson that the crowd should not rule, and the case against democracy has been argued from his books ever since.",
  {'table': {'head': ["Years (BCE)", "Phase", "What happened"], 'rows': [
    ["431-421", "Archidamian War", "Spartan raids on Attica; plague in Athens (430-426); Pericles dies"],
    ["421", "Peace of Nicias", "a truce that lasted six years"],
    ["416", "Melos", "the island is conquered; its men killed, women and children enslaved"],
    ["415-413", "Sicilian expedition", "an Athenian army and fleet destroyed at Syracuse"],
    ["411", "Oligarchic coup", "democracy suspended for a few months"],
    ["405-404", "Aegospotami; surrender", "Sparta, with Persian money, wins at sea; the Thirty take power"]], 'note': "[[c-war-course]] [[c-plague]] [[c-melos]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 20.6, 'lat': 38.6, 'zoom': 20}, 'caption': "The Peloponnesian War, 431-404 BCE", 'hint': "Click a place",
  'legend': [['acc dash', 'Sicilian expedition, 415 (simplified)'], ['dot', 'battle, siege or key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'route', 'items': [{'path': [[23.63, 37.94], [23.3, 37.4], [23.2, 36.35], [22.3, 36.3], [21.5, 36.8], [20.9, 37.9], [20.3, 39.1], [19.5, 39.8], [18.6, 40.0], [17.3, 39.5], [16.8, 38.6], [15.75, 38.0], [15.4, 37.3], [15.28, 37.07]], 'label': 'to Sicily, 415', 'lab': [18.6, 40.0], 'ldy': -10, 'acc': True, 'head': True}]},
   {'type': 'region', 'items': [{'ll': [22.0, 37.5], 'label': 'PELOPONNESE', 'size': 10}, {'ll': [14.2, 37.6], 'label': 'SICILY', 'size': 10}, {'ll': [25.2, 38.4], 'label': 'AEGEAN SEA', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [23.72, 37.97], 'label': 'Athens', 'date': 'plague 430; surrender 404', 'acc': True, 'big': True, 'dy': -10, 'plate': {'kicker': '8.3 · Athens', 'title': 'The plague of Athens', 'sub': 'from 430 BCE', 'text': "[[c-plague]] [[c-plague-toll]] [[c-typhoid]]", 'sources': ['thuc2', 'sd-typhoid2006', 'ijid-noproof']}},
    {'ll': [22.4247, 37.0818], 'label': 'Sparta', 'acc': True, 'big': True, 'anchor': 'end', 'plate': {'kicker': '8.3 · Sparta', 'title': 'Why the war came', 'sub': '431 BCE', 'text': "[[c-truest-cause]] [[c-resources431]]", 'sources': ['thuc1', 'thuc2']}},
    {'ll': [23.8416, 40.8258], 'label': 'Amphipolis', 'date': '424: Thucydides exiled', 'acc': True, 'anchor': 'end', 'plate': {'kicker': '8.3 · the historian', 'title': 'Thucydides', 'sub': 'general and exile', 'text': "[[c-thuc-exile]] [[c-thuc-speeches]]", 'sources': ['thuc5', 'thuc1']}},
    {'ll': [24.4233, 36.7439], 'label': 'Melos', 'date': '416', 'acc': True, 'big': True, 'dy': 14, 'plate': {'kicker': '8.3 · power', 'title': 'Melos', 'sub': '416 BCE', 'text': "[[c-melos]]", 'sources': ['thuc5']}},
    {'ll': [15.2833, 37.0701], 'label': 'Syracuse', 'date': 'Athenian defeat, 413', 'acc': True, 'big': True, 'dy': 14},
    {'ll': [26.5994, 40.3315], 'label': 'Aegospotami', 'date': '405', 'acc': True, 'dy': -8},
    {'ll': [26.555, 39.105], 'label': 'Mytilene', 'date': 'revolt 428-427', 'dy': 14}]}]},
 'practice': [
  q("What is the safest way to use the Melian Dialogue as evidence?",
    ["As a word-for-word record of what the envoys said", "As Thucydides' reconstruction, tied to a real outcome", "As a story whose outcome is as invented as its speeches", "As proof that Melos joined the Athenian empire willingly"], 1,
    "Thucydides says he wrote speeches to fit 'the general sense' of what was said, while he narrates the fate of Melos as fact.",
    {0: "The dialogue is Thucydides' own composition.", 2: "The killing and enslavement of the Melians is narrated as fact.", 3: "Melos wanted to stay neutral, and when it fell Athens killed its men."}),
  q("What is the status of the 2006 claim that typhoid caused the plague of Athens?",
    ["Settled, and now the standard view among specialists", "A DNA result challenged at once; the cause is still open", "Disproved, because Thucydides names the disease as smallpox", "Based on DNA taken from the tomb of Pericles himself"], 1,
    "A single result, quickly disputed, does not close a long debate; no newer study has settled it.",
    {0: "A reply titled 'No proof that typhoid caused the Plague of Athens' challenged it at once.", 2: "Thucydides describes the symptoms; smallpox is one of several earlier candidates, and none is settled.", 3: "The teeth came from a mass grave in the Kerameikos cemetery."})]}

PAGES = [P0, P1, P2, P3]
