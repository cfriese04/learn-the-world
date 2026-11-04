# Chapter 11, pages 11.0 to 11.3. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 11.0
 'cudl-genizah': ("Cambridge Digital Library, \"The Genizah collection\"", "https://cudl.lib.cam.ac.uk/collections/genizah/1"),
 'cam-genizah-unit': ("Cambridge University Library, Taylor-Schechter Genizah Research Unit", "https://www.lib.cam.ac.uk/collections/departments/taylor-schechter-genizah-research-unit"),
 'brit-idrisi': ("Encyclopaedia Britannica, \"al-Idrisi\"", "https://www.britannica.com/print/article/282089"),
 'brit-bakri': ("Encyclopaedia Britannica, \"Abu Ubayd al-Bakri\"", "https://www.britannica.com/biography/Abu-Ubayd-al-Bakri"),
 'cu-printing': ("Columbia University, Asia for Educators, \"Printing\" (Song dynasty module)", "https://afe.easia.columbia.edu/songdynasty-module/tech-printing.html"),
 'unesco-lanse2': ("UNESCO World Heritage Centre, \"L'Anse aux Meadows National Historic Site\"", "https://whc.unesco.org/en/list/4/"),
 # 11.1
 'brit-baghdad': ("Encyclopaedia Britannica, \"Baghdad: history\"", "https://www.britannica.com/place/Baghdad/History"),
 'acm-belitung': ("Asian Civilisations Museum, Singapore, \"The Tang shipwreck\"", "https://www.acm.nhb.gov.sg/galleries/maritime-trade/tang-shipwreck"),
 'met-dinar780': ("The Met, gold dinar of al-Mahdi, 780 (A.H. 164)", "https://www.metmuseum.org/art/collection/search/457626"),
 'met-dirham-sas': ("The Met, early Islamic silver dirham modelled on the Sasanian drachm", "https://www.metmuseum.org/art/collection/search/479441"),
 'bloom1999': ("Jonathan Bloom, \"Revolution by the ream: a history of paper\", Aramco World (1999)", "https://archive.aramcoworld.com/issue/199903/revolution.by.the.ream-a.history.of.paper.htm"),
 'hoi-samarkand': ("History of Information, on paper in Samarkand before 751", "https://www.historyofinformation.com/detail.php?id=5028"),
 'sep-greek-arabic': ("Cristina D'Ancona, \"Greek sources in Arabic and Islamic philosophy\", Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/arabic-islamic-greek/"),
 'hoi-gutas': ("History of Information, quoting Dimitri Gutas, Greek Thought, Arabic Culture (1998), on the bayt al-hikma", "https://historyofinformation.com/detail.php?id=1583"),
 'brit-bayt': ("Encyclopaedia Britannica, \"Bayt al-Hikmah\"", "https://www.britannica.com/place/Bayt-al-Hikmah"),
 'brit-khwarizmi': ("Encyclopaedia Britannica, \"al-Khwarizmi\"", "https://www.britannica.com/biography/al-Khwarizmi"),
 'brit-fatimid': ("Encyclopaedia Britannica, \"Fatimid dynasty\"", "https://www.britannica.com/topic/Fatimid-dynasty"),
 'brit-seljuk': ("Encyclopaedia Britannica, \"Seljuq\"", "https://www.britannica.com/print/article/598045"),
 # 11.2
 'brit-abdalrahman3': ("Encyclopaedia Britannica, \"Abd al-Rahman III\"", "https://www.britannica.com/biography/Abd-al-Rahman-III"),
 'brit-muslim-spain': ("Encyclopaedia Britannica, \"Spain: Muslim Spain\"", "https://www.britannica.com/place/Spain/Muslim-Spain"),
 'brit-cordoba': ("Encyclopaedia Britannica, \"Córdoba\" (Spain)", "https://www.britannica.com/place/Cordoba-Spain"),
 'unesco-cordoba': ("UNESCO World Heritage Centre, \"Historic Centre of Cordoba\"", "https://whc.unesco.org/en/list/313/"),
 'unesco-zahra': ("UNESCO World Heritage Centre, \"Caliphate City of Medina Azahara\"", "https://whc.unesco.org/en/list/1560/"),
 'brit-hasdai': ("Encyclopaedia Britannica, \"Hisdai ibn Shaprut\"", "https://www.britannica.com/biography/Hisdai-ibn-Shaprut"),
 'brit-nagid': ("Encyclopaedia Britannica, \"Samuel ha-Nagid\"", "https://www.britannica.com/biography/Samuel-ha-Nagid"),
 'jvl-granada': ("Jewish Virtual Library, \"Granada\"", "https://www.jewishvirtuallibrary.org/granada"),
 'brit-taifa': ("Encyclopaedia Britannica, \"Taifa\"", "https://www.britannica.com/topic/taifa"),
 'brit-almoravids': ("Encyclopaedia Britannica, \"Almoravids\"", "https://www.britannica.com/topic/Almoravids"),
 'brit-almohads': ("Encyclopaedia Britannica, \"Almohads\"", "https://www.britannica.com/topic/Almohads"),
 'brit-maimonides': ("Encyclopaedia Britannica, \"Moses Maimonides\"", "https://www.britannica.com/biography/Moses-Maimonides"),
 'brit-averroes': ("Encyclopaedia Britannica, \"Averroes\"", "https://www.britannica.com/biography/Averroes"),
 'nybr-irwin': ("Robert Irwin, \"The contested legacy of Muslim Spain\", New York Review of Books (2019)", "https://www.nybooks.com/articles/2019/03/21/contested-legacy-muslim-spain/"),
 'oteo2025': ("Oteo-Garcia et al., ancient genomes from eastern Iberia, Genome Biology 26 (2025)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12036142"),
 # 11.3
 'brit-alfonso3': ("Encyclopaedia Britannica, \"Alfonso III\" (king of Asturias)", "https://www.britannica.com/print/article/14656"),
 'brit-sancho3': ("Encyclopaedia Britannica, \"Sancho III Garcés\"", "https://www.britannica.com/biography/Sancho-III-Garces"),
 'brit-castile': ("Encyclopaedia Britannica, \"Castile\"", "https://www.britannica.com/place/Castile-region-Spain"),
 'brit-aragon': ("Encyclopaedia Britannica, \"Kingdom of Aragon\"", "https://www.britannica.com/place/Kingdom-of-Aragon"),
 'brit-afonso1': ("Encyclopaedia Britannica, \"Afonso I\" (king of Portugal)", "https://www.britannica.com/biography/Afonso-I-king-of-Portugal"),
 'brit-toledo1085': ("Encyclopaedia Britannica, \"Siege of Toledo\"", "https://www.britannica.com/event/Siege-of-Toledo"),
 'brit-gerard': ("Encyclopaedia Britannica, \"Gerard of Cremona\"", "https://www.britannica.com/biography/Gerard-of-Cremona"),
 'brit-cid': ("Encyclopaedia Britannica, \"El Cid: conquest of Valencia\"", "https://www.britannica.com/biography/El-Cid-Castilian-military-leader/Conquest-of-Valencia"),
 'bne-cantar': ("Enrique Jerez, \"Un códice único para un poema único\", Biblioteca Nacional de España", "https://www.bne.es/sites/default/files/repositorio-archivos/ENRIQUE_JEREZ._Un_cxdice_xnico_para_un_poema_xnico.pdf"),
 'unesco-santiago': ("UNESCO World Heritage Centre, \"Routes of Santiago de Compostela\"", "https://whc.unesco.org/en/list/669/"),
 'brit-navas': ("Encyclopaedia Britannica, \"Battle of Las Navas de Tolosa\"", "https://www.britannica.com/event/Battle-of-Las-Navas-de-Tolosa"),
 'brit-castile-aragon': ("Encyclopaedia Britannica, \"Spain: the rise of Castile and Aragon\"", "https://www.britannica.com/place/Spain/The-rise-of-Castile-and-Aragon"),
 'jmis-garcia': ("Alejandro García-Sanjuán, on the concept of Reconquista, Journal of Medieval Iberian Studies (2016), abstract", "https://informahealthcare.com/doi/abs/10.1080/17546559.2016.1268263"),
 'medievalismo-2025': ("J. M. Monsalvo Antón, review of D. Porrinas (ed.), ¡Reconquista! ¿Reconquista? (2024), Medievalismo 35 (2025)", "https://revistas.um.es/medievalismo/article/download/694131/393741/2752601"),
}

C = {
 # 11.0
 'c-genizah': c("Jews of medieval Cairo placed worn-out writings in a storeroom, a genizah, of the Ben Ezra Synagogue rather than destroy them; in 1896-97 Solomon Schechter brought some 193,000 manuscript fragments to Cambridge, including business letters, accounts and marriage and divorce deeds from the 11th century onward.", 'consensus', ['cudl-genizah', 'cam-genizah-unit'], show=False),
 'c-idrisi': c("The geographer al-Idrisi, born in Ceuta, completed a geography of the known world for the Norman king Roger II of Sicily in 1154, combining Arabic and Greek works with eyewitness reports; for Roger he also made a silver planisphere showing a map of the world.", 'consensus', ['brit-idrisi'], show=False),
 'c-bakri': c("The Córdoban geographer al-Bakri (died 1094) described the capital of Ghana as two towns, a stone-built one for Muslim traders and a mud-built one for the local Mande.", 'consensus', ['brit-bakri'], show=False),
 'c-printing-cost': c("Printing dramatically lowered the price of books in Song China, aiding the spread of literacy; movable type was first made by Bi Sheng (990-1051), but carved woodblocks remained the usual method.", 'consensus', ['cu-printing'], show=False),
 'c-sagas-test': c("Archaeology can test medieval sagas: the 11th-century Norse site at L'Anse aux Meadows matches the Icelandic Vinland sagas' accounts of voyages to North America.", 'consensus', ['unesco-lanse2'], show=False),
 # 11.1
 'c-baghdad': c("The caliph al-Mansur founded Baghdad in 762 as Madinat al-Salam, the 'Round City', about 2,700 m across inside three concentric walls; its wharves received ships from China, India and East Africa.", 'consensus', ['brit-baghdad'], show=False),
 'c-belitung': c("A ship wrecked off Belitung in Indonesia in about the 830s, sewn from planks in the style of the Persian Gulf, carried more than 50,000 painted bowls made in China.", 'approx', ['acm-belitung'], "Dated from objects in the cargo."),
 'c-abbasid-coins': c("Abbasid gold dinars carried only inscriptions, no images, like the Umayyad reform coins (10.9); the silver dirham had begun as a copy of the Sasanian drachm.", 'consensus', ['met-dinar780', 'met-dirham-sas'], show=False),
 'c-paper-talas': c("A later story credits Chinese prisoners captured at the battle of Talas in 751 with bringing paper-making to the Islamic world.", 'debated', ['bloom1999', 'hoi-samarkand'], "Jonathan Bloom treats the story cautiously; paper was already known in Samarkand decades before 751."),
 'c-paper-baghdad': c("Abbasid officials promoted paper for government records, partly because documents on paper were harder to alter undetected than those on parchment.", 'tradition', ['bloom1999'], "The story of al-Fadl ibn Yahya comes from Ibn Khaldun; the point about forgery is Bloom's reasoning."),
 'c-translation': c("Translation of Greek philosophy and science into Arabic, often by way of Syriac, flourished under the Abbasids, above all under al-Ma'mun (813-833); the Nestorian Christian physician Hunayn ibn Ishaq led one of the great translation circles.", 'consensus', ['sep-greek-arabic'], show=False),
 'c-house-wisdom': c("How much of an institution the Abbasid 'House of Wisdom' (bayt al-hikma) was is debated.", 'debated', ['hoi-gutas', 'sep-greek-arabic', 'brit-bayt'], "Dimitri Gutas sees a library and bureau modelled on Sasanian administration, 'certainly not a center for the translation of Greek works into Arabic'; Cristina D'Ancona agrees that it 'cannot be viewed as an institutional center' for such translations. Older accounts, which Britannica mentions, call it an academy."),
 'c-khwarizmi': c("Al-Khwarizmi (about 780-850) wrote the book whose title gave us the word 'algebra'; his own name, in Latin 'Algoritmi', gave us 'algorithm', and his work introduced Hindu-Arabic numerals to the West.", 'consensus', ['brit-khwarizmi'], show=False),
 'c-abbasid-fragment': c("Abbasid power fragmented: the caliphs lived at Samarra from 836 to 892, a Persian dynasty, the Buyids, controlled Baghdad from 945 to 1055, and the Seljuk Turks entered it in 1055.", 'consensus', ['brit-baghdad', 'brit-seljuk'], show=False),
 'c-fatimids': c("The Fatimids, an Ismaili Shia dynasty claiming the caliphate, took Egypt in 969 and built Cairo as their capital.", 'consensus', ['brit-fatimid'], show=False),
 # 11.2
 'c-caliphate929': c("Abd al-Rahman III, emir of Córdoba from 912, took the title of caliph in 929, partly to answer the Fatimids' claim to it; the caliphate of Córdoba lasted until 1031.", 'consensus', ['brit-abdalrahman3', 'brit-muslim-spain'], show=False),
 'c-cordoba-pop': c("Córdoba around the year 1000 was probably the largest city in Europe, with some 100,000 people.", 'approx', ['brit-cordoba', 'brit-abdalrahman3'], "A modern estimate; the medieval boast that the city had 3,000 mosques and more than 100,000 shops and houses is not a census figure."),
 'c-mezquita': c("The Great Mosque of Córdoba was begun in the 8th century over the remains of a Visigothic church, extended over three centuries, and made a cathedral in 1236.", 'consensus', ['unesco-cordoba'], show=False),
 'c-zahra': c("Madinat al-Zahra, the palace city of the caliphs built in the mid-10th century, was laid waste in the civil war of 1009-1010 and rediscovered in the early 20th century.", 'consensus', ['unesco-zahra'], show=False),
 'c-hasdai': c("Hasdai ibn Shaprut (about 915-975), a Jewish physician, served Abd al-Rahman III as court doctor and, in effect, minister, and was a patron of Hebrew learning.", 'consensus', ['brit-hasdai'], show=False),
 'c-nagid': c("Samuel ha-Nagid (993-1055/56), scholar, poet and soldier, became vizier of the taifa kingdom of Granada; his son Joseph, who succeeded him, was killed in a revolt in 1066 in which much of Granada's Jewish community died.", 'approx', ['brit-nagid', 'jvl-granada'], "The death toll of 1066 is uncertain."),
 'c-taifas': c("After 1009 the caliphate collapsed into at least 23 'party kingdoms' (taifas), several of which paid tribute to Alfonso VI of Castile.", 'consensus', ['brit-taifa', 'brit-muslim-spain'], show=False),
 'c-almoravids': c("After Toledo fell in 1085 the taifa kings called in the Almoravids, a Berber confederation from the Sahara, who defeated Castile at al-Zallaqa in 1086 and then absorbed the taifas in 1090-91.", 'consensus', ['brit-almoravids', 'brit-taifa', 'brit-muslim-spain'], show=False),
 'c-almohads': c("The Almohads, a Berber movement preaching a strict doctrine of God's unity, took Marrakesh in 1147 and Seville in 1172, and were crushed at Las Navas de Tolosa in 1212.", 'consensus', ['brit-almohads'], show=False),
 'c-maimonides': c("When the Almohads took Córdoba in 1148, its Jews had to convert or leave; the family of Moses Maimonides left, eventually settling in Egypt, where he wrote the Mishneh Torah in Hebrew and the Guide for the Perplexed in Arabic.", 'consensus', ['brit-maimonides'], show=False),
 'c-averroes': c("Ibn Rushd (Averroes, 1126-1198), chief judge of Córdoba, wrote commentaries on Aristotle that made him 'the Commentator' to Latin scholars, and defended philosophy against al-Ghazali's attack.", 'consensus', ['brit-averroes'], show=False),
 'c-convivencia': c("Whether al-Andalus was a land of 'convivencia', peaceful coexistence of Muslims, Christians and Jews, is contested; Robert Irwin calls the field 'an academic battleground'.", 'debated', ['nybr-irwin'], "Américo Castro coined the term (1948); María Rosa Menocal praised an enlightened culture; Darío Fernández-Morera describes pervasive religious repression; Brian Catlos argues tolerance was real but grew from economic and political necessity."),
 'c-iberia-dna': c("Ancient genomes from eastern Iberia show North African ancestry becoming established during the Islamic period and persisting after the Christian conquest, until the expulsion of the Moriscos in 1609.", 'approx', ['oteo2025'], "New (2025); a single regional study."),
 # 11.3
 'c-asturias': c("Alfonso III of Asturias (866-910) moved his capital forward from Oviedo to León.", 'approx', ['brit-alfonso3'], "Some accounts date the move to his sons, about 910-914."),
 'c-sancho3': c("Sancho III of Navarre (died 1035) dominated the Christian states of Spain and divided his lands into four kingdoms among his sons.", 'consensus', ['brit-sancho3'], show=False),
 'c-castile-leon': c("Ferdinand I (1037-65) was the first king of Castile; Castile and León were finally united in 1230.", 'consensus', ['brit-castile'], show=False),
 'c-aragon': c("Aragon took Zaragoza from its Muslim rulers in 1118 and united with Catalonia in 1137, forming the Crown of Aragon.", 'consensus', ['brit-aragon'], show=False),
 'c-portugal': c("Afonso Henriques took the title king of Portugal in 1139 and in 1147, with the help of passing crusaders, captured Lisbon.", 'consensus', ['brit-afonso1'], show=False),
 'c-toledo1085': c("Alfonso VI of Castile took Toledo in May 1085; its Muslims were allowed to keep their property and practise their religion.", 'consensus', ['brit-toledo1085'], show=False),
 'c-gerard': c("In Toledo, Gerard of Cremona (about 1114-1187) and others translated works of science and philosophy from Arabic into Latin; about 80 translations, including Ptolemy's Almagest and Avicenna's Canon of Medicine, are attributed to him.", 'consensus', ['brit-gerard'], show=False),
 'c-cid': c("Rodrigo Díaz, El Cid, a Castilian lord who fought for both Christian and Muslim rulers, took Valencia in 1094 and held it until his death in 1099.", 'consensus', ['brit-cid'], show=False),
 'c-cantar': c("The epic Cantar de mio Cid survives in a single manuscript in the National Library of Spain, copied from an exemplar made by one Per Abad in 1207.", 'debated', ['bne-cantar'], "Some scholars date the poem's composition to the mid-12th century, others to the early 13th."),
 'c-santiago': c("A tomb believed to be that of the apostle James was discovered in Galicia in the 9th century, and Santiago de Compostela became a pilgrimage centre comparable to Jerusalem and Rome.", 'tradition', ['unesco-santiago'], "The pilgrimage is historical; the identification of the tomb is a matter of faith and tradition."),
 'c-navas': c("On 16 July 1212, at Las Navas de Tolosa, the combined armies of Castile, Aragon, Navarre and Portugal, under a crusade proclaimed by Pope Innocent III, defeated the Almohad caliph.", 'consensus', ['brit-navas'], show=False),
 'c-1236-1248': c("Ferdinand III of Castile took Córdoba in 1236 and Seville in 1248; James I of Aragon took Valencia in 1238. The Muslims retained only the kingdom of Granada.", 'consensus', ['brit-castile-aragon', 'brit-aragon'], show=False),
 'c-reconquista-term': c("Whether to call these wars the 'Reconquista' is debated among Spanish historians.", 'debated', ['jmis-garcia', 'medievalismo-2025'], "Critics such as Alejandro García-Sanjuán and Martín Ríos Saloma call it a 19th-century nationalist construction that peaked under Franco; defenders such as Carlos de Ayala and Francisco García Fitz note that the idea of recovering lost lands appears in 9th-century Asturian sources."),
}

# ---------------------------------------------------------------- 11.0
P0 = {
 'title': "Regional webs", 'sub': "c. 750 to 1250",
 'lede': "Between the Abbasid revolution and the Mongol invasions there was no single centre of the world. Instead several large, connected regions, the Islamic world, China, Latin and Greek Christendom, India and Southeast Asia, Africa's trading states and the Americas, each grew rich in its own way, linked by trade, pilgrimage and the movement of books.",
 'body': [
  "The Islamic world had a new capital at Baghdad, whose wharves received ships from China, India and East Africa. [[c-baghdad]] Song China printed books [[c-printing-cost]] (11.4). Latin Europe revived under Charlemagne (11.5), Byzantium converted the Slavs (11.7), Scandinavians crossed the Atlantic (11.6), and around 1100 crusaders and Iberian kings turned Christendom's energies against Islam (11.3, 11.8).",
  "This chapter can draw on new kinds of evidence. In Cairo, Jews kept their used papers rather than destroy them, and one synagogue's storeroom preserved centuries of business letters and contracts. [[c-genizah]] Arab geographers described distant lands: al-Bakri, from Córdoba, wrote about the African kingdom of Ghana, [[c-bakri]] and al-Idrisi drew a map of the world for a Christian king of Sicily. [[c-idrisi]] And archaeology can test legend: Norse sagas told of voyages to North America, and the ruins have been found. [[c-sagas-test]]",
  {'table': {'head': ["Source", "Where", "What it shows"], 'rows': [
    ["Cairo Genizah", "Fustat (Old Cairo)", "Jewish merchants' letters, contracts and accounts"],
    ["Arab geographers", "Córdoba, Sicily", "descriptions of Africa, Europe and Asia"],
    ["Printed books", "Song China", "cheap books and wider literacy"],
    ["Archaeology and sagas", "Newfoundland", "Norse voyages to America"],
    ["Ancient DNA", "across Europe", "who moved where (11.6)"]], 'note': "[[c-genizah]] [[c-bakri]] [[c-idrisi]] [[c-printing-cost]] [[c-sagas-test]] [[c-margaryan]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 29.0, 'lat': 35.0, 'zoom': 2.2}, 'caption': "Regional webs, c. 750-1250", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [45.0, 27.0], 'label': 'ISLAMIC WORLD', 'size': 10}, {'ll': [110.0, 30.0], 'label': 'SONG CHINA', 'size': 10}, {'ll': [8.0, 50.0], 'label': 'LATIN CHRISTENDOM', 'size': 9}, {'ll': [78.0, 20.0], 'label': 'INDIA', 'size': 10}]},
   {'type': 'points', 'items': [
    {'ll': [44.4008, 33.3406], 'label': 'Baghdad', 'date': 'founded 762', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '11.1 · Baghdad', 'title': 'The Round City', 'sub': '762', 'text': "[[c-baghdad]]", 'sources': ['brit-baghdad']}},
    {'ll': [31.2386, 30.0053], 'label': 'Fustat', 'date': 'the Genizah', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.0 · how we know', 'title': 'The Cairo Genizah', 'sub': '11th century onward', 'text': "[[c-genizah]]", 'sources': ['cudl-genizah', 'cam-genizah-unit']}},
    {'ll': [-4.7725, 37.8914], 'label': 'Córdoba', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.0 · geographers', 'title': 'Al-Bakri', 'sub': 'died 1094', 'text': "[[c-bakri]]", 'sources': ['brit-bakri']}},
    {'ll': [13.3633, 38.1164], 'label': 'Palermo', 'date': "al-Idrisi's map, 1154", 'acc': True, 'dy': -8, 'plate': {'kicker': '11.0 · geographers', 'title': 'Al-Idrisi', 'sub': '1154', 'text': "[[c-idrisi]]", 'sources': ['brit-idrisi']}},
    {'ll': [114.3072, 34.7986], 'label': 'Kaifeng', 'date': 'Song capital', 'acc': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '11.0 · printing', 'title': 'Printing', 'sub': 'Song China', 'text': "[[c-printing-cost]]", 'sources': ['cu-printing']}},
    {'ll': [-55.5319, 51.5953], 'label': "L'Anse aux Meadows", 'date': 'Norse, 11th century', 'acc': True, 'dy': 16, 'plate': {'kicker': '11.0 · sagas', 'title': 'Sagas and archaeology', 'sub': "L'Anse aux Meadows", 'text': "[[c-sagas-test]]", 'sources': ['unesco-lanse2']}}]}]},
 'practice': [
  q("Why is the Cairo Genizah so valuable for economic history?",
    ["Worn-out business papers were stored, not destroyed", "It was the Fatimid treasury's own archive of tax records", "Solomon Schechter assembled it from purchases across Europe", "Its sacred texts were kept, and its letters destroyed"], 0,
    "Rather than destroy worn-out writings, Cairo's Jews stored them, so business letters, accounts and marriage and divorce deeds survived alongside religious texts.",
    {1: "It was a storeroom of the Ben Ezra Synagogue.", 2: "He brought the material from Cairo to Cambridge in 1896-97.", 3: "Writings of every kind were kept, including business letters, accounts and deeds."}),
  q("Al-Idrisi's geography of 1154, made for Roger II of Sicily, best illustrates which theme of this chapter?",
    ["Knowledge crossed religious and political borders", "Abbasid rule over Norman Sicily in the 12th century", "Chinese printing reaching Sicily's royal court", "The end of Arabic scholarship after the crusades"], 0,
    "A Muslim scholar wrote for a Christian king, combining Arabic and Greek works with eyewitness reports.",
    {1: "Sicily was ruled by a Norman king, Roger II.", 2: "His sources were Arabic and Greek works and eyewitness reports.", 3: "He completed a major Arabic geography in 1154, after the crusades had begun around 1100."})]}

# ---------------------------------------------------------------- 11.1
P1 = {
 'title': "The Abbasids and Baghdad", 'sub': "750 to 1055",
 'lede': "The Abbasid caliphs built a new capital at Baghdad. It became famous for paper, books and the translation of Greek science, before their empire broke into pieces ruled by other dynasties in their name.",
 'body': [
  "In 762 the caliph al-Mansur founded a new capital on the Tigris, a round city whose wharves received ships from China, India and East Africa. [[c-baghdad]] One such ship, wrecked off Indonesia in the 830s, still held over 50,000 Chinese bowls. [[c-belitung]] The caliphs struck gold dinars that carried only inscriptions, and silver dirhams that had begun as copies of Sasanian coins. [[c-abbasid-coins]]",
  "Paper came from China by way of Central Asia, though not necessarily as the famous story tells it. [[c-paper-talas]] Officials in Baghdad adopted it for records, [[c-paper-baghdad]] and books multiplied. Scholars, many of them Christians, translated Greek philosophy, medicine and mathematics into Arabic, [[c-translation]] though historians now doubt that the 'House of Wisdom' was the great academy of legend. [[c-house-wisdom]] Al-Khwarizmi's work gave the world the words 'algebra' and 'algorithm'. [[c-khwarizmi]]",
  "The empire did not hold together. Rival caliphs ruled in Córdoba (11.2) and, from 969, in Cairo, [[c-fatimids]] and in Baghdad itself real power passed to Persian and then Turkish military dynasties. [[c-abbasid-fragment]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["762", "Baghdad founded"],
    ["813-833", "al-Ma'mun: translation at its height"],
    ["836-892", "caliphs at Samarra"],
    ["945-1055", "the Buyids control Baghdad"],
    ["969", "Fatimids take Egypt and build Cairo"],
    ["1055", "Seljuk Turks enter Baghdad"]], 'note': "[[c-baghdad]] [[c-translation]] [[c-abbasid-fragment]] [[c-fatimids]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 66.0, 'lat': 22.0, 'zoom': 4.2}, 'caption': "The Abbasid world and its trade, c. 750-1055", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [45.0, 30.0], 'label': 'IRAQ', 'size': 10}, {'ll': [100.0, 32.0], 'label': 'CHINA', 'size': 10}, {'ll': [78.0, 20.0], 'label': 'INDIA', 'size': 10}]},
   {'type': 'points', 'items': [
    {'ll': [44.4008, 33.3406], 'label': 'Baghdad', 'date': 'founded 762', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '11.1 · Baghdad', 'title': 'Baghdad', 'sub': 'the Round City', 'text': "[[c-baghdad]] [[c-translation]] [[c-house-wisdom]] [[c-khwarizmi]]", 'sources': ['brit-baghdad', 'sep-greek-arabic', 'hoi-gutas', 'brit-khwarizmi']}},
    {'ll': [43.8856, 34.1958], 'label': 'Samarra', 'date': 'capital 836-892', 'anchor': 'end', 'dy': -8},
    {'ll': [66.9644, 39.6544], 'label': 'Samarkand', 'date': 'paper', 'acc': True, 'dy': -8, 'plate': {'kicker': '11.1 · paper', 'title': 'Paper', 'sub': '8th century', 'text': "[[c-paper-talas]] [[c-paper-baghdad]]", 'sources': ['bloom1999', 'hoi-samarkand']}},
    {'ll': [31.2386, 30.0053], 'label': 'Cairo', 'date': 'Fatimids, 969', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.1 · rivals', 'title': 'The Fatimids', 'sub': 'from 969', 'text': "[[c-fatimids]] [[c-abbasid-fragment]]", 'sources': ['brit-fatimid', 'brit-baghdad']}},
    {'ll': [107.63, -2.73], 'label': 'Belitung wreck', 'date': 'c. 830s', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.1 · trade', 'title': 'The Belitung wreck', 'sub': 'c. 830s', 'text': "[[c-belitung]] [[c-abbasid-coins]]", 'sources': ['acm-belitung', 'met-dinar780']}}]}]},
 'practice': [
  q("Which statement best matches Dimitri Gutas's view of the Abbasid 'House of Wisdom'?",
    ["A Sasanian-style library and bureau, not a translation centre", "An academy for the ancient sciences, as older accounts say", "An institution founded after the Seljuks entered Baghdad", "A translation centre, as Cristina D'Ancona also holds"], 0,
    "Gutas sees a library and bureau modelled on Sasanian administration, 'certainly not a center for the translation of Greek works into Arabic'.",
    {1: "That is the older view Gutas rejects.", 2: "Translation flourished above all under al-Ma'mun (813-833), long before the Seljuks entered Baghdad in 1055.", 3: "D'Ancona agrees with Gutas that it 'cannot be viewed as an institutional center' for translation."}),
  q("Why did paper matter to the Abbasid state?",
    ["Records on paper were harder to alter undetected", "It was invented in Baghdad's government offices", "Paper notes replaced the caliphs' dinars as money", "Prisoners from Talas brought it straight to Baghdad"], 0,
    "Officials promoted paper for government records, partly because documents on paper were harder to alter undetected than those on parchment; the point about forgery is Jonathan Bloom's reasoning.",
    {1: "It came from China by way of Central Asia.", 2: "The caliphs went on striking gold dinars and silver dirhams.", 3: "Bloom treats the Talas story cautiously; paper was known in Samarkand decades before 751."})]}

# ---------------------------------------------------------------- 11.2
P2 = {
 'title': "Al-Andalus at its height", 'sub': "929 to 1212",
 'lede': "Around the year 1000 Córdoba was probably the largest city in Europe and the capital of a caliphate. Its Muslims, Christians and Jews produced major works of philosophy, poetry and architecture, and how they lived together is still argued over, in Spain and beyond.",
 'body': [
  "Abd al-Rahman III declared himself caliph in 929. [[c-caliphate929]] His capital may have held 100,000 people, [[c-cordoba-pop]] with its Great Mosque, later a cathedral, [[c-mezquita]] and the palace city of Madinat al-Zahra outside it. [[c-zahra]] Jews rose high in government: Hasdai ibn Shaprut served the caliph, [[c-hasdai]] and in the 11th century Samuel ha-Nagid became vizier of Granada, though the community suffered a massacre a generation later. [[c-nagid]]",
  "After 1009 the caliphate split into rival 'taifa' kingdoms, several of which paid tribute to the king of Castile. [[c-taifas]] When Castile took Toledo in 1085 they called in the Almoravids from North Africa, who swallowed them, [[c-almoravids]] to be followed by the stricter Almohads. [[c-almohads]] Under the Almohads Córdoba's Jews were forced to convert or leave; Maimonides grew up in exile. [[c-maimonides]] His Muslim contemporary Ibn Rushd became the West's great interpreter of Aristotle. [[c-averroes]]",
  "Was this a golden age of tolerance? Historians are sharply divided, [[c-convivencia]] and the debate carries political weight in modern Spain. Ancient DNA adds that North African ancestry became established under Islamic rule and outlasted it. [[c-iberia-dna]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["929", "Abd al-Rahman III declares the caliphate"],
    ["1009-1031", "civil war; the caliphate breaks into taifas"],
    ["1066", "massacre of Granada's Jews"],
    ["1086", "Almoravids defeat Castile at al-Zallaqa"],
    ["1148", "Almohads take Córdoba"],
    ["1212", "Almohads defeated at Las Navas de Tolosa"]], 'note': "[[c-caliphate929]] [[c-taifas]] [[c-nagid]] [[c-almoravids]] [[c-maimonides]] [[c-almohads]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ledger', 'signs': False, 'caption': "Convivencia?", 'title': "How historians have described relations among Muslims, Christians and Jews in al-Andalus",
  'left': {'h': 'Coexistence', 'items': [
   {'t': "'Convivencia': peaceful coexistence", 's': 'Américo Castro (1948)'},
   {'t': "'The most advanced culture in Europe'", 's': 'María Rosa Menocal'},
   {'t': 'Jews served as physicians and viziers', 's': 'Hasdai ibn Shaprut; Samuel ha-Nagid'},
   {'t': 'Tolerance grew from economic and political necessity', 's': 'Brian Catlos (a middle view)'}]},
  'right': {'h': 'Repression', 'items': [
   {'t': "'Religious and therefore cultural repression'", 's': 'Darío Fernández-Morera (book jacket)'},
   {'t': 'Massacre of Granada\'s Jews', 's': '1066'},
   {'t': 'Convert or leave', 's': 'Almohad Córdoba, 1148'},
   {'t': 'Non-Muslims paid special taxes as dhimmis', 's': 'see 10.8'}]},
  'notes': ["Each side quotes real evidence; they disagree about what was typical."]},
 'practice': [
  q("Which view does Brian Catlos hold, according to Robert Irwin's review?",
    ["Tolerance was real, but it grew out of necessity", "Coexistence was real, and it grew out of shared ideals", "Religious repression was pervasive in al-Andalus", "Al-Andalus was an enlightened, tolerant culture"], 0,
    "Catlos argues tolerance was real but grew from economic and political necessity.",
    {1: "Catlos sees tolerance growing from economic and political necessity, not shared ideals.", 2: "That is Darío Fernández-Morera's argument.", 3: "That is closer to María Rosa Menocal's praise of an enlightened culture."}),
  q("How did the taifa period end?",
    ["They called in the Almoravids, who absorbed them in 1090-91", "They called in the Almohads, who absorbed them in 1031", "Abd al-Rahman III reunited them under his Córdoba caliphate", "Castile conquered them after its victory at al-Zallaqa"], 0,
    "After Toledo fell in 1085 the taifa kings called in the Almoravids, who defeated Castile in 1086 and then absorbed the taifas: the rescuers became the new rulers.",
    {1: "The taifas emerged after 1009; the Almohads came later, taking Marrakesh in 1147.", 2: "He became caliph in 929; the taifas appeared after the caliphate collapsed in 1009.", 3: "The Almoravids defeated Castile at al-Zallaqa in 1086."})]}

# ---------------------------------------------------------------- 11.3
P3 = {
 'title': "The Christian kingdoms of Iberia", 'sub': "c. 850 to 1248",
 'lede': "From the mountains of the north, small Christian kingdoms pushed south over four centuries until, by 1248, only Granada remained under Muslim rule. Spain's national story was later built around this advance, and the name of that story is now itself a subject of debate.",
 'body': [
  "The kingdom that began at Covadonga (10.9) moved its capital south to León. [[c-asturias]] Navarre briefly dominated the Christian north and its king divided his realms among his sons, [[c-sancho3]] creating kingdoms of Castile and Aragon. [[c-castile-leon]] Portugal became a kingdom in 1139 and took Lisbon with crusaders' help. [[c-portugal]]",
  "The decisive gains came after the caliphate's collapse. Castile took Toledo in 1085, guaranteeing its Muslims their property and faith. [[c-toledo1085]] There, scholars translated Arabic science and philosophy into Latin, passing Greek learning preserved in Arabic to the rest of Europe. [[c-gerard]] Aragon took Zaragoza; [[c-aragon]] a Castilian lord, El Cid, carved out a principality at Valencia, [[c-cid]] and later became the hero of Spain's great epic. [[c-cantar]] Pilgrims came from all over Europe to the shrine of St James at Santiago. [[c-santiago]]",
  "In 1212 a crusading coalition of Christian kings broke the Almohads at Las Navas de Tolosa, [[c-navas]] and within a generation Córdoba, Valencia and Seville had fallen. [[c-1236-1248]] Historians now argue whether 'Reconquista', 'reconquest', is the right word for all this. [[c-reconquista-term]]",
  {'table': {'head': ["Year", "Christian conquest"], 'rows': [
    ["1085", "Toledo (Castile)"],
    ["1118", "Zaragoza (Aragon)"],
    ["1147", "Lisbon (Portugal)"],
    ["1212", "Las Navas de Tolosa"],
    ["1236", "Córdoba (Castile)"],
    ["1238", "Valencia (Aragon)"],
    ["1248", "Seville (Castile)"]], 'note': "[[c-toledo1085]] [[c-aragon]] [[c-portugal]] [[c-navas]] [[c-1236-1248]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': -4.2, 'lat': 40.0, 'zoom': 30}, 'caption': "The Christian advance in Iberia, 850-1248", 'hint': "Click a place",
  'legend': [['dot', 'conquest or key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [-4.3, 41.9], 'label': 'CASTILE AND LEÓN', 'size': 10}, {'ll': [-0.6, 42.3], 'label': 'ARAGON', 'size': 9}, {'ll': [-8.3, 40.2], 'label': 'PORTUGAL', 'size': 9}, {'ll': [-3.8, 37.0], 'label': 'GRANADA', 'size': 8}]},
   {'type': 'points', 'items': [
    {'ll': [-5.8447, 43.3603], 'label': 'Oviedo', 'anchor': 'end', 'dy': -6},
    {'ll': [-5.5703, 42.6], 'label': 'León', 'date': 'capital c. 910', 'dy': -8, 'plate': {'kicker': '11.3 · the north', 'title': 'Asturias and León', 'sub': '9th-10th centuries', 'text': "[[c-asturias]] [[c-castile-leon]]", 'sources': ['brit-alfonso3', 'brit-castile']}},
    {'ll': [-8.5456, 42.8803], 'label': 'Santiago', 'date': 'pilgrimage', 'acc': True, 'anchor': 'end', 'plate': {'kicker': '11.3 · pilgrimage', 'title': 'Santiago de Compostela', 'sub': '9th century onward', 'text': "[[c-santiago]]", 'sources': ['unesco-santiago']}},
    {'ll': [-1.6431, 42.8167], 'label': 'Pamplona', 'date': 'Navarre', 'dy': -8, 'plate': {'kicker': '11.3 · Navarre', 'title': 'Sancho III', 'sub': 'died 1035', 'text': "[[c-sancho3]]", 'sources': ['brit-sancho3']}},
    {'ll': [-0.8772, 41.6558], 'label': 'Zaragoza', 'date': '1118', 'acc': True, 'dy': 16},
    {'ll': [-4.0225, 39.8581], 'label': 'Toledo', 'date': '1085', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '11.3 · Toledo', 'title': 'Toledo', 'sub': '1085', 'text': "[[c-toledo1085]] [[c-gerard]]", 'sources': ['brit-toledo1085', 'brit-gerard']}},
    {'ll': [-9.1497, 38.725], 'label': 'Lisbon', 'date': '1147', 'acc': True, 'dy': 16, 'plate': {'kicker': '11.3 · Portugal', 'title': 'Lisbon', 'sub': '1147', 'text': "[[c-portugal]]", 'sources': ['brit-afonso1']}},
    {'ll': [-0.3794, 39.4739], 'label': 'Valencia', 'date': 'Cid 1094; Aragon 1238', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.3 · El Cid', 'title': 'El Cid', 'sub': 'Valencia, 1094-1099', 'text': "[[c-cid]] [[c-cantar]]", 'sources': ['brit-cid', 'bne-cantar']}},
    {'ll': [-3.606, 38.278], 'label': 'Las Navas de Tolosa', 'date': '1212', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '11.3 · 1212', 'title': 'Las Navas de Tolosa', 'sub': '16 July 1212', 'text': "[[c-navas]] [[c-reconquista-term]]", 'sources': ['brit-navas', 'jmis-garcia', 'medievalismo-2025']}},
    {'ll': [-4.7725, 37.8914], 'label': 'Córdoba', 'date': '1236', 'acc': True, 'anchor': 'end', 'dy': 4},
    {'ll': [-5.9731, 37.3828], 'label': 'Seville', 'date': '1248', 'acc': True, 'anchor': 'end', 'dy': 16}]}]},
 'practice': [
  q("What is the core argument of critics of the term 'Reconquista', such as Martín Ríos Saloma?",
    ["That it is a 19th-century nationalist construction", "That Christian kings seldom fought Muslim rulers", "That the idea goes back to 9th-century Asturian texts", "That Franco's historians coined it in the 1930s"], 0,
    "Critics such as Alejandro García-Sanjuán and Martín Ríos Saloma call it a 19th-century nationalist construction that peaked under Franco.",
    {1: "A Christian coalition broke the Almohads at Las Navas de Tolosa in 1212; the dispute is about the label.", 2: "That is the defenders' point, made by Carlos de Ayala and Francisco García Fitz.", 3: "Critics call it a 19th-century construction; it peaked under Franco, but did not begin with him."}),
  q("How does the historical Cid relate to the Cantar de mio Cid?",
    ["A real lord took Valencia; his epic was written later", "He was invented by the poet Per Abad in 1207", "A companion wrote the poem just after his death in 1099", "He was a real lord who held Valencia for the Almoravids"], 0,
    "Rodrigo Díaz took Valencia in 1094 and held it until his death in 1099; the poem survives in one manuscript copied from an exemplar of 1207, and scholars date its composition to the mid-12th or early 13th century.",
    {1: "Rodrigo Díaz was a real Castilian lord; Per Abad made the exemplar from which the surviving copy was made.", 2: "Scholars date the poem to the mid-12th or early 13th century.", 3: "He took Valencia in 1094 and held it himself, carving out a principality, until his death."})]}

PAGES = [P0, P1, P2, P3]
