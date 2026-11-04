# Chapter 11, pages 11.8 to 11.11. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 11.8
 'brit-crusades': ("Encyclopaedia Britannica, \"Crusades\"", "https://www.britannica.com/event/Crusades"),
 'fordham-urban': ("Fordham Medieval Sourcebook, \"Urban II: speech at Clermont, five versions\"", "https://sourcebooks.web.fordham.edu/source/urban2-5vers.asp"),
 'nyrb-tyerman': ("New York Review of Books, \"The holy terror\" (2006), review of Christopher Tyerman, God's War", "https://www.nybooks.com/articles/2006/10/19/the-holy-terror/"),
 'brit-hattin': ("Encyclopaedia Britannica, \"Battle of Hattin\"", "https://www.britannica.com/event/Battle-of-Hattin"),
 'brit-crusade4': ("Encyclopaedia Britannica, \"Fourth Crusade\"", "https://www.britannica.com/event/Fourth-Crusade"),
 'brit-latin-empire': ("Encyclopaedia Britannica, \"Latin Empire of Constantinople\"", "https://www.britannica.com/place/Latin-Empire-of-Constantinople"),
 'throop2018': ("Susanna Throop, \"'Not cruelty but piety'\" (2018), on definitions of crusading", "https://core.ac.uk/download/214259421.pdf"),
 'ihr-ocallaghan': ("Institute of Historical Research, Reviews in History 344: Joseph O'Callaghan, Reconquest and Crusade in Medieval Spain", "https://reviews.history.ac.uk/review/344"),
 'routledge-hillenbrand': ("Routledge, Carole Hillenbrand, The Crusades: Islamic Perspectives", "https://www.routledge.com/The-Crusades-Islamic-Perspectives/Hillenbrand/p/book/9781579582104"),
 # 11.9
 'medslavery-bakri': ("Medieval Slavery project, \"Source: al-Bakri, The Book of Highways and Kingdoms\"", "https://medievalslavery.org/?p=2822"),
 'jjay-bakri': ("Al-Bakri on Ghana, tr. J. F. P. Hopkins in Levtzion and Hopkins, Corpus of Early Arabic Sources (1981), excerpt at John Jay College", "https://jjcweb.jjay.cuny.edu/history/worldspring09/paperdemo/albakri.html"),
 'bu-ghana': ("Boston University African Studies Center, \"Kingdom of Ghana\" (with al-Bakri's text)", "https://www.bu.edu/africa/outreach/teachingresources/history/ancient-to-medieval-history/k_o_ghana"),
 'met-transsaharan': ("The Met, \"The trans-Saharan gold trade (7th-14th century)\"", "https://www.metmuseum.org/essays/the-trans-saharan-gold-trade-7th-14th-century"),
 'brit-kanem': ("Encyclopaedia Britannica (student edition), \"Kanem-Bornu\"", "https://kids.britannica.com/students/article/Kanem-Bornu/327929"),
 'unesco-kilwa': ("UNESCO World Heritage Centre, \"Ruins of Kilwa Kisiwani and Ruins of Songo Mnara\"", "https://whc.unesco.org/en/list/144/"),
 'harvard-swahili': ("Harvard University release on Brielle et al., ancient DNA of the Swahili coast, Nature (2023), via Newswise", "https://www.newswise.com/articles/ancient-dna-reveals-asian-ancestry-introduced-to-east-africa-in-early-modern-times"),
 'unesco-mapungubwe': ("UNESCO World Heritage Centre, \"Mapungubwe Cultural Landscape\"", "https://whc.unesco.org/en/list/1099/"),
 'unesco-zimbabwe': ("UNESCO World Heritage Centre, \"Great Zimbabwe National Monument\"", "https://whc.unesco.org/en/list/364/"),
 'unesco-lalibela': ("UNESCO World Heritage Centre, \"Rock-Hewn Churches, Lalibela\"", "https://whc.unesco.org/en/list/18/"),
 'cam-genizah-news': ("University of Cambridge, on the Ben Ezra Synagogue genizah fragments", "https://cam.ac.uk/node/25881"),
 'ucp-goitein': ("University of California Press, S. D. Goitein, A Mediterranean Society", "https://www.ucpress.edu/books/a-mediterranean-society-volume-iii/paper"),
 # 11.10
 'unesco-chola': ("UNESCO World Heritage Centre, \"Great Living Chola Temples\"", "https://whc.unesco.org/en/list/250/"),
 'kulke-chola': ("Hermann Kulke, \"The naval expeditions of the Cholas in the context of Asian history\", in Nagapattinam to Suvarnadwipa (ISEAS), abstract", "https://www.cambridge.org/core/product/identifier/CBO9789812309389A012/type/BOOK_PART"),
 'brit-srivijaya': ("Encyclopaedia Britannica, \"Srivijaya empire\"", "https://www.britannica.com/place/Srivijaya-empire"),
 'unesco-borobudur': ("UNESCO World Heritage Centre, \"Borobudur Temple Compounds\"", "https://whc.unesco.org/en/list/592/"),
 'brit-angkorwat': ("Encyclopaedia Britannica, \"Angkor Wat\"", "https://www.britannica.com/topic/Angkor-Wat"),
 'evans2015': ("Evans and Fletcher, \"The landscape of Angkor Wat redefined\", Antiquity 89 (2015)", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0003598X1500157X"),
 'klassen2021': ("Klassen et al., \"Diachronic modeling of the population within the medieval Greater Angkor Region\", Science Advances (2021)", "https://angkordatabase.asia/publications/diachronic-modeling-of-the-population-within-the-medieval-greater-angkor-region-settlement-complex"),
 'brit-mahmud': ("Encyclopaedia Britannica (student edition), \"Mahmud of Ghazna\"", "https://kids.britannica.com/students/article/Mahmud-of-Ghazna/275618"),
 'eaton-temples': ("Richard M. Eaton, \"Temple desecration and Indo-Muslim states\"", "https://mail.franpritchett.com/00islamlinks/txt_eaton_temples1.pdf"),
 'diplomat-eaton': ("The Diplomat, \"Richard Eaton on the desecration of Hindu temples in India\" (January 2024)", "https://thediplomat.com/2024/01/richard-eaton-on-the-desecration-of-hindu-temples-in-india"),
 'verso-thapar': ("Romila Thapar, Somanatha: The Many Voices of a History (Verso), publisher's description", "https://bookwire.bowker.com/book/USA/Somanatha-9781784780654-Romila-Thapar-51419953"),
 'pmindia-somnath': ("Prime Minister of India, address at the Somnath Swabhiman Parv (11 January 2026)", "https://www.pmindia.gov.in/?p=16769307"),
 'brit-delhi-sultanate': ("Encyclopaedia Britannica, \"Delhi sultanate\"", "https://www.britannica.com/place/Delhi-sultanate"),
 # 11.11
 'unesco-cahokia': ("UNESCO World Heritage Centre, \"Cahokia Mounds State Historic Site\"", "https://whc.unesco.org/en/list/198/"),
 'white2019': ("White et al., \"Fecal stanols show simultaneous flooding and seasonal precipitation change correlate with Cahokia's population decline\", PNAS (2019), record", "https://experts.umn.edu/en/publications/fecal-stanols-show-simultaneous-flooding-and-seasonal-precipitati/"),
 'hd-cahokia2024': ("HeritageDaily, on Rankin and Mueller, The Holocene (2024): no drought signal at Cahokia", "https://www.heritagedaily.com/2024/07/study-challenges-the-narrative-of-cahokias-abandonment/152521"),
 'unesco-chaco': ("UNESCO World Heritage Centre, \"Chaco Culture\"", "https://whc.unesco.org/en/list/353/"),
 'evans2018': ("Evans et al., \"Quantification of drought during the collapse of the classic Maya civilization\", Science 361 (2018), St Andrews repository", "https://research-repository.st-andrews.ac.uk/handle/10023/16993"),
 'cam-maya2025': ("University of Cambridge, \"Mexico cave reveals Maya droughts\" (2025)", "https://www.cam.ac.uk/stories/mexico-cave-maya-drought"),
 'unesco-chichen': ("UNESCO World Heritage Centre, \"Pre-Hispanic City of Chichen-Itza\"", "https://whc.unesco.org/en/list/483/"),
 'brit-postclassic': ("Encyclopaedia Britannica, \"Pre-Columbian civilizations: archaeological remains of Postclassic civilization\"", "https://www.britannica.com/topic/pre-Columbian-civilizations/Archaeological-remains-of-Postclassic-civilization"),
 'wilmshurst2011': ("Wilmshurst, Hunt, Lipo and Anderson, \"High-precision radiocarbon dating shows recent and rapid initial human colonization of East Polynesia\", PNAS 108 (2011), record", "https://experts.arizona.edu/en/publications/high-precision-radiocarbon-dating-shows-recent-and-rapid-initial-/"),
 'landcare-nz': ("Manaaki Whenua Landcare Research, \"Human arrival\" in New Zealand", "https://oldwww.landcareresearch.co.nz/science/plants-animals-fungi/ecosystems/prehistoric-settlement/human-arrival"),
 'sciam-rapanui': ("Scientific American, \"Rethinking Easter Island's historic 'collapse'\"", "https://www.scientificamerican.com/article/rethinking-easter-islands-historic-collapse/"),
 'davis2024': ("Davis et al., on Rapa Nui's rock gardens, Science Advances (2024), record", "https://experts.arizona.edu/en/publications/island-wide-characterization-of-agricultural-production-challenge/"),
 'ku-rapanui2024': ("University of Copenhagen, \"Easter Island population collapse never happened\" (2024), on Moreno-Mayar et al., Nature", "https://archaeology.ku.dk/news/easter-island-population-collapse-never-happened/"),
}

C = {
 # 11.8
 'c-clermont': c("Pope Urban II called a council at Clermont in November 1095 and summoned western knights to help the Christians of the East; those who went were promised remission of their sins.", 'consensus', ['brit-crusades', 'fordham-urban'], show=False),
 'c-urban-sources': c("The council's official record is lost; Urban's speech survives in several differing accounts, most by men who said they were present.", 'consensus', ['fordham-urban'], show=False),
 'c-rhineland': c("In 1096 crusading bands attacked the Jewish communities of the Rhineland, at Speyer, Worms, Mainz and Cologne; forced to convert or die, many Jews chose death.", 'consensus', ['brit-crusades'], show=False),
 'c-jerusalem1099': c("The crusaders took Jerusalem in July 1099, and Muslims and Jews were killed in the slaughter that followed.", 'debated', ['brit-crusades', 'nyrb-tyerman'], "That a massacre happened is agreed; Christopher Tyerman argues contemporary chroniclers exaggerated its scale."),
 'c-crusader-states': c("The crusaders founded four states: the county of Edessa, the principality of Antioch, the county of Tripoli and the kingdom of Jerusalem; Edessa fell in 1144.", 'consensus', ['brit-crusades'], show=False),
 'c-hattin': c("Saladin destroyed the army of the kingdom of Jerusalem at Hattin on 4 July 1187 and took Jerusalem that October.", 'consensus', ['brit-hattin'], show=False),
 'c-saladin': c("Saladin was long admired in Europe for his valour and generosity.", 'debated', ['nyrb-tyerman'], "Tyerman sees a 'shrewd politician whose generosity, like his occasional savagery, was carefully calculated'."),
 'c-1204': c("The Fourth Crusade, unable to pay Venice for its ships, was diverted to Zara and then to Constantinople, which it captured and sacked in 1204; the Latin empire it founded lasted until the Byzantines retook the city in 1261.", 'consensus', ['brit-crusade4', 'brit-latin-empire'], show=False),
 'c-1204-judgement': c("How to judge the sack of 1204 divides historians.", 'debated', ['nyrb-tyerman'], "Steven Runciman wrote that there was never 'a greater crime against humanity than the Fourth Crusade'; Christopher Tyerman calls it, by the standards of the time, 'an atrocity, but not a war-crime'."),
 'c-pluralist': c("Most historians now follow Jonathan Riley-Smith's 'pluralist' definition: crusades were marked by papal authorisation, vows and the remission of sins, and included campaigns in Spain, the Baltic and against heretics, not only those to Jerusalem.", 'debated', ['throop2018'], "Throop lists papal authorisation alongside vows and the remission of sins as marks of a crusade, and notes that 'even the pluralist position is admittedly imperfect'."),
 'c-crusade-view': c("Historians' overall judgement has shifted.", 'debated', ['nyrb-tyerman'], "Steven Runciman (1950s) concluded that the Holy War was 'a long act of intolerance in the name of God'; Riley-Smith's generation challenged stereotypes of crusaders as uniformly brutal and greedy, stressing religious motives."),
 'c-spain-crusade': c("Joseph O'Callaghan argues that the papacy turned the Iberian wars into crusades, with the same spiritual rewards as the expeditions to Jerusalem.", 'debated', ['ihr-ocallaghan'], "His reviewer wanted more of the papal documents quoted; see 11.3 on the debate over 'Reconquista'."),
 'c-hillenbrand': c("Carole Hillenbrand's The Crusades: Islamic Perspectives studies how Muslims experienced and answered the invaders, and how jihad was revived against them.", 'consensus', ['routledge-hillenbrand'], show=False),
 # 11.9
 'c-bakri-method': c("Al-Bakri wrote his account of West Africa in 1068 in al-Andalus, from other people's reports; he never travelled there.", 'consensus', ['medslavery-bakri', 'brit-bakri'], show=False),
 'c-ghana-towns': c("He describes the city of Ghana as two towns on a plain, a merchants' town with twelve mosques and the king's town six miles away.", 'tradition', ['jjay-bakri'], "This is what his text says, in J. F. P. Hopkins's translation."),
 'c-ghana-gold': c("According to al-Bakri, the king levied 'one golden dinar' on every donkey-load of salt brought into the country and kept all gold nuggets for himself, leaving only gold dust to the people.", 'tradition', ['bu-ghana', 'jjay-bakri'], "The text's description; no Ghanaian record survives to check it."),
 'c-gold-trade': c("Gold from the western and central Sudan was the main commodity of the trans-Saharan trade, and the trade encouraged further conversion of the Berbers to Islam.", 'consensus', ['met-transsaharan'], show=False),
 'c-kanem': c("Around the 9th century the kingdom of Kanem formed north-east of Lake Chad; its ruler became a Muslim in the late 11th century.", 'approx', ['brit-kanem'], "Dates are approximate."),
 'c-kilwa': c("From the 13th century the merchants of Kilwa, on the coast of today's Tanzania, traded in gold, silver, pearls and perfumes, and controlled Indian Ocean trade with Arabia, India and China; its Great Mosque is the oldest standing mosque on the East African coast.", 'consensus', ['unesco-kilwa'], show=False),
 'c-swahili-dna': c("Ancient DNA published in 2023 shows that from about 1000 CE, migrants from Southwest Asia contributed close to half of the ancestry of the people studied on the Swahili coast, at first mostly Persian men who had children with African women, while the language and culture stayed African and Bantu.", 'debated', ['harvard-swahili'], "The genetics are new; how they relate to the Swahili 'Shirazi' traditions of Persian ancestry is debated. Known here through Harvard's summary of the Nature paper."),
 'c-mapungubwe': c("Mapungubwe, in today's South Africa, controlled trade in gold and ivory to the Indian Ocean between about 900 and 1300; its power then shifted north to Great Zimbabwe.", 'approx', ['unesco-mapungubwe'], "UNESCO gives both the end of the 13th and the 14th century for its abandonment."),
 'c-great-zimbabwe': c("Great Zimbabwe, built by ancestors of the Shona between the 11th and 15th centuries, has yielded glass beads and porcelain from China and Persia and coins from Kilwa.", 'approx', ['unesco-zimbabwe'], "On its later growth, see 12.8."),
 'c-lalibela': c("At Lalibela in Ethiopia, eleven churches were carved out of solid rock in the 12th and 13th centuries; tradition says King Lalibela meant them as a 'New Jerusalem'.", 'tradition', ['unesco-lalibela'], "The churches are real; the king's purpose comes from tradition."),
 'c-genizah2': c("The Ben Ezra Synagogue's genizah preserved butchers' bills, marriage contracts, private letters and IOUs, because writings that might contain the name of God could not be thrown away; S. D. Goitein rebuilt from them the Jewish trading world of the 10th to 13th centuries.", 'consensus', ['cam-genizah-news', 'ucp-goitein'], show=False),
 # 11.10
 'c-chola-temples': c("The Chola king Rajaraja I consecrated the great Brihadisvara temple at Thanjavur in 1009-1010; his son Rajendra I completed another at Gangaikondacholapuram in 1035. Both are still places of worship.", 'consensus', ['unesco-chola'], show=False),
 'c-chola-raid': c("In 1025 a Chola fleet raided the ports of Srivijaya across the Bay of Bengal and captured its king.", 'consensus', ['kulke-chola', 'brit-srivijaya'], show=False),
 'c-chola-why': c("Why the Cholas launched the raid is, in Hermann Kulke's words, 'still a moot point'.", 'debated', ['kulke-chola'], "K. A. Nilakanta Sastri thought Srivijaya obstructed Chola trade with China; George Spencer saw a 'politics of plunder'; Tansen Sen does not rule out a 'trade war'."),
 'c-srivijaya': c("Srivijaya, based at Palembang on Sumatra, controlled the Strait of Malacca from the 7th to the 13th century and was a centre of Mahayana Buddhism.", 'consensus', ['brit-srivijaya'], show=False),
 'c-borobudur': c("Borobudur in Java, one of the greatest Buddhist monuments in the world, was built under the Sailendra (Syailendra) dynasty in the 8th and 9th centuries and rediscovered in the 19th.", 'consensus', ['unesco-borobudur'], show=False),
 'c-angkorwat': c("Angkor Wat was built in the 12th century by King Suryavarman II and dedicated to Vishnu; it later became a Buddhist shrine.", 'consensus', ['brit-angkorwat'], show=False),
 'c-angkor-pop': c("Airborne laser scanning (lidar) has revealed Angkor as a vast, low-density urban landscape; one model puts the population of Greater Angkor at 700,000 to 900,000 in the 13th century.", 'approx', ['evans2015', 'klassen2021'], "A model-based estimate from mapped settlement."),
 'c-mahmud': c("Mahmud of Ghazni (971-1030) led some 17 raids into India; his raid on the temple of Somnath in 1026 brought, by one count, twenty million dinars in plunder.", 'approx', ['brit-mahmud', 'eaton-temples'], "The plunder figure is Eaton's, following C. E. Bosworth."),
 'c-mahmud-why': c("Why Mahmud raided temples is debated.", 'debated', ['eaton-temples', 'diplomat-eaton', 'verso-thapar'], "Medieval Persian chronicles celebrated the raids as victories for Islam; Richard Eaton argues that temple desecration in India was mainly political and economic, aimed at royal temples as symbols of enemy kings."),
 'c-somnath-memory': c("How Somnath has been remembered is itself history: Romila Thapar argues the raid was first presented as a lasting Hindu trauma in Britain's House of Commons, and in January 2026 India's government marked its thousandth anniversary.", 'debated', ['verso-thapar', 'pmindia-somnath'], "The publisher describes her findings as contesting 'Hindu religious nationalism'; the 2026 commemoration presented the temple's survival over a thousand years as a national symbol."),
 'c-delhi': c("The Delhi Sultanate grew out of Ghurid campaigns into north India between 1175 and 1206; Sultan Iltutmish (1211-36) made Delhi his permanent capital.", 'consensus', ['brit-delhi-sultanate'], show=False),
 # 11.11
 'c-cahokia': c("Cahokia, near today's St Louis, was the largest settlement north of Mexico before Columbus, with perhaps 10,000-20,000 people at its height around 1050-1150.", 'approx', ['unesco-cahokia'], "Population estimates vary."),
 'c-cahokia-decline': c("Why Cahokia declined after about 1150 is debated.", 'debated', ['white2019', 'hd-cahokia2024'], "A 2019 study links its decline to flooding and summer droughts; a 2024 study by Caitlin Rankin and Natalie Mueller found no drought signal in the soils and suggests people dispersed gradually."),
 'c-chaco': c("Chaco Canyon in New Mexico was a major centre of Ancestral Pueblo culture between 850 and 1250, linked to outlying 'great houses' by engineered roads.", 'consensus', ['unesco-chaco'], show=False),
 'c-maya-drought': c("Lake sediments show that during the Classic Maya collapse, annual rainfall in the northern lowlands fell by 41-54 percent, at times by up to 70 percent.", 'debated', ['evans2018'], "The drought is measured; how far it caused the collapse, alongside war and political change, is debated."),
 'c-maya-2025': c("A 2025 study of a Yucatán stalagmite found eight droughts lasting three years or more between 871 and 1021, the longest 13 years.", 'approx', ['cam-maya2025'], "New. The authors caution that this 'doesn't necessarily mean' Chichen Itza was abandoned during them."),
 'c-chichen': c("Chichen Itza is the most important archaeological site of the Maya-Toltec civilisation in Yucatán (10th-15th centuries).", 'consensus', ['unesco-chichen'], show=False),
 'c-tula': c("Tula in central Mexico, the Toltec capital, grew rapidly between about 900 and 1200; Britannica calls the resemblance between it and Chichen Itza 'extraordinarily close'.", 'debated', ['brit-postclassic'], "Which city influenced which is debated."),
 'c-polynesia': c("High-precision radiocarbon dating shows East Polynesia was settled late and fast: the Society Islands about 1025-1120, and the remaining islands, including Rapa Nui and Aotearoa New Zealand, in one pulse about 1190-1290.", 'approx', ['wilmshurst2011'], "Based on 1,434 radiocarbon dates; earlier chronologies were up to several centuries older."),
 'c-nz': c("The earliest evidence of people in Aotearoa New Zealand dates to about 1280-1300, from rat-gnawed seeds and re-dated rat bones.", 'approx', ['landcare-nz'], "Calibrated radiocarbon dates."),
 'c-rapanui': c("The story that Rapa Nui's people destroyed their own environment and society has been strongly challenged.", 'debated', ['sciam-rapanui', 'davis2024', 'ku-rapanui2024'], "Jared Diamond popularised the 'collapse'; 2024 studies found far less farmland than once claimed and ancient genomes showing a population that grew steadily until European contact. Not all specialists accept the revision: Jo Anne Van Tilburg calls the collapse narrative the revisionists attack 'a straw man'."),
}

# ---------------------------------------------------------------- 11.8
P8 = {
 'title': "The Crusades", 'sub': "1095 to 1204",
 'lede': "In 1095 a pope called on western knights to march to the East. Over the next two centuries crusading armies took and lost Jerusalem, massacred Jews and Muslims, built states in Syria and Palestine, and sacked Constantinople, the Byzantine capital. Few subjects in medieval history are judged so differently.",
 'body': [
  "At Clermont in 1095 Urban II summoned knights to help the Christians of the East, promising them remission of their sins; [[c-clermont]] what exactly he said is uncertain, since only differing accounts survive. [[c-urban-sources]] The first victims were Jews in the Rhineland. [[c-rhineland]] In 1099 the crusaders took Jerusalem amid great killing, [[c-jerusalem1099]] and founded four states along the eastern Mediterranean. [[c-crusader-states]]",
  "Muslim leaders revived the idea of jihad against the invaders. [[c-hillenbrand]] In 1187 Saladin destroyed the kingdom's army at Hattin and retook Jerusalem; [[c-hattin]] his reputation for generosity is now judged more coolly. [[c-saladin]] In 1204 the Fourth Crusade, deep in debt to Venice, turned on Constantinople instead and sacked it, [[c-1204]] an act still judged harshly. [[c-1204-judgement]]",
  "What counts as a crusade? Most historians now include papally authorised wars in Spain and the Baltic as well as in the East, [[c-pluralist]] [[c-spain-crusade]] and the overall verdict has moved from Steven Runciman's condemnation to a closer study of crusaders' own religious motives. [[c-crusade-view]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["1095", "Council of Clermont"],
    ["1096", "massacres of Rhineland Jews"],
    ["1099", "Jerusalem taken"],
    ["1144", "Edessa falls"],
    ["1187", "Hattin; Saladin retakes Jerusalem"],
    ["1204", "Fourth Crusade sacks Constantinople"],
    ["1261", "Byzantines retake Constantinople"]], 'note': "[[c-clermont]] [[c-rhineland]] [[c-jerusalem1099]] [[c-crusader-states]] [[c-hattin]] [[c-1204]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 21.0, 'lat': 40.0, 'zoom': 7.5}, 'caption': "The Crusades, 1095-1204", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [40.3, 35.3], 'label': 'CRUSADER STATES', 'size': 8}, {'ll': [31.0, 39.5], 'label': 'SELJUK ANATOLIA', 'size': 9}, {'ll': [8.0, 47.5], 'label': 'LATIN CHRISTENDOM', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [3.0867, 45.7794], 'label': 'Clermont', 'date': '1095', 'acc': True, 'big': True, 'anchor': 'end', 'plate': {'kicker': '11.8 · the call', 'title': 'Clermont', 'sub': 'November 1095', 'text': "[[c-clermont]] [[c-urban-sources]]", 'sources': ['brit-crusades', 'fordham-urban']}},
    {'ll': [8.28, 49.9817], 'label': 'Mainz', 'date': 'Jews massacred, 1096', 'acc': True, 'dy': -8, 'plate': {'kicker': '11.8 · 1096', 'title': 'The Rhineland massacres', 'sub': '1096', 'text': "[[c-rhineland]]", 'sources': ['brit-crusades']}},
    {'ll': [28.9494, 41.0136], 'label': 'Constantinople', 'date': 'sacked 1204', 'acc': True, 'big': True, 'dy': -10, 'plate': {'kicker': '11.8 · 1204', 'title': 'The Fourth Crusade', 'sub': '1204', 'text': "[[c-1204]] [[c-1204-judgement]]", 'sources': ['brit-crusade4', 'brit-latin-empire', 'nyrb-tyerman']}},
    {'ll': [36.1572, 36.2064], 'label': 'Antioch', 'anchor': 'end', 'dy': -6},
    {'ll': [38.7939, 37.1669], 'label': 'Edessa', 'date': 'falls 1144', 'dy': -8},
    {'ll': [35.8439, 34.4333], 'label': 'Tripoli', 'anchor': 'end', 'dy': 4},
    {'ll': [35.4586, 32.7975], 'label': 'Hattin', 'date': '1187', 'acc': True, 'dy': 4, 'plate': {'kicker': '11.8 · Saladin', 'title': 'Hattin', 'sub': '4 July 1187', 'text': "[[c-hattin]] [[c-saladin]] [[c-hillenbrand]]", 'sources': ['brit-hattin', 'nyrb-tyerman', 'routledge-hillenbrand']}},
    {'ll': [35.2167, 31.7833], 'label': 'Jerusalem', 'date': '1099; 1187', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.8 · Jerusalem', 'title': 'Jerusalem', 'sub': '1099 and 1187', 'text': "[[c-jerusalem1099]] [[c-crusader-states]]", 'sources': ['brit-crusades', 'nyrb-tyerman']}}]}]},
 'practice': [
  q("Why do historians treat any single text of Urban II's speech at Clermont with caution?",
    ["The official record is lost, and the accounts differ", "The official record survives but contradicts itself", "Its accounts come from writers who were not present", "It survives in one late copy, made after the crusade"], 0,
    "The council's official record is lost; the speech survives in several differing accounts, most by men who said they were present.",
    {1: "The official record has not survived.", 2: "Most of the accounts are by men who said they were present.", 3: "It survives in several differing accounts, not a single copy."}),
  q("What does Jonathan Riley-Smith's 'pluralist' definition of crusading include that a Jerusalem-only definition does not?",
    ["Papally authorised wars in Spain, the Baltic and on heretics", "Any war fought by Christian kings against non-Christians", "The armed pilgrimages to Jerusalem from 1095 onward", "Wars that won their goal, whoever authorised them"], 0,
    "Papal authorisation, vows and the remission of sins mark a crusade, wherever it went, so campaigns in Spain, the Baltic and against heretics count.",
    {1: "Papal authorisation is one of the marks of a crusade; a war without it does not qualify.", 2: "Expeditions to Jerusalem count under both definitions.", 3: "The marks are papal authorisation, vows and the remission of sins, not success."})]}

# ---------------------------------------------------------------- 11.9
P9 = {
 'title': "Africa's trade webs", 'sub': "c. 800 to 1250",
 'lede': "Gold from West Africa crossed the Sahara to Mediterranean markets, ivory and gold from the south flowed to Indian Ocean ports, and Ethiopian Christians carved churches out of rock. Arabic writers, archaeology and now ancient DNA let us see these African worlds in more detail than ever.",
 'body': [
  "Gold from south of the Sahara was the main cargo of the camel caravans across the desert, and the trade encouraged the Berbers' conversion to Islam. [[c-gold-trade]] A detailed early description of the kingdom of Ghana comes from al-Bakri, who never went there, [[c-bakri-method]] and who describes a capital of two towns, one for Muslim merchants and one for the king, [[c-ghana-towns]] and a king who taxed salt in gold. [[c-ghana-gold]] Further east, the kingdom of Kanem took shape by Lake Chad. [[c-kanem]]",
  "On the east coast, Swahili towns such as Kilwa traded with Arabia, India and China. [[c-kilwa]] Ancient DNA from burials on this coast shows that close to half the ancestry of the people studied came from Asian migrants, at first mostly Persian men who had children with African women, while their language stayed African. [[c-swahili-dna]] Inland, Mapungubwe controlled the gold and ivory trade, [[c-mapungubwe]] before power moved north to Great Zimbabwe. [[c-great-zimbabwe]] In the Ethiopian highlands, Christian kings carved churches from the living rock at Lalibela. [[c-lalibela]]",
  "In Fatimid Cairo, a synagogue storeroom preserved the everyday papers of a Jewish community, from which S. D. Goitein rebuilt the Mediterranean world of the 10th to 13th centuries. [[c-genizah2]]",
  {'table': {'head': ["Place", "Region", "Known for"], 'rows': [
    ["Ghana", "West African Sahel", "gold, salt taxes; al-Bakri's account (1068)"],
    ["Kanem", "Lake Chad", "Muslim ruler from the late 11th century"],
    ["Kilwa", "Swahili coast", "Indian Ocean trade; oldest standing mosque on the coast"],
    ["Mapungubwe", "Limpopo valley", "gold and ivory trade, c. 900-1300"],
    ["Lalibela", "Ethiopian highlands", "eleven rock-cut churches"],
    ["Fustat (Cairo)", "Egypt", "the Genizah: merchants' letters"]], 'note': "[[c-bakri-method]] [[c-kanem]] [[c-kilwa]] [[c-mapungubwe]] [[c-lalibela]] [[c-genizah2]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 15.0, 'lat': 6.0, 'zoom': 3.8}, 'caption': "Africa's trade webs, c. 800-1250", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [2.0, 23.0], 'label': 'SAHARA', 'size': 11}, {'ll': [28.0, -12.0], 'label': 'BANTU AFRICA', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [-4.28, 31.28], 'label': 'Sijilmasa', 'date': 'caravan terminus', 'anchor': 'end', 'dy': -6},
    {'ll': [-10.4058, 17.4233], 'label': 'Awdaghust', 'anchor': 'end', 'dy': -6},
    {'ll': [-7.9767, 15.7667], 'label': 'Ghana', 'date': 'capital; site approximate', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '11.9 · Ghana', 'title': 'Ghana', 'sub': 'al-Bakri, 1068', 'text': "[[c-bakri-method]] [[c-ghana-towns]] [[c-ghana-gold]] [[c-gold-trade]]", 'sources': ['medslavery-bakri', 'jjay-bakri', 'bu-ghana', 'met-transsaharan']}},
    {'ll': [14.4539, 13.1242], 'label': 'Lake Chad', 'date': 'Kanem', 'acc': True, 'dy': 16, 'plate': {'kicker': '11.9 · Kanem', 'title': 'Kanem', 'sub': 'from c. 9th century', 'text': "[[c-kanem]]", 'sources': ['brit-kanem']}},
    {'ll': [31.2308, 30.0056], 'label': 'Fustat', 'date': 'the Genizah', 'acc': True, 'dy': -8, 'plate': {'kicker': '11.9 · Cairo', 'title': 'The Genizah', 'sub': '10th-13th centuries', 'text': "[[c-genizah2]]", 'sources': ['cam-genizah-news', 'ucp-goitein']}},
    {'ll': [39.0475, 12.0319], 'label': 'Lalibela', 'date': 'rock churches', 'acc': True, 'dy': -8, 'plate': {'kicker': '11.9 · Ethiopia', 'title': 'Lalibela', 'sub': '12th-13th centuries', 'text': "[[c-lalibela]]", 'sources': ['unesco-lalibela']}},
    {'ll': [39.4981, -8.9589], 'label': 'Kilwa', 'date': 'Swahili port', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '11.9 · Swahili coast', 'title': 'Kilwa', 'sub': '13th century onward', 'text': "[[c-kilwa]] [[c-swahili-dna]]", 'sources': ['unesco-kilwa', 'harvard-swahili']}},
    {'ll': [30.9344, -20.2731], 'label': 'Great Zimbabwe', 'acc': True, 'dy': -8, 'plate': {'kicker': '11.9 · the south', 'title': 'Mapungubwe and Great Zimbabwe', 'sub': 'c. 900-1450', 'text': "[[c-mapungubwe]] [[c-great-zimbabwe]]", 'sources': ['unesco-mapungubwe', 'unesco-zimbabwe']}},
    {'ll': [29.3725, -22.2069], 'label': 'Mapungubwe', 'date': 'c. 900-1300', 'acc': True, 'anchor': 'end', 'dy': 16}]}]},
 'practice': [
  q("Al-Bakri's account of Ghana is valuable but must be used with care. Why?",
    ["He wrote in al-Andalus from reports, never visiting Ghana", "He was a court official writing propaganda for Ghana's king", "He saw Ghana on one brief visit, years after its fall", "It describes a Ghana that had already vanished by 1068"], 0,
    "He wrote in 1068 in al-Andalus, from other people's reports: a second-hand account is still precious, but second-hand.",
    {1: "He wrote in al-Andalus, far from Ghana's court.", 2: "He never travelled to West Africa.", 3: "He describes a working kingdom whose king taxed every load of salt."}),
  q("What did the 2023 ancient-DNA study of the Swahili coast show?",
    ["Ancestry was mixed, but the culture stayed African", "Arab colonists replaced the local people of the coast", "Asian ancestry came with the Portuguese, not before", "The first migrants were mostly Indian women, not Persian men"], 0,
    "From about 1000 CE migrants from Southwest Asia, at first mostly Persian men who had children with African women, contributed close to half the ancestry of the people studied, while the language and culture stayed African and Bantu.",
    {1: "The ancestry was mixed, and the language and culture stayed African.", 2: "Asian ancestry arrived from about 1000 CE.", 3: "The early migrants were mostly Persian men who had children with African women."})]}

# ---------------------------------------------------------------- 11.10
P10 = {
 'title': "India and Southeast Asia", 'sub': "temples, fleets and raiders, c. 800-1250",
 'lede': "South India's Chola kings built great temples and sent a fleet across the Bay of Bengal. In Southeast Asia, Indian religions inspired the monuments of Borobudur and Angkor Wat. In the north-west, raids from Afghanistan were followed by Ghurid conquests that created the Delhi Sultanate, and how one of the raids is remembered is still a live political issue.",
 'body': [
  "The Cholas of Tamil Nadu built great temples at Thanjavur and Gangaikondacholapuram, still in worship today, [[c-chola-temples]] and in 1025 their navy struck Srivijaya, [[c-chola-raid]] the Buddhist trading power that controlled the Strait of Malacca. [[c-srivijaya]] Why they did it is unclear. [[c-chola-why]]",
  "In Java, the Sailendra kings built Borobudur, a Buddhist monument on a vast scale. [[c-borobudur]] In Cambodia, the Khmer king Suryavarman II built Angkor Wat for Vishnu, [[c-angkorwat]] at the heart of a sprawling, low-density city mapped by laser surveys; one model puts Greater Angkor's population at 700,000 to 900,000. [[c-angkor-pop]]",
  "From Afghanistan, Mahmud of Ghazni raided India repeatedly and in 1026 plundered the temple of Somnath. [[c-mahmud]] Historians disagree about his motives, [[c-mahmud-why]] and the memory of Somnath has become a national symbol, commemorated by India's government in 2026 and analysed by historians as a story built over centuries. [[c-somnath-memory]] By 1206 the Ghurid conquests had produced the Delhi Sultanate. [[c-delhi]]",
  {'table': {'head': ["Monument or event", "Where", "When"], 'rows': [
    ["Borobudur", "Java", "8th-9th centuries"],
    ["Brihadisvara temple", "Thanjavur", "1009-1010"],
    ["Chola raid on Srivijaya", "Sumatra and Malaya", "1025"],
    ["Somnath raided", "Gujarat", "1026"],
    ["Angkor Wat", "Cambodia", "12th century"],
    ["Delhi Sultanate founded", "north India", "c. 1206"]], 'note': "[[c-borobudur]] [[c-chola-temples]] [[c-chola-raid]] [[c-mahmud]] [[c-angkorwat]] [[c-delhi]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 88.0, 'lat': 14.0, 'zoom': 5.0}, 'caption': "India and Southeast Asia, c. 800-1250", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'arrow', 'items': [{'path': [[79.85, 10.8], [85.0, 8.0], [92.0, 6.5], [98.0, 4.5], [102.0, 1.0], [104.75, -2.92]], 'label': 'Chola fleet, 1025', 'lab': [92.0, 6.5], 'ldy': 18}]},
   {'type': 'region', 'items': [{'ll': [78.0, 22.0], 'label': 'INDIA', 'size': 11}, {'ll': [104.0, 15.5], 'label': 'KHMER', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [68.4208, 33.5539], 'label': 'Ghazni', 'date': "Mahmud's capital", 'anchor': 'end', 'dy': -6},
    {'ll': [70.4011, 20.8881], 'label': 'Somnath', 'date': '1026', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 4, 'plate': {'kicker': '11.10 · Somnath', 'title': 'Somnath', 'sub': '1026 and its memory', 'text': "[[c-mahmud]] [[c-mahmud-why]] [[c-somnath-memory]]", 'sources': ['brit-mahmud', 'eaton-temples', 'verso-thapar', 'pmindia-somnath']}},
    {'ll': [77.2, 28.5167], 'label': 'Delhi', 'date': 'sultanate from c. 1206', 'acc': True, 'dy': -8, 'plate': {'kicker': '11.10 · Delhi', 'title': 'The Delhi Sultanate', 'sub': '1206 onward', 'text': "[[c-delhi]]", 'sources': ['brit-delhi-sultanate']}},
    {'ll': [79.1319, 10.7829], 'label': 'Thanjavur', 'date': 'temple 1010', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.10 · the Cholas', 'title': 'The Chola temples', 'sub': '1010 and 1035', 'text': "[[c-chola-temples]] [[c-chola-raid]] [[c-chola-why]]", 'sources': ['unesco-chola', 'kulke-chola']}},
    {'ll': [104.7456, -2.9167], 'label': 'Palembang', 'date': 'Srivijaya', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.10 · Srivijaya', 'title': 'Srivijaya', 'sub': '7th-13th centuries', 'text': "[[c-srivijaya]] [[c-chola-raid]]", 'sources': ['brit-srivijaya']}},
    {'ll': [110.2039, -7.6078], 'label': 'Borobudur', 'date': '8th-9th c.', 'acc': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '11.10 · Java', 'title': 'Borobudur', 'sub': '8th-9th centuries', 'text': "[[c-borobudur]]", 'sources': ['unesco-borobudur']}},
    {'ll': [103.8664, 13.4122], 'label': 'Angkor', 'date': 'Angkor Wat, 12th c.', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '11.10 · Angkor', 'title': 'Angkor', 'sub': '12th-13th centuries', 'text': "[[c-angkorwat]] [[c-angkor-pop]]", 'sources': ['brit-angkorwat', 'evans2015', 'klassen2021']}}]}]},
 'practice': [
  q("What does the evidence say about why the Chola fleet raided Srivijaya in 1025?",
    ["Its motive is unclear; trade and plunder are both proposed", "Sastri proved Srivijaya was blocking Chola trade with China", "Chinese records show the Song court ordered the raid", "George Spencer showed it was a trade war, not plunder"], 0,
    "Hermann Kulke calls the motive 'still a moot point': Sastri thought Srivijaya obstructed Chola trade, Spencer saw a 'politics of plunder', and Tansen Sen does not rule out a 'trade war'.",
    {1: "Sastri suggested it; Kulke calls the question 'still a moot point'.", 2: "The explanations proposed are trade obstruction, plunder or a trade war, not a Chinese order.", 3: "Spencer saw a 'politics of plunder'; it is Tansen Sen who does not rule out a 'trade war'."}),
  q("Why does Romila Thapar's book on Somnath matter to debates about the 1026 raid?",
    ["It traces the 'trauma' story to Britain's House of Commons", "It argues the raid of 1026 is a later invention", "It shows Somnath was remembered as a trauma from 1026 on", "It is the official history used for the 2026 commemoration"], 0,
    "Thapar argues the raid was first presented as a lasting Hindu trauma in Britain's House of Commons: she studies how the event was remembered as well as the event itself.",
    {1: "Her argument concerns how the raid was remembered; the raid and its plunder are recorded.", 2: "She argues the 'trauma' framing first appeared much later, in Britain's House of Commons.", 3: "It is an independent study whose publisher describes it as contesting 'Hindu religious nationalism'."})]}

# ---------------------------------------------------------------- 11.11
P11 = {
 'title': "The Americas and the Pacific", 'sub': "c. 850 to 1300",
 'lede': "Beyond the reach of Eurasia's webs, the Americas had their own: great towns on the Mississippi and in the deserts of New Mexico, and Maya and Toltec cities in Mexico. In the Pacific, Polynesian navigators settled the remaining islands of East Polynesia, reaching Rapa Nui and New Zealand.",
 'body': [
  "Cahokia, on the Mississippi, was the largest town north of Mexico, [[c-cahokia]] and its decline after about 1150 is now debated. [[c-cahokia-decline]] In the deserts of New Mexico, Chaco Canyon was the centre of a network of 'great houses' linked by roads. [[c-chaco]]",
  "As the great Classic Maya cities declined, the lowlands suffered severe, repeated droughts, [[c-maya-drought]] some of which can now be dated year by year, though how far drought caused the collapse is debated. [[c-maya-2025]] In the north, Chichen Itza flourished, [[c-chichen]] its buildings closely resembling those of Tula in central Mexico. [[c-tula]]",
  "After the Society Islands, Polynesians settled all the remaining islands of East Polynesia in a single pulse of about a century, [[c-polynesia]] reaching Aotearoa New Zealand around 1280. [[c-nz]] Rapa Nui (Easter Island) was once held up as a warning of ecological self-destruction; new evidence suggests that story is wrong. [[c-rapanui]]",
  {'table': {'head': ["Place", "Region", "When"], 'rows': [
    ["Chaco Canyon", "New Mexico", "850-1250"],
    ["Tula", "central Mexico", "grew c. 900-1200"],
    ["Chichen Itza", "Yucatán", "10th-15th centuries"],
    ["Cahokia", "Mississippi valley", "peak c. 1050-1150"],
    ["Society Islands settled", "East Polynesia", "c. 1025-1120"],
    ["Rapa Nui and New Zealand settled", "East Polynesia", "c. 1190-1300"]], 'note': "[[c-chaco]] [[c-tula]] [[c-chichen]] [[c-cahokia]] [[c-polynesia]] [[c-nz]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "The Americas and the Pacific, 850-1300", 'title': "Selected centres and settlements, CE",
  'max': -840, 'min': -1310, 'unit': 'ka', 'ticks': [-850, -950, -1050, -1150, -1250], 'tickLabels': ['850', '950', '1050', '1150', '1250 CE'],
  'axis': "years CE; all dates approximate", 'hint': "Hover or click a row",
  'rows': [
   {'t': 'Chaco Canyon', 'sub': 'New Mexico', 'from': -850, 'to': -1250, 'lab': '850-1250', 'acc': True, 'plate': {'kicker': '11.11 · Chaco', 'title': 'Chaco Canyon', 'sub': '850-1250', 'text': "[[c-chaco]]", 'sources': ['unesco-chaco']}},
   {'t': 'Maya droughts', 'sub': 'Yucatán stalagmite', 'from': -871, 'to': -1021, 'lab': '871-1021', 'open': True, 'plate': {'kicker': '11.11 · the Maya', 'title': 'Maya droughts', 'sub': '9th-11th centuries', 'text': "[[c-maya-drought]] [[c-maya-2025]]", 'sources': ['evans2018', 'cam-maya2025']}},
   {'t': 'Tula grows', 'sub': 'Toltec capital', 'from': -900, 'to': -1200, 'lab': 'c. 900-1200', 'acc': True, 'plate': {'kicker': '11.11 · Mexico', 'title': 'Tula and Chichen Itza', 'sub': '10th-12th centuries', 'text': "[[c-tula]] [[c-chichen]]", 'sources': ['brit-postclassic', 'unesco-chichen']}},
   {'t': 'Cahokia at its peak', 'sub': 'Mississippi valley', 'from': -1050, 'to': -1150, 'lab': 'c. 1050-1150', 'acc': True, 'plate': {'kicker': '11.11 · Cahokia', 'title': 'Cahokia', 'sub': 'c. 1050-1150', 'text': "[[c-cahokia]] [[c-cahokia-decline]]", 'sources': ['unesco-cahokia', 'white2019', 'hd-cahokia2024']}},
   {'t': 'Society Islands settled', 'from': -1025, 'to': -1120, 'lab': 'c. 1025-1120', 'acc': True, 'plate': {'kicker': '11.11 · Polynesia', 'title': 'Settling East Polynesia', 'sub': 'c. 1025-1290', 'text': "[[c-polynesia]] [[c-rapanui]]", 'sources': ['wilmshurst2011', 'ku-rapanui2024']}},
   {'t': 'Rest of East Polynesia', 'sub': 'incl. Rapa Nui, New Zealand', 'from': -1190, 'to': -1290, 'lab': 'c. 1190-1290', 'acc': True},
   {'t': 'New Zealand: first evidence', 'from': -1280, 'to': -1300, 'lab': 'c. 1280-1300', 'acc': True, 'plate': {'kicker': '11.11 · Aotearoa', 'title': 'Aotearoa New Zealand', 'sub': 'c. 1280', 'text': "[[c-nz]]", 'sources': ['landcare-nz']}}]},
 'practice': [
  q("What does the 2025 Yucatán stalagmite study add to the debate over the Maya collapse?",
    ["It dates eight long droughts but does not show abandonment", "It proves drought caused Chichen Itza to be abandoned", "It shows rainfall rose in Yucatán during the collapse", "It shows warfare, not climate, drove the Maya decline"], 0,
    "It found eight droughts of three years or more between 871 and 1021, the longest 13 years; the authors caution that this 'doesn't necessarily mean' Chichen Itza was abandoned during them.",
    {1: "The authors caution that their finding 'doesn't necessarily mean' Chichen Itza was abandoned during the droughts.", 2: "Lake sediments show rainfall fell by 41-54 percent.", 3: "The study is about climate; it does not test warfare."}),
  q("What did Wilmshurst and colleagues (2011) change about the settlement of East Polynesia?",
    ["Settlement was later and faster than once thought", "They pushed first settlement back to about 500 BCE", "They showed New Zealand was settled centuries before Rapa Nui", "They showed settlement was earlier and slower than thought"], 0,
    "High-precision radiocarbon dating put the Society Islands at about 1025-1120 and the remaining islands in one pulse about 1190-1290; earlier chronologies were up to several centuries older.",
    {1: "Their dates are much later; the older chronologies were the earlier ones.", 2: "Both lie in the same pulse of settlement, about 1190-1290.", 3: "The reverse: their dates are later, and the spread faster, than earlier chronologies."})]}

PAGES = [P8, P9, P10, P11]
