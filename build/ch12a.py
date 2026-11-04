# Chapter 12, pages 12.0 to 12.3. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 12.0
 'brit-mongol-empire': ("Encyclopaedia Britannica, \"Mongol empire\"", "https://www.britannica.com/place/Mongol-empire"),
 'wch-abulughod': ("Scott C. Bailey, review of Janet Abu-Lughod, Before European Hegemony, World History Connected 3.1", "https://worldhistoryconnected.press.uillinois.edu/3.1/br_bailey.html"),
 'whe-secret': ("World History Encyclopedia, \"The Secret History of the Mongols\"", "https://www.worldhistory.org/The_Secret_History_of_the_Mongols/"),
 'brit-rashid': ("Encyclopaedia Britannica, \"Rashid al-Din\"", "https://britannica.com/biography/Rashid-al-Din"),
 'brit-ibnbattuta': ("Encyclopaedia Britannica, \"Ibn Battuta: time in India and later journeys\"", "https://www.britannica.com/biography/Ibn-Battuta/Time-in-India-and-later-journeys"),
 'natgeo-bd': ("National Geographic, \"Scientists sequence the full Black Death genome\" (2011), on Bos et al., Nature", "https://www.nationalgeographic.com/science/article/scientists-sequence-the-full-black-death-genome-and-find-the-mother-of-all-plagues"),
 'agu-lead': ("American Geophysical Union, on More et al., GeoHealth (2017): lead in an Alpine ice core", "https://news.agu.org/press-release/human-activity-has-polluted-european-air-for-2000-years-study-finds/"),
 'cam-volcano': ("University of Cambridge, \"Volcanoes may have helped bring the Black Death to Europe\" (2025), on Bauch and Büntgen", "https://www.cam.ac.uk/stories/volcanoes-black-death"),
 # 12.1
 'brit-genghis': ("Encyclopaedia Britannica, \"Genghis Khan\"", "https://www.britannica.com/biography/Genghis-Khan"),
 'brit-merv': ("Encyclopaedia Britannica, \"Merv\"", "https://www.britannica.com/place/Merv"),
 'jiiph2014': ("Journal of Iranian Islamic Period History 4/8 (2014), on Mongol massacres in Khurasan", "https://www.magiran.com/paper/1391719?lang=en"),
 'national-jackson': ("Steve Donoghue, review of Peter Jackson, The Mongols and the Islamic World (Yale, 2017), The National", "https://thenationalnews.com/arts/book-review-an-epic-new-history-looks-at-the-mongols-in-the-islamic-world-1.76235"),
 'reaktion-may': ("Reaktion Books, Timothy May, The Mongol Conquests in World History (2011)", "https://reaktionbooks.co.uk/?p=28406"),
 # 12.2
 'brit-mustasim': ("Encyclopaedia Britannica, \"al-Mustasim\"", "https://www.britannica.com/biography/al-Mustasim"),
 'brit-ainjalut': ("Encyclopaedia Britannica, \"Battle of Ayn Jalut\"", "https://britannica.com/event/Battle-of-Ayn-Jalut"),
 'brit-ghazan': ("Encyclopaedia Britannica, \"Mahmud Ghazan\" (summary)", "https://www.britannica.com/summary/Mahmud-Ghazan"),
 'brit-goldenhorde': ("Encyclopaedia Britannica, \"Golden Horde\"", "https://www.britannica.com/place/Golden-Horde"),
 'ihr-ostrowski': ("Will Ryan, review of Donald Ostrowski, Muscovy and the Mongols (1998), Reviews in History 129", "https://reviews.history.ac.uk/review/129"),
 'halperin2025': ("Charles J. Halperin, on the term 'Tatar yoke', Golden Horde Review 13/1 (2025)", "https://journals.rcsi.science/2308-152X/article/view/289287"),
 'brit-kublai': ("Encyclopaedia Britannica, \"Kublai Khan: unification of China\"", "https://www.britannica.com/biography/Kublai-Khan/Unification-of-China"),
 'arch-kamikaze': ("Archaeology 56/1 (2003), \"Kamikaze\": underwater finds at Takashima", "https://archive.archaeology.org/0301/etc/kamikaze.html"),
 'uw-rubruck': ("University of Washington, Silk Road Seattle: William of Rubruck (tr. Rockhill)", "https://depts.washington.edu/silkroad/texts/rubruck.html"),
 'gorgias-sauma': ("Gorgias Press, An Eastern Embassy to Europe in the Years 1287-8 (Rabban Sauma)", "https://www.gorgiaspress.com/an-eastern-embassy-to-europe-in-the-years-1287-8"),
 'routledge-wood': ("Routledge, Frances Wood, Did Marco Polo Go to China?", "https://www.routledge.com/Did-Marco-Polo-Go-To-China/Wood/p/book/9780813389998"),
 'tuebingen-vogel': ("University of Tübingen press release (2012) on Hans Ulrich Vogel, Marco Polo Was in China", "https://uni-tuebingen.de/uploads/media/12-04-16MarcoPoloengl.pdf"),
 # 12.3
 'spyrou2022': ("Spyrou et al., \"The source of the Black Death in fourteenth-century central Eurasia\", Nature 606 (2022)", "https://www.nature.com/articles/s41586-022-04800-3"),
 'eurekalert-wardi': ("EurekAlert (University of Exeter), on Omar and Fancy, Journal of Arabic and Islamic Studies (2025)", "https://www.eurekalert.org/news-releases/1104400"),
 'medievalists-caffa': ("Medievalists.net, \"Biological warfare at the 1346 siege of Caffa\", on Wheelis (2002)", "https://www.medievalists.net/2012/08/biological-warfare-at-the-1346-siege-of-caffa/"),
 'brit-blackdeath': ("Encyclopaedia Britannica, \"Black Death\"", "https://www.britannica.com/event/Black-Death"),
 'arthur2010': ("Paula Arthur, \"The Black Death and mortality: a reassessment\", Fourteenth Century England VI (2010)", "https://www.cambridge.org/core/books/abs/fourteenth-century-england-vi/black-death-and-mortality-a-reassessment/AA308C01F4BE44F11B3AEC47249F868C"),
 'boydell-benedictow': ("Boydell & Brewer, Ole Benedictow, The Complete History of the Black Death", "https://boydellandbrewer.com/9781783275168"),
 'reading-pollen': ("University of Reading, on Izdebski et al., Nature Ecology & Evolution (2022)", "https://www.reading.ac.uk/news/2022/Research-News/Black-Death-mortality"),
 'pup-dols': ("Princeton University Press, Michael Dols, The Black Death in the Middle East (1977)", "https://press.princeton.edu/books/ebook/9780691196688/the-black-death-in-the-middle-east-pdf-0"),
}

C = {
 # 12.0
 'c-mongol-area': c("At its peak the Mongol empire covered some 23 million square km, the largest contiguous land empire in world history.", 'approx', ['brit-mongol-empire'], "A modern estimate for frontiers that shifted constantly."),
 'c-abulughod': c("Janet Abu-Lughod described a Eurasian 'world system' of about 1250-1350, made possible by the Mongol empire and made of eight overlapping circuits of trade, which plague and other epidemics and the Mongols' loss of China in 1368 helped to break apart.", 'debated', ['wch-abulughod'], "An influential model, not a settled fact. Her point was that Europe's later dominance was not an 'inherent historical necessity'."),
 'c-secret-history': c("The Secret History of the Mongols, by an unknown 13th-century author, is the main account from the Mongol side.", 'debated', ['whe-secret', 'brit-genghis'], "Its date is uncertain (Britannica gives 1240 with a query). Its early parts cannot be checked against other sources, but historians warn it would be 'unwise to dismiss' it 'as pure fiction'."),
 'c-rashid': c("Rashid al-Din (1247-1318), who came from a Jewish family of Hamadan and converted to Islam, served the Mongol rulers of Iran as vizier and wrote a universal history, the Jami' al-tawarikh, beginning with a history of the Mongols commissioned by Ghazan.", 'consensus', ['brit-rashid', 'brit-ghazan'], show=False),
 'c-ibnbattuta': c("The Moroccan traveller Ibn Battuta saw the Black Death in Syria in 1348.", 'consensus', ['brit-ibnbattuta'], show=False),
 'c-bd-genome': c("In 2011 scientists reconstructed the genome of the Black Death bacterium, Yersinia pestis, from a London plague cemetery; all the strains that infect humans today descend from it.", 'consensus', ['natgeo-bd'], show=False),
 'c-lead-plague': c("Lead pollution in an Alpine ice core fell to natural levels in 1349-53, when the Black Death halted mining and smelting.", 'consensus', ['agu-lead'], show=False),
 'c-bluerings': c("Unusual 'blue rings' in Pyrenean trees record cold, wet summers in 1345, 1346 and 1347.", 'approx', ['cam-volcano'], "Probably the result of a volcanic eruption around 1345; see 12.3."),
 # 12.1
 'c-temujin': c("Temüjin, the future Chinggis Khan, may have been born in 1155, 1162 (the date favoured in Mongolia today) or 1167.", 'approx', ['brit-genghis'], "No contemporary record gives the year."),
 'c-kuriltai': c("In 1206 a great assembly by the Onon River proclaimed him Chinggis Khan; the title probably meant 'Universal Ruler'.", 'consensus', ['brit-genghis'], show=False),
 'c-decimal': c("His army was divided on the decimal system, in units of tens.", 'consensus', ['brit-genghis'], show=False),
 'c-jin': c("He attacked the Jin empire of northern China in 1211 and took Beijing in 1215.", 'consensus', ['brit-genghis'], show=False),
 'c-khwarazm': c("After the governor of Otrar massacred a caravan sent under Mongol protection, Chinggis invaded the Khwarazmian empire; Bukhara, Samarkand and the capital Urgench were taken and sacked in 1220-21.", 'consensus', ['brit-genghis', 'brit-mongol-empire'], show=False),
 'c-merv': c("Merv, an ancient city of Central Asia, was destroyed by the Mongols in 1221 and never regained its former prosperity.", 'consensus', ['brit-merv'], show=False),
 'c-death1227': c("Chinggis Khan died on 18 August 1227.", 'consensus', ['brit-genghis'], show=False),
 'c-tolls': c("How many people the conquests killed is unknown.", 'debated', ['jiiph2014', 'national-jackson'], "A 2014 Iranian study argues the actual 'rate of murder and pillage' was 'much lower' than some historians claim. Reviewing Peter Jackson (2017), Steve Donoghue writes that 'as Jackson readily admits, such reclamation has its limits'; Jackson notes that Nishapur was 'singled out for especially harsh treatment'."),
 'c-may': c("Timothy May calls the Mongols 'the most destructive force in the pre-modern world', yet argues that their rule also had 'stabilizing effects'.", 'debated', ['reaktion-may'], "One historian's balance; others weigh the destruction more heavily."),
 # 12.2
 'c-baghdad1258': c("In February 1258 Hülegü, a grandson of Chinggis, took Baghdad and killed many of its inhabitants; the execution of the caliph al-Musta'sim left Islam without a caliph for the first time in its history.", 'consensus', ['brit-mustasim'], show=False),
 'c-ainjalut': c("At Ain Jalut in Palestine, on 3 September 1260, the Mamluks of Egypt under Qutuz and Baybars defeated a Mongol army, halting the westward expansion of the Mongol empire.", 'approx', ['brit-ainjalut'], "Some sources give 8 September."),
 'c-ghazan': c("Ghazan, Mongol ruler of Iran, converted from Buddhism to Islam before taking the throne in 1295; Rashid al-Din became his vizier.", 'consensus', ['brit-ghazan', 'brit-rashid'], show=False),
 'c-goldenhorde': c("The Golden Horde ruled the western steppe from Sarai on the lower Volga. Russian princes, above all those of Moscow, collected its tribute; under Öz Beg (1312-41) the Horde became Muslim, in 1380 Russian princes defeated it at Kulikovo, and its last remnant was destroyed in 1502.", 'consensus', ['brit-goldenhorde'], show=False),
 'c-yoke': c("The traditional Russian view saw the Mongol conquest as a disaster, the 'Tatar yoke'.", 'debated', ['ihr-ostrowski'], "Reviewing Donald Ostrowski (1998), Will Ryan says he takes the revisionist position 'that after an initial period of deprivation Muscovy for the most part flourished', and finds his case that Muscovy took its 'dual structure' of administration from the Horde 'demonstrated persuasively if not conclusively'. Ostrowski observes that the older view of economic destruction has 'a metahistorical appeal both to Russian nationalists and to Marxist historians'."),
 'c-yoke-term': c("The earliest known use of the phrase 'Tatar yoke' in Slavic writing dates from the second half of the 17th century.", 'debated', ['halperin2025'], "Halperin (2025) reports that the earliest known Slavic use, found by Lev Dmitriev, dates from the second half of the 17th century, while Seleznev has found two Latin references from the 13th century. He argues that 'any author familiar with Scripture could easily independently have made the leap from \"Yoke\" to \"Tatar Yoke\"'."),
 'c-khubilai': c("Khubilai Khan proclaimed the Yuan dynasty in 1271, ruled from Dadu (Beijing), ended the Song in 1279 and made paper money the sole medium of exchange.", 'consensus', ['brit-kublai'], show=False),
 'c-japan': c("Khubilai's invasions of Japan in 1274 and 1281 failed; his fleets were virtually annihilated, as much by storms as by Japanese resistance.", 'debated', ['brit-kublai', 'arch-kamikaze'], "Chinese records claim 4,400 ships in 1281; the underwater archaeologist Kenzo Hayashida thinks the fleet's size was exaggerated, and found anchors 'only roughly finished'."),
 'c-rubruck': c("The Franciscan William of Rubruck (1253-55) was the first European to visit the Mongol capital, Karakorum, and return to write about it.", 'consensus', ['uw-rubruck'], show=False),
 'c-sauma': c("Rabban Sauma, a Syriac Christian monk, came to Europe in 1287 for the Mongol ruler of Iran to seek joint action against the Muslims of Palestine, and met the kings of France and England.", 'consensus', ['gorgias-sauma'], show=False),
 'c-polo': c("Whether Marco Polo really went to China is debated.", 'debated', ['routledge-wood', 'tuebingen-vogel'], "Frances Wood asks why his book omits 'tea, foot-binding, or even the Great Wall'; Hans Ulrich Vogel (2013) finds that he alone described 'precisely how paper for money was made' and that his account of salt production 'checks out with Chinese documents'."),
 # 12.3
 'c-origin': c("Ancient DNA from graves at Kara-Djigach and Burana in Kyrgyzstan, whose tombstones of 1338-39 record deaths from 'pestilence', contains the plague strain from which the Black Death's lineages branched out, supporting an origin in that region.", 'approx', ['spyrou2022'], "Spyrou et al. (2022). The Tian Shan region is the strongest candidate, not a proven single source."),
 'c-ibnwardi': c("An Arabic account by Ibn al-Wardi, long used to trace the plague's rapid overland spread, has been argued (2025) to be a literary work that 'should not be taken literally'.", 'debated', ['eurekalert-wardi'], "New, by Muhammed Omar and Nahyan Fancy; they say the 'Quick Transit Theory' built on it is 'severely called into question'."),
 'c-caffa': c("Gabriele de' Mussis wrote that at the siege of Caffa in Crimea (1346) the Mongol army hurled plague-infected corpses into the city.", 'debated', ['medievalists-caffa'], "Mark Wheelis (2002) finds the story plausible but concludes that plague likely entered Europe from Crimea independently of it."),
 'c-grain': c("Martin Bauch and Ulf Büntgen (2025) argue that a volcanic eruption around 1345 caused cold summers and famine, so that Venice, Genoa and Pisa imported grain from the Golden Horde in 1347, and infected fleas most likely travelled with it.", 'debated', ['cam-volcano'], "New; the authors present the chain as likely, not proven."),
 'c-bd-europe': c("The Black Death ravaged Europe between 1347 and 1351, taking a proportionally greater toll of life than any earlier epidemic or war.", 'consensus', ['brit-blackdeath'], show=False),
 'c-mortality': c("Estimates of the share of Europe's population that died range from 30-40 percent (Philip Ziegler) through 40-50 (Robert Gottfried) and 47-48 (Rosemary Horrox) to about 60 percent (Ole Benedictow).", 'debated', ['arthur2010', 'boydell-benedictow'], "Paula Arthur (2010) argues for a 'much higher mortality figure' than the older estimates."),
 'c-pollen': c("A 2022 study of 1,634 pollen samples from 261 sites in 19 countries found farming collapsed in Scandinavia, France, south-western Germany, Greece and central Italy, but continued or grew in Ireland, Iberia and much of central and eastern Europe.", 'debated', ['reading-pollen'], "Izdebski et al. It challenges the idea of uniformly high mortality across Europe."),
 'c-dols': c("Michael Dols traced the plague in the Middle East from Arabic sources and found that its recurrences 'appreciably slowed population growth' in Egypt and Syria for a century and a half.", 'approx', ['pup-dols'], "Dols (1977); no reliable census exists."),
}

# ---------------------------------------------------------------- 12.0
P0 = {
 'title': "The Mongols and the Black Death", 'sub': "c. 1250 to 1500",
 'lede': "In the 13th century the Mongols built the largest contiguous land empire in history. Their rule linked China, Iran, Russia and the Middle East, and in the 14th century a plague from the steppe killed a large part of the population from Europe to Egypt. This chapter follows both stories and the worlds that recovered afterwards.",
 'body': [
  "Chinggis Khan and his heirs conquered an empire of some 23 million square km. [[c-mongol-area]] Janet Abu-Lughod argued that Mongol rule tied Eurasia into a single 'world system' of trade, and that plague and the Mongols' loss of China helped break it apart; Europe's later dominance, she argued, was no historical necessity. [[c-abulughod]]",
  "Our sources come from every side. The Secret History of the Mongols gives the Mongols' own view; [[c-secret-history]] Rashid al-Din, a convert from Judaism who served the Mongol rulers of Iran, wrote their history from within their court; [[c-rashid]] and the traveller Ibn Battuta saw the plague at first hand in Syria. [[c-ibnbattuta]]",
  "Science now adds evidence no chronicler could. Ancient DNA has identified the Black Death's cause, [[c-bd-genome]] lead in Alpine ice shows mining stopping as the plague struck, [[c-lead-plague]] and tree rings record the cold summers that came just before it. [[c-bluerings]]",
  {'table': {'head': ["Evidence", "What it shows"], 'rows': [
    ["The Secret History", "the Mongols' own account (12.1)"],
    ["Rashid al-Din", "the Mongol court in Iran (12.2)"],
    ["Ibn Battuta", "a traveller's eyewitness view of the plague"],
    ["Ancient DNA", "the cause and origin of the Black Death (12.3)"],
    ["Ice cores and tree rings", "mining collapse; cold summers before the plague"]], 'note': "[[c-secret-history]] [[c-rashid]] [[c-ibnbattuta]] [[c-bd-genome]] [[c-lead-plague]] [[c-bluerings]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 57.0, 'lat': 42.0, 'zoom': 2.2}, 'caption': "The Mongol world and the plague, c. 1250-1350", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [105.0, 34.0], 'label': 'YUAN', 'size': 10}, {'ll': [52.0, 34.5], 'label': 'ILKHANATE', 'size': 9}, {'ll': [52.0, 52.0], 'label': 'GOLDEN HORDE', 'size': 9}, {'ll': [64.0, 45.0], 'label': 'CHAGATAI', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [102.83, 47.2], 'label': 'Karakorum', 'date': 'Mongol capital', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '12.0 · the empire', 'title': 'The Mongol empire', 'sub': '13th century', 'text': "[[c-mongol-area]] [[c-secret-history]] [[c-abulughod]]", 'sources': ['brit-mongol-empire', 'whe-secret', 'wch-abulughod']}},
    {'ll': [46.29, 38.08], 'label': 'Tabriz', 'date': 'Rashid al-Din', 'acc': True, 'dy': -8, 'plate': {'kicker': '12.0 · sources', 'title': 'Rashid al-Din', 'sub': '1247-1318', 'text': "[[c-rashid]]", 'sources': ['brit-rashid']}},
    {'ll': [36.29, 33.51], 'label': 'Damascus', 'date': 'Ibn Battuta, 1348', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '12.0 · witnesses', 'title': 'Ibn Battuta', 'sub': '1348', 'text': "[[c-ibnbattuta]]", 'sources': ['brit-ibnbattuta']}},
    {'ll': [-0.07, 51.51], 'label': 'London', 'date': 'plague genome', 'acc': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '12.0 · DNA', 'title': 'The plague genome', 'sub': '2011', 'text': "[[c-bd-genome]]", 'sources': ['natgeo-bd']}},
    {'ll': [7.88, 45.93], 'label': 'Colle Gnifetti', 'date': 'ice core', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.0 · ice', 'title': 'Lead in Alpine ice', 'sub': '1349-53', 'text': "[[c-lead-plague]] [[c-bluerings]]", 'sources': ['agu-lead', 'cam-volcano']}},
    {'ll': [74.62, 42.83], 'label': 'Chüy valley', 'date': 'plague graves, 1338-39', 'acc': True, 'dy': 16},
    {'ll': [116.4, 39.9], 'label': 'Dadu (Beijing)', 'dy': 16}]}]},
 'practice': [
  q("Which evidence most directly identifies the cause of the Black Death?",
    ["Yersinia pestis DNA from a London plague cemetery", "Ibn Battuta's eyewitness account of plague in Syria", "The fall in lead in an Alpine ice core in 1349-53", "Blue rings in Pyrenean trees from 1345 to 1347"], 0,
    "In 2011 scientists reconstructed the bacterium's genome from a London plague cemetery: a recovered genome identifies the pathogen itself.",
    {1: "He saw the Black Death in Syria in 1348, but a traveller's account cannot identify a microbe.", 2: "The lead record shows that mining and smelting stopped, not which disease stopped them.", 3: "The blue rings record cold, wet summers before the plague, not its cause."}),
  q("What did Janet Abu-Lughod's 'world system' model mainly challenge?",
    ["The idea that Europe's later dominance was inevitable", "The idea that the Mongol empire made Eurasian trade possible", "The idea that plague helped break up Eurasian trade", "The idea that trade circuits linked Europe and China"], 0,
    "She described a Eurasian trading system of about 1250-1350, made possible by Mongol rule, and argued that Europe's later dominance was not an 'inherent historical necessity'.",
    {1: "Her model holds that the system was made possible by the Mongol empire.", 2: "She herself linked the system's breakdown to plague and other epidemics.", 3: "Her eight overlapping circuits of trade are exactly such links."})]}

# ---------------------------------------------------------------- 12.1
P1 = {
 'title': "Chinggis Khan and the conquests", 'sub': "1206 to 1227",
 'lede': "A Mongol chief named Temüjin united the peoples of the steppe, took the title Chinggis Khan and led his armies into China and Central Asia. Within two decades he had destroyed some of the great cities of the Islamic world. How to weigh that destruction against what followed is still argued over.",
 'body': [
  "Temüjin's birth year is uncertain. [[c-temujin]] In 1206 a great assembly proclaimed him Chinggis Khan, [[c-kuriltai]] and he organised his army in units of tens. [[c-decimal]] He attacked the Jin dynasty of northern China in 1211 and took Beijing in 1215. [[c-jin]]",
  "Then he turned west. When a governor of the Khwarazmian empire massacred a caravan sent under his protection, Chinggis invaded; Bukhara, Samarkand and Urgench were sacked, [[c-khwarazm]] and Merv was destroyed and never recovered its old prosperity. [[c-merv]] He died in 1227. [[c-death1227]]",
  "Chroniclers recorded enormous slaughter, but no one can count the dead, [[c-tolls]] and historians disagree about how to balance the empire's destruction against the order it later imposed. [[c-may]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["1155, 1162 or 1167", "Temüjin born"],
    ["1206", "proclaimed Chinggis Khan"],
    ["1211", "war on the Jin begins"],
    ["1215", "Beijing taken"],
    ["1220-21", "Bukhara, Samarkand, Urgench, Merv"],
    ["1227", "death of Chinggis Khan"]], 'note': "[[c-temujin]] [[c-kuriltai]] [[c-jin]] [[c-khwarazm]] [[c-merv]] [[c-death1227]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 88.0, 'lat': 42.0, 'zoom': 5.0}, 'caption': "The conquests of Chinggis Khan, 1206-1227", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [104.0, 45.5], 'label': 'MONGOLIA', 'size': 10}, {'ll': [112.0, 36.0], 'label': 'JIN', 'size': 9}, {'ll': [60.5, 45.5], 'label': 'KHWARAZM', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [110.8, 48.8], 'label': 'Onon River', 'date': 'assembly, 1206', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '12.1 · 1206', 'title': 'Chinggis Khan', 'sub': '1206', 'text': "[[c-temujin]] [[c-kuriltai]] [[c-decimal]] [[c-death1227]]", 'sources': ['brit-genghis']}},
    {'ll': [116.4, 39.9], 'label': 'Zhongdu (Beijing)', 'date': 'taken 1215', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '12.1 · China', 'title': 'The Jin', 'sub': '1211-1215', 'text': "[[c-jin]]", 'sources': ['brit-genghis']}},
    {'ll': [68.3, 42.85], 'label': 'Otrar', 'date': 'caravan massacred', 'acc': True, 'dy': -8, 'plate': {'kicker': '12.1 · Khwarazm', 'title': 'The war on Khwarazm', 'sub': '1219-1221', 'text': "[[c-khwarazm]] [[c-tolls]] [[c-may]]", 'sources': ['brit-genghis', 'brit-mongol-empire', 'jiiph2014', 'national-jackson', 'reaktion-may']}},
    {'ll': [64.42, 39.77], 'label': 'Bukhara', 'date': '1220', 'anchor': 'end', 'dy': -6},
    {'ll': [66.96, 39.65], 'label': 'Samarkand', 'date': '1220', 'dy': 16},
    {'ll': [59.15, 42.32], 'label': 'Urgench', 'date': '1221', 'anchor': 'end', 'dy': -6},
    {'ll': [62.19, 37.66], 'label': 'Merv', 'date': 'destroyed 1221', 'acc': True, 'dy': 16, 'plate': {'kicker': '12.1 · Merv', 'title': 'Merv', 'sub': '1221', 'text': "[[c-merv]]", 'sources': ['brit-merv']}},
    {'ll': [58.8, 36.21], 'label': 'Nishapur', 'anchor': 'end', 'dy': 16}]}]},
 'practice': [
  q("Why do historians treat the enormous death tolls in medieval accounts of the Mongol conquests with caution?",
    ["The deaths cannot be checked, and one study finds fewer", "The Mongols left Bukhara and Samarkand largely intact", "Merv recovered its old prosperity within a decade", "Excavations have since produced exact counts of the dead"], 0,
    "The destruction is not in doubt; its scale is. No one can count the dead, and a 2014 Iranian study argues the actual 'rate of murder and pillage' was 'much lower' than some historians claim.",
    {1: "Bukhara, Samarkand and Urgench were taken and sacked in 1220-21.", 2: "Merv was destroyed in 1221 and never regained its former prosperity.", 3: "How many people the conquests killed is unknown; no one can count the dead."}),
  q("What provoked Chinggis Khan's war on the Khwarazmian empire?",
    ["Otrar's governor massacred a Mongol-protected caravan", "Khwarazm's seizure of Beijing from the Jin in 1215", "The sack of a Mongol caravan by the people of Merv", "A Khwarazmian army's invasion of the Mongols' homeland"], 0,
    "After the governor of Otrar massacred a caravan sent under Mongol protection, Chinggis invaded: the war in the west began with an attack on traders.",
    {1: "Beijing was taken by the Mongols themselves, from the Jin, in 1215.", 2: "The caravan was massacred by the governor of Otrar; Merv was destroyed later, in 1221.", 3: "The war began with the massacre of a caravan at Otrar, after which Chinggis invaded Khwarazm."})]}

# ---------------------------------------------------------------- 12.2
P2 = {
 'title': "The khanates and the Pax Mongolica", 'sub': "c. 1250 to 1368",
 'lede': "Chinggis Khan's descendants divided his empire. One sacked Baghdad and killed its Abbasid caliph, another ruled the Russian lands from the steppe, and Khubilai Khan made himself emperor of China. Under Mongol rule merchants, monks and envoys crossed Eurasia, and some wrote about what they saw.",
 'body': [
  "In 1258 Hülegü sacked Baghdad and put to death al-Musta'sim, the last Abbasid caliph in Baghdad, [[c-baghdad1258]] but two years later the Mamluks of Egypt stopped the Mongols at Ain Jalut. [[c-ainjalut]] Hülegü's descendants ruled Iran, and one of them, Ghazan, became a Muslim in 1295. [[c-ghazan]]",
  "On the western steppe the Golden Horde ruled the Russian principalities through their own princes, who collected its tribute. [[c-goldenhorde]] Russian tradition remembers this as the 'Tatar yoke', a view historians have challenged, [[c-yoke]] and the phrase itself appears in Slavic writing only in the later 17th century, although Latin writers used it as early as the 13th. [[c-yoke-term]]",
  "In China, Khubilai founded the Yuan dynasty and completed the conquest of the Song, [[c-khubilai]] though his invasions of Japan failed. [[c-japan]] Travellers crossed the empire in both directions: the friar William of Rubruck reached Karakorum, [[c-rubruck]] the monk Rabban Sauma travelled to Europe for the Mongol ruler of Iran, [[c-sauma]] and Marco Polo described the court of Khubilai, though whether he really went there is debated. [[c-polo]]",
  {'table': {'head': ["Khanate", "Ruled", "Notable"], 'rows': [
    ["Yuan", "China, Mongolia", "Khubilai; Dadu (Beijing); paper money"],
    ["Ilkhanate", "Iran, Iraq", "Baghdad 1258; Ghazan becomes Muslim 1295"],
    ["Golden Horde", "western steppe, the Rus'", "tribute through Russian princes; Kulikovo 1380"],
    ["Chagatai", "Central Asia", "between the Yuan and the Ilkhanate"]], 'note': "[[c-khubilai]] [[c-baghdad1258]] [[c-ghazan]] [[c-goldenhorde]] [[c-mongol-area]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 75.0, 'lat': 43.0, 'zoom': 2.9}, 'caption': "The Mongol khanates, c. 1260-1368", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [108.0, 33.0], 'label': 'YUAN', 'size': 10}, {'ll': [58.0, 33.0], 'label': 'ILKHANATE', 'size': 9}, {'ll': [55.0, 53.5], 'label': 'GOLDEN HORDE', 'size': 9}, {'ll': [76.0, 41.0], 'label': 'CHAGATAI', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [44.36, 33.31], 'label': 'Baghdad', 'date': 'sacked 1258', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '12.2 · 1258', 'title': 'The fall of Baghdad', 'sub': 'February 1258', 'text': "[[c-baghdad1258]]", 'sources': ['brit-mustasim']}},
    {'ll': [35.36, 32.55], 'label': 'Ain Jalut', 'date': '1260', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '12.2 · 1260', 'title': 'Ain Jalut', 'sub': '3 September 1260', 'text': "[[c-ainjalut]]", 'sources': ['brit-ainjalut']}},
    {'ll': [46.29, 38.08], 'label': 'Tabriz', 'date': 'Ilkhanid capital', 'acc': True, 'dy': -8, 'plate': {'kicker': '12.2 · Iran', 'title': 'Ghazan', 'sub': '1295', 'text': "[[c-ghazan]] [[c-sauma]]", 'sources': ['brit-ghazan', 'brit-rashid', 'gorgias-sauma']}},
    {'ll': [47.43, 47.18], 'label': 'Sarai', 'date': 'Golden Horde', 'acc': True, 'dy': 16, 'plate': {'kicker': "12.2 · the Rus'", 'title': 'The Golden Horde', 'sub': '1240s-1502', 'text': "[[c-goldenhorde]] [[c-yoke]] [[c-yoke-term]]", 'sources': ['brit-goldenhorde', 'ihr-ostrowski', 'halperin2025']}},
    {'ll': [38.67, 53.67], 'label': 'Kulikovo', 'date': '1380', 'anchor': 'end', 'dy': -6},
    {'ll': [102.83, 47.2], 'label': 'Karakorum', 'date': 'Rubruck, 1254', 'acc': True, 'dy': -8, 'plate': {'kicker': '12.2 · travellers', 'title': 'William of Rubruck', 'sub': '1253-55', 'text': "[[c-rubruck]]", 'sources': ['uw-rubruck']}},
    {'ll': [116.4, 39.9], 'label': 'Dadu (Beijing)', 'date': 'Yuan capital', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '12.2 · Yuan', 'title': 'Khubilai Khan', 'sub': '1271-1294', 'text': "[[c-khubilai]] [[c-polo]]", 'sources': ['brit-kublai', 'routledge-wood', 'tuebingen-vogel']}},
    {'ll': [130.4, 33.6], 'label': 'Hakata Bay', 'date': '1274, 1281', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '12.2 · Japan', 'title': 'The invasions of Japan', 'sub': '1274 and 1281', 'text': "[[c-japan]]", 'sources': ['brit-kublai', 'arch-kamikaze']}}]}]},
 'practice': [
  q("What does Donald Ostrowski's revision of the 'Tatar yoke' mainly argue?",
    ["Muscovy mostly flourished and borrowed from the Horde", "The Horde took no tribute from the Russian princes", "The Horde converted the Russian princes to Islam", "The yoke ruined Muscovy, as Marxist historians had held"], 0,
    "His reviewer, Will Ryan, says he argues 'that after an initial period of deprivation Muscovy for the most part flourished', and that it took its 'dual structure' of administration from the Horde.",
    {1: "Russian princes, above all those of Moscow, collected tribute for the Horde.", 2: "The Horde itself became Muslim under Öz Beg; the Rus' did not.", 3: "That is the older view; Ostrowski notes its appeal to Russian nationalists and Marxist historians."}),
  q("Which evidence best supports Hans Ulrich Vogel's view that Marco Polo really was in China?",
    ["His exact account of paper money and salt making", "His careful description of the Great Wall's course", "His account of tea-drinking and foot-binding", "Chinese court records that name him as an official"], 0,
    "Vogel finds that Polo alone described 'precisely how paper for money was made', and that his account of salt production 'checks out with Chinese documents'.",
    {1: "His book does not mention the Great Wall, one of Frances Wood's arguments against him.", 2: "Wood points out that his book mentions neither tea nor foot-binding.", 3: "Vogel's case rests on Polo's descriptions checking out against Chinese documents, not on records naming him."})]}

# ---------------------------------------------------------------- 12.3
P3 = {
 'title': "The Black Death", 'sub': "1338 to 1353",
 'lede': "In the 1340s a plague reached the Mediterranean from the steppe and spread across Europe, North Africa and the Middle East. Ancient DNA has confirmed its cause and probable origin, but how it travelled and how many it killed are still being worked out.",
 'body': [
  "Graves in Kyrgyzstan dated 1338-39 have yielded the strain of plague from which the pandemic's lineages branched out. [[c-origin]] How it reached the Black Sea is less clear: one Arabic account of its rapid spread may be literature rather than report, [[c-ibnwardi]] and the famous story of corpses hurled into besieged Caffa may not explain its arrival in Europe. [[c-caffa]] A new hypothesis links its arrival to grain shipped to Italy after a volcanic eruption and failed harvests. [[c-grain]]",
  "Between 1347 and 1351 the plague killed a larger share of Europe's people than any earlier epidemic or war. [[c-bd-europe]] Estimates of how large a share range from about a third to about 60 percent, [[c-mortality]] and pollen evidence suggests some regions lost far more than others. [[c-pollen]]",
  "The plague also struck the Islamic world. In Egypt and Syria it kept returning, and its recurrences slowed population growth for a century and a half. [[c-dols]]",
  {'table': {'head': ["Date", "Event"], 'rows': [
    ["1338-39", "plague deaths in the Chüy valley, Kyrgyzstan"],
    ["c. 1345", "probable volcanic eruption; cold summers 1345-47"],
    ["1346", "siege of Caffa"],
    ["1347", "Italian cities import grain from the Golden Horde"],
    ["1347-51", "the Black Death in Europe"],
    ["1348", "plague in Syria"]], 'note': "[[c-origin]] [[c-grain]] [[c-caffa]] [[c-bd-europe]] [[c-ibnbattuta]]"}}],
 'figure': {'kind': 'chart', 'chart': 'bars', 'caption': "How many died?", 'title': "Estimated share of Europe's population killed by the Black Death, percent",
  'max': 70, 'ticks': [0, 10, 20, 30, 40, 50, 60, 70], 'axis': "percent of the population; midpoints of each estimate", 'hint': "Hover a bar",
  'rows': [
   {'t': 'Philip Ziegler', 'v': 35, 'lab': '30-40%', 'tip': 'older estimate'},
   {'t': 'Robert Gottfried', 'v': 45, 'lab': '40-50%'},
   {'t': 'Rosemary Horrox', 'v': 47.5, 'lab': '47-48%'},
   {'t': 'Ole Benedictow', 'v': 60, 'lab': 'about 60%', 'acc': True, 'plate': {'kicker': '12.3 · mortality', 'title': 'How many died?', 'sub': '1347-51', 'text': "[[c-mortality]] [[c-pollen]]", 'sources': ['arthur2010', 'boydell-benedictow', 'reading-pollen']}}],
  'notes': ["Sources: Arthur (2010); Benedictow.", "Pollen data (2022) show wide regional variation."]},
 'practice': [
  q("What does the 2022 pollen study most directly imply about a single figure such as Benedictow's 60 percent?",
    ["One European figure hides big regional differences", "Benedictow's 60 percent applies evenly across Europe", "Mortality was highest in Ireland and in Iberia", "It proves Ziegler's 30-40 percent was too low"], 0,
    "Pollen shows farming collapsing in Scandinavia, France, south-western Germany, Greece and central Italy, but continuing or growing in Ireland, Iberia and much of central and eastern Europe.",
    {1: "The study challenges the idea of uniformly high mortality across Europe.", 2: "Farming continued or grew in Ireland and Iberia.", 3: "The pollen study shows regional variation; it does not settle the overall figure."}),
  q("Why are the gravestones of 1338-39 in Kyrgyzstan important?",
    ["They date and place the plague's parent strain", "They prove the Mongols hurled corpses at Caffa", "They record the first plague deaths in Europe", "They show the plague began in southern China"], 0,
    "Their graves contain the plague strain from which the Black Death's lineages branched out, and the tombstones date the deaths: dated inscriptions plus a genome point to Central Asia.",
    {1: "Caffa is in Crimea, and its story rests on Gabriele de' Mussis's written account.", 2: "Kyrgyzstan is in Central Asia; Europe's epidemic began in 1347.", 3: "The Tian Shan region of Central Asia is the strongest candidate for the origin."})]}

PAGES = [P0, P1, P2, P3]
