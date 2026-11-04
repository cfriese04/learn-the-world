# Chapter 12, pages 12.8 to 12.11. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 12.8
 'brit-mali': ("Encyclopaedia Britannica, \"Mali (historical empire, Africa)\"", "https://www.britannica.com/place/Mali-historical-empire-Africa"),
 'brit-sundiata': ("Encyclopaedia Britannica, \"Sundiata\"", "https://www.britannica.com/biography/Sundiata"),
 'conrad1992': ("David C. Conrad, \"Searching for history in the Sunjata epic: the case of Fakoli\", History in Africa 19 (1992)", "https://www.cambridge.org/core/journals/history-in-africa/article/abs/searching-for-history-in-the-sunjata-epic-the-case-of-fakoli1/38A0DB3D1DB47D729223D42951A01604"),
 'bulman-sunjata': ("Stephen Bulman, University of Birmingham, \"The collection and analysis of the Sunjata epic\"", "https://www.birmingham.ac.uk/documents/college-artslaw/history/brihc/2017/the-collection-and-analysis-of-the-sunjata-epic.pdf"),
 'brit-musa': ("Encyclopaedia Britannica, \"Musa I of Mali\"", "https://www.britannica.com/biography/Musa-I-of-Mali"),
 'livesci-catalan': ("Live Science, on the Catalan Atlas (1375) and Mansa Musa", "https://www.livescience.com/64641-medieval-map-richest-man-africa.html"),
 'unesco-timbuktu': ("UNESCO World Heritage Centre, \"Timbuktu\"", "https://whc.unesco.org/en/list/119/"),
 'hmml-mali': ("Hill Museum & Manuscript Library, \"A decade in Mali\"", "https://hmml.org/stories/a-decade-in-mali/"),
 'brit-songhai': ("Encyclopaedia Britannica, \"Songhai empire\"", "https://www.britannica.com/place/Songhai-empire"),
 'unesco-zimbabwe2': ("UNESCO World Heritage Centre, \"Great Zimbabwe National Monument\"", "https://whc.unesco.org/en/list/364/"),
 'unesco-kilwa2': ("UNESCO World Heritage Centre, \"Ruins of Kilwa Kisiwani and Ruins of Songo Mnara\"", "https://whc.unesco.org/en/list/144/"),
 'brit-solomonid': ("Encyclopaedia Britannica, \"Solomonid dynasty\"", "https://www.britannica.com/topic/Solomonid-dynasty"),
 'brit-kebra': ("Encyclopaedia Britannica, \"Kebra Negast\"", "https://www.britannica.com/topic/Kebra-Negast"),
 'brit-benin': ("Encyclopaedia Britannica, \"Benin (historical kingdom, West Africa)\"", "https://www.britannica.com/place/Benin-historical-kingdom-West-Africa"),
 'brit-kongo': ("Encyclopaedia Britannica, \"Kongo (historical kingdom, Africa)\"", "https://www.britannica.com/place/Kongo-historical-kingdom-Africa"),
 # 12.9
 'brit-hongwu': ("Encyclopaedia Britannica, \"Hongwu\"", "https://www.britannica.com/biography/Hongwu"),
 'brit-redturbans': ("Encyclopaedia Britannica, \"Red Turbans\"", "https://www.britannica.com/topic/Red-Turbans"),
 'brit-yongle': ("Encyclopaedia Britannica, \"Yongle\"", "https://www.britannica.com/biography/Yongle"),
 'brit-zhenghe': ("Encyclopaedia Britannica, \"Zheng He's achievements\" (summary)", "https://www.britannica.com/summary/Zheng-Hes-Achievements"),
 'eaa-yangwei': ("Yang Wei, \"Admiral Zheng He's voyages to the 'West Oceans'\", Education About Asia 19:2 (2014)", "https://www.asianstudies.org/wp-content/uploads/admiral-zheng-hes-voyages-to-the-west-oceans.pdf"),
 'pwh-dolyk2026': ("Dolyk and Kozlovskyi, on the size of Zheng He's treasure ships, Problems of World History 33 (2026)", "https://journal.ivinas.gov.ua/pwh/article/view/388"),
 'unesco-hunmin': ("UNESCO Memory of the World, nomination of the Hunmin Chongum manuscript (Republic of Korea)", "https://media.unesco.org/sites/default/files/webform/mow001/republic_of_korea_hunmin_chongum.pdf"),
 'brit-muromachi': ("Encyclopaedia Britannica, \"Japan: the Muromachi (or Ashikaga) period\"", "https://www.britannica.com/place/Japan/The-Muromachi-or-Ashikaga-period-1338-1573"),
 # 12.10
 'brit-delhi2': ("Encyclopaedia Britannica, \"Delhi sultanate\"", "https://www.britannica.com/place/Delhi-sultanate"),
 'brit-tughluq': ("Encyclopaedia Britannica, \"Muhammad ibn Tughluq\"", "https://www.britannica.com/biography/Muhammad-ibn-Tughluq"),
 'brit-ibnbattuta2': ("Encyclopaedia Britannica, \"Ibn Battuta: time in India and later journeys\"", "https://www.britannica.com/biography/Ibn-Battuta/Time-in-India-and-later-journeys"),
 'brit-bahmani': ("Encyclopaedia Britannica, \"Bahmani sultanate\"", "https://www.britannica.com/place/Bahmani-sultanate"),
 'brit-vijayanagar': ("Encyclopaedia Britannica, \"Vijayanagar\"", "https://www.britannica.com/place/Vijayanagar"),
 'unesco-hampi': ("UNESCO World Heritage Centre, \"Group of Monuments at Hampi\"", "https://whc.unesco.org/en/list/241/"),
 'sahapedia-calicut': ("Ullattil Manmadhan, \"Oceans crossroads\", Sahapedia", "https://www.sahapedia.org/oceans-crossroads"),
 'brit-melaka': ("Encyclopaedia Britannica, \"Malacca\"", "https://www.britannica.com/print/article/359413"),
 'unesco-melaka': ("UNESCO World Heritage Centre, \"Melaka and George Town\"", "https://whc.unesco.org/en/list/1223/"),
 # 12.11
 'brit-tenochtitlan': ("Encyclopaedia Britannica, \"Tenochtitlan\"", "https://www.britannica.com/place/Tenochtitlan"),
 'brit-aztec': ("Encyclopaedia Britannica, \"Aztec\"", "https://www.britannica.com/topic/Aztec"),
 'archmag-tzompantli': ("Archaeology Magazine (Archaeology News Network), \"38 percent of Aztec skull rack contained heads of sacrificed women\" (2023)", "https://archaeologymag.com/2023/02/38-percent-of-aztec-skull-rack-contained-heads-of-sacrificed-women/"),
 'history-sacrifice': ("History.com, Dave Roos, \"Aztec human sacrifice\"", "https://www.history.com/articles/aztec-human-sacrifice-religion"),
 'pennock2012': ("Caroline Dodds Pennock, \"Mass murder or religious homicide? Rethinking human sacrifice and interpersonal violence in Aztec society\", Historical Social Research (2012)", "https://eprints.whiterose.ac.uk/id/eprint/98071/"),
 'brit-pachacuti': ("Encyclopaedia Britannica, \"Pachacuti Inca Yupanqui\"", "https://www.britannica.com/biography/Pachacuti-Inca-Yupanqui"),
 'unesco-qhapaq': ("UNESCO World Heritage Centre, \"Qhapaq Ñan, Andean Road System\"", "https://whc.unesco.org/en/list/1459/"),
 'harvard-khipu': ("Harvard Gazette (2017), on Manny Medrano and Gary Urton's khipu study", "https://content.news.harvard.edu/gazette/story/2017/08/a-students-mines-voices-from-the-incan-past/"),
 'hyland2025': ("Hyland et al., \"Stable isotope evidence for the participation of commoners in Inka khipu production\", Science Advances 11 (2025), record", "https://research-portal.st-andrews.ac.uk/en/publications/stable-isotope-evidence-for-the-participation-of-commoners-in-ink/"),
 'unesco-chanchan': ("UNESCO World Heritage Centre, \"Chan Chan Archaeological Zone\"", "https://whc.unesco.org/en/list/366/"),
 'koch2019': ("Koch, Brierley, Maslin and Lewis, \"Earth system impacts of the European arrival and Great Dying in the Americas after 1492\", Quaternary Science Reviews (2019)", "https://discovery.ucl.ac.uk/id/eprint/10068488/"),
 'koch2019-full': ("Koch et al. (2019), full text, White Rose eprints", "https://eprints.whiterose.ac.uk/id/eprint/154711/1/1-s2.0-S0277379118307261-main.pdf"),
}

C = {
 # 12.8
 'c-sundiata': c("Sundiata (died 1255) founded the empire of Mali; Britannica dates his decisive victory over the Susu ruler Sumanguru to 1230.", 'approx', ['brit-mali', 'brit-sundiata'], "The dates come from later sources."),
 'c-sunjata-epic': c("Most of what is told about Sundiata comes from an oral epic, recorded in many versions since the late 19th century; the earliest written mention is by Ibn Khaldun in the late 14th century.", 'debated', ['conrad1992', 'bulman-sunjata'], "David Conrad: 'Some themes are obviously mythical, while others could have a historical basis but cannot be independently confirmed.' Some scholars read the epic chiefly as literature, others as a historical source to set beside documents and archaeology."),
 'c-musa': c("Mansa Musa of Mali made the pilgrimage to Mecca in 1324, and in Cairo he spent so much gold that its value there fell.", 'approx', ['brit-musa'], "His reign is dated from 1307 or 1312; Britannica says the Cairo gold market had not fully recovered some years later."),
 'c-musa-mosques': c("Musa had the scholar and architect al-Sahili build mosques at Gao and Timbuktu, and the Sankore mosque at Timbuktu became a centre of teaching.", 'consensus', ['brit-musa'], show=False),
 'c-musa-wealth': c("Popular claims that Musa was the wealthiest person who ever lived cannot be checked.", 'debated', ['livesci-catalan', 'brit-musa'], "The Catalan Atlas of 1375 shows him holding a gold coin, and a curator describes him as having 'unlimited access to wealth'; no record allows a modern money value."),
 'c-timbuktu': c("Timbuktu was an intellectual and spiritual capital of Islam in Africa, at its height in the 15th and 16th centuries, with three great mosques: Djingareyber, Sankore and Sidi Yahia.", 'consensus', ['unesco-timbuktu'], show=False),
 'c-timbuktu-mss': c("Manuscripts from more than 30 family libraries in Timbuktu were moved to Bamako in about 1,400 metal boxes; armed groups occupied the city from April 2012 until January 2013.", 'consensus', ['hmml-mali'], show=False),
 'c-songhai': c("Mali lost Timbuktu to the Tuareg and its power to Songhay, whose ruler Sonni Ali drove the Tuareg from Timbuktu and in 1473 took Djenné.", 'approx', ['brit-songhai', 'brit-mali'], "Britannica's pages give 1431 and 1433 for the Tuareg capture of Timbuktu."),
 'c-gz': c("Great Zimbabwe, built by the Shona between the 11th and 15th centuries, was an important trading centre.", 'approx', ['unesco-zimbabwe2'], "UNESCO dates the site to 1100-1450 and the Great Enclosure to the 14th century; on its beginnings see 11.9."),
 'c-kilwa2': c("Kilwa was at its height in the 13th and 14th centuries; Ibn Battuta, who visited in 1331-32, called it one of the most beautiful cities of the world.", 'consensus', ['unesco-kilwa2'], show=False),
 'c-solomonid': c("In 1270 Yekuno Amlak took the throne of Ethiopia, founding a dynasty that claimed descent from King Solomon and the Queen of Sheba through their son Menilek.", 'tradition', ['brit-solomonid'], "The accession is historical; the descent is the dynasty's claim."),
 'c-kebra': c("The Kebra Nagast, written in the early 14th century, tells how Menilek, son of Solomon and the Queen of Sheba, brought the Ark of the Covenant to Aksum.", 'tradition', ['brit-kebra'], "Britannica calls it 'a combination of mythical history, allegory, and apocalypse'. The Queen of Sheba's visit to Solomon is in 1 Kings 10; Menilek and the Ark story come from Ethiopian tradition."),
 'c-benin': c("Edo tradition traces Benin's royal line to a prince from Ife; Ewuare (reigned c. 1440-80) greatly enlarged the kingdom.", 'tradition', ['brit-benin'], "Ewuare's reign is approximate; the founding story is tradition."),
 'c-kongo': c("The kingdom of Kongo was traditionally founded around 1390; the Portuguese arrived in 1483, and in 1491 its king, Nzinga a Nkuwu, and his son were baptised.", 'tradition', ['brit-kongo'], "The founding date is traditional; the baptism is recorded."),
 # 12.9
 'c-hongwu': c("Zhu Yuanzhang, born a poor peasant in 1328, rose through the rebellions against the Mongols and reigned as the Hongwu emperor, founder of the Ming, from 1368 to 1398.", 'consensus', ['brit-hongwu'], show=False),
 'c-redturbans': c("The Red Turbans, peasant rebels of the mid-14th century who regarded their leader as an incarnation of the bodhisattva Maitreya, rose against the Yuan; their rebellion was put down, but rival rebel forces under Zhu Yuanzhang toppled the dynasty.", 'approx', ['brit-redturbans'], "Zhu first served in a Red Turban army; Britannica treats his later forces as a rival movement."),
 'c-yongle': c("The Yongle emperor seized the throne in 1402, moved the capital from Nanjing to Beijing and rebuilt it with the Forbidden City.", 'consensus', ['brit-yongle'], show=False),
 'c-zhenghe': c("Between 1405 and 1433 the eunuch admiral Zheng He led seven voyages; the first carried some 27,800 men on 317 ships, and the fleets reached Calicut, Hormuz and East Africa.", 'approx', ['brit-zhenghe', 'eaa-yangwei'], "The figures come from Chinese records."),
 'c-zhenghe-why': c("The voyages displayed Ming power and brought foreign rulers into the tribute system, adding legitimacy to an emperor who had seized the throne.", 'debated', ['eaa-yangwei'], "An old story that they were a search for the deposed emperor Jianwen is one 'most historians discredit'."),
 'c-shipsize': c("Chinese texts give the largest treasure ships lengths of about 117-149 m; whether wooden ships that big could be built is debated.", 'debated', ['pwh-dolyk2026'], "Joseph Needham, Louise Levathes and Edward Dreyer accepted the figures; Sleeswyk, Wake and Church judged them impossible. A 2026 review suggests 60-76 m."),
 'c-zhenghe-end': c("The voyages ended amid concern about their high cost, fuelled by the objections of Confucian scholar-officials.", 'debated', ['eaa-yangwei'], "Yang Wei's account; the decision has been explained in several ways."),
 'c-hangul': c("King Sejong of Korea completed an alphabet of 28 letters in 1443 and proclaimed it in 1446, because Chinese characters were not suitable for writing Korean and common people could not record their thoughts.", 'consensus', ['unesco-hunmin'], show=False),
 'c-ashikaga': c("In Japan the Ashikaga shoguns ruled from Kyoto from the 1330s, but their power was relatively weak from the outset, and as time passed the office of shogun became increasingly impotent; the Ōnin War was fought in 1467-77.", 'consensus', ['brit-muromachi'], show=False),
 # 12.10
 'c-khaljis': c("Under the Khalji sultans (1290-1320) the Delhi Sultanate became an imperial power, repelling Mongol attacks and making the southern kingdoms its vassals.", 'consensus', ['brit-delhi2'], show=False),
 'c-tughluq': c("Muhammad bin Tughluq (reigned 1325-51) moved his capital to Daulatabad in the Deccan and issued coins of base metal with the face value of silver, an experiment that 'failed dismally'.", 'consensus', ['brit-tughluq'], show=False),
 'c-tughluq-view': c("Muhammad bin Tughluq's reputation is disputed.", 'debated', ['brit-tughluq', 'brit-ibnbattuta2'], "Britannica calls him 'controversial and enigmatic' and his measures 'neither vicious nor visionary'. Ibn Battuta, who served him as grand qadi of Delhi, described him with what Britannica calls 'mixed feelings of terror and sympathy'."),
 'c-timur-delhi': c("Timur's invasion of 1398-99 shattered the power of the Delhi Sultanate in north India.", 'consensus', ['brit-delhi2'], show=False),
 'c-vijayanagara': c("Vijayanagara was founded in 1336 by the Sangama brothers; UNESCO calls its capital, Hampi, the 'last capital of the last great Hindu Kingdom'.", 'consensus', ['brit-vijayanagar', 'unesco-hampi'], show=False),
 'c-bahmani': c("The Bahmani sultanate, founded in 1347 by rebels against Delhi, fought Vijayanagara almost continually over the fertile Raichur doab.", 'consensus', ['brit-bahmani'], show=False),
 'c-calicut': c("Under its rulers, the Zamorins, Calicut on the Malabar coast became a great port of the Indian Ocean, where Arab merchants bought pepper and ginger and Chinese treasure ships called in the 15th century.", 'consensus', ['sahapedia-calicut'], show=False),
 'c-melaka': c("Melaka, founded around 1400 by Parameswara, became a tributary of Ming China, and by the 1430s it was the leading commercial emporium of Southeast Asia.", 'approx', ['brit-melaka', 'unesco-melaka'], "Britannica says its ruler became a Muslim, taking the name Iskandar Shah, in 1414; whether this was Parameswara himself or his son is uncertain."),
 # 12.11
 'c-tenochtitlan': c("The Mexica (Aztecs) founded Tenochtitlan around 1325 on islands in Lake Texcoco; by 1519 Britannica estimates it held some 400,000 people.", 'approx', ['brit-tenochtitlan'], "1325 is the traditional date; population estimates vary."),
 'c-triple': c("Under Itzcoatl (1428-40) Tenochtitlan allied with Texcoco and Tlacopan in the Triple Alliance, which collected tribute from conquered regions according to what each produced.", 'consensus', ['brit-aztec'], show=False),
 'c-aztec-sacrifice': c("In Aztec religion human sacrifice, particularly by offering a victim's heart to Tonatiuh, was commonly practised, as was bloodletting.", 'consensus', ['brit-aztec'], show=False),
 'c-tzompantli': c("The Huey Tzompantli, a great skull rack excavated in Mexico City from 2015, was built in stages between 1486 and 1502; of the skulls studied, 60 percent were men, 38 percent women and 2 percent children.", 'approx', ['archmag-tzompantli'], "Figures from INAH's 2023 study; work continues."),
 'c-sacrifice-scale': c("The scale of Aztec human sacrifice is debated.", 'debated', ['history-sacrifice', 'pennock2012', 'archmag-tzompantli'], "Many historians once dismissed Spanish reports as exaggerated propaganda; archaeology now confirms sacrifice on a large scale, but not the largest Spanish figures, such as Diego Durán's 80,400 victims at one temple dedication. Caroline Dodds Pennock questions the 'sensationalism' that has hindered 'impartial and empathetic' study of it."),
 'c-pachacuti': c("Pachacuti, Inca ruler from 1438, began the rapid expansion of the Inca empire; tradition credits him with the plan of Cuzco.", 'approx', ['brit-pachacuti'], "Britannica gives his reign as 1438-71; the plan of Cuzco is one he 'is said to have devised'."),
 'c-qhapaq': c("The Inca road system, the Qhapaq Ñan, ran some 30,000 km through six modern countries and reached its greatest extent in the 15th century.", 'approx', ['unesco-qhapaq'], "UNESCO's figure for the whole network."),
 'c-khipu': c("Inca records were kept on khipus, knotted cords; in 2017 researchers matched six khipus to a Spanish census of 1670, a partial reading rather than a full decipherment.", 'debated', ['harvard-khipu'], "Most khipus remain unread."),
 'c-khipu2025': c("A 2025 study found that one khipu's main cord was made of human hair from someone with a commoner's diet, suggesting commoners took part in making khipus.", 'debated', ['hyland2025'], "New; based on a single khipu."),
 'c-chanchan': c("Chan Chan, capital of the Chimú kingdom on Peru's coast, the largest earthen city of the pre-Columbian Americas, reached its height in the 15th century, not long before it fell to the Incas.", 'consensus', ['unesco-chanchan'], show=False),
 'c-pop1492': c("Estimates of the population of the Americas in 1492 range from about 54 million (William Denevan) to 112 million (Henry Dobyns); a 2019 synthesis gives 60.5 million, with a middle range of 44.8-78.2 million.", 'debated', ['koch2019', 'koch2019-full'], "Koch et al. (2019). Early-20th-century estimates were much lower. The collapse after 1492 is told in Chapter 13."),
}

# ---------------------------------------------------------------- 12.8
P8 = {
 'title': "Africa, 1250 to 1500", 'sub': "gold, scholarship and kingship",
 'lede': "Mali's kings grew rich on West African gold, and one of them astonished Cairo on his way to Mecca. Timbuktu became a city of scholars. In the south, Great Zimbabwe and Kilwa flourished on trade, and in Ethiopia a new dynasty claimed descent from Solomon.",
 'body': [
  "Mali was founded by Sundiata in the 13th century, [[c-sundiata]] though most of his story comes from an epic that historians use with care. [[c-sunjata-epic]] Its most famous ruler, Mansa Musa, made his pilgrimage in 1324 and spent so much gold in Cairo that its price fell, [[c-musa]] and he built mosques at Gao and Timbuktu. [[c-musa-mosques]] His wealth became legendary. [[c-musa-wealth]]",
  "Timbuktu became one of Islam's great centres of learning. [[c-timbuktu]] Its family libraries survived into the 21st century, and their manuscripts were moved south to Bamako around the time armed groups occupied the city in 2012-13. [[c-timbuktu-mss]] Mali's power passed in the 15th century to Songhay. [[c-songhai]]",
  "In the south, Great Zimbabwe was an important trading centre of the interior, [[c-gz]] and Kilwa a prosperous port on the coast. [[c-kilwa2]] In Ethiopia the Solomonic dynasty took power in 1270, [[c-solomonid]] its claims set out in the Kebra Nagast. [[c-kebra]] On the Atlantic side, the kingdoms of Benin [[c-benin]] and Kongo were growing when the Portuguese arrived. [[c-kongo]]",
  {'table': {'head': ["Kingdom or city", "Region", "Known for"], 'rows': [
    ["Mali", "West African Sahel", "Sundiata; Mansa Musa's hajj, 1324"],
    ["Timbuktu", "Niger bend", "mosques and manuscripts"],
    ["Songhay", "Niger bend", "succeeds Mali in the 15th century"],
    ["Great Zimbabwe", "Zimbabwe plateau", "stone city, 11th-15th centuries"],
    ["Kilwa", "Swahili coast", "height in the 13th-14th centuries"],
    ["Solomonic Ethiopia", "Ethiopian highlands", "from 1270; the Kebra Nagast"],
    ["Kongo", "west-central Africa", "king baptised 1491"]], 'note': "[[c-musa]] [[c-timbuktu]] [[c-songhai]] [[c-gz]] [[c-kilwa2]] [[c-solomonid]] [[c-kongo]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 15.0, 'lat': 6.0, 'zoom': 3.8}, 'caption': "Africa, 1250-1500", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [-9.5, 10.5], 'label': 'MALI', 'size': 10}, {'ll': [2.0, 23.0], 'label': 'SAHARA', 'size': 11}]},
   {'type': 'points', 'items': [
    {'ll': [-3.01, 16.77], 'label': 'Timbuktu', 'date': 'Sankore', 'acc': True, 'big': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '12.8 · Mali', 'title': 'Timbuktu', 'sub': '14th-16th centuries', 'text': "[[c-musa-mosques]] [[c-timbuktu]] [[c-timbuktu-mss]] [[c-songhai]]", 'sources': ['brit-musa', 'unesco-timbuktu', 'hmml-mali', 'brit-songhai']}},
    {'ll': [-0.04, 16.27], 'label': 'Gao', 'date': 'Songhay', 'dy': 16},
    {'ll': [-4.55, 13.91], 'label': 'Djenné', 'anchor': 'end', 'dy': 16},
    {'ll': [31.24, 30.04], 'label': 'Cairo', 'date': 'Musa, 1324', 'acc': True, 'dy': -8, 'plate': {'kicker': '12.8 · the hajj', 'title': 'Mansa Musa', 'sub': '1324', 'text': "[[c-sundiata]] [[c-sunjata-epic]] [[c-musa]] [[c-musa-wealth]]", 'sources': ['brit-mali', 'conrad1992', 'brit-musa', 'livesci-catalan']}},
    {'ll': [38.72, 14.13], 'label': 'Aksum', 'date': 'the Kebra Nagast', 'acc': True, 'dy': -8, 'plate': {'kicker': '12.8 · Ethiopia', 'title': 'The Solomonic dynasty', 'sub': 'from 1270', 'text': "[[c-solomonid]] [[c-kebra]]", 'sources': ['brit-solomonid', 'brit-kebra']}},
    {'ll': [5.63, 6.34], 'label': 'Benin City', 'date': 'Ewuare, c. 1440', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.8 · Benin', 'title': 'Benin', 'sub': '15th century', 'text': "[[c-benin]]", 'sources': ['brit-benin']}},
    {'ll': [14.24, -6.27], 'label': 'Mbanza Kongo', 'date': 'baptism, 1491', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '12.8 · Kongo', 'title': 'Kongo', 'sub': 'c. 1390-1491', 'text': "[[c-kongo]]", 'sources': ['brit-kongo']}},
    {'ll': [39.51, -8.96], 'label': 'Kilwa', 'date': 'Ibn Battuta, 1331', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.8 · Swahili coast', 'title': 'Kilwa', 'sub': '13th-14th centuries', 'text': "[[c-kilwa2]]", 'sources': ['unesco-kilwa2']}},
    {'ll': [30.93, -20.27], 'label': 'Great Zimbabwe', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '12.8 · the south', 'title': 'Great Zimbabwe', 'sub': '11th-15th centuries', 'text': "[[c-gz]]", 'sources': ['unesco-zimbabwe2']}}]}]},
 'practice': [
  q("Why do historians use the Sunjata epic with caution as evidence for 13th-century Mali?",
    ["It mixes myth with episodes no one has confirmed", "It was invented by French officers in the 1880s", "Conrad reads it as pure invention with no history", "It survives in one fixed version from the 1300s"], 0,
    "David Conrad: 'Some themes are obviously mythical, while others could have a historical basis but cannot be independently confirmed.'",
    {1: "Ibn Khaldun mentioned Sundiata in the late 14th century; versions of the epic have been recorded since the late 19th century.", 2: "Conrad allows that some themes 'could have a historical basis'.", 3: "It has been recorded in many versions since the late 19th century."}),
  q("In economic terms, what did Mansa Musa's spending in Cairo in 1324 do?",
    ["It flooded Cairo with gold, so gold's value fell", "It made gold scarcer in Cairo, so its value rose", "It proved Musa the richest person who has ever lived", "It kept Mali's gold wealth hidden from outsiders"], 0,
    "He spent so much gold in Cairo that its value there fell: more supply, lower price.",
    {1: "The reverse: the gold he spent made its value fall.", 2: "Claims that he was the wealthiest person who ever lived cannot be checked; no record allows a modern money value.", 3: "His wealth became famous; the Catalan Atlas of 1375 shows him holding a gold coin."})]}

# ---------------------------------------------------------------- 12.9
P9 = {
 'title': "Ming China and East Asia", 'sub': "1368 to 1477",
 'lede': "A peasant rebel drove out the Mongols and founded the Ming dynasty. His son built the Forbidden City and sent great fleets across the Indian Ocean, and then China stopped sending them. In Korea a king invented an alphabet, and in Japan the shoguns' power weakened.",
 'body': [
  "The Red Turban rebellion against the Mongols was put down, [[c-redturbans]] but a rival rebel, the peasant-born Zhu Yuanzhang, toppled the Yuan dynasty and founded the Ming in 1368. [[c-hongwu]] His son, the Yongle emperor, seized the throne and moved the capital to Beijing. [[c-yongle]]",
  "Yongle also sent the admiral Zheng He on the first of seven great voyages, [[c-zhenghe]] to display Ming power and draw distant rulers into the tribute system. [[c-zhenghe-why]] How large his ships were is still argued over. [[c-shipsize]] After 1433 the voyages stopped, criticised as too costly. [[c-zhenghe-end]]",
  "In Korea, King Sejong created an alphabet so that ordinary people could write their own language. [[c-hangul]] In Japan the Ashikaga shoguns' power was weak from the outset and weakened further; the Ōnin War broke out in 1467. [[c-ashikaga]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["1368", "Ming dynasty founded"],
    ["1402", "Yongle seizes the throne"],
    ["1405", "Zheng He's first voyage"],
    ["1433", "last voyage"],
    ["1443/1446", "Hangul completed and proclaimed"],
    ["1467-77", "Ōnin War in Japan"]], 'note': "[[c-hongwu]] [[c-yongle]] [[c-zhenghe]] [[c-hangul]] [[c-ashikaga]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 87.0, 'lat': 18.0, 'zoom': 2.6}, 'caption': "Ming China and Zheng He's voyages, 1405-1433", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'arrow', 'items': [{'path': [[118.8, 32.06], [120.3, 31.95], [121.95, 31.45], [122.8, 30.0], [121.9, 28.0], [120.7, 26.3], [120.2, 24.8], [117.5, 22.6], [113.5, 20.5], [110.5, 15.5], [110.0, 12.0], [107.0, 7.0], [104.6, 1.8], [104.5, 1.4], [103.8, 1.18], [103.3, 1.35], [102.6, 1.75], [101.0, 2.7], [99.6, 4.6], [97.8, 5.9], [95.5, 6.2], [80.6, 5.2], [77.3, 7.3], [76.1, 9.3], [75.5, 10.6], [75.78, 11.25], [70.0, 16.0], [62.0, 21.0], [58.2, 24.6], [56.75, 26.45], [56.45, 27.09]], 'label': "Zheng He's fleets", 'lab': [88.0, 6.0], 'ldy': 18}]},
   {'type': 'region', 'items': [{'ll': [108.0, 31.0], 'label': 'MING', 'size': 10}]},
   {'type': 'points', 'items': [
    {'ll': [118.8, 32.06], 'label': 'Nanjing', 'date': 'Ming capital, 1368', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.9 · the Ming', 'title': 'Hongwu', 'sub': '1368-1398', 'text': "[[c-redturbans]] [[c-hongwu]]", 'sources': ['brit-redturbans', 'brit-hongwu']}},
    {'ll': [116.39, 39.92], 'label': 'Beijing', 'date': 'Forbidden City', 'acc': True, 'big': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '12.9 · Yongle', 'title': 'Yongle and Zheng He', 'sub': '1402-1433', 'text': "[[c-yongle]] [[c-zhenghe]] [[c-zhenghe-why]] [[c-shipsize]] [[c-zhenghe-end]]", 'sources': ['brit-yongle', 'brit-zhenghe', 'eaa-yangwei', 'pwh-dolyk2026']}},
    {'ll': [126.98, 37.58], 'label': 'Hanyang (Seoul)', 'date': 'Hangul, 1443', 'acc': True, 'dy': -8, 'plate': {'kicker': '12.9 · Korea', 'title': "King Sejong's alphabet", 'sub': '1443/1446', 'text': "[[c-hangul]]", 'sources': ['unesco-hunmin']}},
    {'ll': [135.77, 35.01], 'label': 'Kyoto', 'date': 'Ashikaga', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.9 · Japan', 'title': 'The Ashikaga shoguns', 'sub': '1330s-1573', 'text': "[[c-ashikaga]]", 'sources': ['brit-muromachi']}},
    {'ll': [75.78, 11.25], 'label': 'Calicut', 'acc': True, 'anchor': 'end', 'dy': 4},
    {'ll': [56.45, 27.09], 'label': 'Hormuz', 'anchor': 'end', 'dy': -6},
    {'ll': [40.12, -3.22], 'label': 'Malindi', 'date': 'East Africa', 'anchor': 'end', 'dy': 4}]}]},
 'practice': [
  q("Why do estimates of the size of Zheng He's largest ships vary so widely?",
    ["Texts give 117-149 m, too long for wooden ships, critics say", "No Chinese text records the treasure ships' lengths", "A complete treasure ship has been excavated and measured", "Needham and Levathes judged such ships impossible"], 0,
    "Chinese texts give lengths of about 117-149 m, but whether wooden ships that big could be built is debated; a 2026 review suggests 60-76 m.",
    {1: "Chinese texts give the largest ships lengths of about 117-149 m.", 2: "The debate rests on the texts and on whether such wooden ships could be built.", 3: "Needham, Levathes and Dreyer accepted the figures; Sleeswyk, Wake and Church judged them impossible."}),
  q("What reason was given for creating the Korean alphabet?",
    ["Chinese characters did not suit writing Korean", "Korea needed a script of its own for dealing with the Ming", "Korean envoys needed a script for writing Japanese", "To give Korean thousands of new characters"], 0,
    "Chinese characters were not suitable for writing Korean, so common people could not record their thoughts.",
    {1: "The reason given was that common people could not record their thoughts in Chinese characters.", 2: "It was made for writing Korean.", 3: "It has 28 letters, not thousands of characters."})]}

# ---------------------------------------------------------------- 12.10
P10 = {
 'title': "India and the Indian Ocean", 'sub': "1290 to 1500",
 'lede': "The Delhi Sultanate became an imperial power and then broke apart, its power in the north shattered by Timur. New states rose in the south, Hindu Vijayanagara and the Muslim Bahmani sultanate. Along the coasts, ports such as Calicut and Melaka flourished on Indian Ocean trade.",
 'body': [
  "The Khalji sultans made Delhi an imperial power. [[c-khaljis]] Muhammad bin Tughluq moved his capital south and experimented with token coins, [[c-tughluq]] and historians still argue over whether he was a visionary or a tyrant. [[c-tughluq-view]] In 1398 Timur's invasion broke the Sultanate's power in the north. [[c-timur-delhi]]",
  "In the Deccan and the south, Vijayanagara [[c-vijayanagara]] and the Bahmani sultanate fought for generations. [[c-bahmani]]",
  "The Indian Ocean linked them all to the wider world. Calicut traded pepper with Arab merchants and received the Chinese fleets, [[c-calicut]] and Melaka, on the strait between the Indian Ocean and the South China Sea, became the region's greatest market. [[c-melaka]]",
  {'table': {'head': ["State or port", "Founded or flourished", "Notable"], 'rows': [
    ["Delhi Sultanate (Khaljis)", "1290-1320", "imperial power"],
    ["Delhi Sultanate (Tughluqs)", "1325-51", "token coinage; capital moved"],
    ["Vijayanagara", "1336", "capital at Hampi"],
    ["Bahmani sultanate", "1347", "wars with Vijayanagara"],
    ["Calicut", "15th century", "pepper; Chinese fleets"],
    ["Melaka", "c. 1400", "leading emporium by the 1430s"]], 'note': "[[c-khaljis]] [[c-tughluq]] [[c-vijayanagara]] [[c-bahmani]] [[c-calicut]] [[c-melaka]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 88.0, 'lat': 15.5, 'zoom': 8}, 'caption': "India and the Indian Ocean, 1290-1500", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [80.0, 24.5], 'label': 'DELHI SULTANATE', 'size': 9}, {'ll': [78.5, 14.0], 'label': 'DECCAN', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [77.21, 28.61], 'label': 'Delhi', 'date': 'Timur, 1398', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '12.10 · Delhi', 'title': 'The Delhi Sultanate', 'sub': '1290-1399', 'text': "[[c-khaljis]] [[c-tughluq-view]] [[c-timur-delhi]]", 'sources': ['brit-delhi2', 'brit-tughluq', 'brit-ibnbattuta2']}},
    {'ll': [75.21, 19.94], 'label': 'Daulatabad', 'date': 'capital moved here', 'acc': True, 'anchor': 'end', 'dy': -6, 'plate': {'kicker': '12.10 · Tughluq', 'title': 'Muhammad bin Tughluq', 'sub': '1325-1351', 'text': "[[c-tughluq]] [[c-tughluq-view]]", 'sources': ['brit-tughluq', 'brit-ibnbattuta2']}},
    {'ll': [76.83, 17.33], 'label': 'Gulbarga', 'date': 'Bahmani, 1347', 'acc': True, 'dy': -6, 'plate': {'kicker': '12.10 · the Deccan', 'title': 'The Bahmani sultanate', 'sub': 'from 1347', 'text': "[[c-bahmani]]", 'sources': ['brit-bahmani']}},
    {'ll': [76.46, 15.33], 'label': 'Hampi', 'date': 'Vijayanagara, 1336', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '12.10 · the south', 'title': 'Vijayanagara', 'sub': 'from 1336', 'text': "[[c-vijayanagara]]", 'sources': ['brit-vijayanagar', 'unesco-hampi']}},
    {'ll': [75.78, 11.25], 'label': 'Calicut', 'date': 'pepper port', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '12.10 · the ocean', 'title': 'Calicut', 'sub': '15th century', 'text': "[[c-calicut]]", 'sources': ['sahapedia-calicut']}},
    {'ll': [102.25, 2.19], 'label': 'Melaka', 'date': 'c. 1400', 'acc': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '12.10 · the strait', 'title': 'Melaka', 'sub': 'c. 1400-1511', 'text': "[[c-melaka]]", 'sources': ['brit-melaka', 'unesco-melaka']}}]}]},
 'practice': [
  q("Which description best fits Muhammad bin Tughluq's token currency?",
    ["Base-metal coins with a silver face value", "Paper notes copied from those of Yuan China", "A successful reform kept by his successors", "A plan to move the royal mint to Calicut"], 0,
    "He issued coins of base metal with the face value of silver, an experiment that 'failed dismally'.",
    {1: "The token currency was coins of base metal, not paper.", 2: "It 'failed dismally'.", 3: "His move was of the capital, to Daulatabad in the Deccan; the token currency was base-metal coin."}),
  q("What best explains Melaka's rise by the 1430s?",
    ["Its strait position and ties with Ming China", "Its founding by Portuguese traders around 1400", "Its role as the port of Vijayanagara's empire", "Timur's conquest, which made it his naval base"], 0,
    "Melaka lay on the strait between the Indian Ocean and the South China Sea, and became a tributary of Ming China; by the 1430s it was Southeast Asia's leading emporium.",
    {1: "It was founded around 1400 by Parameswara.", 2: "Vijayanagara's capital was Hampi in the south of India; Melaka was a tributary of Ming China.", 3: "Timur's invasion struck Delhi in 1398-99."})]}

# ---------------------------------------------------------------- 12.11
P11 = {
 'title': "The Americas", 'sub': "the Mexica and the Inca, c. 1325 to 1500",
 'lede': "In the 15th century two great empires rose in the Americas, the Mexica (Aztec) in central Mexico and the Inca in the Andes. Both grew rapidly in the 15th century, and both drew tribute from the peoples they conquered.",
 'body': [
  "The Mexica founded Tenochtitlan on a lake in central Mexico, [[c-tenochtitlan]] and after 1428 their Triple Alliance collected tribute across much of Mexico. [[c-triple]] Human sacrifice was commonly practised as part of their religion. [[c-aztec-sacrifice]] The great skull rack found in Mexico City has confirmed it on a large scale, including women and children, [[c-tzompantli]] though the numbers given by Spanish writers are still disputed. [[c-sacrifice-scale]]",
  "In the Andes, Pachacuti began the Inca expansion in the mid-15th century, [[c-pachacuti]] knitting the empire together with roads [[c-qhapaq]] and keeping records on knotted cords that are only beginning to be read. [[c-khipu]] [[c-khipu2025]] Among the peoples the Inca conquered were the Chimú of the Peruvian coast. [[c-chanchan]]",
  "How many people lived in the Americas on the eve of contact is uncertain, [[c-pop1492]] and what happened to them after 1492 is the story of Chapter 13.",
  {'table': {'head': ["Estimate of population, 1492", "Scholar"], 'rows': [
    ["about 54 million", "William Denevan"],
    ["60.5 million (middle range 44.8-78.2)", "Koch et al. (2019)"],
    ["112 million", "Henry Dobyns"]], 'note': "[[c-pop1492]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': -86.0, 'lat': 3.0, 'zoom': 5}, 'caption': "The Americas, c. 1325-1500", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [-99.0, 22.5], 'label': 'MEXICA', 'size': 10}, {'ll': [-74.0, -10.0], 'label': 'INCA', 'size': 10}]},
   {'type': 'points', 'items': [
    {'ll': [-99.13, 19.43], 'label': 'Tenochtitlan', 'date': 'c. 1325', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '12.11 · the Mexica', 'title': 'Tenochtitlan', 'sub': 'c. 1325-1519', 'text': "[[c-tenochtitlan]] [[c-triple]] [[c-aztec-sacrifice]] [[c-tzompantli]] [[c-sacrifice-scale]]", 'sources': ['brit-tenochtitlan', 'brit-aztec', 'archmag-tzompantli', 'pennock2012']}},
    {'ll': [-79.07, -8.11], 'label': 'Chan Chan', 'date': 'Chimú', 'acc': True, 'anchor': 'end', 'dy': 4, 'plate': {'kicker': '12.11 · Chimú', 'title': 'Chan Chan', 'sub': '15th century', 'text': "[[c-chanchan]]", 'sources': ['unesco-chanchan']}},
    {'ll': [-71.97, -13.52], 'label': 'Cuzco', 'date': 'Pachacuti, 1438', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '12.11 · the Inca', 'title': 'Pachacuti and the roads', 'sub': 'from 1438', 'text': "[[c-pachacuti]] [[c-qhapaq]] [[c-khipu]] [[c-khipu2025]]", 'sources': ['brit-pachacuti', 'unesco-qhapaq', 'harvard-khipu', 'hyland2025']}},
    {'ll': [-78.51, -0.22], 'label': 'Quito', 'anchor': 'end', 'dy': 4}]}]},
 'practice': [
  q("What have the Huey Tzompantli excavations done to the debate over Aztec sacrifice?",
    ["Confirmed mass sacrifice, but not the top Spanish figures", "Confirmed Diego Durán's 80,400 victims at one dedication", "Shown that sacrifice victims were adult male warriors", "Dated the rack to the years after the Spanish conquest"], 0,
    "Archaeology now confirms sacrifice on a large scale, including women and children, but not the largest Spanish figures.",
    {1: "Archaeology does not confirm the largest Spanish figures, such as Durán's.", 2: "Of the skulls studied, 38 percent were women and 2 percent children.", 3: "It was built in stages between 1486 and 1502."}),
  q("Which statement about the population of the Americas in 1492 is best supported?",
    ["A 2019 synthesis gives 60.5 million, within a wide range", "Inca and Mexica censuses give exact totals for both continents", "Dobyns's 112 million is now the agreed figure", "Recent estimates put it below 20 million people"], 0,
    "Estimates range from about 54 million (Denevan) to 112 million (Dobyns); Koch et al. (2019) give 60.5 million, with a middle range of 44.8-78.2 million.",
    {1: "Khipus are only beginning to be read: six were matched to a Spanish census of 1670.", 2: "Estimates range from about 54 million to 112 million, and a 2019 synthesis gives 60.5 million.", 3: "Denevan gives about 54 million and Dobyns 112 million; it was early-20th-century estimates that were much lower."})]}

PAGES = [P8, P9, P10, P11]
