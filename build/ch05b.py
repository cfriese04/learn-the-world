# Chapter 5, pages 5.4 to 5.7. Coordinates are [longitude, latitude].
from common import c, q

S = {
 'brit-yangshao': ("Encyclopaedia Britannica, \"Yangshao culture\"", "https://www.britannica.com/topic/Yangshao-culture"),
 'brit-banpo': ("Encyclopaedia Britannica, \"Banpo site\"", "https://www.britannica.com/place/Banpo-site"),
 'unesco-liangzhu': ("UNESCO World Heritage, \"Archaeological Ruins of Liangzhu City\"", "https://whc.unesco.org/en/list/1592/"),
 'chinadaily-liangzhu': ("China Daily, \"Ancient site stands the test of time\" (2019)", "https://www.chinadaily.com.cn/global/2019-07/08/content_37489051.htm"),
 'phys-liangzhu': ("Phys.org on Liu Bin et al., \"Earliest hydraulic enterprise in China\", PNAS (2017)", "https://phys.org/news/2017-12-earliest-large-hydraulic-enterprise-excavated.html"),
 'renfrew-liu2018': ("Renfrew and Liu, \"The emergence of complex society in China: the case of Liangzhu\", Antiquity (2018)", "https://www.cambridge.org/core/journals/antiquity/article/emergence-of-complex-society-in-china-the-case-of-liangzhu/0D4FD61E9460755CED69047FAD7FA2AD"),
 'smarthistory-cong': ("Smarthistory, \"Cong\" (with British Museum)", "https://smarthistory.org/?p=4777"),
 'brit-longshan': ("Encyclopaedia Britannica, \"Longshan culture\"", "https://www.britannica.com/topic/Longshan-culture"),
 'icomos-taosi': ("ICOMOS-IAU Astronomical Heritage thematic study, \"Taosi\"", "https://web.astronomicalheritage.org/images/astronomicalheritage.org/thematic-study/ch05cs1.pdf"),
 'wu2009-taosi': ("Wu, Chen and Liu, \"Astronomical function and date of the Taosi observatory\", Science in China G (2009)", "https://link.springer.com/doi/10.1007/s11433-009-0017-1"),
 'natgeo-shimao': ("National Geographic on carvings and sacrifice at Shimao", "https://www.nationalgeographic.com/history/article/mysterious-carvings-evidence-human-sacrifice-uncovered-ancient-city-china"),
 'nature-shimao2025': ("Chen et al., ancient genomes from Shimao, Nature (2025)", "https://www.nature.com/articles/s41586-025-09799-x"),
 'jaang2018': ("Jaang et al., \"When peripheries were centres: the Shimao-centred polity\", Antiquity (2018)", "https://www.cambridge.org/core/journals/antiquity/article/when-peripheries-were-centres-a-preliminary-study-of-the-shimaocentred-polity-in-the-loess-highland-china/EA48B7FEF5512D41D615DC3480DE0DDC"),
 'newschina-origins': ("NewsChina, \"All Points of Origin\" (2022)", "https://www.pressreader.com/china/newschina/20221124/281934546812534"),
 'zhang2019': ("Zhang, Pollard, Rawson et al., \"China's major Late Neolithic centres and the rise of Erlitou\", Antiquity (2019)", "https://www.cambridge.org/core/journals/antiquity/article/chinas-major-late-neolithic-centres-and-the-rise-of-erlitou/F24DD8C8A86BF6FA5953A9045A0223CD"),
 'lawler2009b': ("Andrew Lawler, \"Founding Dynasty or Myth?\", Science 325 (2009)", "https://www.andrewlawler.com/?p=1193"),
 'gt-erlitou': ("Global Times on the Erlitou site museum (2023)", "https://globaltimes.cn/page/202303/1287035.shtml"),
 'stonepages-dragon': ("Stone Pages, the Erlitou turquoise dragon", "https://www.stonepages.com/news/archives/002011.html"),
 'brit-xia': ("Encyclopaedia Britannica, \"Xia dynasty\"", "https://www.britannica.com/topic/Xia-dynasty"),
 'liu-xu2007': ("Liu Li and Xu Hong, \"Rethinking Erlitou: legend, history and Chinese archaeology\", Antiquity (2007)", "https://www.cambridge.org/core/journals/antiquity/article/abs/rethinking-erlitou-legend-history-and-chinese-archaeology/FDBD0E8E7C661FC180CAD54AD9742E31"),
 'scinews-flood': ("Sci.News on Wu Qinglong et al., Science (2016)", "https://www.sci.news/archaeology/geological-evidence-chinas-great-flood-04083.html"),
 'science-flood-comment': ("Comment on the Jishi Gorge flood claim, Science (2017)", "https://ui.adsabs.harvard.edu/abs/2017Sci...355Q1382W"),
 'brit-shang': ("Encyclopaedia Britannica, \"Shang dynasty\"", "https://www.britannica.com/topic/Shang-dynasty"),
 'met-shangzhou': ("The Met, \"Shang and Zhou Dynasties: The Bronze Age of China\"", "https://www.metmuseum.org/essays/shang-and-zhou-dynasties-the-bronze-age-of-china"),
 'brit-china-shang': ("Encyclopaedia Britannica, \"China: the Shang dynasty\"", "https://www.britannica.com/place/China/The-Shang-dynasty"),
 'unesco-yinxu': ("UNESCO World Heritage, \"Yin Xu\"", "https://whc.unesco.org/en/list/1114/"),
 'sapiens-oracle': ("Christina Cheung, SAPIENS, on Shang sacrifice and oracle bones (2018)", "https://www.sapiens.org/archaeology/chinese-oracle-bones-history/"),
 'smarthistory-fuhao': ("Smarthistory, \"Who was Fu Hao?\"", "https://smarthistory.org/?p=59817"),
 'hunan-ding': ("Hunan Museum, the Si Mu Wu (Houmuwu) ding", "https://web.hnmuseum.com/en/node/6744"),
 'rawson2020': ("Rawson et al., on chariots and Anyang (2020)", "https://libmast.utm.my/Record/oxford-uuid:51b8bf31-edcf-408d-a149-4bff736dcd89"),
 'brit-shangdi': ("Encyclopaedia Britannica, \"Shangdi\"", "https://www.britannica.com/topic/Shangdi"),
 'whe-oracle': ("World History Encyclopedia, \"Oracle Bones\"", "https://www.worldhistory.org/Oracle_Bones/"),
 'tencent-oracle': ("Tencent, oracle bone corpus project (2024)", "https://www.tencent.com/en-us/articles/2201854.html"),
 'brit-oraclebone': ("Encyclopaedia Britannica, \"Oracle bone\"", "https://www.britannica.com/topic/oracle-bone"),
 'hyperallergic-oracle': ("Hyperallergic, \"Oracle bones: a 3,000-year-old voice of the dead\"", "https://hyperallergic.com/oracle-bones-a-3000-year-old-voice-of-the-dead"),
 'hust-oracle': ("Huazhong University of Science and Technology, AI and oracle-bone decipherment (2024)", "https://english.hust.edu.cn/info/1106/3917.htm"),
 'cam-oracle': ("Cambridge University Library, \"Inscriptions on bone\"", "https://exhibitions.lib.cam.ac.uk/linesofthought/artifacts/inscriptions-on-bone/"),
 'li2003-jiahu': ("Li, Harbottle, Zhang and Wang, \"The earliest writing? Sign use in the seventh millennium BC at Jiahu\", Antiquity (2003)", "https://www.cambridge.org/core/product/6DDB3E0583ACB6896B3DBCAC143FA846"),
}

C = {
 # 5.4
 'c-yangshao': c("The Yangshao culture of the Yellow River basin, about 5000-3000 BCE, farmed millet and made painted pottery; Banpo near Xi'an is its best-known village.", 'approx', ['brit-yangshao', 'brit-banpo'], show=False),
 'c-liangzhu': c("Liangzhu, near the lower Yangzi, about 3300-2300 BCE, was a walled city of roughly 300 hectares, with a system of dams in the surrounding hills and plain.", 'approx', ['unesco-liangzhu', 'chinadaily-liangzhu', 'phys-liangzhu'], "Sources give the inner city as about 280-300 hectares."),
 'c-liangzhu-water': c("Its dams, built about 5,000 years ago, are among the oldest large-scale water-management works in the world; one estimate is that 3,000 people worked for 8 years on one of the larger dams.", 'approx', ['phys-liangzhu', 'unesco-liangzhu'], show=False),
 'c-liangzhu-state': c("Some archaeologists argue Liangzhu was the earliest state society in East Asia.", 'debated', ['renfrew-liu2018'], "Colin Renfrew and Liu Bin make the case; whether 'state' is the right word depends on definitions."),
 'c-jade': c("Liangzhu's elite were buried with jade cong (square tubes) and bi (discs), whose meaning is unknown.", 'consensus', ['smarthistory-cong'], show=False),
 'c-longshan': c("The Longshan culture, about 2600-2000 BCE, built rammed-earth walls and divined by cracking heated bones.", 'approx', ['brit-longshan'], show=False),
 'c-taosi': c("Taosi in Shanxi grew to a walled town of about 2.8 km² in the 21st century BCE.", 'approx', ['icomos-taosi'], show=False),
 'c-taosi-obs': c("A semicircular platform at Taosi has slots that line up with sunrise at the solstices about 2100 BCE, and is claimed as an observatory.", 'debated', ['wu2009-taosi', 'icomos-taosi'], "Chinese excavators and astronomers argue it marked a solar calendar; others are more cautious about how precisely the slots can be read."),
 'c-shimao': c("Shimao, in northern Shaanxi, about 2300-1800 BCE, was a stone-walled city of roughly 400 hectares with a terraced core about 70 metres high and pits of human skulls at its gate.", 'approx', ['natgeo-shimao', 'nature-shimao2025'], show=False),
 'c-shimao-dna': c("Ancient DNA from 169 people at Shimao (2025) shows ancestry mainly from earlier farmers of the region, family trees traced through men, and that the skull-pit victims at the East Gate were mostly male.", 'approx', ['nature-shimao2025'], "Earlier studies of the bones had suggested most victims were young women; DNA shows 9 of 10 sampled were male. Victims in elite cemeteries were mostly female."),
 'c-many-centres': c("Archaeologists debate whether Chinese civilization grew from one centre in the Central Plains or from many regional centres, like 'stars in the sky'.", 'debated', ['newschina-origins', 'zhang2019', 'jaang2018'], "Su Bingqi proposed several regional origins; Yan Wenming stressed overall unity with a central role for the Central Plains. Large centres such as Liangzhu, Taosi and Shimao lay outside the Central Plains."),
 # 5.5
 'c-erlitou': c("Erlitou, near Luoyang, was a planned centre with palace foundations, bronze workshops and some of China's earliest bronze ritual vessels, from about 1750 BCE.", 'approx', ['lawler2009b', 'gt-erlitou'], "Newer radiocarbon dates moved its start later, from about 1900 to about 1750 BCE."),
 'c-dragon': c("A dragon made of more than 2,000 pieces of turquoise was found in an elite grave at Erlitou in 2002.", 'consensus', ['gt-erlitou', 'stonepages-dragon'], show=False),
 'c-xia-trad': c("Chinese historical tradition makes the Xia the first dynasty, founded by Yu the Great, who tamed a great flood; modern Chinese chronology dates it about 2070-1600 BCE.", 'tradition', ['brit-xia'], "The 2070-1600 dates come from the Xia-Shang-Zhou Chronology Project (2000); older traditional reckonings differ. The Xia is known from texts written more than a thousand years later."),
 'c-erlitou-xia': c("Most Chinese archaeologists identify Erlitou as a Xia capital; many scholars elsewhere are cautious, because no writing of the time names the Xia.", 'debated', ['gt-erlitou', 'liu-xu2007', 'lawler2009b'], "Liu Li and Xu Hong argue for separating the legendary texts from the archaeological record; the later radiocarbon dates also fit the traditional Xia dates less well."),
 'c-yu-flood': c("A 2016 study linked the flood of Yu to a landslide-dam outburst in the Yellow River about 1920 BCE; other scientists say the evidence cannot bear that conclusion.", 'debated', ['scinews-flood', 'science-flood-comment'], show=False),
 # 5.6
 'c-shang-dates': c("The Shang dynasty is conventionally dated about 1600-1046 BCE; its last capital, at Anyang, about 1250-1046.", 'approx', ['brit-shang', 'brit-china-shang', 'unesco-yinxu'], "Other estimates for the founding range from 1760 to 1520 BCE; UNESCO dates the move to Anyang about 1300 BCE.", show=False),
 'c-shang-cities': c("Earlier Shang cities at Zhengzhou and Yanshi had massive rammed-earth walls; Zhengzhou's was 36 metres wide at its base.", 'approx', ['brit-china-shang'], show=False),
 'c-yinxu': c("Yinxu, the Shang capital at Anyang, has more than 80 palace and temple foundations and the earliest large royal cemetery in China.", 'consensus', ['unesco-yinxu'], show=False),
 'c-sacrifice': c("More than 13,000 people may have been sacrificed at Anyang over about two centuries, often 50 and sometimes 300 at a time; isotopes suggest many were outsiders.", 'approx', ['sapiens-oracle'], "Oracle-bone texts name Qiang captives; the physical evidence cannot yet confirm who the victims were."),
 'c-fuhao': c("The tomb of Fu Hao, a royal consort and general, found intact in 1976, held 468 bronzes, 755 jades, about 6,900 cowrie shells, 16 human victims and 6 dogs.", 'consensus', ['smarthistory-fuhao'], show=False),
 'c-piece-mould': c("Shang bronzes were cast in sectioned clay moulds; the largest known, the Houmuwu ding, weighs about 833 kg.", 'consensus', ['met-shangzhou', 'hunan-ding'], show=False),
 'c-chariot': c("Horse-drawn chariots appear in China about 1200 BCE, arriving from the steppe to the north and west.", 'approx', ['brit-china-shang', 'rawson2020'], "How they arrived, by conquest or by contact, is debated.", show=False),
 'c-di': c("Shang kings sacrificed to their ancestors; above them stood Di, a supreme deity who governed weather, harvests and war but had no cult of his own and was thought too distant to be influenced by mortals.", 'consensus', ['brit-shangdi', 'brit-china-shang'], show=False),
 # 5.7
 'c-oracle-discovery': c("Oracle bones were recognised in 1899 when the scholar Wang Yirong noticed writing on 'dragon bones' sold as medicine; in 1908 Luo Zhenyu traced them to Anyang.", 'tradition', ['sapiens-oracle', 'whe-oracle'], "The details of the story are partly legend."),
 'c-oracle-count': c("About 150,000-160,000 inscribed oracle-bone fragments are known, mostly from Anyang.", 'approx', ['sapiens-oracle', 'tencent-oracle'], show=False),
 'c-divination': c("Diviners heated ox shoulder blades and turtle shells until they cracked, read the cracks as answers, and recorded the question, the king's prediction and sometimes what actually happened.", 'consensus', ['brit-oraclebone', 'whe-oracle'], show=False),
 'c-oracle-topics': c("The questions concern weather, harvests, war, illness, childbirth and sacrifices.", 'consensus', ['hyperallergic-oracle', 'brit-oraclebone'], show=False),
 'c-graphs': c("The oracle-bone script has about 4,500 distinct characters, of which about a third have been matched to modern Chinese characters.", 'approx', ['tencent-oracle', 'hust-oracle'], "Counts differ between projects."),
 'c-continuity': c("Oracle-bone writing is the oldest known Chinese script and the direct ancestor of Chinese characters used today.", 'consensus', ['cam-oracle', 'brit-oraclebone'], show=False),
 'c-jiahu': c("Signs carved on tortoise shells at Jiahu, about 6600 BCE, resemble some later characters; their discoverers think they were ritual symbols, not writing.", 'debated', ['li2003-jiahu'], show=False),
 'c-ai-oracle': c("Since 2024, AI tools have been used to suggest modern equivalents for undeciphered oracle-bone characters.", 'consensus', ['tencent-oracle', 'hust-oracle'], show=False),
}

P4 = {
 'title': "Before the Shang", 'sub': "Neolithic China, c. 5000 to 1800 BCE",
 'lede': "Long before any dynasty, farmers along the Yellow River and the Yangzi built villages, then walled towns, then cities. Some of the largest lay far from the region later histories called the centre of China.",
 'body': [
  "Farming villages of the Yangshao culture, about 5000-3000 BCE, grew millet along the Yellow River and made painted pottery; Banpo near Xi'an is the best known. [[c-yangshao]]",
  "In the lower Yangzi, Liangzhu (about 3300-2300 BCE) was a walled city of some 300 hectares, with dams in the hills beyond that controlled flooding and water supply, [[c-liangzhu]] one of the oldest large water-management systems in the world. [[c-liangzhu-water]] Its elite were buried with jade discs and square jade tubes whose meaning is unknown. [[c-jade]] Some archaeologists call it East Asia's first state. [[c-liangzhu-state]]",
  "In the north, the Longshan culture built rammed-earth walls and divined the future by cracking heated bones, [[c-longshan]] a practice the Shang would make famous. Taosi in Shanxi grew to a walled town of nearly 3 km², [[c-taosi]] with a platform that some interpret as a solar observatory. [[c-taosi-obs]] Shimao, on the loess plateau, was a stone-walled city of some 400 hectares with a terraced core about 70 metres high and pits of skulls at its gate. [[c-shimao]] Genomes from Shimao published in 2025 show family lines traced through men, and that the victims at its gate were mostly men, not women as once thought. [[c-shimao-dna]]",
  {'table': {'head': ["Site", "Region", "Dates (BCE)", "Notable for"], 'rows': [
    ["Banpo", "Wei valley (Xi'an)", "Yangshao culture", "painted pottery village"],
    ["Liangzhu", "lower Yangzi", "c. 3300-2300", "dams, jade"],
    ["Taosi", "Shanxi", "c. 2300-1900", "walled town; 'observatory'"],
    ["Shimao", "northern Shaanxi", "c. 2300-1800", "stone walls, sacrifice"]]}},
  "These finds have changed how Chinese civilization's origins are told. The old story began in the Central Plains of the middle Yellow River; many archaeologists now see several regional centres, like 'stars in the sky', that later came together. [[c-many-centres]]"],
 'figure': {'kind': 'map', 'view': {'lon': 114.3, 'lat': 34.0, 'zoom': 28}, 'caption': "Neolithic centres of China, c. 5000-1800 BCE", 'hint': "Click a site",
  'legend': [['pt', 'site'], ['dot', 'large walled centre']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [111.6, 33.0], 'label': 'CENTRAL PLAINS', 'size': 11}, {'ll': [111.0, 37.3], 'label': 'LOESS PLATEAU', 'size': 10}]},
   {'type': 'points', 'items': [
    {'ll': [109.051, 34.273], 'label': 'Banpo', 'date': 'Yangshao', 'anchor': 'end', 'plate': {'kicker': '5.4 · Neolithic China', 'title': 'Banpo', 'sub': 'a Yangshao village near Xi\'an', 'text': "[[c-yangshao]]", 'sources': ['brit-yangshao', 'brit-banpo']}},
    {'ll': [119.991, 30.396], 'label': 'Liangzhu', 'date': 'c. 3300-2300 BCE', 'acc': True, 'big': True, 'anchor': 'end', 'plate': {'kicker': '5.4 · Neolithic China', 'title': 'Liangzhu', 'sub': 'c. 3300 to 2300 BCE', 'text': "[[c-liangzhu]] [[c-liangzhu-water]] [[c-jade]] [[c-liangzhu-state]]", 'facts': [['inner city', 'about 280-300 ha'], ['dams', '11'], ['UNESCO', '2019']], 'sources': ['unesco-liangzhu', 'chinadaily-liangzhu', 'phys-liangzhu']}},
    {'ll': [111.497, 35.891], 'label': 'Taosi', 'date': 'c. 2300-1900 BCE', 'acc': True, 'anchor': 'end', 'plate': {'kicker': '5.4 · Neolithic China', 'title': 'Taosi', 'sub': 'c. 2300 to 1900 BCE', 'text': "[[c-taosi]] [[c-taosi-obs]]", 'sources': ['icomos-taosi', 'wu2009-taosi']}},
    {'ll': [110.325, 38.566], 'label': 'Shimao', 'date': 'c. 2300-1800 BCE', 'acc': True, 'plate': {'kicker': '5.4 · Neolithic China', 'title': 'Shimao', 'sub': 'c. 2300 to 1800 BCE', 'text': "[[c-shimao]] [[c-shimao-dna]]", 'sources': ['natgeo-shimao', 'nature-shimao2025', 'jaang2018']}},
    {'ll': [113.667, 33.613], 'label': 'Jiahu', 'date': 'signs on shells (5.7)', 'dy': 14},
    {'ll': [112.690, 34.693], 'label': 'Erlitou', 'date': 'from c. 1750 BCE (5.5)', 'dy': -8}]}]},
 'practice': [
  q("Why do Liangzhu, Taosi and Shimao matter for the question 'where did Chinese civilization begin?'",
    ["They show that civilization spread out from one Central Plains core", "Large walled centres grew outside the Central Plains before Erlitou", "Their oracle-bone inscriptions are the oldest Chinese writing found", "They were provincial capitals of the Shang in the Yellow River basin"], 1,
    "They support Su Bingqi's view that complex societies arose in several regions, not in the Central Plains alone.",
    {0: "They lay outside the Central Plains, so they support the view that there were several regional centres.", 2: "Longshan diviners cracked bones, a practice the Shang later made famous; no writing is reported from these sites.", 3: "All three are older than the Shang, and Liangzhu lies on the lower Yangzi."}),
  q("What did the 2025 genetic study of Shimao change?",
    ["It showed Shimao's people descended mostly from steppe herders", "It showed the skulls at the gate came from burials, not sacrifice", "It showed the East Gate skull-pit victims were mostly men, not women", "It showed family lines at Shimao were traced through women"], 2,
    "Nine of ten victims sampled were male, overturning earlier estimates made from the bones.",
    {0: "Their ancestry came mainly from earlier farmers of the region.", 1: "The study sampled the skull-pit victims; its new finding concerned their sex.", 3: "The family trees traced descent through men."})]}

P5 = {
 'title': "Erlitou and the Xia question", 'sub': "archaeology meets tradition",
 'lede': "Chinese tradition says the first dynasty was the Xia, founded by Yu the Great after he tamed a flood. Archaeology has found an impressive early city at Erlitou. Whether the two are the same is one of the most charged questions in Chinese history.",
 'body': [
  "Erlitou, near Luoyang, was a planned centre with walled palaces, roads and bronze workshops that made some of China's earliest bronze ritual vessels. [[c-erlitou]] In an elite grave, archaeologists found a dragon made of more than 2,000 pieces of turquoise. [[c-dragon]]",
  "Chinese historical tradition, written down more than a thousand years later, makes the Xia the first dynasty; modern Chinese chronology dates it about 2070-1600 BCE. [[c-xia-trad]] Most archaeologists in China identify Erlitou as a Xia capital. Many scholars elsewhere are more cautious: no writing from the period names the Xia, and newer radiocarbon dates put Erlitou's start about 1750 BCE, well after the traditional beginning of the Xia. [[c-erlitou-xia]]",
  "The tradition says Yu earned his throne by controlling a great flood. In 2016 a team of geologists argued that a landslide that dammed the Yellow River about 1920 BCE, and then burst, could be the historical kernel of that story; others replied that the evidence cannot support the claim. [[c-yu-flood]]",
  {'table': {'head': ["", "Tradition", "Archaeology"], 'rows': [
    ["first dynasty", "Xia, founded by Yu", "Erlitou culture (name of a site)"],
    ["dates", "c. 2070-1600 BCE (modern reckoning)", "c. 1750 BCE onward"],
    ["writing", "later texts (e.g. Sima Qian)", "none found at Erlitou"],
    ["capital", "several, named in texts", "planned palace centre"]],
   'note': "[[c-xia-trad]] [[c-erlitou-xia]]"}},
  {'compare': "Compare the Sumerian King List (3.4): later texts can preserve real memories and also shape them for political purposes. Page 5.10 looks at how China's early chronology was built."}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "Early China: archaeology and tradition", 'title': "Sites (solid) and traditional dynasties (hatched), BCE",
  'max': 3400, 'min': 1000, 'unit': 'ka', 'ticks': [3400, 3000, 2600, 2200, 1800, 1400, 1000], 'tickLabels': ['3400 BCE', '3000', '2600', '2200', '1800', '1400', '1000'],
  'axis': "years BCE", 'hint': "Hover or click a row",
  'rows': [
   {'t': 'Liangzhu', 'from': 3300, 'to': 2300, 'lab': 'c. 3300-2300'},
   {'t': 'Taosi', 'from': 2300, 'to': 1900, 'lab': 'c. 2300-1900'},
   {'t': 'Shimao', 'from': 2300, 'to': 1800, 'lab': 'c. 2300-1800'},
   {'t': 'Xia', 'sub': 'traditional dates', 'from': 2070, 'to': 1600, 'lab': 'c. 2070-1600', 'open': True, 'plate': {'kicker': '5.5 · tradition', 'title': 'The Xia dynasty', 'sub': 'c. 2070 to 1600 BCE (traditional)', 'text': "[[c-xia-trad]] [[c-erlitou-xia]]", 'sources': ['brit-xia', 'liu-xu2007']}},
   {'t': 'Erlitou', 'from': 1750, 'to': 1520, 'lab': 'from c. 1750', 'acc': True, 'plate': {'kicker': '5.5 · archaeology', 'title': 'Erlitou', 'sub': 'from c. 1750 BCE', 'text': "[[c-erlitou]] [[c-dragon]]", 'sources': ['lawler2009b', 'gt-erlitou']}},
   {'t': 'Shang', 'sub': 'traditional dates', 'from': 1600, 'to': 1046, 'lab': 'c. 1600-1046', 'open': True},
   {'t': 'Anyang (Yinxu)', 'from': 1250, 'to': 1046, 'lab': 'c. 1250-1046', 'acc': True}]},
 'practice': [
  q("Why do many scholars outside China hesitate to call Erlitou 'Xia'?",
    ["Erlitou has no palaces that could have housed a royal court", "Erlitou has no writing of its own time that names the Xia", "Erlitou dates from after the fall of the Shang in 1046 BCE", "Erlitou has no bronze, so it looks too simple for a dynasty"], 1,
    "The name comes from texts written more than a thousand years later, so the identification rests on matching those histories to the archaeology.",
    {0: "It has palace foundations.", 2: "It dates from about 1750 BCE.", 3: "It has early bronze vessels and workshops."}),
  q("How did newer radiocarbon dates affect the identification of Erlitou with the Xia?",
    ["They pushed Erlitou's start back to before 2070 BCE", "They put its start well after the Xia's traditional start", "They showed that Erlitou and Anyang were occupied at the same time", "They settled the debate by matching the traditional Xia dates"], 1,
    "A start about 1750 BCE fits the traditional Xia dates of about 2070-1600 BCE less well, weakening a simple match.",
    {0: "They moved its start later, not earlier.", 2: "The new dates concern Erlitou's start, about 1750 BCE; they say nothing about Anyang.", 3: "The debate continues."})]}

P6 = {
 'title': "The Shang", 'sub': "bronze, ancestors and sacrifice, c. 1600 to 1046 BCE",
 'lede': "The Shang are the first Chinese dynasty confirmed by their own writing. Their kings ruled through ancestors and divination, cast bronze on a colossal scale, and sacrificed people by the thousand.",
 'body': [
  "The Shang are conventionally dated about 1600-1046 BCE. [[c-shang-dates]] Their early cities at Zhengzhou and Yanshi had massive walls of rammed earth. [[c-shang-cities]] Their last capital, at Anyang, called Yinxu ('the ruins of Yin'), has more than 80 palace and temple foundations and China's first great royal cemetery. [[c-yinxu]]",
  "Shang religion centred on the dead. The king sacrificed to his ancestors. Above them stood Di, a supreme deity who governed weather, harvests and war but had no cult of his own and was thought too remote to be swayed by mortals. [[c-di]] Offerings were made in bronze vessels, cast in sectioned clay moulds; the largest known weighs about 833 kg. [[c-piece-mould]]",
  "Sacrifice included people. More than 13,000 may have been killed at Anyang over about two centuries, often 50 and sometimes 300 at a time; isotopes suggest many came from elsewhere, perhaps as captives. [[c-sacrifice]]",
  "One tomb, found intact in 1976, belonged to Fu Hao, a royal consort who, oracle bones say, led armies in battle. [[c-fuhao]] Horse-drawn chariots appear at Anyang about 1200 BCE, a technology that came from the steppe. [[c-chariot]]",
  {'table': {'head': ["Fu Hao's tomb", "Count"], 'rows': [["bronze objects", "468"], ["jades", "755"], ["cowrie shells", "about 6,900"], ["human victims", "16"], ["dogs", "6"]], 'note': "Smarthistory. [[c-fuhao]]"}},
  {'compare': "Compare the royal tombs of Ur (3.5) and the 1st-Dynasty kings of Egypt (4.1), also buried with people killed to accompany them."}],
 'figure': {'kind': 'map', 'view': {'lon': 113.5, 'lat': 35.4, 'zoom': 140}, 'caption': "Shang cities on the middle Yellow River", 'hint': "Click a city",
  'legend': [['pt', 'city'], ['dot', 'Shang capital']], 'seas': False,
  'layers': [{'type': 'points', 'items': [
   {'ll': [112.690, 34.693], 'label': 'Erlitou', 'date': 'pre-Shang', 'anchor': 'end', 'dy': 14},
   {'ll': [112.74, 34.73], 'label': 'Yanshi', 'date': 'early Shang walls', 'dy': -8, 'plate': {'kicker': '5.6 · the Shang', 'title': 'Yanshi and Zhengzhou', 'sub': 'early Shang cities', 'text': "[[c-shang-cities]]", 'sources': ['brit-china-shang']}},
   {'ll': [113.690, 34.752], 'label': 'Zhengzhou', 'date': 'c. 1600 BCE', 'acc': True},
   {'ll': [114.319, 36.123], 'label': 'Anyang (Yinxu)', 'date': 'c. 1250-1046 BCE', 'acc': True, 'big': True, 'anchor': 'end', 'plate': {'kicker': '5.6 · the Shang', 'title': 'Yinxu, the last Shang capital', 'sub': 'Anyang, c. 1250 to 1046 BCE', 'text': "[[c-yinxu]] [[c-sacrifice]] [[c-fuhao]] [[c-chariot]]", 'facts': [['palace and temple foundations', 'over 80'], ['tomb of Fu Hao', 'found intact, 1976']], 'sources': ['unesco-yinxu', 'sapiens-oracle', 'smarthistory-fuhao']}}]}]},
 'practice': [
  q("What does the tomb of Fu Hao show that the great royal tombs at Anyang cannot?",
    ["That the Shang court had not yet begun to use writing", "A full set of elite grave goods, since it was found intact", "That royal women at Anyang took no part in war or politics", "That the Shang had stopped killing people to bury with the dead"], 1,
    "It was found intact in 1976, with 468 bronzes, 755 jades and about 6,900 cowrie shells.",
    {0: "Oracle bones mention Fu Hao, so the court was already writing.", 2: "Oracle bones say Fu Hao, a royal consort, led armies in battle.", 3: "It held 16 human victims."}),
  q("Which statement about Shang human sacrifice fits the evidence?",
    ["Most victims were local nobles who chose to die with their kings", "Oracle bones and DNA suggest most victims were Qiang captives", "Thousands died over two centuries; isotopes suggest many outsiders", "Sacrifice began after the Shang fell, under the early Zhou kings"], 2,
    "More than 13,000 may have been killed at Anyang over about two centuries, and isotopes point to non-local origins.",
    {0: "Isotopes suggest many were not local.", 1: "No DNA study has identified the victims; the Qiang link comes from oracle-bone texts and is unconfirmed.", 3: "It is documented at Anyang, under the late Shang."})]}

P7 = {
 'title': "Oracle bones and Chinese writing", 'sub': "questions put to the ancestors",
 'lede': "The Shang kings asked their ancestors about everything: rain, harvests, war, childbirth, toothache. The answers, cut into bone and shell, are the oldest Chinese writing, and the ancestor of the characters used by over a billion people today.",
 'body': [
  "The story goes that in 1899 a scholar, Wang Yirong, noticed writing on 'dragon bones' sold as medicine; in 1908 another scholar, Luo Zhenyu, traced them to Anyang. [[c-oracle-discovery]] About 150,000 inscribed fragments are now known. [[c-oracle-count]]",
  "Diviners drilled hollows in an ox shoulder blade or a turtle shell, applied heat until it cracked, and read the cracks as the ancestors' answer. Then a scribe carved the record: the date and the diviner, the question, the king's reading of the cracks, and sometimes what actually happened. [[c-divination]] The questions concern weather, harvests, war, illness, childbirth and sacrifices. [[c-oracle-topics]] One shell asks whether Fu Hao's childbirth will go well.",
  "Because many records note the outcome, the oracle bones are a dated archive of events, and they confirmed the list of Shang kings preserved by later historians (5.10).",
  {'table': {'head': ["Part of an inscription", "Example of the kind of thing recorded"], 'rows': [["preface", "the day and the diviner's name"], ["charge", "'It will rain'"], ["prognostication", "the king reads the cracks"], ["verification", "what happened afterwards"]], 'note': "[[c-divination]]"}},
  "The script already looks mature, which suggests writing began earlier, perhaps on materials that have not survived; signs carved on shells at Jiahu thousands of years before are probably symbols, not writing. [[c-jiahu]] About 4,500 distinct oracle-bone characters are known, and about a third have been matched to modern ones. [[c-graphs]] Since 2024, AI tools have been suggesting matches for the rest. [[c-ai-oracle]] The writing system is continuous: these characters are the direct ancestors of Chinese characters today. [[c-continuity]]",
  {'compare': "Compare cuneiform (3.2) and hieroglyphs (4.5), which died out and had to be deciphered. Chinese writing never stopped being used."}],
 'figure': {'kind': 'chart', 'chart': 'split', 'caption': "How much of the oracle-bone script can be read?", 'title': "About 4,500 distinct oracle-bone characters",
  'hint': "Hover a bar",
  'rows': [
   {'t': 'Characters matched to modern Chinese', 'parts': [{'v': 1550, 'lab': 'read: about a third', 'acc': True, 'name': 'deciphered', 'tip': 'about 1,500-1,600 characters'}, {'v': 2950, 'lab': 'not yet read: about two thirds', 'name': 'undeciphered'}]}],
  'notes': ["Sources: Tencent (2024); Huazhong University of Science and Technology (2024). Counts differ between projects."]},
 'practice': [
  q("Why are the 'verification' lines on oracle bones so valuable to historians?",
    ["They list the Xia kings who ruled before the Shang came to power", "They record what happened afterwards, giving dated events", "They were written by commoners, not by the king's diviners", "They are in a script unrelated to later Chinese characters"], 1,
    "Outcomes added after the king's prediction turn divination records into a dated archive of events.",
    {0: "The oracle bones confirmed the list of Shang kings, not Xia kings.", 2: "The records centre on the king, whose reading of the cracks they note.", 3: "The script is the direct ancestor of Chinese characters."}),
  q("What do the signs on shells from Jiahu, about 6600 BCE, show?",
    ["Fully developed writing was already in use in China by that early date", "Signs predate Shang writing by millennia but are probably not writing", "The Jiahu signs can now be read as early Chinese characters", "Divination with inscribed oracle bones first began at Jiahu"], 1,
    "The signs resemble some later characters, but their discoverers interpret them as ritual symbols, not writing.",
    {0: "Even their discoverers think the signs were ritual symbols, not writing.", 2: "They resemble some later characters but have no accepted readings.", 3: "Inscribed oracle bones come from the Shang, mostly from Anyang."})]}

PAGES = [P4, P5, P6, P7]
