# Chapter 10, pages 10.4 to 10.7. Coordinates are [longitude, latitude].
from common import c, q

QC = "https://quran.com/"
S = {
 # 10.4
 'brit-adrianople': ("Encyclopaedia Britannica, \"Battle of Adrianople\"", "https://www.britannica.com/event/Battle-of-Adrianople-378"),
 'brit-sack410': ("Encyclopaedia Britannica, \"Sack of Rome (410)\"", "https://www.britannica.com/event/Sack-of-Rome-410"),
 'brit-alaric': ("Encyclopaedia Britannica, \"Alaric\"", "https://www.britannica.com/biography/Alaric"),
 'aug-civ1': ("Augustine, City of God, Book I (Nicene and Post-Nicene Fathers translation, New Advent)", "https://www.newadvent.org/fathers/120101.htm"),
 'aug-civ14': ("Augustine, City of God, Book XIV (Nicene and Post-Nicene Fathers translation, New Advent)", "https://www.newadvent.org/fathers/120114.htm"),
 'brit-odoacer': ("Encyclopaedia Britannica, \"Odoacer\"", "https://www.britannica.com/biography/Odoacer"),
 'brit-romulus': ("Encyclopaedia Britannica, \"Romulus Augustulus\"", "https://www.britannica.com/biography/Romulus-Augustulus"),
 'tmr-cameron': ("Averil Cameron, review of Motions of Late Antiquity, The Medieval Review 17.01.17", "https://scholarworks.iu.edu/journals/index.php/tmr/article/view/23305"),
 'bham-trw': ("University of Birmingham, \"Transformation of the Roman World\" research project", "https://research.birmingham.ac.uk/en/projects/transformation-of-the-roman-world"),
 'ox-wardperkins': ("Oxford History Faculty, Bryan Ward-Perkins, The Fall of Rome and the End of Civilization (2005)", "https://www.history.ox.ac.uk/node/112181"),
 'cj-heather': ("Peter S. Wells, review of Peter Heather, The Fall of the Roman Empire, Classical Journal", "https://cj.camws.org/Wells%20on%20Heather.pdf"),
 'the-kingsley': ("Sean Kingsley, review of Ward-Perkins, Times Higher Education", "https://www.timeshighereducation.com/node/83996"),
 'eurekalert-speidel': ("Francis Crick Institute, on Speidel et al., ancient DNA and first-millennium migrations, Nature (2025)", "https://www.eurekalert.org/news-releases/1069205"),
 'unesco-toledo': ("UNESCO World Heritage Centre, \"Historic City of Toledo\"", "https://whc.unesco.org/en/list/379/"),
 'brit-recared': ("Encyclopaedia Britannica, \"Recared\"", "https://www.britannica.com/biography/Recared"),
 'brit-toledo-councils': ("Encyclopaedia Britannica, \"Councils of Toledo\"", "https://www.britannica.com/event/councils-of-Toledo"),
 'cohen-spain': ("Rodrigo Laham Cohen, \"Spain\", in The Jews in Late Antiquity (Arc Humanities, 2018)", "https://cambridge.org/core/books/jews-in-late-antiquity/spain/45E37A2BFF2B5C093D55F0616597FC49"),
 # 10.5
 'brit-justinian': ("Encyclopaedia Britannica, \"Justinian I\"", "https://www.britannica.com/biography/Justinian-I"),
 'brit-justinian-law': ("Encyclopaedia Britannica, \"Roman law: the law of Justinian\"", "https://www.britannica.com/topic/Roman-law/The-law-of-Justinian"),
 'brit-civil-law': ("Encyclopaedia Britannica, \"Civil law (Romano-Germanic)\"", "https://www.britannica.com/topic/civil-law-Romano-Germanic"),
 'brit-nika': ("Encyclopaedia Britannica, \"Nika riots\"", "https://www.britannica.com/topic/Nika-riots"),
 'unesco-istanbul': ("UNESCO World Heritage Centre, \"Historic Areas of Istanbul\"", "https://whc.unesco.org/en/list/356/"),
 'brit-gelimer': ("Encyclopaedia Britannica, \"Gelimer\"", "https://www.britannica.com/biography/Gelimer"),
 'brit-totila': ("Encyclopaedia Britannica, \"Totila\"", "https://www.britannica.com/biography/Totila"),
 'procopius-plague': ("Procopius, Wars II.22-23, tr. Dewing (1914), in Ancient Civilizations (Oregon State)", "https://open.oregonstate.education/ancientcivilizations/chapter/plague-of-justinian/"),
 'wagner2014': ("Northern Arizona University, on Wagner et al., Yersinia pestis and the Plague of Justinian, Lancet Infectious Diseases (2014)", "https://www.eurekalert.org/pub_releases/2014-01/nau-ruh012714.php"),
 'mainz-plague2013': ("Johannes Gutenberg University Mainz, 'Scientists confirm that the Justinianic plague was caused by the bacterium Yersinia pestis' (2013)", "https://press.uni-mainz.de/scientists-confirm-that-the-justinianic-plague-was-caused-by-the-bacterium-yersinia-pestis/"),
 'keller2019': ("Phys.org, on Keller et al., genomes of the Justinianic plague, PNAS (2019)", "https://phys.org/news/2019-06-bacterial-diversity-justinianic-plague.amp"),
 'fau-jerash2025': ("Florida Atlantic University, on Yersinia pestis from the Jerash mass grave (2025)", "https://www.fau.edu/newsdesk/articles/genomic-origins-first-pandemic"),
 'mordechai2019': ("McMaster Ancient DNA Centre, on Mordechai et al., \"The Justinianic Plague: an inconsequential pandemic?\", PNAS (2019)", "https://adna.mcmaster.ca/the-justinianic-plague-an-inconsequential-pandemic"),
 'sarris-sb': ("ScienceBlog, on Peter Sarris, Past & Present (2021)", "https://scienceblog.com/justinianic-plague-was-nothing-like-flu-and-may-have-hit-england-before-constantinople/"),
 'buntgen2016-pdf': ("Büntgen et al., \"Cooling and societal change during the Late Antique Little Ice Age\", Nature Geoscience 9 (2016)", "https://www.climatology.uni-mainz.de/files/2012/03/Buentgen_2016_NatureGeo.pdf"),
 'toohey2016': ("ScienceDaily, on Toohey et al., the eruptions of 536 and 540, Climatic Change (2016)", "https://sciencedaily.com/releases/2016/04/160419083247.htm"),
 # 10.6
 'robin-himyar': ("Christian Julien Robin, \"The Judaism of the ancient kingdom of Ḥimyar\", in Diversity and Rabbinization (Open Book, 2021)", "https://books.openbookpublishers.com/10.11647/obp.0219/ch7.xhtml"),
 'brit-lakhmid': ("Encyclopaedia Britannica, \"Lakhmid dynasty\"", "https://www.britannica.com/topic/Lakhmid-dynasty"),
 'brit-ghassanid': ("Encyclopaedia Britannica, \"Ghassanid dynasty\"", "https://www.Britannica.Com/place/Ghassanid-dynasty"),
 'crone2007': ("Patricia Crone, \"Quraysh and the Roman army: making sense of the Meccan leather trade\", BSOAS 70 (2007)", "https://www.ias.edu/sites/default/files/hs/Crone_Articles/Crone_Quraysh_Leather_Trade.pdf"),
 'brit-muhammad': ("Encyclopaedia Britannica, \"Muhammad\"", "https://www.britannica.com/biography/Muhammad"),
 'shaddel-dj': ("Mehdy Shaddel, \"Doctrina Iacobi and the rise of Islam\", forthcoming in Viermann and Wienand (eds.), Reading the Late Roman Monarchy (pre-publication copy)", "https://almuslih.org/wp-content/uploads/2024/11/Shaddel-M-Doctrina-Iacobi-.pdf"),
 'hagarism': ("Patricia Crone and Michael Cook, Hagarism (Cambridge, 1977), publisher's description", "https://blackwells.co.uk/bookshop/product/Hagarism-The-Making-of-the-Islamic-World-by-Patricia-Crone-Michael-Cook/9780521297547"),
 'shoemaker2012': ("Stephen Shoemaker, The Death of a Prophet (Pennsylvania, 2012), record", "https://oeaw.ac.at/resources/Record/9780812205138"),
 'neuenkirchen2016': ("Paul Neuenkirchen, review of Shoemaker, Studia Islamica 111 (2016)", "https://www.academia.edu/37046142"),
 'hup-donner': ("Harvard University Press, Fred Donner, Muhammad and the Believers (2010)", "https://www.hup.harvard.edu/books/9780674064140"),
 'hoyland2007': ("Robert Hoyland, \"Writing the biography of the Prophet Muhammad: problems and solutions\", History Compass (2007)", "https://www.academia.edu/3303289"),
 # 10.7
 'pup-scriptures': ("Princeton University Press, sample chapter 'The Scriptures: Bible, New Testament, and Quran'", "https://assets.press.princeton.edu/chapters/s7593.pdf"),
 'brit-quran': ("Encyclopaedia Britannica, \"Qur'an\"", "https://www.britannica.com/topic/Quran"),
 'quran-15-9': ("Quran 15:9, tr. Abdel Haleem (quran.com)", QC + "15/9?translations=85"),
 'bukhari-4987': ("Sahih al-Bukhari 4987 (sunnah.com)", "https://sunnah.com/bukhari/66/9"),
 'bham-quran': ("University of Birmingham, Cadbury Research Library, \"The Birmingham Qur'an manuscript: FAQs\"", "https://www.birmingham.ac.uk/facilities/cadbury/birmingham-quran-mingana-collection/birmingham-quran/faqs"),
 'marx-jocham2019': ("Michael Marx and Tobias Jocham, \"Radiocarbon (14C) dating of Qur'an manuscripts\" (Brill, 2019), Corpus Coranicum", "https://corpuscoranicum.de/pdf/Radiocarbon_Dating_of_Quran_Manuscripts.pdf"),
 'iis-sanaa': ("Institute of Ismaili Studies, Asma Hilali, The Sanaa Palimpsest (2017)", "https://iis.ac.uk/publications-listing/2017/the-sanaa-palimpsest"),
 'sinai2020': ("Nicolai Sinai, review of Hilali, Journal of the American Oriental Society 140 (2020)", "https://lockwoodonlinejournals.com/index.php/jaos/article/download/760/603/1620"),
 'sinai2014': ("Nicolai Sinai, \"When did the consonantal skeleton of the Quran reach closure?\", BSOAS 77 (2014)", "https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/when-did-the-consonantal-skeleton-of-the-quran-reach-closure-part-i1/D2C425AFB394D8979DE11DA4E0AAE086"),
 'ucp-shoemaker2022': ("University of California Press, Stephen Shoemaker, Creating the Qur'an (2022)", "https://www.ucpress.edu/books/creating-the-quran/paper"),
 'quran-2-127': ("Quran 2:127, tr. Abdel Haleem (quran.com)", QC + "2/127?translations=85"),
 'quran-2-136': ("Quran 2:136, tr. Abdel Haleem (quran.com)", QC + "2/136?translations=85"),
 'quran-3-42': ("Quran 3:42, tr. Abdel Haleem (quran.com)", QC + "3/42?translations=85"),
 'quran-4-157': ("Quran 4:157, tr. Abdel Haleem (quran.com)", QC + "4/157?translations=85"),
 'reynolds2009': ("Gabriel Said Reynolds, \"The Muslim Jesus: dead or alive?\", BSOAS 72 (2009)", "https://core-prod.cambridgecore.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/muslim-jesus-dead-or-alive/527849E7101E74FC672FB8B4F8AC5B07"),
 'nd-reynolds2018': ("University of Notre Dame, on Gabriel Said Reynolds, The Qur'an and the Bible: Text and Commentary (Yale, 2018)", "https://theology.nd.edu/news/new-faculty-book-i-the-quran-and-the-bible-text-and-commentary-i-by-gabriel-said-reynolds/"),
}

C = {
 # 10.4
 'c-adrianople': c("On 9 August 378, near Adrianople (Edirne), Goths who had been admitted into the empire and then rebelled destroyed a Roman army and killed the emperor Valens.", 'consensus', ['brit-adrianople'], show=False),
 'c-adrianople-toll': c("Some ancient accounts put the Roman dead at over 40,000, and the historian Ammianus called it the worst slaughter since Cannae.", 'approx', ['brit-adrianople'], "Ancient casualty figures are unreliable."),
 'c-sack410': c("On 24 August 410 Alaric's Visigoths entered Rome and plundered it for three days; the city had not been captured by a foreign enemy for nearly 800 years. Most citizens were spared.", 'consensus', ['brit-sack410', 'brit-alaric'], show=False),
 'c-augustine': c("Augustine began the City of God in 413 to answer pagans who blamed Christianity for the disaster; he contrasted two cities, one built by love of self and one by love of God.", 'consensus', ['brit-sack410', 'aug-civ1', 'aug-civ14'], show=False),
 'c-476': c("In 476 the general Odoacer deposed the boy emperor Romulus Augustulus and ruled Italy as king; the date is traditionally taken as the end of the western Roman empire.", 'tradition', ['brit-odoacer', 'brit-romulus'], "It is a convention: the eastern court never recognised Romulus, and little changed in Italy that year."),
 'c-fall-debate': c("Whether the western empire 'fell' or was 'transformed' is one of the great debates of history.", 'debated', ['tmr-cameron', 'bham-trw', 'ox-wardperkins', 'cj-heather'], "Peter Brown and the European 'Transformation of the Roman World' project (1993-98) stressed continuity; Bryan Ward-Perkins (2005) calls that view 'badly in error' and describes 'a time of horror and dislocation'; Peter Heather argues the main cause was the military power of Rome's enemies."),
 'c-material': c("Ward-Perkins points to material evidence: in much of the West, roof tiles and coins disappeared from daily life, and cattle shrank from about 120 cm to about 112 cm at the shoulder.", 'approx', ['the-kingsley'], "These are his figures as reported by a reviewer; critics accept the decline but argue about how much it mattered."),
 'c-speidel2025': c("A 2025 study of more than 1,500 ancient genomes found ancestry from Iron Age Scandinavia spreading into southern Germany, Italy, Poland and Britain during the first millennium CE.", 'debated', ['eurekalert-speidel'], "New. It shows that people really moved; the authors say the 'nature, scale and even the trajectories' of the movements are still disputed."),
 'c-toledo': c("Toledo became the capital of the Visigothic kingdom of Spain.", 'consensus', ['unesco-toledo'], show=False),
 'c-recared': c("King Reccared (586-601) converted from Arian to Catholic Christianity, and at the Third Council of Toledo in 589 Catholicism became the religion of the kingdom; eighteen councils met at Toledo between about 400 and 702 and shaped its law and politics.", 'consensus', ['brit-recared', 'brit-toledo-councils'], show=False),
 'c-visigoth-jews': c("Visigothic kings turned on the kingdom's Jews: Sisebut ordered them to convert between 612 and 616, and a council in 694 decreed their enslavement.", 'debated', ['cohen-spain'], "The laws are certain; how far they were enforced, and whether they targeted converts, is unclear."),
 # 10.5
 'c-justinian': c("Justinian, born about 483 in the Balkans and a native Latin speaker, ruled the eastern empire from 527 to 565.", 'consensus', ['brit-justinian'], show=False),
 'c-corpus': c("His lawyers compiled the Corpus Juris Civilis: the Code of imperial laws (529, revised 534), the Digest of the jurists in 50 books (533), the Institutes, a textbook, and the Novels, his own new laws.", 'consensus', ['brit-justinian-law'], show=False),
 'c-civil-law': c("Rediscovered in the Middle Ages, Justinian's Corpus became the basis of legal study across Europe and a main root of the civil-law tradition of continental Europe, later adopted in much of Latin America.", 'consensus', ['brit-civil-law', 'brit-justinian-law'], show=False),
 'c-nika': c("In January 532 the rival Blue and Green circus factions united in the Nika riot, burned much of Constantinople and proclaimed a rival emperor; Justinian stayed, on the advice of the empress Theodora, and his general Belisarius crushed the revolt in a massacre.", 'consensus', ['brit-nika'], show=False),
 'c-hagia': c("The Hagia Sophia, designed by Anthemius of Tralles and Isidore of Miletus to replace a church burned in the riot, was built in just five years, 532-537.", 'consensus', ['unesco-istanbul', 'brit-nika'], show=False),
 'c-africa': c("Belisarius destroyed the Vandal kingdom in North Africa in 533-534, restoring Roman rule there.", 'consensus', ['brit-gelimer'], show=False),
 'c-italy': c("Italy was harder: the Goths were beaten by 540, but under Totila they won most of it back, and only in 552 did Narses defeat Totila at Taginae.", 'consensus', ['brit-totila'], show=False),
 'c-procopius-plague': c("The historian Procopius says the plague began at Pelusium in Egypt and reached Constantinople in 542, where at its height it killed 5,000 and then 10,000 people a day, with 'a bubonic swelling'.", 'tradition', ['procopius-plague'], "An eyewitness account; his numbers cannot be checked."),
 'c-ypestis': c("DNA from victims' teeth at Aschheim in Bavaria confirmed in 2013 that the pandemic was caused by Yersinia pestis, the bacterium of the later Black Death; the first genome followed in 2014, showing a different lineage that died out, and a 2019 study of 21 sites across western Europe added eight more genomes.", 'consensus', ['mainz-plague2013', 'wagner2014', 'keller2019'], show=False),
 'c-jerash': c("In 2025 researchers reported plague genomes from a mass grave under the hippodrome at Jerash in Jordan, the first direct genetic proof of the pandemic inside the eastern empire.", 'approx', ['fau-jerash2025'], "New. The burials are dated to about 550-660."),
 'c-plague-toll': c("How many died is fiercely debated.", 'debated', ['mordechai2019', 'sarris-sb'], "Older estimates ran to tens of millions. Lee Mordechai, Merle Eisenberg and colleagues (2019) found that papyri, laws, coins and pollen do not support such figures; Peter Sarris (2021) answers that laws, coin weights and new DNA show a catastrophe."),
 'c-536': c("Volcanic eruptions in 536 and 540 brought what was probably the coldest decade of the last 2,000 years in the northern hemisphere, the start of a 'Late Antique Little Ice Age' that lasted to about 660.", 'approx', ['buntgen2016-pdf', 'toohey2016'], "The cooling is measured in tree rings and ice cores; the volcanoes themselves have not been securely identified."),
 # 10.6
 'c-himyar': c("In Himyar, the kingdom of Yemen, royal inscriptions abandoned the old gods for a single 'Lord of the Sky' around 380-384, and a community calling itself 'Israel' appears; the kingdom's rulers leaned towards Judaism.", 'debated', ['robin-himyar'], "Christian Julien Robin calls it a 'discreet conversion', because royal inscriptions never name Judaism outright; how close it was to rabbinic Judaism is disputed."),
 'c-najran': c("The Jewish king Joseph (Yusuf) rebelled against Aksumite overlordship in 522-523; Christian and Muslim accounts say he massacred the Christians of Najran, and Aksum invaded in 525 and killed him.", 'tradition', ['robin-himyar'], "The campaigns are recorded in some ten contemporary inscriptions of 523, which make no clear mention of religion, though two of them invoke Rahmanan as 'Lord of the Jews'; the massacre is known from Syriac and Greek Christian texts and later Muslim narratives."),
 'c-lakhmid-ghassanid': c("In the north, two Arab Christian dynasties guarded the empires' desert frontiers: the Lakhmids at al-Hira for Persia, ended in 602, and the Ghassanids for Rome, whose last ruler was defeated by the Muslim armies in 636.", 'consensus', ['brit-lakhmid', 'brit-ghassanid'], show=False),
 'c-mecca-trade': c("What made Mecca prosperous is debated.", 'debated', ['crone2007'], "Patricia Crone called the old picture of a rich spice and incense trade a myth, and suggested Meccan merchants sold leather and wool, perhaps to the Roman army, an idea she said 'can be made' but is 'not proved'."),
 'c-muhammad-life': c("According to Muslim tradition, Muhammad was born in Mecca about 570, received his first revelation at about 40, emigrated to Medina in 622 (the hijra, year 1 of the Islamic calendar), took Mecca in 630 and died in Medina in 632.", 'tradition', ['brit-muhammad'], "The outline comes from Muslim sources written down a century and more later."),
 'c-sira': c("The Quran itself gives little biography; the earliest full life, by Ibn Ishaq (died 767/768), survives mainly in a later abridgement. Non-Muslim sources from within decades of his death confirm that an Arab prophet named Muhammad existed.", 'consensus', ['brit-muhammad'], show=False),
 'c-doctrina': c("A Greek Christian text, the Doctrina Jacobi, reports that 'a prophet appeared, coming with the Saracens', proclaiming 'the arrival of the coming Anointed One and Christ'.", 'debated', ['shaddel-dj'], "It is usually dated to about 634, which would make it the earliest outside reference; Mehdy Shaddel argues it was written decades later, in the Umayyad period."),
 'c-revisionists': c("Historians disagree about how far the traditional biography can be trusted.", 'debated', ['hagarism', 'shoemaker2012', 'neuenkirchen2016', 'hup-donner', 'hoyland2007'], "Patricia Crone and Michael Cook (1977) rebuilt early Islam from non-Muslim sources alone; Stephen Shoemaker argues Muhammad lived to lead the first attack on Palestine in 634; Fred Donner describes an open movement of 'Believers'; Robert Hoyland surveys both sides and finds no reliable test of authenticity. Traditional Muslim scholarship accepts the outline of the sira."),
 # 10.7
 'c-quran-structure': c("The Quran, roughly the length of the New Testament, has 114 suras (chapters), usually counted as 6,236 verses; after the short opening sura they are arranged roughly from longest to shortest.", 'consensus', ['brit-quran', 'pup-scriptures'], show=False),
 'c-quran-muslim': c("Muslims hold the Quran to be the very word of God, revealed through the angel Gabriel to Muhammad; it says of itself, 'We have sent down the Quran Ourself, and We Ourself will guard it' (15:9).", 'tradition', ['brit-quran', 'quran-15-9'], "This is the belief of Muslims and the text's own claim; the translation is Abdel Haleem's."),
 'c-uthman': c("Muslim tradition holds that the caliph Uthman had a standard text copied from the manuscripts kept by Hafsa, sent a copy to every Muslim province, and ordered all other Quranic material burned, so that Muslims would not 'differ about the Book (Qur'an) as Jews and the Christians did before'.", 'tradition', ['bukhari-4987'], "Reported in the hadith collection of al-Bukhari, compiled in the 9th century."),
 'c-birmingham': c("Two leaves in Birmingham, with parts of suras 18-20, are written on parchment radiocarbon-dated to between 568 and 645.", 'approx', ['bham-quran', 'marx-jocham2019'], "The date is when the animal died, not when the text was written; the university does not call them the oldest Quran."),
 'c-early-mss': c("Other manuscripts tested by the Corpus Coranicum project date to the 7th century, for example 606-649 and 606-652.", 'approx', ['marx-jocham2019'], "The authors warn that manuscripts can be dated precisely neither by handwriting nor by radiocarbon."),
 'c-sanaa': c("In the Sanaa palimpsest, a 7th-century Quran was scraped off and overwritten; the lower text is the only known manuscript whose consonantal text differs from the standard one.", 'debated', ['iis-sanaa', 'sinai2020'], "Asma Hilali reads it as a teaching text; Nicolai Sinai argues it came from a full copy that preserved a different version."),
 'c-closure': c("When the Quran's text was fixed is debated.", 'debated', ['sinai2014', 'ucp-shoemaker2022'], "Nicolai Sinai (2014) argues that 'neither the epigraphic nor the literary evidence' for a late closure 'is incompatible with the conventional dating' under Uthman (reigned 644-656); Stephen Shoemaker (2022) argues that the canonical text was 'most likely produced only around the turn of the eighth century', under Abd al-Malik."),
 'c-abraham-quran': c("The Quran tells how 'Abraham and Ishmael built up the foundations of the House', the Kaaba at Mecca (2:127).", 'consensus', ['quran-2-127'], show=False),
 'c-prophets': c("It tells believers to accept what was revealed to Abraham, Moses, Jesus and the other prophets: 'We make no distinction between any of them' (2:136).", 'consensus', ['quran-2-136'], show=False),
 'c-mary': c("Mary is honoured as chosen 'above all women' (3:42), and a whole sura bears her name.", 'consensus', ['quran-3-42', 'bham-quran'], show=False),
 'c-crucifixion': c("Of Jesus the Quran says 'they did not kill him, nor did they crucify him, though it was made to appear like that to them' (4:157).", 'debated', ['quran-4-157', 'reynolds2009'], "Most classical Muslim commentators held that someone else was made to look like Jesus and that Jesus did not die; Gabriel Said Reynolds argues that 'the Quran rather accepts that Jesus died', and that it denies only that his enemies killed him."),
 'c-quran-bible': c("Biblical characters, images and stories feature prominently in the Quran.", 'debated', ['nd-reynolds2018'], "Believers read them as one God's revelation, restating and correcting earlier scriptures; historians read them as the Quran's engagement with the Jewish and Christian traditions around it."),
}

# ---------------------------------------------------------------- 10.4
P4 = {
 'title': "Did Rome fall?", 'sub': "the West, 376 to 589",
 'lede': "In the 5th century the western half of the Roman empire broke up into kingdoms ruled by Goths, Vandals, Franks and others. Whether that was a catastrophe or a gradual transformation is one of the oldest arguments in history, and new evidence, from cattle bones to ancient DNA, keeps changing it.",
 'body': [
  "Gothic refugees fleeing the Huns were let into the empire, mistreated, and rebelled. At Adrianople in 378 they killed an emperor and destroyed his army. [[c-adrianople]] [[c-adrianople-toll]] In 410 another Gothic army sacked Rome itself. [[c-sack410]] Augustine, a bishop in North Africa, answered those who blamed the Christian God by writing the City of God. [[c-augustine]] In 476 the boy emperor Romulus Augustulus, conventionally the last in the West, was quietly deposed. [[c-476]]",
  "For a generation of historians led by Peter Brown, this was a 'transformation': Roman law, Latin, cities and the Church carried on under new rulers. Others answer that it was a collapse, measurable in the ground. [[c-fall-debate]] In much of the West, pottery, roof tiles, coins and even the size of cattle shrank. [[c-material]] Ancient DNA now shows that real migrations of people took place, though not how large or violent they were. [[c-speidel2025]]",
  "In Spain the Visigoths built the most lasting of the successor kingdoms, with its capital at Toledo. [[c-toledo]] They were Arian Christians ruling Catholic subjects until King Reccared converted in 589; councils of bishops at Toledo then became the kingdom's lawmakers. [[c-recared]] The same councils passed increasingly harsh laws against the kingdom's Jews. [[c-visigoth-jews]] The kingdom lasted until 711 (see 10.9).",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["378", "Battle of Adrianople; emperor Valens killed"],
    ["410", "Visigoths sack Rome"],
    ["413", "Augustine begins the City of God"],
    ["476", "Romulus Augustulus deposed"],
    ["589", "Third Council of Toledo: Visigothic Spain becomes Catholic"]], 'note': "[[c-adrianople]] [[c-sack410]] [[c-augustine]] [[c-476]] [[c-recared]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ledger', 'signs': False, 'caption': "Fall, or transformation?", 'title': "Two readings of the West, c. 400-600",
  'left': {'h': "'Transformation' (Brown, Pohl)", 'items': [
   {'t': 'Roman law, Latin and the Church carried on', 's': 'continuity under new rulers'},
   {'t': 'New kingdoms used Roman officials and taxes', 's': "e.g. Visigothic Toledo"},
   {'t': 'Culture flourished in new forms', 's': 'monasteries, councils, saints'},
   {'t': 'Movement, not invasion, of peoples', 's': 'the 1993-98 European project'}]},
  'right': {'h': "'Fall' (Ward-Perkins, Heather)", 'items': [
   {'t': 'Roof tiles and coins vanished from daily life', 's': 'Ward-Perkins'},
   {'t': 'Cattle shrank from c. 120 to c. 112 cm', 's': 'Ward-Perkins, via a reviewer'},
   {'t': "Enemies' military power broke the West", 's': 'Heather'},
   {'t': 'DNA confirms that people really did move', 's': 'Speidel et al. (2025); scale still disputed'}]},
  'notes': ["Both sides accept much of the other's evidence; they disagree about what mattered most."]},
 'practice': [
  q("Ward-Perkins points to smaller cattle and the disappearance of roof tiles and coins. What is this evidence meant to show?",
    ["That material living standards in the West really fell", "That Roman life went on under new rulers, with little change", "That the military power of Rome's enemies caused the fall", "That large migrations from Scandinavia really took place"], 0,
    "He tests everyday comfort, not just politics: in much of the West, tiles and coins disappeared from daily life and cattle shrank.",
    {1: "That is the continuity view he calls 'badly in error'.", 2: "That is Peter Heather's argument about the cause; Ward-Perkins' material evidence measures how far life declined.", 3: "That is the finding of the 2025 ancient-DNA study, not of tiles, coins and cattle."}),
  q("Why did the Council of Toledo in 589 matter?",
    ["It made the Arian Goths' kingdom officially Catholic", "It was the first of the councils held at Toledo", "It ordered the kingdom's Jews to accept baptism", "It converted the Visigoths from Catholicism to Arianism"], 0,
    "After King Reccared converted from Arian to Catholic Christianity, the Third Council of Toledo made Catholicism the religion of the kingdom, uniting rulers and ruled in one church.",
    {1: "Eighteen councils met at Toledo between about 400 and 702; this was the third.", 2: "That order came from King Sisebut, between 612 and 616.", 3: "Reccared converted the other way, from Arian to Catholic Christianity."})]}

# ---------------------------------------------------------------- 10.5
P5 = {
 'title': "Justinian and the plague", 'sub': "the eastern empire, 527-565",
 'lede': "In Constantinople the Roman empire carried on. Its most ambitious ruler, Justinian, codified Roman law, built the greatest church in Christendom and won back Africa and Italy. Then the first great plague pandemic and a sudden cold snap struck, and historians are still arguing about how much damage they did.",
 'body': [
  "Justinian, a Latin speaker of peasant stock from the Balkans and nephew of the emperor Justin I, came to the throne in 527. [[c-justinian]] His lawyers condensed centuries of Roman law into the Corpus Juris Civilis. [[c-corpus]] Rediscovered in medieval Italy, it became the basis of legal study across Europe and a main root of the civil-law systems of continental Europe, which much of Latin America later adopted. [[c-civil-law]] In 532 a riot nearly toppled him; [[c-nika]] he rebuilt the burned city centre around the Hagia Sophia. [[c-hagia]] His generals retook North Africa from the Vandals [[c-africa]] and, after twenty years of war, Italy from the Goths. [[c-italy]]",
  "In 541 plague arrived in Egypt and the next year in the capital. Procopius saw it and gives terrifying figures. [[c-procopius-plague]] Ancient DNA has identified the killer as Yersinia pestis, the bacterium of the Black Death, [[c-ypestis]] and in 2025 its genome was recovered from a mass grave in Jordan. [[c-jerash]] But how many died is one of the hottest arguments in the field. [[c-plague-toll]]",
  "Nature struck in another way too. Huge volcanic eruptions in 536 and 540 brought what was probably the coldest decade in two thousand years. [[c-536]] Whether the cold, the plague and the wars together explain the shrinking of the empire in the 7th century, and the success of the Arab conquests (10.8), is still being tested.",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["527", "Justinian becomes emperor"],
    ["529-534", "Code, Digest and Institutes"],
    ["532", "Nika riot; Hagia Sophia begun (finished 537)"],
    ["533-534", "Vandal Africa reconquered"],
    ["536 and 540", "great eruptions; probably the coldest decade in 2,000 years"],
    ["541-542", "plague reaches Egypt, then Constantinople"],
    ["552", "Totila defeated; Italy reconquered"]], 'note': "[[c-justinian]] [[c-corpus]] [[c-nika]] [[c-africa]] [[c-536]] [[c-procopius-plague]] [[c-italy]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 19.0, 'lat': 39.0, 'zoom': 7.5}, 'caption': "Justinian's wars and the first plague pandemic, 533-660", 'hint': "Click a place",
  'legend': [['acc', 'reconquests (simplified)'], ['dot', 'plague evidence'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'arrow', 'items': [
    {'path': [[28.98, 41.01], [24.0, 37.0], [17.0, 36.0], [10.33, 36.87]], 'label': 'Africa, 533', 'lab': [17.0, 36.0], 'ldy': 18},
    {'path': [[10.33, 36.87], [13.0, 38.0], [15.0, 40.0], [12.51, 41.89], [12.2, 44.41]], 'label': 'Italy, 535-552', 'lab': [15.0, 40.0], 'ldx': 8, 'anchor': 'start'}]},
   {'type': 'region', 'items': [{'ll': [15.8, 41.0], 'label': 'ITALY', 'size': 9}, {'ll': [8.0, 33.5], 'label': 'AFRICA', 'size': 9}, {'ll': [31.0, 39.0], 'label': 'ANATOLIA', 'size': 9}, {'ll': [-1.5, 40.0], 'label': 'VISIGOTHIC SPAIN', 'size': 8}]},
   {'type': 'points', 'items': [
    {'ll': [28.98, 41.008], 'label': 'Constantinople', 'date': 'Nika 532; Hagia Sophia 537', 'acc': True, 'big': True, 'dy': -10, 'plate': {'kicker': '10.5 · the capital', 'title': 'Constantinople', 'sub': '527-565', 'text': "[[c-justinian]] [[c-corpus]] [[c-nika]] [[c-hagia]]", 'sources': ['brit-justinian', 'brit-justinian-law', 'brit-nika', 'unesco-istanbul']}},
    {'ll': [10.333, 36.867], 'label': 'Carthage', 'date': 'retaken 533', 'dy': -8},
    {'ll': [12.201, 44.413], 'label': 'Ravenna', 'date': 'taken 540', 'dy': -8},
    {'ll': [12.779, 43.229], 'label': 'Taginae', 'date': '552', 'dy': 16},
    {'ll': [32.54, 31.043], 'label': 'Pelusium', 'date': 'plague begins, 541', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '10.5 · plague', 'title': 'The plague of Justinian', 'sub': 'from 541', 'text': "[[c-procopius-plague]] [[c-plague-toll]]", 'sources': ['procopius-plague', 'mordechai2019', 'sarris-sb']}},
    {'ll': [35.899, 32.281], 'label': 'Jerash', 'date': 'plague genomes, 2025', 'acc': True, 'dy': -8, 'plate': {'kicker': '10.5 · new DNA', 'title': 'Jerash', 'sub': 'reported 2025', 'text': "[[c-jerash]]", 'sources': ['fau-jerash2025']}},
    {'ll': [11.717, 48.171], 'label': 'Aschheim', 'date': 'first plague genome, 2014', 'acc': True, 'dy': -8, 'plate': {'kicker': '10.5 · ancient DNA', 'title': 'Yersinia pestis', 'sub': 'confirmed 2013; genome 2014', 'text': "[[c-ypestis]] [[c-536]]", 'sources': ['wagner2014', 'keller2019', 'buntgen2016-pdf']}}]}]},
 'practice': [
  q("What do the plague genomes from Aschheim and Jerash settle, and what do they leave open?",
    ["They confirm Yersinia pestis, but not the death toll", "They show the strain led to the Black Death, but not its toll", "They show it began in Constantinople, but not the toll", "They confirm the toll, but not which germ was responsible"], 0,
    "DNA identifies the killer as Yersinia pestis; how many died is still argued from papyri, laws, coins and pollen.",
    {1: "The Justinianic genome belongs to a different lineage, which died out.", 2: "Procopius says it began at Pelusium in Egypt and reached Constantinople in 542.", 3: "The reverse: DNA identified the germ, and the toll is fiercely debated."}),
  q("Which reading of the 'Late Antique Little Ice Age' is most careful?",
    ["The cooling is measured; its social effects are still tested", "The volcanoes are known, and their link to upheaval proved", "The cold is measured, and it caused the Arab conquests", "The cold of 536 explains the Nika riot in Constantinople"], 0,
    "Tree rings and ice cores measure the cooling; whether cold, plague and war together explain the shrinking of the empire is still being tested.",
    {1: "The volcanoes have not been securely identified, and the link to upheaval is still being tested.", 2: "Whether the cold, the plague and the wars explain the Arab conquests is still being tested.", 3: "The riot was in January 532, before the eruptions of 536 and 540."})]}

# ---------------------------------------------------------------- 10.6
P6 = {
 'title': "Arabia and the Prophet", 'sub': "c. 380 to 632",
 'lede': "Arabia was not cut off from the late antique world. Its southern kings turned to Judaism, its northern tribes served Rome and Persia as Christian allies, and the two empires fought over its edges. Into this world, by the account of Muslim tradition, Muhammad was born around 570.",
 'body': [
  "In Yemen, the kings of Himyar gave up their old gods in the 380s for a single 'Lord of the Sky', and a Jewish community appears in their inscriptions. [[c-himyar]] In the 520s a Jewish king fought the Christian kingdom of Aksum across the Red Sea, and was defeated. [[c-najran]] In the north, Arab Christian dynasties guarded the frontiers of Persia and Rome. [[c-lakhmid-ghassanid]] Mecca, in the Hijaz between them, was a shrine town whose trade is still debated. [[c-mecca-trade]]",
  "Muslim tradition gives a clear outline of Muhammad's life: born in Mecca, called as a prophet at about 40, driven to Medina in 622, victorious over Mecca in 630, dead in 632. [[c-muhammad-life]] That outline was written down a century and more after his death. [[c-sira]] A Christian text that may date from the 630s mentions a prophet among the Arabs, [[c-doctrina]] and historians disagree about how much of the traditional story can be checked. [[c-revisionists]]",
  "What is not in doubt is the result. Muhammad united much of Arabia behind a new faith and a single leadership in Medina. Within two years of his death his successors were attacking the two great empires (10.8).",
  {'table': {'head': ["Approach", "Who", "Main argument"], 'rows': [
    ["Traditional Muslim", "classical and modern Muslim scholarship", "the sira's outline is reliable"],
    ["Sceptical", "Crone and Cook (1977)", "rebuild early Islam from non-Muslim sources"],
    ["Apocalyptic", "Shoemaker (2012)", "Muhammad expected the end and led the first attacks"],
    ["Ecumenical", "Donner (2010)", "a 'Believers' movement' open to Jews and Christians"],
    ["Methodological", "Hoyland (2007)", "no reliable test of authenticity; weigh each report"]], 'note': "[[c-revisionists]] [[c-muhammad-life]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 42.0, 'lat': 24.0, 'zoom': 12}, 'caption': "Arabia between the empires, c. 380-632", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [41.5, 21.5], 'label': 'HIJAZ', 'size': 10}, {'ll': [45.5, 15.8], 'label': 'HIMYAR', 'size': 10}, {'ll': [37.5, 12.5], 'label': 'AKSUM', 'size': 10}, {'ll': [46.5, 33.8], 'label': 'PERSIA', 'size': 9}, {'ll': [36.0, 35.5], 'label': 'ROME', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [39.826, 21.426], 'label': 'Mecca', 'date': 'Muhammad b. c. 570 (tradition)', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 4, 'plate': {'kicker': '10.6 · the Prophet', 'title': 'Mecca', 'sub': 'c. 570-630', 'text': "[[c-muhammad-life]] [[c-mecca-trade]] [[c-sira]]", 'sources': ['brit-muhammad', 'crone2007']}},
    {'ll': [39.614, 24.469], 'label': 'Medina', 'date': 'hijra, 622', 'acc': True, 'big': True, 'dy': -10, 'plate': {'kicker': '10.6 · the sources', 'title': 'How we know', 'sub': 'the sira and its critics', 'text': "[[c-sira]] [[c-doctrina]] [[c-revisionists]]", 'sources': ['brit-muhammad', 'shaddel-dj', 'hoyland2007']}},
    {'ll': [44.128, 17.493], 'label': 'Najran', 'date': 'Christians killed, 523', 'acc': True, 'dy': -8, 'plate': {'kicker': '10.6 · Himyar', 'title': 'Najran', 'sub': '523', 'text': "[[c-najran]]", 'sources': ['robin-himyar']}},
    {'ll': [44.401, 14.213], 'label': 'Zafar', 'date': 'Himyarite capital', 'acc': True, 'dy': 16, 'plate': {'kicker': '10.6 · Himyar', 'title': 'Himyar', 'sub': 'monotheism from c. 380', 'text': "[[c-himyar]]", 'sources': ['robin-himyar']}},
    {'ll': [38.723, 14.121], 'label': 'Aksum', 'date': 'invades Himyar, 525', 'anchor': 'end', 'dy': 16},
    {'ll': [44.487, 31.89], 'label': 'al-Hira', 'date': 'Lakhmids, to 602', 'acc': True, 'dy': -8, 'plate': {'kicker': '10.6 · frontier Arabs', 'title': 'Lakhmids and Ghassanids', 'sub': 'to 602 and 636', 'text': "[[c-lakhmid-ghassanid]]", 'sources': ['brit-lakhmid', 'brit-ghassanid']}},
    {'ll': [36.012, 32.942], 'label': 'al-Jabiya', 'date': 'Ghassanid centre', 'anchor': 'end', 'dy': -6}]}]},
 'practice': [
  q("Why do historians argue over the Doctrina Jacobi?",
    ["Its date decides if it is the earliest outside witness", "It is the earliest Muslim biography, older than Ibn Ishaq's", "It supplies the 622 date for Muhammad's hijra to Medina", "It is used to argue that Muhammad was a later legend"], 0,
    "If it dates from about 634, as usually thought, it is the earliest outside reference to the prophet; Mehdy Shaddel argues it was written decades later.",
    {1: "It is a Greek Christian text; the earliest full Muslim biography is Ibn Ishaq's.", 2: "That date comes from Muslim tradition.", 3: "Non-Muslim sources from within decades of his death confirm that an Arab prophet named Muhammad existed."}),
  q("Which statement about southern Arabia before Islam is accurate?",
    ["Himyar's kings turned to one god and leaned towards Judaism", "Himyar was a Persian client, like the Lakhmids at al-Hira", "The Ghassanids guarded Persia's frontier as Zoroastrians", "Himyar's kings named Judaism outright in their inscriptions"], 0,
    "Around 380-384 royal inscriptions abandoned the old gods for a single 'Lord of the Sky', and the kingdom's rulers leaned towards Judaism.",
    {1: "Himyar's king rebelled against Aksumite, not Persian, overlordship; the Lakhmids guarded Persia's frontier in the north.", 2: "The Ghassanids were an Arab Christian dynasty that guarded Rome's frontier.", 3: "Christian Julien Robin calls it a 'discreet conversion' because royal inscriptions never name Judaism outright."})]}

# ---------------------------------------------------------------- 10.7
P7 = {
 'title': "The Quran", 'sub': "scripture, manuscripts and scholarship",
 'lede': "For Muslims the Quran is the literal word of God. For historians it is the one text that almost certainly goes back to the earliest Muslim community. Both readings can be set side by side, together with what radiocarbon dating of the oldest manuscripts now shows.",
 'body': [
  "The Quran is about as long as the New Testament: 114 suras, arranged roughly from longest to shortest. [[c-quran-structure]] Muslims hold it to be God's own speech, revealed to Muhammad, and the text claims divine protection for itself. [[c-quran-muslim]] Muslim tradition says the caliph Uthman fixed a single standard text and sent copies to the provinces. [[c-uthman]]",
  "Manuscripts now let historians test this. Leaves in Birmingham and other early Qurans are written on parchment from the 7th century, [[c-birmingham]] [[c-early-mss]] and the Sanaa palimpsest preserves, under a later text, a version whose wording differs from the standard one. [[c-sanaa]] Most scholars think the evidence fits a standard text fixed in the mid-7th century; a minority argue for about 700. [[c-closure]]",
  "The Quran speaks to readers of the Bible. It tells of Abraham building the Kaaba with Ishmael, [[c-abraham-quran]] honours all the prophets from Abraham to Jesus, [[c-prophets]] and names a sura after Mary. [[c-mary]] On Jesus' death it differs sharply from the Gospels. [[c-crucifixion]] Believers and historians read these shared stories differently. [[c-quran-bible]]",
  {'table': {'head': ["Figure", "Quran", "Hebrew Bible and New Testament"], 'rows': [
    ["Abraham", "builds the Kaaba with Ishmael (2:127)", "no link with Mecca (Genesis)"],
    ["Moses", "his story is retold in many suras", "the central figure of Exodus-Deuteronomy"],
    ["Mary", "chosen above all women (3:42); sura 19 named after her", "mother of Jesus (Gospels)"],
    ["Jesus", "messenger and Messiah; not crucified, 'it was made to appear' so (4:157)", "crucified and risen (Gospels)"]], 'note': "[[c-abraham-quran]] [[c-mary]] [[c-crucifixion]] [[c-prophets]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "How old are the oldest Qurans?", 'title': "Radiocarbon dates of early Quran manuscripts (95% ranges, CE)",
  'max': -550, 'min': -780, 'unit': 'ka', 'ticks': [-550, -600, -650, -700, -750], 'tickLabels': ['550 CE', '600', '650', '700', '750 CE'],
  'axis': "calibrated radiocarbon date of the parchment, CE", 'hint': "Hover or click a row",
  'marks': [{'ya': -622, 't': 'hijra, 622'}, {'ya': -632, 't': "Muhammad's death, 632 (tradition)"}, {'ya': -691, 't': 'Dome of the Rock, 691/692', 'anchor': 'end'}],
  'rows': [
   {'t': 'Birmingham', 'sub': 'Mingana 1572a', 'from': -568, 'to': -645, 'lab': '568-645', 'acc': True, 'plate': {'kicker': '10.7 · manuscripts', 'title': 'The Birmingham leaves', 'sub': '568-645', 'text': "[[c-birmingham]] [[c-early-mss]]", 'sources': ['bham-quran', 'marx-jocham2019']}},
   {'t': 'Sanaa palimpsest', 'sub': 'lower text', 'from': -606, 'to': -649, 'lab': '606-649', 'acc': True, 'plate': {'kicker': '10.7 · manuscripts', 'title': 'The Sanaa palimpsest', 'sub': '7th century', 'text': "[[c-sanaa]] [[c-closure]]", 'sources': ['iis-sanaa', 'sinai2020', 'sinai2014', 'ucp-shoemaker2022']}},
   {'t': 'Berlin', 'sub': 'Ms. or. fol. 4313', 'from': -606, 'to': -652, 'lab': '606-652', 'acc': True},
   {'t': 'Sanaa', 'sub': 'DAM 01-29.1', 'from': -633, 'to': -665, 'lab': '633-665', 'acc': True},
   {'t': 'Tübingen', 'sub': 'Ma VI 165', 'from': -649, 'to': -675, 'lab': '649-675', 'acc': True},
   {'t': 'Leiden', 'sub': 'Or. 14.545a', 'from': -652, 'to': -763, 'lab': '652-763', 'open': True}],
  },
 'practice': [
  q("The Birmingham leaves date to 568-645 at 95 percent probability. What does that result show?",
    ["It dates the parchment, not the writing on it", "The text was certainly written in Muhammad's lifetime", "It is the oldest Quran, as the university announced", "It preserves a complete Quran from the 7th century"], 0,
    "Radiocarbon dates when the animal died, not when the text was written; the result fits a 7th-century text.",
    {1: "The date is when the animal died; the writing could be later.", 2: "The university does not call them the oldest Quran.", 3: "They are two leaves with parts of suras 18-20."}),
  q("Why does the lower text of the Sanaa palimpsest matter?",
    ["It is the only known Quran with wording unlike the standard", "Its lower text is a Christian scripture, not a Quran", "Sinai reads it as a teaching text, not a full copy", "It proves the standard text was fixed only around 700"], 0,
    "The lower text, a 7th-century Quran, is the only known manuscript whose consonantal text differs from the standard one.",
    {1: "The lower text is a 7th-century Quran that was scraped off and overwritten.", 2: "That is Asma Hilali's reading; Nicolai Sinai argues it came from a full copy that preserved a different version.", 3: "It shows that a different version existed; when the standard text was fixed is still debated."})]}

PAGES = [P4, P5, P6, P7]
