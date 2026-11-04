# Chapter 10, pages 10.0 to 10.3. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 10.0
 'princeton-brown': ("Princeton University, Department of History, \"Peter Brown\"", "https://history.princeton.edu/people/peter-brown"),
 'bmcr-kulikowski2024': ("Michael Kulikowski, review in Bryn Mawr Classical Review 2024.08.43", "https://bmcr.brynmawr.edu/?p=86771"),
 'balzan-brown': ("Peter Brown, lecture at the Balzan Forum (2011)", "https://www.balzan.org/wp-content/uploads/2022/05/Forum2011_BROWN.pdf"),
 'brit-gibbon': ("Encyclopaedia Britannica, \"Edward Gibbon: The Decline and Fall\"", "https://www.britannica.com/biography/Edward-Gibbon/The-Decline-and-Fall"),
 'ox-oxyrhynchus': ("University of Oxford, Faculty of Classics, \"The Oxyrhynchus papyri\"", "https://www.sds.ox.ac.uk/oxyrhynchus-papyri"),
 'pnas-mcconnell2018': ("McConnell et al., \"Lead pollution recorded in Greenland ice...\", PNAS 115 (2018)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5984482"),
 'sd-buntgen2016': ("ScienceDaily, on Büntgen et al., the Late Antique Little Ice Age (2016)", "https://sciencedaily.com/releases/2016/02/160208112918.htm"),
 'arch-taranto2024': ("Archaeology, on Zonneveld, Harper et al., plagues and climate in a Gulf of Taranto core, Science Advances (2024)", "https://archaeology.org/news/2024/01/30/240131-disease-climate-model/"),
 'riken-speidel': ("RIKEN iTHEMS, on Speidel et al., ancient DNA and first-millennium migrations, Nature (2025)", "https://ithems.riken.jp/en/news/ancient-dna-unlocks-new-understanding-of-migrations-in-the-first-millennium-ad"),
 # 10.1
 'brit-sasanian': ("Encyclopaedia Britannica, \"Ancient Iran: the Sasanian period\"", "https://www.britannica.com/place/ancient-Iran/The-Sasanian-period"),
 'unesco-sasanian': ("UNESCO World Heritage Centre, \"Sassanid Archaeological Landscape of Fars Region\"", "https://whc.unesco.org/en/list/1568/"),
 'brit-shapur1': ("Encyclopaedia Britannica, \"Shapur I\"", "https://www.britannica.com/biography/Shapur-I"),
 'lactantius-mp': ("Lactantius, On the Deaths of the Persecutors (New Advent)", "https://www.newadvent.org/fathers/0705.htm"),
 'caley1956': ("Earle R. Caley and Harold D. McBride, \"Chemical composition of antoniniani of Trajan Decius, Trebonianus Gallus, and Valerian\", Ohio Journal of Science 56 (1956)", "https://core.ac.uk/download/76293692.pdf"),
 'livius-tetrarchy': ("Livius, \"Tetrarchy\"", "https://www.livius.org/articles/concept/tetrarchy/"),
 'brit-diocletian': ("Encyclopaedia Britannica, \"Diocletian: domestic reforms\"", "https://www.britannica.com/biography/Diocletian/Domestic-reforms"),
 # 10.2
 'brit-constantine': ("Encyclopaedia Britannica, \"Constantine I\" summary", "https://www.britannica.com/summary/Constantine-I-Roman-emperor"),
 'ect-lactantius-vision': ("Lactantius, On the Deaths of the Persecutors 44 (Early Church Texts)", "https://www.earlychurchtexts.com/public/lactantius_constantine_heavenly_vision.htm"),
 'eusebius-vc1': ("Eusebius, Life of Constantine 1.28-31 (New Advent)", "https://www.newadvent.org/fathers/25021.htm"),
 'girardet2023': ("Klaus Martin Girardet, on Constantine's sign in the sky, Römische Quartalschrift 118 (2023)", "https://herder.de/rq/hefte/archiv/118-2023/3-4-2023/der-kaiser-und-ein-gottzeichen-am-himmel-konstantin-dgr-in-den-ersten-jahren-als-christ"),
 'unifr-milan': ("Lactantius, On the Deaths of the Persecutors 48 (Bibliothek der Kirchenväter, Fribourg)", "https://bkv.unifr.ch/fr/works/cpl-91/versions/of-the-manner-in-which-the-persecutors-died/divisions/49"),
 'ft-wilken': ("First Things, quoting Robert Louis Wilken on the 'Edict of Milan'", "https://firstthings.com/?p=24594"),
 'brit-nicaea': ("Encyclopaedia Britannica, \"First Council of Nicaea\"", "https://www.britannica.com/event/First-Council-of-Nicaea-325"),
 'ebsco-theodosius': ("EBSCO Research Starters, \"Theodosius's edicts promote Christian orthodoxy\"", "https://www.ebsco.com/research-starters/religion-and-philosophy/theodosiuss-edicts-promote-christian-orthodoxy"),
 'brit-constantinople': ("Encyclopaedia Britannica, \"Istanbul: Constantinople\"", "https://www.britannica.com/place/Istanbul/Constantinople"),
 'brit-julian': ("Encyclopaedia Britannica, \"Julian\" summary", "https://www.britannica.com/summary/Julian-Roman-emperor"),
 'ehrman-growth': ("Bart Ehrman, \"The rate of Christian growth\" (Ehrman Blog)", "https://ehrmanblog.org/the-rate-of-christian-growth/"),
 'ehrman-significant': ("Bart Ehrman, \"How significant was early Christianity?\" (Ehrman Blog)", "https://ehrmanblog.org/how-significant-was-early-christianity/"),
 'lucero2021': ("Lucero, a model of early Christian growth (arXiv preprint, 2021)", "https://arxiv.org/pdf/2111.08833"),
 'npr-nicaea2025': ("NPR, \"Pope Leo prays at Nicaea with the Ecumenical Patriarch\" (28 November 2025)", "https://www.npr.org/2025/11/28/nx-s1-5621985/pope-leo-prays-nicaea-turkey-patriarch"),
 'archmag-frankfurt': ("Archaeology Magazine (Greece), on the 'Frankfurt silver inscription' (December 2024)", "https://archaeologymag.com/2024/12/oldest-evidence-of-christianity-north-of-the-alps"),
 # 10.3
 'ucp-payne': ("University of California Press, Richard Payne, A State of Mixture (2015)", "https://www.ucpress.edu/books/a-state-of-mixture/epub-pdf"),
 'brit-mani': ("Encyclopaedia Britannica, \"Mani\"", "https://www.britannica.com/biography/Mani-Iranian-religious-leader"),
 'uw-manichaeism': ("Lance Jenott, \"Manichaeism\", University of Washington Silk Road Seattle", "https://depts.washington.edu/silkroad/exhibit/religion/manichaeism/essay.html"),
 'iranica-jews': ("Jacob Neusner, on the Jews in Sasanian Babylonia, Encyclopaedia Iranica", "https://www.iranicaonline.org/?p=2146"),
 'brit-talmud': ("Encyclopaedia Britannica, \"Talmud and Midrash: early compilations\"", "https://www.britannica.com/topic/Talmud/Early-compilations"),
 'cojs-talmud': ("Lawrence Schiffman, \"The Babylonian Talmud\", Center for Online Judaic Studies", "https://cojs.org/the_babylonian_talmud/"),
 'iranica-christianity': ("James Russell, \"Christianity i: in pre-Islamic Persia\", Encyclopaedia Iranica", "https://iranicaonline.org/articles/christianity-i"),
 'bm-drachm': ("British Museum, silver drachm of Khusrau II (C.MAR.535)", "https://www.britishmuseum.org/collection/object/C_MAR-535"),
 'seshat-sasanian': ("Seshat Global History Databank, \"Sasanid Empire II\"", "https://seshat-db.com/core/polity/130"),
 'unesco-takht': ("UNESCO World Heritage Centre, \"Takht-e Soleyman\"", "https://whc.unesco.org/en/list/1077/"),
}

C = {
 # 10.0
 'c-brown': c("Peter Brown's The World of Late Antiquity (1971) is credited with creating the field; he has argued that the period was not simply one of decline, and in 2011 said that historians 'have grown tired of melodramatic ruminations on decline and fall'.", 'debated', ['princeton-brown', 'bmcr-kulikowski2024', 'balzan-brown'], "Brown's view; critics such as Bryan Ward-Perkins argue that in the West it was a real fall (see 10.4)."),
 'c-gibbon': c("Edward Gibbon's Decline and Fall of the Roman Empire (1776-88) summed up the story as 'the triumph of barbarism and religion'.", 'consensus', ['brit-gibbon'], show=False),
 'c-oxyrhynchus': c("Rubbish dumps at Oxyrhynchus in Egypt, dug in 1896-1907, yielded thousands of texts on papyrus from the 2nd century BCE to the 7th century CE: tax records, census returns, petitions, letters, and early copies of the Bible.", 'consensus', ['ox-oxyrhynchus'], show=False),
 'c-ice10': c("Lead in Greenland ice records European mining and smelting year by year; it shows the Roman economy's long growth ending with the Antonine plague of the 160s.", 'debated', ['pnas-mcconnell2018'], "The record is secure; reading it as a measure of the whole economy is debated."),
 'c-taranto': c("A 2024 study of a sediment core from the Gulf of Taranto found that three great epidemics, in the 160s, the 250s and the 540s, each came during a cooler, drier phase in Italy.", 'debated', ['arch-taranto2024'], "New. A correlation in time; the mechanism is unknown, and so are the pathogens of the first two."),
 # 10.1
 'c-ardashir': c("In about 224 Ardashir, a prince of Fars, defeated the last Parthian king and founded the Sasanian dynasty, which ruled Iran and Iraq until 651.", 'approx', ['brit-sasanian', 'unesco-sasanian'], "Britannica's own article gives both 224 and 226 for the decisive battle."),
 'c-shapur-claims': c("Shapur I (reigned 241-272) recorded his victories over Rome in Persian, Parthian and Greek on a monument at Naqsh-e Rostam, claiming the death of one emperor, a ransom of 500,000 gold pieces from another, and 60,000 Romans destroyed in one battle.", 'tradition', ['brit-sasanian'], "These are the king's own claims."),
 'c-valerian': c("In 260 Shapur captured the Roman emperor Valerian near Edessa and held him for the rest of his life; rock reliefs show the scene.", 'consensus', ['brit-shapur1'], show=False),
 'c-valerian-legend': c("The Christian writer Lactantius says Shapur used Valerian as a footstool and later had his skin dyed red and hung in a temple.", 'tradition', ['lactantius-mp'], "Lactantius tells it as God's punishment of a persecutor of Christians; it is polemic, not reporting."),
 'c-deportees': c("Roman prisoners from Antioch were settled in Iran, where they built the city of Gundeshapur and a great dam at Shushtar.", 'consensus', ['brit-shapur1'], show=False),
 'c-debasement3': c("Chemical analysis shows the main silver coin, the antoninianus, fell from about 35 percent silver under Decius (249-251) to about 18 percent under Valerian and about 5 percent under Gallienus in the 260s.", 'approx', ['caley1956'], "Averages from analysed coins; individual coins vary."),
 'c-tetrarchy': c("Diocletian (284-305) shared power: from 286 two senior emperors (Augusti) and from 293 two junior ones (Caesars), the 'tetrarchy'; in 305 he and his colleague abdicated.", 'consensus', ['livius-tetrarchy', 'brit-diocletian'], show=False),
 'c-diocletian-reforms': c("Diocletian reorganised taxation around new assessments of land and people, made at first every five years and later on a fifteen-year cycle, enlarged the army by about a quarter, restored good gold and silver coins and nearly doubled the number of mints (from 8 to 15).", 'consensus', ['brit-diocletian'], show=False),
 'c-price-edict': c("His Edict on Maximum Prices (301) fixed maximum prices and wages for about 1,000 goods and services on pain of death; it proved unenforceable and was abandoned.", 'consensus', ['brit-diocletian'], show=False),
 'c-persecution': c("On 23 February 303 soldiers razed the church at Nicomedia, the start of the 'Great Persecution'; four edicts followed, until Galerius issued an edict of toleration in April 311.", 'consensus', ['lactantius-mp', 'brit-diocletian'], show=False),
 # 10.2
 'c-milvian': c("Constantine defeated his rival Maxentius at the Milvian Bridge outside Rome in 312 and became master of the West.", 'consensus', ['brit-constantine'], show=False),
 'c-sign': c("Two Christian writers describe a sign before the battle: Lactantius says Constantine was told in a dream to put a heavenly sign on his soldiers' shields; Eusebius, who says Constantine told him under oath, describes a cross of light in the sky with the words 'Conquer by this'.", 'tradition', ['ect-lactantius-vision', 'eusebius-vc1'], "The two accounts differ, and what Constantine saw, if anything, is unknowable."),
 'c-girardet': c("A 2023 study argues that the detailed description of the sign in Lactantius is a later addition, and that he meant a simple cross.", 'debated', ['girardet2023'], "New; Klaus Girardet's argument is not yet widely tested."),
 'c-milan': c("In 313 Constantine and his co-emperor Licinius agreed to grant 'the Christians and all others' freedom of religion; the text that survives is a letter Licinius posted in the East, so the famous 'Edict of Milan' was neither an edict nor issued at Milan.", 'consensus', ['unifr-milan', 'ft-wilken'], show=False),
 'c-nicaea': c("The Council of Nicaea (325), called by Constantine, condemned Arius, who taught that the Son was a created being, and declared the Son 'of one substance' (homoousios) with the Father, a word not found in Scripture.", 'consensus', ['brit-nicaea'], show=False),
 'c-constantinople': c("Constantine refounded Byzantium as 'New Rome', inaugurated on 11 May 330; it became Constantinople.", 'consensus', ['brit-constantinople'], show=False),
 'c-julian': c("Julian (361-363), the last pagan emperor, proclaimed freedom of worship while favouring the old gods; he was killed on campaign in Persia.", 'consensus', ['brit-julian'], show=False),
 'c-theodosius': c("Theodosius I made Nicene Christianity the empire's official faith by an edict of 380, and in 391-392 banned pagan sacrifice; in about 391 the great temple of Serapis in Alexandria was destroyed.", 'debated', ['ebsco-theodosius'], "The 380 edict defined which Christians were orthodox; the laws of 391-392 struck at public pagan cult. Which counts as making Christianity the 'state religion' is a matter of definition."),
 'c-stark': c("Sociologist Rodney Stark calculated that steady growth of about 40 percent a decade would take Christians from about 1,000 in 40 CE to about 6 million, a tenth of the empire, by 300, with no mass conversions needed.", 'debated', ['ehrman-growth', 'ehrman-significant'], "A model, not a count; Bart Ehrman calls these figures 'guestimates and round numbers' for illustration."),
 'c-stark-critics': c("Critics note that the same steady rate would give some 170 million Christians by 400, more than the empire's whole population, so growth must have slowed.", 'debated', ['ehrman-growth', 'lucero2021'], "Bart Ehrman and others; one 2021 model has growth slowing to about 21 percent a decade by 400."),
 'c-nicaea2025': c("On 28 November 2025 Pope Leo XIV and the Ecumenical Patriarch Bartholomew prayed together at the ruins of a basilica on the lake at Iznik, ancient Nicaea, for the council's 1,700th anniversary.", 'consensus', ['npr-nicaea2025'], show=False),
 'c-frankfurt': c("In 2024 a silver amulet from a Frankfurt grave of about 230-270, inscribed 'In the name of Jesus Christ, Son of God', was announced as the oldest evidence of Christianity north of the Alps.", 'approx', ['archmag-frankfurt'], "New. The grave's date is approximate."),
 # 10.3
 'c-kartir': c("The Zoroastrian high priest Kartir, powerful from the 270s to the 290s, boasted in inscriptions of suppressing Jews, Buddhists, Brahmins, Christians and others.", 'debated', ['brit-sasanian'], "These are his own claims; how much persecution actually happened is uncertain."),
 'c-payne': c("Richard Payne (2015) argues that Christians in Sasanian Iran were less a marginal, persecuted minority than participants integrated into elite networks and imperial institutions, within a hierarchy headed by Zoroastrianism.", 'debated', ['ucp-payne'], "This revises the older picture of a Zoroastrian 'state church' persecuting other faiths."),
 'c-mani': c("Mani, born in Babylonia in 216, preached a religion of light and darkness under Shapur I; under Bahram I he was imprisoned and died in about 274-277.", 'approx', ['brit-mani'], "Sources differ on the year of his death."),
 'c-manichaeism': c("Manichaeism spread west to Roman North Africa, where the young Augustine followed it, and east along the Silk Road, where the Uighurs made it their state religion from about 762 to 840.", 'consensus', ['uw-manichaeism'], show=False),
 'c-exilarch': c("Under the Sasanians the Jews of Babylonia governed their own affairs under a recognised leader, the exilarch, while accepting the rabbi Samuel's rule that 'the law of the government is law' in matters of land and tax.", 'consensus', ['iranica-jews'], show=False),
 'c-bavli': c("The Babylonian Talmud, compiled by the rabbis of Mesopotamia, became the central text of Jewish law; tradition ends its compilation with Rav Ashi (died 427) and Rabina (died 499).", 'debated', ['brit-talmud', 'cojs-talmud'], "Modern scholars see editing continuing well into the 6th century, in informal study circles rather than formal academies."),
 'c-persian-christians': c("Christians, many descended from Roman deportees, had bishops in Persia from early in the Sasanian period, and a Persian bishop attended the Council of Nicaea.", 'approx', ['iranica-christianity'], "Early numbers are uncertain."),
 'c-shapur2-persecution': c("Shapur II began a persecution of Christians in 339 that lasted some forty years, perhaps killing 35,000.", 'debated', ['iranica-christianity'], "The figure comes from later Christian martyr literature; Payne's revision applies here too."),
 'c-church-east': c("In 410 a synod at Ctesiphon adopted the Nicene creed, and in 424 the church of Persia declared its head, the catholicos, independent of western bishops: the 'Church of the East', using Syriac.", 'consensus', ['iranica-christianity'], show=False),
 'c-drachm': c("Sasanian silver drachms, with the crowned king on one side and a fire altar on the other, were struck in huge numbers and weighed about 4 grams.", 'consensus', ['bm-drachm', 'brit-sasanian'], show=False),
 'c-khosrow-tax': c("Khosrow I (531-579) replaced land taxes paid in kind with fixed cash assessments, a system the Arab conquerors kept.", 'consensus', ['brit-sasanian'], show=False),
 'c-sasanian-pop': c("Rough estimates put the Sasanian empire's population at about 9 million around 500 and about 13 million later in the 6th century; a figure of over 20 million for 620-642 counts Roman provinces occupied during the war of 602-628.", 'approx', ['seshat-sasanian'], "Figures from Colin McEvedy and Richard Jones (1978), compiled by the Seshat databank, which flags gaps in them; treat them as rough."),
 'c-takht': c("Takht-e Soleyman in north-west Iran was the Sasanian kings' great fire sanctuary.", 'consensus', ['unesco-takht'], show=False),
}

# ---------------------------------------------------------------- 10.0
P0 = {
 'title': "Late antiquity", 'sub': "c. 250 to 750",
 'lede': "Between the crises of the 3rd century and the Abbasid revolution of 750, the Roman empire became Christian and split in two, its western half broke into kingdoms, Persia had its last great dynasty, and a new faith from Arabia created an empire larger than Rome's. Historians call these centuries 'late antiquity', and they argue about whether to tell them as a fall or a new beginning.",
 'body': [
  "Five acts. In the 3rd century Rome nearly broke apart and Persia gained a new, aggressive dynasty. [[c-ardashir]] Diocletian and Constantine rebuilt the empire, and Constantine made it Christian. [[c-milvian]] The West fragmented in the 5th century, [[c-476]] while the East, under Justinian, codified Roman law and fought off plague. [[c-justinian]] Then, from the 630s, Arab armies inspired by a new prophet [[c-muhammad-life]] took half the Roman empire and, by 651, all of Persia, and by 750 their caliphs ruled from Spain to Central Asia. [[c-umayyads]]",
  "For two centuries the period was told as Gibbon told it, as decline. [[c-gibbon]] Peter Brown taught historians to see a world of new religions, new art and new communities instead. [[c-brown]] The argument is still alive (see 10.4).",
  "New kinds of evidence are reshaping it. Papyri from Egyptian rubbish dumps show ordinary people's lives. [[c-oxyrhynchus]] Greenland ice and Alpine tree rings measure mining and climate year by year, [[c-ice10]] [[c-536]] and sediment cores tie epidemics to cold spells. [[c-taranto]] Ancient DNA shows who moved where. [[c-speidel2025]]",
  {'table': {'head': ["Evidence", "Example", "What it measures"], 'rows': [
    ["Papyri", "Oxyrhynchus, Egypt", "taxes, prices, letters, early Bible copies"],
    ["Coins", "Roman antoniniani; Umayyad dinars", "state finances; public identity"],
    ["Ice cores", "Greenland lead record", "mining and smelting, year by year"],
    ["Tree rings", "Alps and Altai", "summer temperatures; the cold of the 530s-540s"],
    ["Sediment cores", "Gulf of Taranto", "regional climate"],
    ["Ancient DNA", "1,500 genomes (2025); plague victims", "migration; the pathogens of epidemics"]], 'note': "[[c-oxyrhynchus]] [[c-ice10]] [[c-536]] [[c-taranto]] [[c-speidel2025]] [[c-ypestis]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 22.0, 'lat': 50.0, 'zoom': 3.0}, 'caption': "Where the new evidence comes from", 'hint': "Click a place",
  'legend': [['dot', 'source of evidence'], ['pt', 'capital']], 'seas': False,
  'layers': [
   {'type': 'points', 'items': [
    {'ll': [-42.32, 75.1], 'label': 'NGRIP ice core', 'date': 'lead, 1100 BCE-800 CE', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '10.0 · ice', 'title': 'The Greenland lead record', 'sub': 'NGRIP core', 'text': "[[c-ice10]]", 'sources': ['pnas-mcconnell2018']}},
    {'ll': [30.6519, 28.5426], 'label': 'Oxyrhynchus', 'date': 'papyri', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '10.0 · papyri', 'title': 'Oxyrhynchus', 'sub': 'dug 1896-1907', 'text': "[[c-oxyrhynchus]]", 'sources': ['ox-oxyrhynchus']}},
    {'ll': [87.02, 50.73], 'label': 'Altai', 'date': 'tree rings', 'acc': True, 'big': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '10.0 · tree rings', 'title': 'The coldest decade', 'sub': '536-660', 'text': "[[c-536]] [[c-lalia]]", 'sources': ['sd-buntgen2016', 'buntgen2016']}},
    {'ll': [17.33, 40.13], 'label': 'Gulf of Taranto', 'date': 'sediment core', 'acc': True, 'dy': 16, 'plate': {'kicker': '10.0 · sediments', 'title': 'Plague and climate', 'sub': '2024 study', 'text': "[[c-taranto]]", 'sources': ['arch-taranto2024']}},
    {'ll': [-1.083, 53.958], 'label': 'York', 'date': 'ancient DNA', 'acc': True, 'anchor': 'end', 'plate': {'kicker': '10.0 · DNA', 'title': 'Ancient DNA', 'sub': '2025 study', 'text': "[[c-speidel2025]]", 'sources': ['riken-speidel', 'eurekalert-speidel']}},
    {'ll': [11.717, 48.171], 'label': 'Aschheim', 'date': 'plague DNA', 'acc': True, 'dy': -8},
    {'ll': [12.511, 41.892], 'label': 'Rome', 'anchor': 'end', 'dy': 14},
    {'ll': [28.95, 41.014], 'label': 'Constantinople', 'dy': -8},
    {'ll': [44.583, 33.083], 'label': 'Ctesiphon', 'dy': 16}]}]},
 'practice': [
  q("How does Peter Brown's 'late antiquity' differ from Gibbon's 'decline and fall'?",
    ["Brown saw new growth; Gibbon saw barbarism and religion triumph", "Gibbon saw new growth; Brown saw barbarism and religion triumph", "Brown accepts Gibbon's decline but dates it two centuries later", "Gibbon was replying to Brown and his critics, such as Ward-Perkins"], 0,
    "Gibbon summed up the story as 'the triumph of barbarism and religion'; Brown argued the period was not simply one of decline, but a world of new religions, new art and new communities.",
    {1: "Reversed: the phrase 'the triumph of barbarism and religion' is Gibbon's, and Brown rejected the story of decline.", 2: "Brown argued the period was not simply one of decline.", 3: "Gibbon published in 1776-88, two centuries before Brown's book of 1971."}),
  q("Why is the Greenland lead record useful to historians?",
    ["It measures European mining and smelting year by year", "It records the tax Rome raised from its silver mines", "It shows steady economic growth through the 3rd century", "It identifies the germ behind the Antonine plague"], 0,
    "Lead from mining and smelting settled in ice that can be dated year by year: a physical trace that no ancient writer could slant.",
    {1: "It records lead from mining and smelting, not taxes; tax records survive in papyri such as those from Oxyrhynchus.", 2: "It shows the Roman economy's long growth ending with the Antonine plague of the 160s.", 3: "The pathogens of the epidemics of the 160s and 250s are still unknown."})]}

# ---------------------------------------------------------------- 10.1
P1 = {
 'title': "Crisis and repair", 'sub': "the 3rd century and Diocletian, 224-311",
 'lede': "In the middle of the 3rd century the Roman empire nearly fell apart. Emperors came and went in quick succession, a new Persian dynasty captured one of them, and the silver coinage collapsed. Diocletian rebuilt the state by making it bigger, more bureaucratic and more expensive.",
 'body': [
  "In Iran, a new dynasty replaced the Parthians: the Sasanians, who claimed the heritage of the ancient Persian kings. [[c-ardashir]] Its second king, Shapur I, defeated three Roman emperors, by his own account, [[c-shapur-claims]] and in 260 took one of them, Valerian, prisoner. [[c-valerian]] Christian writers turned Valerian's fate into a morality tale. [[c-valerian-legend]] Shapur settled Roman captives in Iran as builders and engineers. [[c-deportees]]",
  "Rome's emperors paid their armies by putting less silver in each coin. By the 260s the main silver coin was mostly copper. [[c-debasement3]] Prices rose, the state took more of its taxes in kind, and plague returned in the 250s. [[c-taranto]]",
  "Diocletian, a soldier from the Balkans, ended the crisis. He divided the empire among four rulers, [[c-tetrarchy]] rebuilt taxation on regular assessments of land and people, enlarged the army and reformed the coinage. [[c-diocletian-reforms]] He also tried to fix prices by law, and failed. [[c-price-edict]] In 303 he turned on the Christians in the last and fiercest persecution, which ended only in 311. [[c-persecution]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["c. 224", "Ardashir founds the Sasanian dynasty"],
    ["249-268", "the silver coinage collapses"],
    ["260", "Shapur I captures the emperor Valerian"],
    ["286-293", "Diocletian's tetrarchy: four emperors"],
    ["301", "Edict on Maximum Prices"],
    ["303-311", "the Great Persecution"]], 'note': "[[c-ardashir]] [[c-debasement3]] [[c-valerian]] [[c-tetrarchy]] [[c-price-edict]] [[c-persecution]]"}},
  {'compare': "Diocletian's Price Edict is the most famous price control of the ancient world: maximum prices and wages for about 1,000 items, enforced by the death penalty, issued after decades in which debased coinage had driven prices up. Britannica calls it unenforceable; it was later revoked. Our only account of its effects is by the hostile Christian writer Lactantius, who says that 'men were afraid to expose anything to sale' until the law was abandoned. Economists often cite it as a textbook case of price caps causing shortages, but the evidence for that is thin."}],
 'figure': {'kind': 'chart', 'chart': 'bars', 'caption': "How the silver disappeared", 'title': "Silver content of the antoninianus, by emperor (percent)",
  'max': 40, 'ticks': [0, 10, 20, 30, 40], 'axis': "percent silver", 'hint': "Hover a bar",
  'rows': [
   {'t': 'Decius', 'sub': '249-251', 'v': 35.4, 'lab': '35.4%'},
   {'t': 'Trebonianus Gallus', 'sub': '251-253', 'v': 31.5, 'lab': '31.5%'},
   {'t': 'Valerian', 'sub': '253-260', 'v': 17.9, 'lab': '17.9%', 'acc': True, 'tip': 'captured by Shapur in 260'},
   {'t': 'Gallienus', 'sub': '260-268', 'v': 5.5, 'lab': 'c. 5-6%', 'acc': True, 'tip': 'older analyses; 4.9-6.0%'},
   {'t': 'Claudius II', 'sub': '268-270', 'v': 4.2, 'lab': '4.2%', 'acc': True, 'plate': {'kicker': '10.1 · money', 'title': 'The debasement', 'sub': '249-270', 'text': "[[c-debasement3]] [[c-diocletian-reforms]] [[c-price-edict]]", 'sources': ['caley1956', 'brit-diocletian']}}],
  'notes': ["Source: Caley and McBride (1956): averages of their analyses for Decius, Gallus and Valerian; for Gallienus (three coins) and Claudius II (one coin), older analyses by von Bibra that they reprint."]},
 'practice': [
  q("Which evidence best shows that the 3rd-century crisis was not purely political?",
    ["A main silver coin that was mostly copper by the 260s", "The rock reliefs of Valerian's capture by Shapur in 260", "Diocletian's division of power among four rulers", "Lactantius' account of Valerian's skin hung in a temple"], 0,
    "The antoninianus fell from about 35 percent silver under Decius to about 5 percent under Gallienus: a fiscal and monetary crisis, not only a political one.",
    {1: "The reliefs record a military event.", 2: "The tetrarchy was a political answer to the crisis, not evidence of its economic side.", 3: "It is hostile Christian polemic, not reporting, let alone economic data."}),
  q("What was Diocletian's Edict on Maximum Prices of 301?",
    ["A failed cap on prices and wages, on pain of death", "A reform restoring good gold and silver coins", "A new tax based on assessments of land and people", "The first edict of the Great Persecution of Christians"], 0,
    "It fixed maximum prices and wages for about 1,000 goods and services on pain of death, proved unenforceable and was abandoned.",
    {1: "Restoring good coins was a separate measure.", 2: "The new assessments of land and people were a separate tax reform.", 3: "The persecution began two years later, in 303."})]}

# ---------------------------------------------------------------- 10.2
P2 = {
 'title': "Constantine and the Christian empire", 'sub': "312 to 392",
 'lede': "In 312 a Roman emperor fought under a Christian sign. Within eighty years Christianity had gone from persecuted sect to the empire's official religion, with its creed defined by imperial councils. How fast it grew, and why, are still argued about.",
 'body': [
  "Constantine won control of the West at the Milvian Bridge in 312. [[c-milvian]] Christian writers tell of a sign from heaven before the battle, though their accounts differ, [[c-sign]] and a recent study questions one of them. [[c-girardet]] In 313 he and his eastern colleague granted freedom of worship to all. [[c-milan]]",
  "Constantine poured money into churches and summoned the bishops to Nicaea in 325, where they defined Christ as 'of one substance' with the Father against the priest Arius. [[c-nicaea]] The creed they began is still recited, and in 2025 a pope and a patriarch prayed together at the site. [[c-nicaea2025]] He also founded a new capital, Constantinople. [[c-constantinople]] One later emperor, Julian, tried to revive the old gods and died after two years. [[c-julian]] Under Theodosius, Nicene Christianity became the official faith and pagan sacrifice was banned. [[c-theodosius]]",
  "How did a small sect become the majority? Rodney Stark argued that steady growth of about 40 percent a decade, through families and networks rather than mass conversions, would be enough. [[c-stark]] Critics point out that the same rate soon becomes impossible, so growth must have slowed, and they debate why. [[c-stark-critics]] Archaeology occasionally adds a datapoint: in 2024 a tiny inscribed silver amulet showed a Christian buried in Germany before 270. [[c-frankfurt]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["311", "Galerius' edict of toleration"],
    ["312", "Milvian Bridge"],
    ["313", "freedom of religion ('Edict of Milan')"],
    ["325", "Council of Nicaea"],
    ["330", "Constantinople inaugurated"],
    ["361-363", "Julian tries to restore paganism"],
    ["380", "Nicene Christianity made the official faith"],
    ["391-392", "pagan sacrifice banned"]], 'note': "[[c-persecution]] [[c-milvian]] [[c-milan]] [[c-nicaea]] [[c-constantinople]] [[c-julian]] [[c-theodosius]]"}}],
 'figure': {'kind': 'chart', 'chart': 'bars', 'caption': "How fast did Christianity grow?", 'title': "Christians in the Roman empire on Stark's model of 40% growth per decade (log scale)",
  'scale': 'log', 'min': 100, 'max': 1000000000, 'ticks': [1000, 1000000, 1000000000], 'tickLabels': ['1,000', '1 million', '1 billion'], 'axis': "number of Christians, log scale", 'hint': "Hover a bar",
  'rows': [
   {'t': '40 CE', 'v': 1000, 'lab': 'c. 1,000', 'tip': "Stark's starting assumption"},
   {'t': '100 CE', 'v': 7400, 'lab': 'c. 7,400'},
   {'t': '200 CE', 'v': 210000, 'lab': 'c. 210,000'},
   {'t': '300 CE', 'v': 6000000, 'lab': 'c. 6 million', 'acc': True, 'tip': 'about a tenth of the empire', 'plate': {'kicker': '10.2 · growth', 'title': "Stark's model", 'sub': 'and its critics', 'text': "[[c-stark]] [[c-stark-critics]]", 'sources': ['ehrman-growth', 'lucero2021']}},
   {'t': '400 CE, same rate', 'sub': 'impossible', 'v': 170000000, 'lab': 'c. 170 million', 'tip': 'more than the whole empire (about 60 million)'}],
  'notes': ["Projections, not counts (Ehrman's figures for Stark's model)."]},
 'practice': [
  q("Why do historians say the 'Edict of Milan' is misnamed?",
    ["It survives as a letter Licinius posted in the East", "It is really Theodosius' law of 380, not Constantine's", "Constantine issued it alone, without his co-emperor", "It protected Christians but left pagans unprotected"], 0,
    "In 313 Constantine and Licinius agreed on religious freedom, but the text that survives is a letter Licinius posted in the East: neither an edict nor issued at Milan.",
    {1: "It was agreed by Constantine and Licinius in 313; Theodosius' edict of 380 is a different text.", 2: "It was agreed by Constantine and his co-emperor Licinius.", 3: "It granted freedom to 'the Christians and all others'."}),
  q("Start with 6 million Christians in 300 and keep growth at 40 percent a decade. What problem appears by 400?",
    ["It gives some 170 million, more than the whole empire", "It gives about 24 million, too few for a Christian empire", "It leaves Christians a tenth of the empire, as in 300", "It needs mass conversions, which no source records"], 0,
    "Critics note that the same steady rate would give some 170 million Christians by 400, more than the empire's whole population, so growth must have slowed.",
    {1: "Ten decades at 40 percent multiply 6 million by about 29, giving some 170 million.", 2: "At 40 percent a decade the number keeps rising; a tenth was the estimate for 300.", 3: "Stark's point is that steady compounding needs no mass conversions."})]}

# ---------------------------------------------------------------- 10.3
P3 = {
 'title': "The Sasanian empire", 'sub': "Persia, 224-651",
 'lede': "Rome's great rival for four centuries was a sophisticated empire of many faiths: Zoroastrian kings, Christian bishops, Jewish rabbis who wrote the Babylonian Talmud, and a prophet, Mani, whose religion spread from North Africa to China.",
 'body': [
  "The Sasanian kings presented themselves as champions of the old Iranian religion of Zoroaster (see 7.8), and their great fire temples were royal shrines. [[c-takht]] One high priest boasted of persecuting other faiths, [[c-kartir]] but Richard Payne argues that the empire mostly included religious minorities in a hierarchy rather than persecuting them. [[c-payne]] The prophet Mani preached a new universal religion at Shapur I's court before dying in prison under Bahram I; [[c-mani]] his faith spread across Eurasia. [[c-manichaeism]]",
  "Mesopotamia was home to one of the largest and most important Jewish communities of the age. Under its own leader, the exilarch, it governed its own affairs, [[c-exilarch]] and its rabbis produced the Babylonian Talmud, still the central text of Jewish law. [[c-bavli]] Christians, many descended from Roman prisoners, built a church across the empire, [[c-persian-christians]] suffered a long persecution under Shapur II, [[c-shapur2-persecution]] and in 410-424 organised themselves as the independent Church of the East. [[c-church-east]]",
  "The state rested on farming the rich lands of Iraq and on silver. Its drachms circulated from Arabia to Central Asia, [[c-drachm]] and Khosrow I's cash land tax outlived the dynasty. [[c-khosrow-tax]] The empire may have held some 13 million people in its last century, [[c-sasanian-pop]] before war with Rome and then the Arab conquests destroyed it (10.8).",
  {'table': {'head': ["Faith", "Key figure", "Under the Sasanians"], 'rows': [
    ["Zoroastrian", "Kartir, high priest", "religion of the kings"],
    ["Manichaean", "Mani (216-c. 274/277)", "patronised, then its founder imprisoned; he died in prison"],
    ["Jewish", "the exilarch; rabbis of Sura and Pumbedita", "self-government; the Babylonian Talmud"],
    ["Christian", "the catholicos of the Church of the East", "persecuted from 339; organised as a recognised church from 410"]], 'note': "[[c-kartir]] [[c-mani]] [[c-exilarch]] [[c-bavli]] [[c-church-east]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 47.5, 'lat': 33.0, 'zoom': 15}, 'caption': "The Sasanian empire: places of power and faith", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [44.0, 31.0], 'label': 'MESOPOTAMIA', 'size': 9}, {'ll': [53.0, 31.5], 'label': 'FARS', 'size': 10}, {'ll': [38.0, 35.5], 'label': 'ROMAN SYRIA', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [44.5833, 33.0833], 'label': 'Ctesiphon', 'date': 'capital; synod of 410', 'acc': True, 'big': True, 'dy': -10, 'plate': {'kicker': '10.3 · Christians', 'title': 'The Church of the East', 'sub': '410-424', 'text': "[[c-persian-christians]] [[c-shapur2-persecution]] [[c-church-east]] [[c-payne]]", 'sources': ['iranica-christianity', 'ucp-payne']}},
    {'ll': [43.79, 33.35], 'label': 'Pumbedita', 'date': 'rabbinic centre', 'acc': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '10.3 · Jews', 'title': 'The Babylonian Talmud', 'sub': '3rd-6th centuries', 'text': "[[c-exilarch]] [[c-bavli]]", 'sources': ['iranica-jews', 'brit-talmud', 'cojs-talmud']}},
    {'ll': [44.45, 31.88], 'label': 'Sura', 'anchor': 'end', 'dy': 14},
    {'ll': [48.5167, 32.2833], 'label': 'Gundeshapur', 'date': 'built by Roman captives', 'acc': True, 'dy': 16, 'plate': {'kicker': '10.3 · Mani', 'title': 'Mani', 'sub': '216 to c. 274-277', 'text': "[[c-mani]] [[c-manichaeism]] [[c-deportees]]", 'sources': ['brit-mani', 'uw-manichaeism', 'brit-shapur1']}},
    {'ll': [52.8749, 29.9887], 'label': 'Naqsh-e Rostam', 'date': "Shapur's and Kartir's inscriptions", 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '10.3 · kings', 'title': 'Naqsh-e Rostam', 'sub': 'royal inscriptions', 'text': "[[c-shapur-claims]] [[c-valerian]] [[c-kartir]]", 'sources': ['brit-sasanian', 'brit-shapur1']}},
    {'ll': [52.572, 28.845], 'label': 'Firuzabad', 'date': "Ardashir's first capital", 'dy': 16},
    {'ll': [47.235, 36.6039], 'label': 'Takht-e Soleyman', 'date': 'royal fire sanctuary', 'acc': True, 'dy': -8, 'plate': {'kicker': '10.3 · Zoroastrians', 'title': 'Takht-e Soleyman', 'sub': 'fire sanctuary', 'text': "[[c-takht]] [[c-drachm]]", 'sources': ['unesco-takht', 'bm-drachm']}},
    {'ll': [41.215, 37.07], 'label': 'Nisibis', 'date': 'Christian school', 'dy': -8},
    {'ll': [38.794, 37.167], 'label': 'Edessa', 'date': 'Valerian captured, 260', 'acc': True, 'dy': 16}]}]},
 'practice': [
  q("Which best describes Jewish life in Sasanian Babylonia?",
    ["An exilarch led the Jews; state law ruled land and tax", "Kartir's campaign forced most Jews to become Zoroastrians", "Babylonia's Jews were expelled to Roman Palestine", "Rabbis ruled Jewish life and set the community's land taxes"], 0,
    "A recognised exilarch governed the community's affairs, while it accepted Samuel's rule that 'the law of the government is law' in matters of land and tax.",
    {1: "Kartir's boasts are his own claims, and the community went on governing itself and producing the Talmud.", 2: "Mesopotamia was home to one of the largest Jewish communities of the age, whose rabbis compiled the Babylonian Talmud.", 3: "The community had its own leader, the exilarch, and accepted that the government's law applied to land and tax."}),
  q("Which statement about the Church of the East is best supported?",
    ["It adopted Nicaea's creed in 410 and independence in 424", "It was organised after the Arab conquest of Persia", "It used Greek and took orders from western bishops", "Shapur I founded it for his Roman deportees"], 0,
    "A synod at Ctesiphon adopted the Nicene creed in 410, and in 424 the church declared its head, the catholicos, independent of western bishops.",
    {1: "Bishops are recorded early in the Sasanian period, and a Persian bishop attended Nicaea in 325.", 2: "It used Syriac, and in 424 declared its head independent of western bishops.", 3: "Many Persian Christians descended from Roman deportees, but the church organised itself through the synods of 410 and 424."})]}

PAGES = [P0, P1, P2, P3]
