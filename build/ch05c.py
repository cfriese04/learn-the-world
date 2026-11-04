# Chapter 5, pages 5.8 to 5.11. Coordinates are [longitude, latitude].
from common import c, q

S = {
 'antiquity2023-sxd': ("Li, Qiu, Guo and Li, \"New discoveries at the Sanxingdui Bronze Age site in south-west China\", Antiquity (2023)", "https://core-prod.cambridgecore.org/core/services/aop-cambridge-core/content/view/D96494368471CF7CBA817690CDCA5A75/S0003598X22001508a.pdf/new_discoveries_at_the_sanxingdui_bronze_age_site_in_southwest_china.pdf"),
 'unesco-shu': ("UNESCO Tentative List, \"Archaeological Sites of the Ancient Shu State\"", "https://whc.unesco.org/en/tentativelists/5816/"),
 'wsj-sxd': ("Wall Street Journal, \"A lost civilization is baffling experts and rewriting China's origin story\" (republished by To Vima)", "https://www.tovima.com/wsj/a-lost-civilization-is-baffling-experts-and-rewriting-chinas-origin-story/"),
 'livescience-sxd': ("Live Science, on the new Sanxingdui pits (2021)", "https://www.livescience.com/ancient-china-city-treasure-artifacts-saxingdui.html"),
 'cgtn-sxd2021': ("CGTN, \"Wonders of Sanxingdui: the bronze wares\" (2021)", "https://news.cgtn.com/news/2021-03-18/Wonders-of-Sanxingdui-The-bronze-wares-from-the-mysterious-culture-YJupHzSd1K/index.html"),
 'thecover-mask': ("The Cover (Sichuan), on the largest Sanxingdui bronze mask", "https://www.thecover.cn/news/7246314"),
 'cgtn-sxd2025': ("CGTN, \"Exact dating of Sanxingdui sacrificial pits announced\" (2025)", "https://news.cgtn.com/news/2025-09-27/New-findings-Exact-dating-of-Sanxingdui-sacrificial-pits-announced-1H0y9ZAloM8/index.html"),
 'scmp-sxd': ("South China Morning Post, on 'alien' theories about Sanxingdui (2021)", "https://www.scmp.com/culture/article/3126720/historical-discovery-revives-wild-theories-alien-civilisation-ancient-china"),
 'cgtn-jinsha': ("CGTN, \"Jinsha Site: a glimpse into China's ancient Shu civilization\" (2025)", "https://news.cgtn.com/news/2025-09-14/Jinsha-Site-A-glimpse-into-China-s-ancient-Shu-civilization-1GF6Jtjriw0/share_amp.html"),
 'shaughnessy1981': ("Edward Shaughnessy, \"'New' evidence on the Zhou conquest\", Early China 6 (1981)", "https://www.cambridge.org/core/journals/early-china/article/abs/new-evidence-on-the-zhou-conquest/CBE3E11961D44DC8638B145BD678FA28"),
 'cgtn-ligui': ("CGTN, on the Li gui and the date of the Zhou conquest", "https://news.cgtn.com/news/3445544d356b7a6333566d54/index.html"),
 'pankenier1981': ("David Pankenier, \"Astronomical dates in Shang and Western Zhou\", Early China 7 (1981)", "https://www.cambridge.org/core/journals/early-china/article/astronomical-dates-in-shang-and-western-zhou/515F9D0434AD981B6756F8ECC3A9A1B4"),
 'shaughnessy1985': ("Edward Shaughnessy, \"The 'current' Bamboo Annals and the date of the Zhou conquest of Shang\", Early China (1985)", "https://core-prod.cambridgecore.org/core/journals/early-china/article/current-bamboo-annals-and-the-date-of-the-zhou-conquest-of-shang/5B7D1EF7B2122C32988C57E066445991"),
 'nivison1999': ("David Nivison, \"The key to the chronology of the Three Dynasties\", Sino-Platonic Papers 93 (1999)", "https://sino-platonic.org/abstracts/spp093_three_dynasties.html"),
 'sep-mencius': ("Stanford Encyclopedia of Philosophy, \"Mencius\"", "https://plato.stanford.edu/entries/mencius/"),
 'lundu2017': ("Lun Du, on the Mandate of Heaven in early Zhou thought, Asian Studies 5 (2017)", "https://doaj.org/article/f8efd6efd0e74f3aafb5bb57172d26d9"),
 'chinadaily-hezun': ("China Daily, \"Bronze vessel from Shaanxi bears the first record of China's name\" (2022)", "https://govt.chinadaily.com.cn/s/202205/05/WS62737fef498e6a12c122b5cf/bronze-vessel-from-shaanxi-bears-the-first-record-of-chinas-name.html"),
 'hou2007': ("Hou Jianxin, on 'feudalism' and fengjian, Frontiers of History in China 2 (2007)", "https://journal.hep.com.cn/fhc/EN/10.1007/s11462-007-0001-0"),
 'iu-zhou': ("Robert Eno, Indiana University, \"Western Zhou\" course topics", "https://chinatxt.sitehost.iu.edu/History/WZhou-Topics-2012.html"),
 'lifeng2006': ("Li Feng, Landscape and Power in Early China (Cambridge, 2006), chapter on the fall of the Western Zhou", "https://www.cambridge.org/core/books/landscape-and-power-in-early-china/fall-of-the-western-zhou-partisan-struggle-and-spatial-collapse/9ED3767010631C65EBB52B4BAF9E5766"),
 'khayutina2008': ("Maria Khayutina, on the fall of the Western Zhou, Oriens Extremus 47 (2008)", "https://archiv.oriens-extremus.org/47/OE47-02.pdf"),
 'ebsco-mandate': ("EBSCO Research Starters, \"Mandate of Heaven\" (2020)", "https://www.ebsco.com/research-starters/history/mandate-heaven"),
 'shaughnessy2023': ("Edward Shaughnessy, review of the Xia-Shang-Zhou Chronology Project report, Early China 46 (2023)", "https://knowledge.uchicago.edu/record/12754/files/Xia-shang-zhou-duandai-gongcheng-baogao.pdf"),
 'nyt2000': ("Erik Eckholm, \"In China, ancient history kindles modern doubts\", New York Times, 10 November 2000 (reposted text)", "https://hcsstt.blogspot.com/2010/12/in-china-ancient-history-kindles-modern.html?m=0"),
 'cgtn-origins': ("CGTN, on the Chinese Civilization Origins Project (2018)", "https://news.cgtn.com/news/3d3d774d77597a4e77457a6333566d54/index.html"),
 'chinadaily-xi2022': ("China Daily, on Xi Jinping's Politburo study session on Chinese civilization (2022)", "https://subsites.chinadaily.com.cn/npc/2022-05/30/c_757762.htm"),
 'bachner2017': ("Andrea Bachner, \"Oracle bones: that dangerous supplement\", via China Heritage", "https://chinaheritage.net/journal/oracle-bones-that-dangerous-supplement/"),
 'chinadaily-kings': ("China Daily, \"Discoveries beyond doubt\" (2025)", "https://govt.chinadaily.com.cn/s/202506/18/WS68521979498eec7e1f73a101/discoveries-beyond-doubt.html"),
 'liu2021-c14': ("Liu et al., radiocarbon dating of Shang oracle bones, Radiocarbon 63 (2021)", "https://www.cambridge.org/core/product/38A7B64D6D538A3A7B96F912BBEE9592"),
 'englund2001': ("Robert Englund, \"Grain accounting practices in archaic Mesopotamia\", MPIWG Preprint 183", "https://mpiwg-berlin.mpg.de/sites/default/files/migrated/p183.pdf"),
 'mcmahon2020': ("Augusta McMahon, \"Early urbanism in northern Mesopotamia\", Journal of Archaeological Research 28 (2020)", "https://core.ac.uk/download/328720952.pdf"),
 'mattessich2002': ("Richard Mattessich, on the Abydos U-j labels, Accounting Historians Journal 29 (2002)", "https://core.ac.uk/download/288025208.pdf"),
 'zettler-ur': ("Richard Zettler, on the Royal Cemetery of Ur, Penn Almanac", "https://almanac.upenn.edu/archive/volumes/v56/n09/zettler.html"),
 'penn-retainers': ("Penn Museum, on courtiers sacrificed with early Egyptian kings", "https://penn.museum/about/press-room/press-releases/archaeologists-discover-evidence-that-courtiers-were-sacrificed-to-accompany-early-egyptian-kings-into-the-afterlife"),
 'henan-yinxu': ("Henan Provincial Government, on the Yinxu site (2025)", "https://english.henan.gov.cn/2025/01-20/3114717.html"),
 'meadow-intro': ("Richard Meadow, \"Harappa: an introduction\", harappa.com", "https://www.harappa.com/indus2/intro.html"),
}

C = {
 # 5.8
 'c-sxd-site': c("Sanxingdui, about 40 km north-east of Chengdu in Sichuan, became a Bronze Age centre about 1800 BCE, with walls enclosing some 360 hectares.", 'approx', ['unesco-shu', 'antiquity2023-sxd'], "Occupation at the site goes back to about 2700 BCE; sources give different figures for its extent."),
 'c-sxd-1986': c("In 1986 brick-factory workers digging clay found two pits holding hundreds of objects of bronze, gold, jade and ivory, many deliberately broken and burned.", 'approx', ['antiquity2023-sxd', 'wsj-sxd'], "The Antiquity report counts more than 900 objects; UNESCO gives more than 6,000 relics, probably counting fragments and small items."),
 'c-sxd-new': c("Six more pits, found from 2019, held a gold mask, a bronze figure carrying a vessel on its head and a painted wooden chest; none of the eight pits held human remains.", 'consensus', ['antiquity2023-sxd', 'livescience-sxd'], show=False),
 'c-sxd-figures': c("Pit 2 held a bronze standing figure 2.6 metres tall with its base, a bronze tree reassembled to almost 4 metres, and a mask 1.38 metres wide whose eyes stick out about 16 cm.", 'consensus', ['cgtn-sxd2021', 'thecover-mask'], show=False),
 'c-cancong': c("Some scholars link the protruding eyes to Cancong, a legendary first king of Shu described in a text of the 4th century CE as having 'vertical eyes'.", 'tradition', ['thecover-mask'], "This is a suggestion; no writing at Sanxingdui names any ruler or god."),
 'c-sxd-dates': c("The pits were filled late in the Shang period, about 1200-1000 BCE; exactly when, and whether all at once, is debated.", 'debated', ['antiquity2023-sxd', 'cgtn-sxd2025'], "Artefact styles put most pits in Anyang's last phase and two perhaps in the early Zhou; a 2025 radiocarbon study dated four pits, including one of those two, to 1201-1012 BCE."),
 'c-sxd-distinct': c("Sanxingdui traded and shared some vessel types with the Central Plains, but its art and religion were its own.", 'consensus', ['unesco-shu', 'antiquity2023-sxd'], show=False),
 'c-sxd-nowriting': c("No writing and no rulers' tombs have been found at Sanxingdui, and only a small fraction of the site has been excavated.", 'consensus', ['wsj-sxd'], show=False),
 'c-aliens': c("Claims that Sanxingdui was built by aliens or by migrants from the Middle East have no evidence behind them; archaeologists call them far-fetched.", 'consensus', ['scmp-sxd'], show=False),
 'c-west-contact': c("A few objects, such as gold sceptres, may hint at contact with lands farther west.", 'debated', ['wsj-sxd'], "This is speculative; no clear evidence of such contact has been published."),
 'c-jinsha': c("Jinsha, in western Chengdu, found in 2001 and dated about 1200-650 BCE, continued Sanxingdui's traditions, including a gold mask and a thin gold 'sun bird' disc.", 'approx', ['cgtn-jinsha', 'unesco-shu'], show=False),
 'c-shu-qin': c("The kingdom of Shu in Sichuan was conquered by Qin in 316 BCE.", 'consensus', ['unesco-shu'], show=False),
 # 5.9
 'c-li-gui': c("The Li gui, a bronze vessel found in 1976, records that King Wu attacked the Shang on a jiazi day, in the morning.", 'consensus', ['shaughnessy1981', 'cgtn-ligui'], "Two characters in the inscription are read by some as 'Jupiter was in position', an astronomical clue to the date; others read them as the names of sacrifices.", show=False),
 'c-conquest-date': c("The Zhou conquest of the Shang is usually dated 1046 BCE.", 'debated', ['cgtn-ligui', 'pankenier1981', 'shaughnessy1985', 'nivison1999'], "1046 is the date of the Xia-Shang-Zhou Chronology Project and of David Pankenier; Edward Shaughnessy argues for 1045 and David Nivison for 1040. Older proposals discussed by Nivison include 1070 and 1027."),
 'c-pankenier': c("David Pankenier links Zhou ideas of the Mandate to a striking gathering of planets he dates to 1059 BCE.", 'debated', ['pankenier1981'], "One scholar's thesis, much discussed but not established."),
 'c-mandate': c("The Zhou kings justified their rule by claiming a mandate from Heaven (tian), which favours rulers of virtue (de).", 'consensus', ['sep-mencius'], show=False),
 'c-mandate-early': c("Bronze inscriptions and some chapters of the Book of Documents (Shangshu) show the Mandate idea in the early Zhou.", 'approx', ['lundu2017'], "Some Shangshu chapters were written down later, so the bronze inscriptions are the safer evidence."),
 'c-he-zun': c("The He zun, a bronze found at Baoji in 1963, has a 122-character inscription containing zhongguo, 'the central lands', the earliest known use of the phrase now used as China's name.", 'consensus', ['chinadaily-hezun'], show=False),
 'c-fengjian': c("The Zhou kings granted territories to relatives and allies who ruled them as hereditary lords; whether to call this 'feudalism' is disputed.", 'debated', ['hou2007', 'iu-zhou'], "Some historians use 'Zhou feudalism' as a model; others, like Hou Jianxin, argue the European term misleads when applied to China."),
 'c-771': c("In 771 BCE attackers from the west sacked the Zhou capitals and killed King You; his successor moved the court east to Luoyi, and Zhou kings never again ruled the west.", 'consensus', ['lifeng2006', 'khayutina2008'], show=False),
 'c-mandate-legacy': c("The Mandate became a lasting idea in Chinese politics: disasters and rebellion could be read as signs Heaven had withdrawn its favour, until the last dynasty fell in the revolution of 1911-12.", 'consensus', ['ebsco-mandate', 'sep-mencius'], show=False),
 # 5.10
 'c-xszcp': c("The state-sponsored Xia-Shang-Zhou Chronology Project brought together about 200 historians, palaeographers, archaeologists and astronomers, led by Li Xueqin; it published a short report in 2000 and its full report in 2022.", 'consensus', ['shaughnessy2023'], show=False),
 'c-xszcp-results': c("It dated the Xia to about 2070-1600 BCE, the Shang to about 1600-1046, and the Zhou conquest to 1046.", 'approx', ['nyt2000', 'shaughnessy2023'], "Only reigns after about 1300 BCE were given specific years."),
 'c-841': c("Sima Qian's history, the Shiji (about 100 BCE), gives year-by-year dates only from 841 BCE; for earlier rulers it gives lists of names.", 'consensus', ['liu2021-c14', 'nyt2000'], show=False),
 'c-xszcp-critics': c("Critics outside China called the project's precision unjustified and its motives partly nationalist; its leaders defended the dates as the best available.", 'debated', ['nyt2000', 'shaughnessy2023'], "Shaughnessy argued in 2023, from fully dated bronze inscriptions, that its Western Zhou chronology is wrong throughout; David Nivison warned that the government's endorsement of the dates 'may poison scholarship for generations'."),
 'c-origins-project': c("A second project, on the origins of Chinese civilization, announced in 2018 that regional civilizations existed by about 5,300 years ago, citing Liangzhu, Taosi and Shimao.", 'debated', ['cgtn-origins'], "It used criteria such as social classes, central cities and state power rather than writing, the classic test of a civilization."),
 'c-xi-5000': c("In 2022 Xi Jinping told a Politburo study session that China has 'more than 5,000 years of civilization', linking research on its origins to cultural confidence and national rejuvenation.", 'consensus', ['chinadaily-xi2022'], show=False),
 'c-national-narrative': c("Some scholars worry that archaeology is being drawn into a national story; for example, Sanxingdui is presented as part of China's 'unity in diversity', though nothing shows its people thought of themselves as Chinese.", 'debated', ['wsj-sxd', 'nyt2000'], "Chinese project leaders have denied being told what to find."),
 'c-oracle-confirm': c("Oracle bones confirmed that the Shang existed, and the line of kings reconstructed from them matches Sima Qian's list, written about a thousand years later, with only minor differences.", 'consensus', ['bachner2017', 'chinadaily-kings'], show=False),
 'c-wuding': c("Radiocarbon dates on oracle bones place the reign of the Shang king Wu Ding about 1254-1197 BCE.", 'approx', ['liu2021-c14'], show=False),
 # 5.11
 'c-cmp-meso': c("The earliest Mesopotamian tablets date from about 3300-3000 BCE, and the largest city, Uruk, covered about 250 hectares.", 'approx', ['englund2001', 'mcmahon2020'], show=False),
 'c-cmp-uj': c("Egypt's earliest writing, on labels from tomb U-j at Abydos, dates to about 3200 BCE.", 'debated', ['mattessich2002'], "Their date and whether they are full writing are debated (4.1)."),
 'c-cmp-indus-early': c("Marks scratched on pottery at Harappa in the Ravi phase, about 3300-2800 BCE, may be early forms of Indus signs.", 'debated', ['meadow-intro'], "Whether they are early writing or potters' marks is uncertain."),
 'c-yinxu-size': c("The Yinxu site at Anyang, the last Shang capital, covers about 30 km².", 'approx', ['henan-yinxu'], show=False),
 'c-cmp-sacrifice': c("Mesopotamia, Egypt and the Shang all buried people killed to accompany rulers; no such burials are known from the Indus.", 'approx', ['zettler-ur', 'penn-retainers', 'sapiens-oracle', 'green2021'], "Few Indus cemeteries have been fully excavated, so absence of evidence is not proof."),
}

P8 = {
 'title': "Sanxingdui", 'sub': "a Bronze Age kingdom nobody expected",
 'lede': "In 1986, workers digging clay in Sichuan found two pits full of bronze heads, gold masks and elephant tusks, broken and burned. Nothing in Chinese texts had prepared anyone for them.",
 'body': [
  "Sanxingdui lies on the Chengdu plain, far south-west of the Shang heartland. It became a walled Bronze Age centre about 1800 BCE. [[c-sxd-site]] The 1986 pits held hundreds of objects of bronze, gold, jade and ivory, many deliberately smashed and burned before they were buried. [[c-sxd-1986]] Six more pits, found from 2019, held still more, including a gold mask. None held human remains, so these were ritual deposits, not graves. [[c-sxd-new]]",
  "The bronzes are like nothing from the Shang: a standing figure over 2.5 metres tall, a bronze tree almost 4 metres high, and a mask more than a metre wide with eyes that stick out on stalks. [[c-sxd-figures]] Some scholars connect those eyes with Cancong, a legendary first king of Shu. [[c-cancong]] The pits were filled late in the Shang period. [[c-sxd-dates]]",
  "Sanxingdui traded with the Central Plains and borrowed some vessel types, but its art and religion were its own. [[c-sxd-distinct]] No writing has been found there, [[c-sxd-nowriting]] which is why its people's beliefs remain a mystery, and why the site has attracted wild theories of aliens or migrants from the Middle East. Those have no evidence behind them. [[c-aliens]] A few objects may hint at contact farther west, but that too is uncertain. [[c-west-contact]]",
  "The culture continued at Jinsha, in modern Chengdu, until about 650 BCE, [[c-jinsha]] and the kingdom of Shu survived until Qin conquered it in 316 BCE. [[c-shu-qin]]",
  {'compare': "Compare Liangzhu and Shimao (5.4): Sanxingdui is more evidence that early China had many centres, not one."}],
 'figure': {'kind': 'map', 'view': {'lon': 109.15, 'lat': 33.4, 'zoom': 36}, 'caption': "Sanxingdui and the Shang, c. 1200 BCE", 'hint': "Click a site",
  'legend': [['pt', 'site'], ['dot', 'major centre']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [105.3, 29.6], 'label': 'SICHUAN BASIN', 'size': 10}, {'ll': [108.4, 33.6], 'label': 'QINLING MOUNTAINS', 'size': 9, 'rot': -8}, {'ll': [113.4, 34.0], 'label': 'CENTRAL PLAINS', 'size': 10}]},
   {'type': 'points', 'items': [
    {'ll': [104.200, 30.993], 'label': 'Sanxingdui', 'date': 'pits c. 1200-1000 BCE', 'acc': True, 'big': True, 'dy': -8, 'plate': {'kicker': '5.8 · Sanxingdui', 'title': 'Sanxingdui', 'sub': 'Guanghan, Sichuan', 'text': "[[c-sxd-site]] [[c-sxd-1986]] [[c-sxd-figures]] [[c-sxd-dates]]", 'facts': [['pits found', '1986; six more from 2019'], ['human remains in pits', 'none'], ['writing', 'none found']], 'sources': ['antiquity2023-sxd', 'unesco-shu', 'cgtn-sxd2025']}},
    {'ll': [104.013, 30.681], 'label': 'Jinsha', 'date': 'c. 1200-650 BCE', 'dy': 14, 'plate': {'kicker': '5.8 · Sanxingdui', 'title': 'Jinsha', 'sub': 'Chengdu, c. 1200 to 650 BCE', 'text': "[[c-jinsha]] [[c-shu-qin]]", 'sources': ['cgtn-jinsha', 'unesco-shu']}},
    {'ll': [114.319, 36.123], 'label': 'Anyang', 'date': 'Shang capital', 'acc': True, 'big': True, 'anchor': 'end'},
    {'ll': [112.690, 34.693], 'label': 'Erlitou', 'dy': 14, 'anchor': 'end'}]}]},
 'practice': [
  q("Why does it matter that the Sanxingdui pits held objects broken and burned, but no human remains?",
    ["It shows Sanxingdui was a colony ruled from the Shang capital", "It shows these were ritual deposits of objects, not graves", "It proves the objects were made far away and then imported", "It shows the site was sacked and burned during a war"], 1,
    "With no bodies and deliberately smashed objects, the pits read as offerings, not tombs.",
    {0: "Sanxingdui traded with the Central Plains, but its art and religion were its own.", 2: "Breaking and burning tell us how objects were treated, not where they were made.", 3: "The objects were deliberately broken and burned before burial, in organised deposits."}),
  q("What is the strongest answer to claims that aliens made the Sanxingdui masks?",
    ["Sanxingdui's art closely copies that of its Shang neighbours", "A strange style marks a little-known culture, not alien makers", "Inscriptions found in the pits name the people who made the masks", "DNA from bodies in the pits proves the makers were local"], 1,
    "The claims have no evidence behind them. With no writing, the makers' beliefs remain a mystery, which is why the site has attracted wild theories.",
    {0: "Its bronzes are like nothing from the Shang, which is why they surprise people.", 2: "No writing has been found at Sanxingdui.", 3: "None of the eight pits held human remains."})]}

P9 = {
 'title': "The Zhou and the Mandate of Heaven", 'sub': "c. 1046 to 771 BCE",
 'lede': "About 1046 BCE the Zhou, from the Wei valley in the west, overthrew the Shang. To explain why they deserved to rule, they offered an idea that lasted three thousand years: Heaven gives power to the virtuous, and takes it away from the wicked.",
 'body': [
  "A bronze vessel cast soon after the event, the Li gui, records that King Wu attacked the Shang on a jiazi day, in the morning. [[c-li-gui]] The year is less certain: it is usually given as 1046 BCE, [[c-conquest-date]] and the arguments for it draw on astronomy as well as texts. [[c-pankenier]]",
  "The Zhou claimed that Heaven (tian) had given them its mandate because the last Shang king was cruel and the Zhou were virtuous. [[c-mandate]] The idea already appears in early Zhou bronzes and texts. [[c-mandate-early]] It cut both ways: if Heaven could transfer the mandate to the Zhou, it could transfer it again. A bronze of the early Zhou, the He zun, also contains the earliest known use of zhongguo, 'the central lands', today the Chinese name for China. [[c-he-zun]]",
  "The Zhou ruled by granting lands to relatives and allies, whose lords owed loyalty and military service. Whether to call this 'feudalism' is disputed. [[c-fengjian]] In 771 BCE attackers from the west sacked the capital and killed King You, and the court moved east to Luoyi. [[c-771]] The Zhou kings reigned for five more centuries, but the real power passed to the lords of the states.",
  {'table': {'head': ["", "Shang", "Zhou"], 'rows': [
    ["homeland", "middle Yellow River", "Wei valley, to the west"],
    ["source of royal power", "ancestors, divination", "the mandate of Heaven"],
    ["supreme power", "Di", "Heaven (tian)"],
    ["main written records", "oracle bones", "bronze inscriptions, later texts"]], 'note': "[[c-di]] [[c-mandate]]"}},
  "The Mandate became one of the great political ideas of world history: floods, famines and rebellions could be read as signs that Heaven had withdrawn its favour, until the last dynasty fell in the revolution of 1911-12. [[c-mandate-legacy]]",
  {'compare': "Compare the Bible's account of kings raised up and brought down by God, as with Saul and David (1 Samuel 15-16), and Egypt's idea of maat (4.2). Each makes a ruler answerable to a higher order."}],
 'figure': {'kind': 'map', 'view': {'lon': 110.9, 'lat': 35.15, 'zoom': 46}, 'caption': "The Western Zhou, c. 1046-771 BCE", 'hint': "Click a place",
  'legend': [['acc', 'conquest of the Shang'], ['acc dash', 'move east, 770 BCE'], ['pt', 'site']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [108.0, 34.75], 'label': 'WEI VALLEY', 'size': 9}, {'ll': [113.4, 33.9], 'label': 'CENTRAL PLAINS', 'size': 10}]},
   {'type': 'arrow', 'items': [{'path': [[108.9, 34.35], [110.6, 35.0], [112.6, 35.6], [114.1, 36.05]], 'label': 'conquest, c. 1046 BCE', 'lab': [111.4, 35.35], 'ldy': -10}]},
   {'type': 'route', 'items': [{'path': [[108.85, 34.12], [110.6, 34.3], [112.3, 34.57]], 'label': 'court moves east, 770 BCE', 'lab': [110.6, 34.3], 'ldy': 16, 'acc': True, 'head': True}]},
   {'type': 'points', 'items': [
    {'ll': [108.72, 34.21], 'label': 'Feng and Hao', 'date': 'Western Zhou capitals', 'acc': True, 'big': True, 'anchor': 'end', 'dy': 14, 'plate': {'kicker': '5.9 · the Zhou', 'title': 'Feng and Hao', 'sub': 'the Western Zhou capitals, near Xi\'an', 'text': "[[c-mandate]] [[c-771]]", 'sources': ['lifeng2006', 'sep-mencius']}},
    {'ll': [107.2, 34.37], 'label': 'Baoji', 'date': 'He zun found, 1963', 'dy': -8, 'plate': {'kicker': '5.9 · the Zhou', 'title': 'The He zun', 'sub': 'found at Baoji, 1963', 'text': "[[c-he-zun]]", 'sources': ['chinadaily-hezun']}},
    {'ll': [114.319, 36.123], 'label': 'Anyang', 'date': 'last Shang capital', 'anchor': 'end', 'dy': -8},
    {'ll': [112.45, 34.62], 'label': 'Luoyi', 'date': 'Eastern Zhou capital', 'dy': 14, 'plate': {'kicker': '5.9 · the Zhou', 'title': 'Luoyi', 'sub': 'modern Luoyang', 'text': "[[c-771]]", 'sources': ['lifeng2006', 'khayutina2008']}}]}]},
 'practice': [
  q("What made the Mandate of Heaven politically powerful?",
    ["It made the Zhou royal line legitimate forever, whatever its conduct", "It tied rule to virtue, so a winning revolt could show Heaven's will", "It was probably an old Shang belief that the Zhou kept and extended", "It forbade rebellion against any king who held the throne"], 1,
    "Heaven favoured rulers of virtue, so legitimacy depended on conduct, not descent alone.",
    {0: "If Heaven could transfer the mandate to the Zhou, it could transfer it again.", 2: "It first appears in early Zhou bronzes and texts; the Shang looked to their ancestors and to Di.", 3: "It justified the Zhou's own revolt against the Shang."}),
  q("Why do historians prize bronze inscriptions such as the Li gui?",
    ["They give exact reign lengths for each one of the early Zhou kings", "They were cast near the events, not edited centuries afterwards", "They settle the year of the conquest beyond further argument", "They preserve a script that nobody has yet managed to read"], 1,
    "The Li gui was cast soon after the conquest, so it is contemporary evidence that can be checked against later histories.",
    {0: "Even the year of the conquest is still debated, let alone the length of each reign.", 2: "Scholars still argue for 1046, 1045 or 1040 BCE.", 3: "The Li gui's inscription is read today: it records King Wu's attack on a jiazi day."})]}

P10 = {
 'title': "How we know early China", 'sub': "texts, bones, bronzes and politics",
 'lede': "Early Chinese history rests on three kinds of evidence: histories written down centuries later, oracle bones and bronzes from the time, and archaeology. Where they meet, history becomes firm. Where they do not, it becomes contested, and sometimes political.",
 'body': [
  "The great early history is the Shiji of Sima Qian, written about 100 BCE. It gives year-by-year dates only from 841 BCE; before that it offers lists of rulers. [[c-841]] For the Shang, those lists were dramatically confirmed. The oracle bones showed the Shang existed, and the line of kings reconstructed from them matches Sima Qian's list, written about a thousand years later, with only minor differences. [[c-oracle-confirm]] Radiocarbon dates on the bones themselves now place King Wu Ding about 1254-1197 BCE. [[c-wuding]] For the Xia, no such confirmation exists (5.5).",
  "In the late 1990s the Chinese state sponsored the Xia-Shang-Zhou Chronology Project, about 200 scholars led by Li Xueqin, [[c-xszcp]] to fix the dates before 841. It placed the Xia about 2070-1600 BCE and the Zhou conquest in 1046. [[c-xszcp-results]] Critics outside China called its precision unjustified, and some saw nationalist motives. [[c-xszcp-critics]]",
  "A second project, on the origins of Chinese civilization, announced in 2018 that regional civilizations existed by about 5,300 years ago, at sites such as Liangzhu. [[c-origins-project]] In 2022 Xi Jinping spoke of China's 'more than 5,000 years of civilization', linking the research to national rejuvenation. [[c-xi-5000]] Some scholars worry that archaeology is being drawn into a national story. [[c-national-narrative]]",
  {'table': {'head': ["Evidence", "Written", "What it can tell us"], 'rows': [
    ["Shiji and other histories", "c. 100 BCE and later", "king lists, stories; dates only from 841 BCE"],
    ["Oracle bones", "c. 1250-1046 BCE", "Shang kings, rituals, events"],
    ["Bronze inscriptions", "Shang and Zhou", "grants, wars, dates within reigns"],
    ["Archaeology and radiocarbon", "not written", "cities, burials, dates in ranges"]]}},
  {'compare': "Compare the Sumerian King List (3.4), the Egyptian king lists (4.12) and the debates over the Bible's early history (4.9). In each case a later written tradition meets archaeology, and the questions are much the same."}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "When did the Zhou conquer the Shang?", 'title': "Proposed dates for the conquest, BCE",
  'max': 1075, 'min': 1015, 'unit': 'ka', 'ticks': [1070, 1060, 1050, 1040, 1030, 1020], 'tickLabels': ['1070 BCE', '1060', '1050', '1040', '1030', '1020'],
  'axis': "years BCE", 'hint': "Hover or click a row",
  'rows': [
   {'t': 'Older proposal', 'from': 1070.6, 'to': 1069.4, 'lab': '1070', 'open': True},
   {'t': 'Radiocarbon range', 'sub': 'used by the Project', 'from': 1050, 'to': 1020, 'lab': 'c. 1050-1020', 'open': True},
   {'t': 'Chronology Project (2000)', 'sub': 'also Pankenier', 'from': 1046.6, 'to': 1045.4, 'lab': '1046', 'acc': True, 'plate': {'kicker': '5.10 · chronology', 'title': 'The Xia-Shang-Zhou Chronology Project', 'sub': '1046 BCE', 'text': "[[c-xszcp]] [[c-xszcp-results]] [[c-xszcp-critics]]", 'sources': ['shaughnessy2023', 'nyt2000']}},
   {'t': 'Shaughnessy (1985)', 'from': 1045.6, 'to': 1044.4, 'lab': '1045'},
   {'t': 'Nivison (1999)', 'from': 1040.6, 'to': 1039.4, 'lab': '1040'},
   {'t': 'Older proposal', 'from': 1027.6, 'to': 1026.4, 'lab': '1027', 'open': True}],
  'notes': ["Sources: CGTN; Pankenier (1981); Shaughnessy (1985); Nivison (1999)."]},
 'practice': [
  q("Why is the match between the oracle bones and Sima Qian's list of Shang kings such a famous result?",
    ["It proved early Chinese traditions true, those about the Xia included", "Records of the time confirmed a list written a thousand years later", "It supplied exact years for the reign of each Shang king", "It settled the year of the Zhou conquest at 1046 BCE"], 1,
    "Evidence from the Shang's own time matched a tradition written about a thousand years later, with only minor differences.",
    {0: "For the Xia no such confirmation exists.", 2: "The bones matched the names and order of kings; the Shiji gives no year-by-year dates before 841 BCE.", 3: "That date is still argued over."}),
  q("What was the core scholarly objection to the Chronology Project?",
    ["It relied on legends and set aside the evidence of archaeology", "Its precise dates were unjustified, and dated bronzes conflict", "Its scholars did not publish a report for others to check", "It dated the Shang too late, putting its start after 1300 BCE"], 1,
    "Critics outside China called its precision unjustified. Shaughnessy argued in 2023, from fully dated bronze inscriptions, that its Western Zhou chronology is wrong throughout.",
    {0: "It brought together archaeologists, palaeographers and astronomers as well as historians.", 2: "It published a short report in 2000 and its full report in 2022.", 3: "It dated the Shang from about 1600 BCE; the complaint was false precision, not lateness."})]}

P11 = {
 'title': "Four river civilizations compared", 'sub': "Mesopotamia, Egypt, the Indus and early China",
 'lede': "The first four civilizations arose on great rivers, separately and in different ways. Set side by side, they show what early states had in common, and how differently they could be organised.",
 'body': [
  "All four grew from farming villages along rivers that flooded, and all built cities, specialised crafts and long-distance trade. Three developed writing early; China's earliest surviving writing comes almost two thousand years after Mesopotamia's.",
  {'table': {'head': ["", "Mesopotamia", "Egypt", "Indus", "Early China"], 'rows': [
    ["first cities", "4th millennium BCE (3.1)", "Memphis, c. 3000 BCE (4.1)", "c. 2600 BCE", "Liangzhu, c. 3300 BCE (5.4)"],
    ["earliest writing", "c. 3300-3000 BCE [[c-cmp-meso]]", "c. 3200 BCE [[c-cmp-uj]]", "signs from c. 3300? [[c-cmp-indus-early]]", "oracle bones, c. 1250 BCE"],
    ["can we read it?", "yes", "yes", "no [[c-no-bilingual]]", "yes; still in use [[c-continuity]]"],
    ["largest city", "Uruk, c. 250 ha (c. 3200 BCE); c. 500 ha by 3000 BCE (3.1)", "uncertain", "Mohenjo-daro c. 240 ha; Rakhigarhi larger?", "Yinxu (Anyang): a scattered site zone of c. 30 km², not comparable with walled-city areas [[c-yinxu-size]]"],
    ["visible kings", "yes: palaces, inscriptions", "yes: pharaohs", "none identified [[c-no-palaces]]", "yes: Shang kings"],
    ["people killed at rulers' burials", "yes, at Ur (3.5)", "yes, in the 1st Dynasty (4.1)", "none known", "yes, at Anyang (5.6)"],
    ["end of the early phase", "Akkad and after (3.6)", "Old Kingdom collapse (4.6)", "gradual decline, from c. 1900 BCE", "Zhou conquest, c. 1046 BCE"]],
   'note': "[[c-cmp-sacrifice]]"}},
  "The biggest contrast is the Indus. The other three left kings everywhere: in palaces, tombs, statues and inscriptions. The Indus, with cities as large and as planned, left no image anyone can identify as a ruler. [[c-no-palaces]] Whether that reflects a different kind of society or only what survives is one of archaeology's great open questions.",
  "The second contrast is writing. Cuneiform and hieroglyphs died out and had to be deciphered in modern times; the Indus script has never been read; Chinese writing has been in continuous use for more than three thousand years. [[c-continuity]]",
  {'compare': "Chapter 6 turns to what happened next: the Late Bronze Age, when Egypt, the Hittites, Babylon and their neighbours formed a club of great powers, and then collapsed together."}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "When did each civilization begin to write?", 'title': "Earliest writing, or possible writing, BCE",
  'max': 3500, 'min': 1000, 'unit': 'ka', 'ticks': [3500, 3000, 2500, 2000, 1500, 1000], 'tickLabels': ['3500 BCE', '3000', '2500', '2000', '1500', '1000'],
  'axis': "years BCE; all dates approximate", 'hint': "Hover or click a row",
  'rows': [
   {'t': 'Mesopotamia', 'sub': 'earliest tablets', 'from': 3300, 'to': 3000, 'lab': 'c. 3300-3000', 'acc': True},
   {'t': 'Egypt', 'sub': 'U-j labels', 'from': 3250, 'to': 3150, 'lab': 'c. 3200', 'acc': True},
   {'t': 'Indus', 'sub': 'early marks', 'from': 3300, 'to': 2800, 'lab': 'c. 3300-2800?', 'open': True, 'plate': {'kicker': '5.11 · writing', 'title': 'Early Indus marks', 'sub': 'Ravi phase, c. 3300 to 2800 BCE', 'text': "[[c-cmp-indus-early]] [[c-is-writing]]", 'sources': ['meadow-intro', 'farmer2004', 'rao2009']}},
   {'t': 'Indus', 'sub': 'mature script', 'from': 2600, 'to': 1900, 'lab': 'c. 2600-1900', 'acc': True},
   {'t': 'China', 'sub': 'oracle bones', 'from': 1250, 'to': 1046, 'lab': 'c. 1250-1046', 'acc': True, 'plate': {'kicker': '5.11 · writing', 'title': 'Oracle-bone writing', 'sub': 'c. 1250 to 1046 BCE', 'text': "[[c-continuity]] [[c-graphs]] [[c-wuding]]", 'sources': ['cam-oracle', 'tencent-oracle', 'liu2021-c14']}}]},
 'practice': [
  q("Which feature most sets the Indus apart from the other three early civilizations?",
    ["Its writing appeared far later than in the other three", "No visible kings, together with a script that is still unread", "Its largest city was far smaller than those of the others", "It alone had cities that grew out of riverside farming villages"], 1,
    "The other three have visible kings and readable writing. The Indus has no identified palaces, royal tombs or images of rulers, and its script is unread.",
    {0: "Marks at Harappa from about 3300-2800 BCE may be early Indus signs, long before China's earliest writing, about 1250 BCE.", 2: "Mohenjo-daro, about 240 hectares, was close to Uruk's 250.", 3: "All four grew from farming villages along rivers."}),
  q("What does the killing of people at royal burials in Mesopotamia, Egypt and Shang China suggest?",
    ["One religion that spread from Mesopotamia to Egypt and to China", "Rulers with power over life and death, a sign of extreme hierarchy", "A custom the four river civilizations shared, the Indus included", "Kings without writing, who showed off their power through burials"], 1,
    "In all three it accompanied the most powerful rulers.",
    {0: "Nothing on this page shows the custom passing between them; they lay far apart.", 2: "No such burials are known from the Indus, though few Indus cemeteries have been fully excavated.", 3: "All three had writing: Mesopotamia from about 3300-3000 BCE, Egypt about 3200 BCE, and the Shang on oracle bones."})]}

PAGES = [P8, P9, P10, P11]
