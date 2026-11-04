# Chapter 11, pages 11.4 to 11.7. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 11.4
 'brit-anlushan': ("Encyclopaedia Britannica, \"An Lushan\"", "https://www.britannica.com/biography/An-Lushan"),
 'carter-anlushan': ("James Carter, \"The end of China's golden age\", The China Project (2021)", "https://thechinaproject.com/2021/02/03/the-end-of-chinas-golden-age/"),
 'brit-song-sum': ("Encyclopaedia Britannica, \"Song dynasty\" summary", "https://www.britannica.com/summary/Song-dynasty"),
 'brit-song-culture': ("Encyclopaedia Britannica, \"China: Song culture\"", "https://www.Britannica.Com/place/China/Song-culture"),
 'standard-jiaozi': ("The Standard (Hong Kong), \"China celebrates paper currency anniversary\" (2024)", "https://www.thestandard.com.hk/news/article/59501/China-celebrates-paper-currency-anniversary"),
 'ox-diamond': ("History of Science Museum, Oxford, \"World's earliest dated printed book: the Diamond Sutra, 868 CE\"", "https://www.cabinet.ox.ac.uk/worlds-earliest-dated-printed-book-diamond-sutra-868-ce"),
 'hartwell1962': ("Robert Hartwell, \"A revolution in the Chinese iron and coal industries during the Northern Sung\", Journal of Asian Studies 21 (1962)", "https://www.cambridge.org/core/journals/journal-of-asian-studies/article/revolution-in-the-chinese-iron-and-coal-industries-during-the-northern-sung-9601126-ad/C4ED428E19B0A04C7225BB57822C89DF"),
 'wagner2001': ("Donald B. Wagner, \"Blast furnaces in Song-Yuan China\", East Asian Science, Technology and Medicine 18 (2001)", "https://core.ac.uk/download/228877749.pdf"),
 'brit-sishu': ("Encyclopaedia Britannica, \"Sishu\" (the Four Books)", "https://britannica.com/topic/Sishu"),
 # 11.5
 'brit-charlemagne800': ("Encyclopaedia Britannica, \"Charlemagne: Emperor of the Romans\"", "https://www.britannica.com/biography/Charlemagne/Emperor-of-the-Romans"),
 'lancaster-minuscule': ("Meg Twycross, Lancaster University palaeography course, Carolingian minuscule", "https://www.lancaster.ac.uk/users/yorkdoom/palweb/week10/palwk10.htm"),
 'medievalists-hodges': ("Medievalists.net, on Richard Hodges, \"Charlemagne minus Mohammed\" (lecture, 2013)", "https://www.medievalists.net/2014/01/charlemagne-minus-mohammed/"),
 'cup-mccormick': ("Michael McCormick, Origins of the European Economy (Cambridge, 2001), introduction", "https://www.cambridge.org/core/books/origins-of-the-european-economy/at-the-origins-of-the-european-economy/AF2FC5D16AF96CB00BEDDC0798416461"),
 'medievalists-brown': ("Medievalists.net, excerpt of Elizabeth A. R. Brown, \"The tyranny of a construct\" (1974)", "https://www.medievalists.net/2013/12/the-tyranny-of-a-construct-feudalism-and-historians-of-medieval-europe/"),
 'oup-reynolds': ("Oxford Academic, Susan Reynolds, Fiefs and Vassals (1994)", "https://academic.oup.com/book/47420"),
 'brit-cluny': ("Encyclopaedia Britannica, \"Cluny\"", "https://www.Britannica.Com/place/Cluny-France"),
 'brit-investiture': ("Encyclopaedia Britannica, \"Investiture Controversy\"", "https://www.britannica.com/event/Investiture-Controversy"),
 # 11.6
 'eh-lindisfarne': ("English Heritage, on the Viking raid on Lindisfarne", "https://www.english-heritage.org.uk/administration/z-archive/04-learn-archive/old-viking-raid"),
 'shm-spillings': ("Swedish History Museum, \"The world's largest Viking treasure\" (the Spillings hoard)", "https://historiska.se/en/explore-history/history-hub/the-worlds-largest-viking-treasure/"),
 'brit-rurik': ("Encyclopaedia Britannica, \"Rurik\"", "https://britannica.com/topic/Rurik"),
 'eu-normanist': ("Encyclopedia of Ukraine, \"Normanist theory\"", "https://www.encyclopediaofukraine.com/pages%5CN%5CO%5CNormanisttheory.htm"),
 'unesco-thingvellir': ("UNESCO World Heritage Centre, \"Þingvellir National Park\"", "https://whc.unesco.org/en/list/1152"),
 'unesco-lanse': ("UNESCO World Heritage Centre, \"L'Anse aux Meadows National Historic Site\"", "https://whc.unesco.org/en/list/4"),
 'kuitems2021': ("Kuitems et al., \"Evidence for European presence in the Americas in AD 1021\", Nature 601 (2022; online 2021), PMC", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8770119"),
 'margaryan2020': ("Margaryan et al., \"Population genomics of the Viking world\", Nature 585 (2020), Royal Danish Library record", "https://pure.kb.dk/en/publications/population-genomics-of-the-viking-world-3/"),
 'medievalists-speidel': ("Medievalists.net, on Speidel et al., Nature (2025)", "https://www.medievalists.net/2025/01/new-genetic-study-maps-early-medieval-migrations-across-europe/"),
 'ajpa-birka': ("Hedenstierna-Jonson et al., \"A female Viking warrior confirmed by genomics\", American Journal of Physical Anthropology (2017), abstract", "https://zendy.io/title/10.1002/ajpa.23308"),
 'price2019': ("Price et al., \"Viking warrior women? Reassessing Birka chamber grave Bj.581\", Antiquity 93 (2019)", "https://core-prod.cambridgecore.org/core/services/aop-cambridge-core/content/view/7CC691F69FAE51DDE905D27E049FADCD/S0003598X18002582a.pdf/viking_warrior_women_reassessing_birka_chamber_grave_bj581.pdf"),
 'jesch-birka': ("Judith Jesch, on the Birka 'warrior woman' (oldnorse.org)", "https://oldnorse.org/portfolio/viking-warrior-women-judith-jesch-an-expert-in-viking-studies-examines-the-latest-evidence/"),
 # 11.7
 'brit-iconoclasm': ("Encyclopaedia Britannica, \"Iconoclastic Controversy\"", "https://britannica.com/event/Iconoclastic-Controversy"),
 'brit-byz867': ("Encyclopaedia Britannica, \"Byzantine Empire: from 867 to the Ottoman conquest\"", "https://www.britannica.com/place/Byzantine-Empire/From-867-to-the-Ottoman-conquest"),
 'brit-cyril': ("Encyclopaedia Britannica, \"Saints Cyril and Methodius\"", "https://britannica.com/biography/Saints-Cyril-and-Methodius"),
 'brit-vladimir': ("Encyclopaedia Britannica, \"Vladimir I\"", "https://www.britannica.com/biography/Vladimir-I"),
 'medievalists-basil': ("Georgios Theotokis, \"Did Basil II blind 15,000 Bulgarian prisoners?\", Medievalists.net (2022)", "https://www.medievalists.net/2022/08/basil-ii-bulgar-slayer-blind-15000-prisoners/"),
 'drm-stephenson': ("Timothy May, review of Paul Stephenson, The Legend of Basil the Bulgar-Slayer, De Re Militari", "https://deremilitari.org/REVIEWS/Stephenson_basil.htm"),
 'brit-schism': ("Encyclopaedia Britannica, \"Christianity: the Photian schism and the great East-West schism\"", "https://www.britannica.com/topic/Christianity/The-Photian-schism-and-the-great-East-West-schism"),
 'vatican-2025': ("Joint Declaration of Pope Leo XIV and Ecumenical Patriarch Bartholomew (29 November 2025)", "https://www.vatican.va/content/leo-xiv/en/travels/2025/documents/20251129-dichiarazione-congiunta.html"),
 'bg-exodus20': ("Exodus 20:4, New Revised Standard Version Updated Edition, BibleGateway", "https://www.biblegateway.com/passage/?search=Exodus%2020%3A4&version=NRSVUE"),
 'brit-manzikert': ("Encyclopaedia Britannica, \"Battle of Manzikert\"", "https://britannica.com/event/Battle-of-Manzikert"),
}

C = {
 # 11.4
 'c-anlushan': c("Late in 755 the general An Lushan rebelled, and within a month took Luoyang; the revolt was finally put down in 763, but warlords held much of China until the Song reunified it in 960.", 'consensus', ['brit-anlushan'], show=False),
 'c-anlushan-toll': c("Some writers, among them Steven Pinker, say the rebellion killed 36 million people.", 'debated', ['carter-anlushan'], "The figure comes from the fall in registered population, which historians say reflects migration and the collapse of record-keeping as well as deaths; it is generally considered too high."),
 'c-song': c("The Song dynasty ruled all China from 960 until 1127 and the south until 1279; it sent ever more candidates through the civil-service examinations, and paper money came into growing use.", 'consensus', ['brit-song-sum'], show=False),
 'c-champa-rice': c("Early-ripening rice from Champa (in today's Vietnam), introduced in the 11th century, allowed two crops a year in the south and helped feed a population of more than 100 million.", 'approx', ['brit-song-culture'], "The population is a round estimate from the registers."),
 'c-jiaozi': c("Merchants in Sichuan issued paper notes called jiaozi; in 1024 the Song government took over their issue, the first government paper money.", 'approx', ['standard-jiaozi'], "China marked the millennium in 2024."),
 'c-diamond': c("The Diamond Sutra found at Dunhuang, printed from woodblocks and dated 11 May 868, is the world's earliest dated printed book.", 'consensus', ['ox-diamond'], show=False),
 'c-hartwell': c("In 1962 Robert Hartwell argued that the Northern Song had an iron and coal 'revolution', estimating iron output in 1078 at about 75,000 tons, later raised to about 125,000.", 'debated', ['hartwell1962', 'wagner2001'], "Donald Wagner finds the size of the figure 'quite credible' but Hartwell's method 'seriously flawed', following Yoshida Mitsukuni; the idea of a Song 'industrial revolution' remains contested."),
 'c-zhuxi': c("Zhu Xi published the 'Four Books' of Confucianism with his commentaries in 1190; they were the syllabus of the civil-service examinations from 1313 to 1905.", 'consensus', ['brit-sishu'], show=False),
 # 11.5
 'c-coronation800': c("On Christmas Day 800 Pope Leo III crowned Charlemagne emperor in St Peter's in Rome.", 'consensus', ['brit-charlemagne800'], show=False),
 'c-coronation-intent': c("Charlemagne's biographer Einhard says he would not have entered St Peter's had he known what was planned.", 'debated', ['brit-charlemagne800'], "Britannica judges that 'the evidence leaves little doubt that king and pope collaborated in planning the coronation'."),
 'c-minuscule': c("Carolingian minuscule, a clear script, was created partly under Charlemagne's patronage, and most of our knowledge of classical literature comes from copies made at his court.", 'consensus', ['lancaster-minuscule'], show=False),
 'c-pirenne': c("Henri Pirenne argued that the Islamic conquests closed the Mediterranean and so forced the West inland: 'without Mohammed Charlemagne would have been inconceivable'.", 'debated', ['medievalists-hodges'], "Archaeologists Richard Hodges and David Whitehouse reply that the collapse of the Roman Mediterranean 'clearly predated Mohammed'."),
 'c-mccormick': c("Michael McCormick's study of travellers and trade found that by 800 'multiple circuits were connecting again', carried now mostly by western traders, with slaves a major export from Europe.", 'debated', ['cup-mccormick', 'medievalists-hodges'], "A revision of Pirenne; the scale of the slave trade is still debated."),
 'c-feudalism': c("Some historians reject the word 'feudalism'.", 'debated', ['medievalists-brown', 'oup-reynolds'], "Elizabeth A. R. Brown (1974) called it a 'tyranny of a construct' that makes historians dismiss inconvenient documents; Susan Reynolds (1994) challenged the standard model of fiefs and vassals. Others still find the term useful as shorthand."),
 'c-cluny': c("The monastery of Cluny in Burgundy, founded in 910, answered to no authority but the pope's and led a wide movement of monastic reform.", 'consensus', ['brit-cluny'], show=False),
 'c-investiture': c("Pope Gregory VII banned lay rulers, kings included, from investing bishops; the German king Henry IV was excommunicated and in 1077 did penance before the pope at Canossa. The Concordat of Worms (1122) ended the dispute with a compromise.", 'consensus', ['brit-investiture'], show=False),
 # 11.6
 'c-lindisfarne': c("On 8 June 793 'heathen men' sacked the monastery of Lindisfarne off the Northumbrian coast. It was not the first Viking raid on England, but it sent a shockwave through Europe.", 'consensus', ['eh-lindisfarne'], show=False),
 'c-spillings': c("The Spillings hoard, found on Gotland in 1999, holds about 76 kg of silver and bronze, mostly Arabic coins (dirhams); the youngest dates to 870.", 'consensus', ['shm-spillings'], show=False),
 'c-rurik': c("The Rus' chronicle says the Scandinavian Rurik was invited to rule Novgorod in 862.", 'tradition', ['brit-rurik'], "Britannica calls him 'semilegendary'; the story is not accepted at face value."),
 'c-normanist': c("Whether Scandinavians founded the state of the Rus' has been argued for three centuries.", 'debated', ['eu-normanist'], "'Normanists' credit Scandinavians; 'anti-Normanists', from Lomonosov to Mykhailo Hrushevsky, stress local Slavic origins. Most Western scholars accept a substantial Scandinavian role; in the Soviet Union, anti-Normanist views were officially sanctioned from the 1930s."),
 'c-althing': c("Iceland's assembly, the Althing, met in the open air at Þingvellir from about 930 until 1798.", 'approx', ['unesco-thingvellir'], "The founding date comes from Icelandic tradition."),
 'c-lanse': c("L'Anse aux Meadows in Newfoundland is an 11th-century Norse settlement, the earliest evidence of Europeans in the Americas; wood cut there with metal tools was felled in 1021.", 'consensus', ['unesco-lanse', 'kuitems2021'], show=False),
 'c-1021-method': c("The exact year comes from a spike in atmospheric radiocarbon caused by a cosmic-ray event in 993, which marks a single tree ring; counting rings outward gives the year of felling.", 'consensus', ['kuitems2021'], show=False),
 'c-margaryan': c("A 2020 study of 442 ancient genomes found that Vikings in England were mostly of Danish descent, in the eastern Baltic mostly Swedish, and in Ireland, Iceland and Greenland mostly Norwegian.", 'consensus', ['margaryan2020'], show=False),
 'c-speidel-viking': c("A 2025 study of over 1,500 genomes found that ancestry from central Europe had become prominent in southern Scandinavia by the Viking Age.", 'approx', ['medievalists-speidel'], "New; known here through a report of the Nature paper."),
 'c-birka': c("A richly armed 10th-century grave at Birka in Sweden (Bj 581) was shown by DNA in 2017 to belong to a woman.", 'debated', ['ajpa-birka', 'price2019', 'jesch-birka'], "Neil Price and colleagues read her as 'a woman who lived as a professional warrior', and allow a symbolic reading; Judith Jesch thinks they 'make too much of rather slim evidence'."),
 # 11.7
 'c-iconoclasm': c("From the 720s Byzantine emperors banned religious images (icons), citing the commandment against images; a council at Nicaea restored them in 787, a second ban followed in 814, and icons were restored for good in 843.", 'consensus', ['brit-iconoclasm'], show=False),
 'c-macedonian': c("The Macedonian dynasty, from 867, brought a renaissance in Byzantine learning; under Basil II the empire covered more of Europe than at any time since Justinian.", 'consensus', ['brit-byz867'], show=False),
 'c-cyril': c("In 863 the brothers Cyril and Methodius went to Great Moravia, invented the Glagolitic alphabet for Slavic, and translated scripture into the language later called Old Church Slavonic.", 'consensus', ['brit-cyril'], show=False),
 'c-vladimir': c("Vladimir of Kyiv agreed to become Christian in about 987-988 as part of a pact to marry the emperor Basil II's sister Anne, after seizing the Byzantine city of Chersonesus.", 'approx', ['brit-vladimir'], "The chronicle story of Vladimir weighing Islam, Judaism and Christianity before choosing is, in Britannica's words, 'apparently mythically symbolic'."),
 'c-basil-blind': c("A chronicle says Basil II blinded about 15,000 Bulgarian prisoners in 1014, and he is remembered as 'Bulgar-slayer'.", 'debated', ['medievalists-basil', 'drm-stephenson'], "Historians think the number exaggerated; Georgios Theotokis notes that the name 'Bulgar-slayer' is not attested until some three centuries later, and Paul Stephenson argues that in his lifetime Basil had no wish to be seen as the 'Bulgar-slayer' and that the name owes much to twelfth-century attitudes to the Bulgars."),
 'c-1054': c("On 16 July 1054 papal legates led by Cardinal Humbert laid a bull excommunicating Patriarch Michael Cerularius on the altar of Hagia Sophia; among its charges was the Greek use of leavened bread in the Eucharist.", 'consensus', ['brit-schism'], show=False),
 'c-1054-meaning': c("At the time 1054 looked like 'a minor storm in which both sides had behaved with some arrogance'; only later was it seen as the final break between East and West.", 'debated', ['brit-schism'], "Britannica describes the break as growing as 'Greeks and Latins became more estranged'; only in hindsight was 1054 seen as 'the moment of the final breach'."),
 'c-1965-2025': c("The excommunications were lifted in 1965, and in a joint declaration on 29 November 2025 Pope Leo XIV and Patriarch Bartholomew renewed their hope for 'full communion'.", 'consensus', ['vatican-2025'], show=False),
 'c-exodus-20-4': c("'You shall not make for yourself an idol, whether in the form of anything that is in heaven above or that is on the earth beneath or that is in the water under the earth' (Exodus 20:4, NRSVUE).", 'tradition', ['bg-exodus20', 'brit-iconoclasm'], "Britannica notes the iconoclasts cited this Old Testament prohibition; Jewish and Christian traditions have read the verse in different ways."),
 'c-manzikert': c("At Manzikert in eastern Anatolia on 26 August 1071 the Seljuk Turks under Alp Arslan defeated and captured the emperor Romanus IV; overthrown at home, Romanus was blinded and killed, and most of Anatolia passed to the Turks.", 'consensus', ['brit-manzikert'], show=False),
}

# ---------------------------------------------------------------- 11.4
P4 = {
 'title': "Tang and Song China", 'sub': "rebellion, rice, print and paper money, 755-1279",
 'lede': "Between the 8th and the 13th centuries China was transformed. Its government came to run on written examinations, its printers produced books in large numbers, and its merchants and officials began to use paper money.",
 'body': [
  "The Tang dynasty (see 10.11) nearly died in 755, when its general An Lushan rebelled. The revolt was crushed after eight years, but regional warlords held power until the Song reunified the country in 960. [[c-anlushan]] One famous death toll is generally considered too high. [[c-anlushan-toll]]",
  "Under the Song the empire was run by scholar-officials chosen by examination, [[c-song]] and from 1313 those examinations followed the Confucian 'Four Books' as edited by Zhu Xi, a syllabus that lasted until 1905. [[c-zhuxi]] Fast-ripening rice from Southeast Asia let farmers in the south grow two crops a year, and the population passed 100 million. [[c-champa-rice]]",
  "China also pioneered two technologies. Printing from carved wooden blocks produced the oldest dated printed book, a Buddhist sutra of 868. [[c-diamond]] And the Song state took over merchants' paper notes to issue the world's first government paper money. [[c-jiaozi]] Some historians speak of a Song 'industrial revolution' in iron and coal; others doubt the numbers behind it. [[c-hartwell]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["755-763", "An Lushan rebellion"],
    ["868", "the Diamond Sutra, earliest dated printed book"],
    ["960", "Song dynasty reunifies China"],
    ["1024", "state paper money (jiaozi) in Sichuan"],
    ["1127", "the north lost; Song continues in the south"],
    ["1190", "Zhu Xi's edition of the Four Books"]], 'note': "[[c-anlushan]] [[c-diamond]] [[c-song]] [[c-jiaozi]] [[c-zhuxi]]"}},
  {'compare': "Movable type was invented in China by Bi Sheng (990-1051), yet carved woodblocks remained the usual way to print there. [[c-printing-cost]]"}],
 'figure': {'kind': 'map', 'view': {'lon': 108.0, 'lat': 33.0, 'zoom': 9}, 'caption': "Tang and Song China, 755-1279", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [114.5, 27.0], 'label': 'RICE SOUTH', 'size': 10}, {'ll': [112.0, 37.5], 'label': 'NORTH CHINA PLAIN', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [108.9286, 34.2583], 'label': "Chang'an", 'date': 'Tang capital', 'acc': True, 'big': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '11.4 · Tang', 'title': 'The An Lushan rebellion', 'sub': '755-763', 'text': "[[c-anlushan]] [[c-anlushan-toll]]", 'sources': ['brit-anlushan', 'carter-anlushan']}},
    {'ll': [114.3072, 34.7986], 'label': 'Kaifeng', 'date': 'Song capital, 960-1127', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '11.4 · Song', 'title': 'The Northern Song', 'sub': '960-1127', 'text': "[[c-song]] [[c-hartwell]] [[c-zhuxi]]", 'sources': ['brit-song-sum', 'hartwell1962', 'wagner2001']}},
    {'ll': [120.1614, 30.2936], 'label': 'Hangzhou', 'date': 'Southern Song capital', 'acc': True, 'dy': 16, 'plate': {'kicker': '11.4 · Song', 'title': 'The Southern Song', 'sub': '1127-1279', 'text': "[[c-champa-rice]] [[c-song]]", 'sources': ['brit-song-culture', 'brit-song-sum']}},
    {'ll': [94.9192, 40.0333], 'label': 'Dunhuang', 'date': 'Diamond Sutra, 868', 'acc': True, 'dy': 16, 'plate': {'kicker': '11.4 · printing', 'title': 'The Diamond Sutra', 'sub': '868', 'text': "[[c-diamond]]", 'sources': ['ox-diamond']}},
    {'ll': [104.0667, 30.6667], 'label': 'Chengdu', 'date': 'paper money, 1024', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.4 · money', 'title': 'Jiaozi', 'sub': '1024', 'text': "[[c-jiaozi]]", 'sources': ['standard-jiaozi']}}]}]},
 'practice': [
  q("Why do many historians doubt that the An Lushan rebellion killed 36 million people?",
    ["It counts a fall in registrations, not deaths", "The revolt was crushed within a few months of 755", "No Tang registers survive to support the figure", "Steven Pinker rejects the figure as far too high"], 0,
    "The figure comes from the fall in registered population, which reflects migration and the collapse of record-keeping as well as deaths: registers measure who was counted, not only who died.",
    {1: "It lasted from late 755 until 763.", 2: "The figure is itself derived from the fall in registered population.", 3: "Pinker is among the writers who give the 36 million figure."}),
  q("What is Donald Wagner's main objection to Robert Hartwell's Song iron figures?",
    ["The total is credible, but the method is flawed", "The method is sound, but the total is far too high", "Wagner shows that output was under 10,000 tons", "He accepts both Hartwell's total and his method"], 0,
    "Wagner finds the size of the figure 'quite credible' but Hartwell's method 'seriously flawed': a credible total can still rest on a flawed calculation.",
    {1: "The reverse: Wagner finds the total 'quite credible' and the method 'seriously flawed'.", 2: "Wagner finds the size of Hartwell's figure, about 75,000 tons and later 125,000, 'quite credible'.", 3: "He calls the method 'seriously flawed'."})]}

# ---------------------------------------------------------------- 11.5
P5 = {
 'title': "Charlemagne and Latin Christendom", 'sub': "800 to 1122",
 'lede': "On Christmas Day 800 a Frankish king was crowned Roman emperor in Rome. His reign shaped the script, the books and the Church of western Europe.",
 'body': [
  "Charlemagne ruled the Franks and greatly enlarged their kingdom; on Christmas Day 800 the pope crowned him emperor. [[c-coronation800]] His biographer insisted he had not wanted it, but Britannica judges that king and pope planned the coronation together. [[c-coronation-intent]] A new, clearer handwriting developed partly under his patronage, and most of our knowledge of classical literature comes from copies made at his court. [[c-minuscule]]",
  "Why did the centre of Europe move north, from the Mediterranean to the Rhineland? Henri Pirenne famously blamed the Arab conquests; archaeologists answer that Roman trade had collapsed before Islam began. [[c-pirenne]] Michael McCormick showed that by 800 trade with the eastern Mediterranean was reviving, much of it in enslaved people. [[c-mccormick]] Historians also argue whether 'feudalism' describes this society at all. [[c-feudalism]]",
  "The Church reformed itself from within. Monasteries such as Cluny answered only to the pope, [[c-cluny]] and reforming popes then demanded that kings stop appointing bishops. The clash came to a head when the excommunicated German king Henry IV stood as a penitent at Canossa in 1077, and was settled by compromise in 1122. [[c-investiture]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["800", "Charlemagne crowned emperor in Rome"],
    ["910", "Cluny founded"],
    ["1076-1077", "Henry IV excommunicated; penance at Canossa"],
    ["1122", "Concordat of Worms"]], 'note': "[[c-coronation800]] [[c-cluny]] [[c-investiture]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 8.0, 'lat': 47.0, 'zoom': 16}, 'caption': "Emperors and popes, 800-1122", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [2.5, 48.5], 'label': 'FRANCIA', 'size': 10}, {'ll': [11.0, 50.5], 'label': 'GERMANY', 'size': 10}, {'ll': [12.0, 43.6], 'label': 'ITALY', 'size': 10}]},
   {'type': 'points', 'items': [
    {'ll': [6.0833, 50.7764], 'label': 'Aachen', 'date': "Charlemagne's court", 'acc': True, 'big': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '11.5 · the court', 'title': 'Aachen', 'sub': 'Charlemagne died here, 814', 'text': "[[c-minuscule]] [[c-pirenne]] [[c-mccormick]]", 'sources': ['lancaster-minuscule', 'medievalists-hodges', 'cup-mccormick']}},
    {'ll': [12.4531, 41.9022], 'label': 'Rome', 'date': 'coronation, 800', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '11.5 · the coronation', 'title': 'Christmas Day 800', 'sub': "St Peter's, Rome", 'text': "[[c-coronation800]] [[c-coronation-intent]]", 'sources': ['brit-charlemagne800']}},
    {'ll': [4.6583, 46.4331], 'label': 'Cluny', 'date': 'founded 910', 'acc': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.5 · reform', 'title': 'Cluny', 'sub': '910', 'text': "[[c-cluny]]", 'sources': ['brit-cluny']}},
    {'ll': [10.41, 44.5972], 'label': 'Canossa', 'date': '1077', 'acc': True, 'dy': -8, 'plate': {'kicker': '11.5 · investiture', 'title': 'Canossa', 'sub': 'January 1077', 'text': "[[c-investiture]]", 'sources': ['brit-investiture']}},
    {'ll': [8.3592, 49.6328], 'label': 'Worms', 'date': 'concordat, 1122', 'acc': True, 'dy': 16}]}]},
 'practice': [
  q("How did Michael McCormick's evidence revise Pirenne's thesis?",
    ["By 800 long-distance trade circuits were connecting again", "The Roman Mediterranean collapsed after Muhammad, not before", "Eastern merchants carried most of the trade around 800", "By 800 Europe had stopped exporting enslaved people"], 0,
    "By 800, in McCormick's words, 'multiple circuits were connecting again', carried mostly by western traders, so Islam's rise did not simply cut the West off.",
    {1: "Hodges and Whitehouse argue the collapse 'clearly predated Mohammed'; McCormick's work concerns the revival by 800.", 2: "By then, McCormick says, the traders were mostly western.", 3: "McCormick found slaves were a major export from Europe."}),
  q("What did the Concordat of Worms (1122) settle?",
    ["It ended the investiture dispute with a compromise", "It ended a dispute that Canossa had settled in 1077", "It gave kings full control over appointing bishops", "It placed Cluny's monasteries under the German king"], 0,
    "Gregory VII had banned lay rulers, kings included, from investing bishops; after Canossa the conflict continued until the Concordat ended it with a compromise.",
    {1: "Henry IV's penance at Canossa in 1077 did not end the dispute; the Concordat of 1122 did.", 2: "It was a compromise, after Gregory VII had banned lay rulers, kings included, from investing bishops.", 3: "Cluny answered to no authority but the pope's; the Concordat settled the investiture dispute."})]}

# ---------------------------------------------------------------- 11.6
P6 = {
 'title': "The Vikings", 'sub': "raiders, traders and settlers, 793 to c. 1050",
 'lede': "For two and a half centuries Scandinavians sailed from Newfoundland to the rivers of eastern Europe. They raided monasteries, traded slaves and silver, founded towns and states, and settled islands in the North Atlantic. New dating methods and ancient DNA have transformed what we know about them.",
 'body': [
  "The sack of Lindisfarne in 793 sent a shockwave through Europe, though it was not the first Viking raid on England. [[c-lindisfarne]] But the Vikings were traders as much as raiders. On Gotland, one hoard alone holds about 76 kg of silver and bronze, mostly Arabic coins (dirhams). [[c-spillings]] In the east, Scandinavians known as the Rus' ruled river towns; a chronicle has them invited to Novgorod in 862, [[c-rurik]] and whether they founded the state of the Rus' has been argued for three centuries; in the Soviet Union, anti-Normanist views were officially sanctioned. [[c-normanist]]",
  "In the North Atlantic they settled Iceland, where an open-air assembly met from about 930, [[c-althing]] and briefly reached North America. At L'Anse aux Meadows in Newfoundland, wood cut with metal tools has been dated to the exact year 1021, [[c-lanse]] using the trace of a cosmic-ray burst in 993 preserved in the tree rings. [[c-1021-method]]",
  "Ancient DNA has added detail. Vikings in England came mostly from Denmark, those in Iceland mostly from Norway, [[c-margaryan]] and Scandinavia itself had absorbed people from central Europe. [[c-speidel-viking]] A famous warrior's grave at Birka turned out to hold a woman, and scholars still disagree about what that means. [[c-birka]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["793", "Lindisfarne sacked"],
    ["862", "Rurik at Novgorod (tradition)"],
    ["c. 870", "youngest coin in the Spillings hoard"],
    ["c. 930", "Althing founded in Iceland"],
    ["1021", "trees felled at L'Anse aux Meadows"]], 'note': "[[c-lindisfarne]] [[c-rurik]] [[c-spillings]] [[c-althing]] [[c-lanse]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': -6.0, 'lat': 57.0, 'zoom': 3.6}, 'caption': "The Viking world, 793-c. 1050", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [12.0, 62.0], 'label': 'SCANDINAVIA', 'size': 11}, {'ll': [-42.0, 72.0], 'label': 'GREENLAND', 'size': 10}, {'ll': [-18.5, 65.3], 'label': 'ICELAND', 'size': 9}, {'ll': [37.0, 52.0], 'label': "RUS'", 'size': 10}]},
   {'type': 'points', 'items': [
    {'ll': [-1.7994, 55.6781], 'label': 'Lindisfarne', 'date': 'raid, 793', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 4, 'plate': {'kicker': '11.6 · raids', 'title': 'Lindisfarne', 'sub': '8 June 793', 'text': "[[c-lindisfarne]] [[c-margaryan]]", 'sources': ['eh-lindisfarne', 'margaryan2020']}},
    {'ll': [17.5461, 59.3364], 'label': 'Birka', 'date': 'grave Bj 581', 'acc': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '11.6 · DNA', 'title': 'The Birka grave', 'sub': '10th century', 'text': "[[c-birka]] [[c-speidel-viking]]", 'sources': ['ajpa-birka', 'price2019', 'jesch-birka']}},
    {'ll': [18.5, 57.5], 'label': 'Gotland', 'date': 'Spillings hoard', 'acc': True, 'dy': 16, 'plate': {'kicker': '11.6 · silver', 'title': 'The Spillings hoard', 'sub': 'found 1999', 'text': "[[c-spillings]]", 'sources': ['shm-spillings']}},
    {'ll': [31.2708, 58.5211], 'label': 'Novgorod', 'date': 'Rurik, 862 (tradition)', 'acc': True, 'dy': -8, 'plate': {'kicker': "11.6 · the Rus'", 'title': "The Rus'", 'sub': '9th century', 'text': "[[c-rurik]] [[c-normanist]]", 'sources': ['brit-rurik', 'eu-normanist']}},
    {'ll': [30.5236, 50.4544], 'label': 'Kyiv', 'anchor': 'end', 'dy': 16},
    {'ll': [-21.125, 64.2581], 'label': 'Þingvellir', 'date': 'Althing, c. 930', 'acc': True, 'dy': 16, 'plate': {'kicker': '11.6 · Iceland', 'title': 'The Althing', 'sub': 'c. 930-1798', 'text': "[[c-althing]]", 'sources': ['unesco-thingvellir']}},
    {'ll': [-55.5319, 51.5953], 'label': "L'Anse aux Meadows", 'date': '1021', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '11.6 · America', 'title': "L'Anse aux Meadows", 'sub': '1021', 'text': "[[c-lanse]] [[c-1021-method]]", 'sources': ['unesco-lanse', 'kuitems2021']}}]}]},
 'practice': [
  q("What makes the 1021 date at L'Anse aux Meadows so precise?",
    ["One ring marks 993; counting on gives the felling year", "The trees were felled in 993, the very year of the spike", "It was the first proof the Norse reached America", "Saga accounts give the year of the Vinland voyage"], 0,
    "A radiocarbon spike from a cosmic-ray event in 993 marks a single tree ring; counting rings outward to the bark gives the year of felling.",
    {1: "993 is the marker ring; the felling it dates is 1021.", 2: "The site was already recognised as an 11th-century Norse settlement; the precision comes from the marker ring.", 3: "The date comes from the wood itself: a radiocarbon spike in one ring and a ring count."}),
  q("What is still debated about the Birka grave Bj 581?",
    ["Whether she was a real fighter or a symbolic one", "Whether DNA shows the skeleton is a woman's", "Whether Jesch sees her as a professional warrior", "Whether the grave dates from the Viking Age"], 0,
    "The DNA settled her sex; it could not settle her role. Neil Price and colleagues read her as 'a woman who lived as a professional warrior' but allow a symbolic reading; Judith Jesch thinks they 'make too much of rather slim evidence'.",
    {1: "DNA showed in 2017 that it belonged to a woman.", 2: "That is Price's reading; Jesch thinks it makes 'too much of rather slim evidence'.", 3: "It is a 10th-century grave."})]}

# ---------------------------------------------------------------- 11.7
P7 = {
 'title': "Byzantium and the Great Schism", 'sub': "726 to 1071",
 'lede': "The eastern Roman empire survived the Arab conquests and fought a bitter internal war over religious images. Then it revived, converted the Slavs, and reached its medieval height, before a quarrel with Rome in 1054 and a defeat by the Turks in 1071, which cost it most of Anatolia.",
 'body': [
  "For over a century Byzantium argued about icons. Emperors banned them as idolatry; a council restored them in 787; the images were restored for good in 843. [[c-iconoclasm]] Under the Macedonian emperors from 867 learning revived and the empire expanded, [[c-macedonian]] though one famous story of Basil II's cruelty is probably exaggerated. [[c-basil-blind]]",
  "Byzantium also sent missions to the Slavs. Two brothers, Cyril and Methodius, created an alphabet for the Slavs and translated scripture into their language. [[c-cyril]] In about 988 Prince Vladimir of Kyiv was baptised as part of a marriage alliance. [[c-vladimir]]",
  "Relations with Rome soured over authority and ritual. In 1054 papal legates excommunicated the patriarch of Constantinople at the altar of Hagia Sophia, [[c-1054]] though contemporaries saw it as a minor quarrel. [[c-1054-meaning]] The excommunications were lifted in 1965, and in 2025 pope and patriarch renewed their hope of reunion. [[c-1965-2025]] Seventeen years after 1054, at Manzikert, the Seljuk Turks captured the emperor, and most of Anatolia passed to the Turks. [[c-manzikert]]",
  {'table': {'head': ["Year", "Event"], 'rows': [
    ["730", "religious images banned"],
    ["787", "Second Council of Nicaea restores icons"],
    ["843", "icons restored for good"],
    ["863", "Cyril and Methodius go to Moravia"],
    ["c. 988", "Vladimir of Kyiv baptised"],
    ["1054", "mutual excommunications"],
    ["1071", "Manzikert"],
    ["1965", "excommunications lifted"]], 'note': "[[c-iconoclasm]] [[c-cyril]] [[c-vladimir]] [[c-1054]] [[c-manzikert]] [[c-1965-2025]]"}},
  {'compare': "The commandment the iconoclasts cited: [[c-exodus-20-4]]"}],
 'figure': {'kind': 'map', 'view': {'lon': 30.0, 'lat': 43.0, 'zoom': 9}, 'caption': "Byzantium and its neighbours, 726-1071", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [32.0, 39.0], 'label': 'ANATOLIA', 'size': 10}, {'ll': [25.0, 42.6], 'label': 'BULGARIA', 'size': 9}, {'ll': [17.8, 49.5], 'label': 'GREAT MORAVIA', 'size': 8}, {'ll': [33.0, 52.5], 'label': "KYIVAN RUS'", 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [28.9494, 41.0136], 'label': 'Constantinople', 'date': 'Hagia Sophia, 1054', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '11.7 · the schism', 'title': '1054', 'sub': '16 July', 'text': "[[c-1054]] [[c-1054-meaning]] [[c-1965-2025]]", 'sources': ['brit-schism', 'vatican-2025']}},
    {'ll': [17.0508, 48.8164], 'label': 'Mikulčice', 'date': 'Great Moravia', 'acc': True, 'anchor': 'end', 'dy': 4, 'plate': {'kicker': '11.7 · missions', 'title': 'Cyril and Methodius', 'sub': '863', 'text': "[[c-cyril]]", 'sources': ['brit-cyril']}},
    {'ll': [33.4956, 44.6133], 'label': 'Chersonesus', 'date': 'taken by Vladimir', 'dy': 16},
    {'ll': [30.5236, 50.4544], 'label': 'Kyiv', 'date': 'baptism, c. 988', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': "11.7 · the Rus'", 'title': 'Vladimir', 'sub': 'c. 988', 'text': "[[c-vladimir]]", 'sources': ['brit-vladimir']}},
    {'ll': [42.5353, 39.1464], 'label': 'Manzikert', 'date': '1071', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 16, 'plate': {'kicker': '11.7 · the Turks', 'title': 'Manzikert', 'sub': '26 August 1071', 'text': "[[c-manzikert]]", 'sources': ['brit-manzikert']}}]}]},
 'practice': [
  q("Which statement best describes the events of 1054?",
    ["A quarrel then, seen as the final break only later", "A final break at the time, and still in force today", "A bull attacking the Greeks' unleavened bread", "A break set off by the crusaders' sack of Constantinople"], 0,
    "At the time it looked like 'a minor storm in which both sides had behaved with some arrogance'; only in hindsight was it seen as 'the moment of the final breach'.",
    {1: "Contemporaries saw a minor storm, and the excommunications were lifted in 1965.", 2: "Among its charges was the Greek use of leavened bread.", 3: "The sack of Constantinople came in 1204, 150 years later."}),
  q("Why do historians handle Basil II's reputation as 'Bulgar-slayer' with care?",
    ["The 15,000 is doubted; the name came centuries later", "Basil lost his war, so the name was meant as mockery", "The 15,000 is well attested, and the name came later", "His contemporaries already called him 'Bulgar-slayer'"], 0,
    "Historians think the 15,000 exaggerated, and the name 'Bulgar-slayer' is not attested until some three centuries later; Paul Stephenson argues it owes much to 12th-century attitudes.",
    {1: "Under Basil II the empire covered more of Europe than at any time since Justinian.", 2: "Historians think the number exaggerated; it comes from a chronicle.", 3: "The name is not attested until some three centuries later."})]}

PAGES = [P4, P5, P6, P7]
