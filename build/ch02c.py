# Chapter 2, pages 2.8 to 2.11. Coordinates are [longitude, latitude].
from common import c, q

S = {
 'unesco-jericho': ("UNESCO World Heritage, \"Ancient Jericho/Tell es-Sultan\"", "https://whc.unesco.org/en/list/1687/"),
 'sd-jericho': ("ScienceDaily on Liran and Barkai, \"Casting a shadow on Neolithic Jericho\", Antiquity (2011)", "https://sciencedaily.com/releases/2011/02/110217125205.htm"),
 'yuncu2025': ("Yüncü et al., \"Female lineages and changing kinship patterns in Neolithic Çatalhöyük\", Science (2025)", "https://research.hub.ku.edu.tr/entities/publication/1a9819a8-c469-4fc9-aa73-50876353a431/full"),
 'bonn-catal': ("University of Bonn, \"Was the Neolithic settlement at Çatalhöyük a matriarchate?\" (2025)", "https://www.uni-bonn.de/en/news/was-the-neolithic-settlement-at-catalhoyuk-a-matriarchate"),
 'catal-guide': ("Çatalhöyük Research Project, Çatalhöyük Guidebook (Koç University)", "https://catalhoyuk.ku.edu.tr/sites/default/files/Catalhoyuk-Guidebook-ENGLISH.pdf"),
 'osu-larsen': ("Ohio State University on Larsen et al., PNAS (2019)", "https://news.osu.edu/9000-years-ago-a-community-with-modern-urban-problems/"),
 'stanford-hodder': ("Stanford University, Ian Hodder on Çatalhöyük (2015)", "https://news.stanford.edu/stories/2015/08/hodder-neolithic-dig-080715"),
 'dsb-aingh': ("Denise Schmandt-Besserat, \"'Ain Ghazal 'Monumental' Figures\" (University of Texas)", "https://sites.utexas.edu/dsb/files/2018/07/Monumental-Figures.pdf"),
 'brit-aingh': ("Encyclopaedia Britannica, \"'Ain Ghazal\"", "https://www.britannica.com/place/Ain-Ghazal"),
 'si-aingh': ("Smithsonian Museum Conservation Institute, \"'Ain Ghazal Statues\"", "https://mci.si.edu/ain-ghazal-statues"),
 'zielhofer2012': ("Zielhofer et al., \"The decline of the early Neolithic population center of 'Ain Ghazal\", Quaternary Research (2012)", "https://www.cambridge.org/core/journals/quaternary-research/article/decline-of-the-early-neolithic-population-center-of-ain-ghazal-and-corresponding-earthsurface-processes-jordan-rift-valley/A85EB4EEFBB2E10F9C11DD6161813B9E"),
 'bocquet2011': ("Jean-Pierre Bocquet-Appel, \"The Agricultural Demographic Transition during and after the Agriculture Inventions\", Current Anthropology 52 (2011)", "https://www.journals.uchicago.edu/doi/full/10.1086/659243"),
 'mummert2011': ("Mummert et al., \"Stature and robusticity during the agricultural transition\", Economics & Human Biology 9 (2011)", "https://econpapers.repec.org/RePEc:eee:ehbiol:v:9:y:2011:i:3:p:284-301"),
 'stock2023': ("Stock et al., \"Long-term trends in human body size track regional variation in subsistence transitions\", PNAS (2023)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9942808"),
 'diamond1987': ("Jared Diamond, \"The Worst Mistake in the History of the Human Race\", Discover (1987)", "https://www.discovermagazine.com/the-worst-mistake-in-the-history-of-the-human-race-12157"),
 'sikora2025': ("University of Cambridge on Sikora et al., Nature (2025)", "https://www.cam.ac.uk/research/news/large-scale-dna-study-maps-37000-years-of-human-disease-history"),
 'richerson2001': ("Richerson, Boyd and Bettinger, \"Was agriculture impossible during the Pleistocene but mandatory during the Holocene?\", American Antiquity 66 (2001)", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0002731600042566"),
 'brit-agri': ("Encyclopaedia Britannica, \"How agriculture and domestication began\"", "https://www.britannica.com/topic/agriculture/How-agriculture-and-domestication-began"),
 'hayden2009': ("Brian Hayden, \"The Proof Is in the Pudding: Feasting and the Origins of Domestication\", Current Anthropology 50 (2009)", "https://www.journals.uchicago.edu/doi/10.1086/605110"),
 'bowles2013': ("Phys.org on Bowles and Choi, PNAS (2013)", "https://phys.org/news/2013-05-simulations-early-farming-caught-due.html"),
 'hofmanova2016': ("University of Mainz on Hofmanová et al., PNAS (2016)", "https://press.uni-mainz.de/early-farmers-from-across-europe-were-direct-descendants-of-aegeans"),
 'haak2015': ("Haak et al., \"Massive migration from the steppe was a source for Indo-European languages in Europe\", Nature (2015)", "https://www.nature.com/articles/nature14317"),
 'allentoft2024': ("Allentoft et al., \"Population genomics of post-glacial western Eurasia\", Nature (2024)", "https://www.nature.com/articles/s41586-023-06865-0"),
 'rivollat2020': ("ScienceDaily on Rivollat et al., Science Advances (2020)", "https://sciencedaily.com/releases/2020/05/200529150654.htm"),
 'brit-lbk': ("Encyclopaedia Britannica, \"LBK culture\"", "https://www.britannica.com/topic/LBK-culture"),
 'brace2019': ("Brace et al., \"Ancient genomes indicate population replacement in Early Neolithic Britain\", Nature Ecology & Evolution (2019)", "https://discovery.ucl.ac.uk/id/eprint/10073386/"),
 'pinhasi2005': ("Pinhasi, Fort and Ammerman, \"Tracing the origin and spread of agriculture in Europe\", PLoS Biology (2005)", "https://doaj.org/article/f8a131c290cf4139a63eb7ec37809a3e"),
 'fortes2024': ("Fortes-Lima et al., \"The genetic legacy of the expansion of Bantu-speaking peoples in Africa\", Nature (2024)", "https://ideas.repec.org/a/nat/nature/v625y2024i7995d10.1038_s41586-023-06770-6.html"),
 'almeida2025': ("Almeida et al., Austronesian expansion, Scientific Reports (2025)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12550076"),
 'radivojevic2010': ("Radivojević et al., \"On the origins of extractive metallurgy\", Journal of Archaeological Science 37 (2010)", "https://www.academia.edu/1957412"),
 'varna-city': ("Varna municipality, \"Varna: the oldest gold treasure in the world\"", "https://visit.varna.bg/en/varna_oldest_gold_treasure_in_the_world.html"),
 'higham2007': ("Higham et al., \"New perspectives on the Varna cemetery\", Antiquity (2007)", "https://www.cambridge.org/core/journals/antiquity/article/new-perspectives-on-the-varna-cemetery-bulgaria-ams-dates-and-social-implications/0D02E895D9732774C4ED192C4D199417"),
 'penn-otzi': ("Penn Museum, Expedition magazine, on Ötzi", "https://www.penn.museum/sites/expedition/?p=23809"),
 'iceman': ("South Tyrol Museum of Archaeology, \"The Iceman\"", "https://www.iceman.it/en/the-iceman/"),
 'iceman-dna': ("South Tyrol Museum of Archaeology on Ötzi's genome, Cell Genomics (2023)", "https://www.iceman.it/en/pr_dna_oetzi_2023/"),
 'mgml-wheel': ("City Museum of Ljubljana on the oldest wooden wheel", "https://mgml.si/en/city-museum/news/667/replica-of-the-oldest-wooden-wheel-with-an-axle-for-the-winner-of-the-26th-tour-of-slovenia/"),
 'brit-wheel': ("Encyclopaedia Britannica, \"Wheel\"", "https://www.britannica.com/technology/wheel"),
 'gatech-wheel': ("Georgia Tech on Alacoque, Bulliet and James, Royal Society Open Science (2024)", "https://ae.gatech.edu/news/2024/11/engineering-origin-wheel"),
 'cnrs-botai': ("CNRS on Gaunitz et al., Science (2018)", "https://www.cnrs.fr/en/unsaddling-old-theory-origin-horses"),
 'librado2021': ("Librado et al., \"The origins and spread of domestic horses from the Western Eurasian steppes\", Nature (2021)", "https://www.nature.com/articles/s41586-021-04018-9"),
 'librado2024': ("Sci.News on Librado et al., Nature (2024)", "https://www.sci.news/genetics/modern-horse-domestication-13000.html"),
 'lazaridis2025': ("Lazaridis et al., \"The genetic origin of the Indo-Europeans\", Nature (2025)", "https://ideas.repec.org/a/nat/nature/v639y2025i8053d10.1038_s41586-024-08531-5.html"),
 'bouckaert2012': ("ScienceDaily on Bouckaert et al., Science (2012)", "https://www.sciencedaily.com/releases/2012/08/120823175406.htm"),
 'heggarty2023': ("University of Jena on Heggarty et al., Science (2023)", "https://www.uni-jena.de/en/230728-indogermanistik"),
 'met-uruk2': ("The Met, \"Uruk: The First City\"", "https://www.metmuseum.org/toah/hd/uruk/hd_uruk.html"),
}

C = {
 # 2.8
 'c-jericho': c("Neolithic Jericho had a wall with a ditch and a stone tower; by the 9th-8th millennium BCE it was a sizeable permanent settlement.", 'consensus', ['unesco-jericho'], show=False),
 'c-jericho-tower': c("The Jericho tower, about 8.5 metres high, was built roughly 11,000 years ago and would have taken years of labour.", 'approx', ['sd-jericho'], "The date is from radiocarbon; older books give about 8000 BCE, from earlier dating."),
 'c-jericho-purpose': c("What the tower was for is debated: defence or a flood barrier, a sign of the village's standing, or a monument tied to the summer solstice that drew people into communal life.", 'debated', ['sd-jericho'], "Ran Barkai and Roy Liran (2011) note that the line of its staircase points to the solstice sunset behind a nearby mountain."),
 'c-catal': c("Çatalhöyük in central Turkey was occupied from about 7100 to 5950 BCE and covered about 13.5 hectares.", 'approx', ['yuncu2025', 'catal-guide'], show=False),
 'c-catal-houses': c("Its houses had no streets between them and no doors: people entered through the roof, and buried their dead beneath the floors.", 'consensus', ['catal-guide'], show=False),
 'c-catal-pop': c("At its peak Çatalhöyük had perhaps 3,500-8,000 people.", 'approx', ['osu-larsen', 'catal-guide', 'stanford-hodder'], "Estimates depend on how many houses were lived in at once; Ian Hodder has suggested as many as 10,000."),
 'c-catal-equal': c("Çatalhöyük shows no palace, temple or elite quarter, and men and women ate similar diets; ancient DNA (2025) shows kinship ran mainly through mothers.", 'debated', ['stanford-hodder', 'catal-guide', 'yuncu2025', 'bonn-catal'], "Hodder reads it as a broadly egalitarian society. The 2025 genomes show maternal links and more grave goods for girls, but the researchers caution that this was not a matriarchy."),
 'c-catal-health': c("Life at Çatalhöyük was hard: 10-13 percent of adult teeth had cavities, infection was common, and healed head injuries became more frequent as the town grew more crowded.", 'approx', ['osu-larsen'], show=False),
 'c-aingh': c("At 'Ain Ghazal in Jordan, people buried caches of lime-plaster human statues and busts, about 9,000 years old.", 'approx', ['dsb-aingh', 'si-aingh'], show=False),
 'c-megasite': c("'Ain Ghazal grew to about 10-12 hectares by about 9,500-9,000 years ago; after about 8,900 years ago its population fell sharply, perhaps because the climate became drier.", 'debated', ['zielhofer2012', 'brit-aingh'], "Zielhofer and colleagues point to aridity; others have argued that people exhausted the land around the site."),
 # 2.9
 'c-ndt': c("When people began to farm, birth rates rose: cemeteries show a sharp rise in the share of children, which Jean-Pierre Bocquet-Appel called the Neolithic Demographic Transition.", 'approx', ['bocquet2011'], "The pattern is widely accepted; its size is model-dependent. In the Levant the rise took 2,600-3,000 years, on the edges of Europe and North Africa 400-800 years."),
 'c-stature': c("Most studies find that adult height fell as people came to rely on farming.", 'consensus', ['mummert2011'], show=False),
 'c-stock': c("A 2023 study of 3,507 skeletons found that in most regions height began to fall before the earliest signs of farming, reaching its lowest about 8,000-6,000 years ago.", 'debated', ['stock2023'], "This complicates the simple story that farming made people shorter; the Levant and China were relatively stable."),
 'c-diamond': c("In 1987 Jared Diamond called agriculture 'the worst mistake in the history of the human race'.", 'consensus', ['diamond1987'], show=False),
 'c-zoonoses': c("In more than 1,300 ancient genomes, diseases caught from animals first appear about 6,500 years ago and are widespread by about 5,000.", 'approx', ['sikora2025'], "A 2025 study; the timing reflects when such pathogens can be detected in ancient DNA."),
 'c-why-farm': c("Why people began to farm anyway is debated: a warmer, more stable climate, population pressure, feasting, and new forms of property have all been proposed.", 'debated', ['richerson2001', 'brit-agri', 'hayden2009', 'bowles2013'], "Richerson and colleagues argue farming was impossible in the Ice Age and almost inevitable after it. Britannica notes populations grew after food production, not before. Brian Hayden proposes feasting; Samuel Bowles and Jung-Kyoo Choi argue that early farming was not more productive but spread together with private property."),
 # 2.10
 'c-europe-farmers': c("Farming spread into Europe mainly with farmers whose ancestors came from Anatolia and the Aegean, reaching Greece about 8,500 years ago, central Europe about 7,500 and Britain about 6,000.", 'consensus', ['hofmanova2016', 'haak2015', 'brace2019'], show=False),
 'c-replacement': c("In much of western and central Europe the newcomers almost entirely replaced the earlier hunter-gatherers' ancestry; the farmers took more than 3,000 years to cross the continent.", 'approx', ['allentoft2024'], "Hunter-gatherer ancestry survived better in some regions, especially east of a line from the Black Sea to the Baltic."),
 'c-routes': c("Farmers followed two routes, along the Danube and along the Mediterranean coast, and mixed with local foragers to different degrees: about 3 percent hunter-gatherer ancestry in central Europe, about 31 percent in southern France.", 'approx', ['rivollat2020'], show=False),
 'c-lbk': c("The Linear Pottery (LBK) farmers settled the loess soils of central Europe from Slovakia to the Netherlands, growing emmer and barley and living in long rectangular houses.", 'consensus', ['brit-lbk'], show=False),
 'c-spread-rate': c("Averaged over the whole continent, farming spread at roughly 0.6-1.3 km a year.", 'approx', ['pinhasi2005'], show=False),
 'c-bantu': c("Later, Bantu-speaking farmers spread from western Africa across much of the continent, beginning about 6,000-4,000 years ago, and Austronesian-speaking farmers spread from Taiwan into Island Southeast Asia and the Pacific from about 4,200 years ago.", 'approx', ['fortes2024', 'almeida2025'], "Dates for both expansions vary between studies by several centuries."),
 # 2.11
 'c-belovode': c("Copper smelting at Belovode in Serbia, about 5000 BCE, is the earliest securely dated metal extraction from ore.", 'debated', ['radivojevic2010'], "Its excavators argue metallurgy was invented independently in the Balkans; the traditional view is that it spread from the Near East, where a site in Iran may be as old but is poorly dated. People had worked native copper since about 9000 BCE."),
 'c-varna': c("The cemetery at Varna in Bulgaria, used about 4560-4450 BCE, held about 3,000 gold objects weighing some 6 kg, the oldest worked gold treasure known, concentrated in a few lavish graves.", 'approx', ['varna-city', 'higham2007'], show=False),
 'c-otzi': c("Ötzi, the 'Iceman', died high in the Alps about 3250 BCE carrying a copper axe, a bow, arrows and a flint dagger; an arrow wound in his shoulder probably killed him.", 'approx', ['penn-otzi', 'iceman'], "His body was found in 1991; a minority of researchers argue the find was a deliberate burial."),
 'c-otzi-dna': c("Ötzi's genome (2023) shows mostly Anatolian-farmer ancestry, dark skin and no steppe ancestry.", 'consensus', ['iceman-dna'], show=False),
 'c-wheel': c("The wheel appears around 3500 BCE; the oldest surviving wheel with its axle, from the Ljubljana Marshes in Slovenia, is about 5,200 years old.", 'debated', ['mgml-wheel', 'brit-wheel', 'gatech-wheel'], "Where it was invented is uncertain. A Sumerian sign for a wheeled sledge dates to about 3500 BCE; a 2024 study proposes copper miners in the Carpathians."),
 'c-horse': c("Horses at Botai in Kazakhstan, about 3500 BCE, were exploited intensively and perhaps tamed, but they were ancestors of Przewalski's horses; modern domestic horses come from the lower Volga-Don and spread only after about 2200 BCE.", 'debated', ['cnrs-botai', 'librado2021', 'librado2024'], "The genetic findings are widely accepted. Whether Botai horses were domesticated at all is debated: some researchers see herding and perhaps riding, others only intensive hunting."),
 'c-yamnaya': c("The Yamnaya herders appeared on the steppe about 3300 BCE and by 3000 BCE ranged from Hungary to Kazakhstan; their ancestry reached most of Europe within about a thousand years.", 'approx', ['lazaridis2025', 'allentoft2024', 'haak2015'], show=False),
 'c-pie': c("Where the Indo-European languages began is debated: on the Pontic-Caspian steppe, in Anatolia with the first farmers, or south of the Caucasus with the steppe as a second homeland.", 'debated', ['haak2015', 'lazaridis2025', 'bouckaert2012', 'heggarty2023'], "Ancient DNA has strengthened the steppe view for most European branches; Heggarty and colleagues (2023) propose a hybrid; Lazaridis and colleagues (2025) trace an earlier 'Indo-Anatolian' source to the Caucasus-lower Volga region."),
 'c-uruk-eve': c("By about 3200 BCE, Uruk in southern Mesopotamia was the largest settlement in the region, perhaps in the world.", 'approx', ['met-uruk2'], show=False),
}

P8 = {
 'title': "The first villages and towns", 'sub': "Jericho, 'Ain Ghazal and Çatalhöyük",
 'lede': "As farming took hold, some settlements grew into places of thousands of people. They were not yet cities: no kings, no writing and, at the largest, no streets.",
 'body': [
  "At Jericho, by a spring in the Jordan valley, people built a stone wall and a tower about 8.5 metres high roughly 11,000 years ago, before pottery and before fully domesticated crops. [[c-jericho]] [[c-jericho-tower]] Why they built it is still argued: defence, a flood barrier, a statement of the village's standing, or a monument aligned with the midsummer sunset that bound the community together. [[c-jericho-purpose]]",
  "Across the Jordan, 'Ain Ghazal grew to about 10-12 hectares, and its people buried caches of plaster statues with staring eyes, some of the oldest large human figures known. [[c-aingh]] Then, after about 8,900 years ago, it shrank, perhaps as the climate dried. [[c-megasite]]",
  "Çatalhöyük, on the plain of central Turkey, was occupied for more than a thousand years, from about 7100 to 5950 BCE. [[c-catal]] Its houses were packed wall to wall with no streets; people walked across the rooftops and climbed down ladders into their homes, and buried their dead under the floors. [[c-catal-houses]] At its height it held perhaps 3,500-8,000 people. [[c-catal-pop]]",
  {'table': {'head': ["Settlement", "Date", "Size"], 'rows': [
    ["Jericho", "tower c. 11,000 years ago", "a village of round mud-brick houses"],
    ["'Ain Ghazal", "from c. 10,200 years ago; shrank after c. 8,900", "about 10-12 ha"],
    ["Çatalhöyük", "c. 7100-5950 BCE", "13.5 ha; perhaps 3,500-8,000 people"]]}},
  "No palace or temple has been found there, and men and women ate much the same food. Ancient DNA published in 2025 shows that where people buried in the same house were related, the links ran mainly through mothers; in later phases many were not related at all. [[c-catal-equal]] Life was not easy: about 10-13 percent of adult teeth had cavities, infection was common, and healed head injuries became more frequent as the town grew more crowded. [[c-catal-health]]"],
 'figure': {'kind': 'map', 'view': {'lon': 35.3, 'lat': 34.8, 'zoom': 30}, 'caption': "Early villages and towns of the Levant and Anatolia",
  'hint': "Click a site", 'legend': [['pt', 'site']], 'seaLabels': [{'t': 'MEDITERRANEAN SEA', 'll': [31.5, 34.2]}],
  'layers': [{'type': 'points', 'items': [
   {'ll': [35.444, 31.871], 'label': 'Jericho', 'date': 'tower c. 11,000 years ago', 'anchor': 'end', 'plate': {'kicker': '2.8 · villages', 'title': 'Jericho', 'sub': 'Tell es-Sultan, Jordan valley', 'text': "[[c-jericho]] [[c-jericho-tower]] [[c-jericho-purpose]]", 'sources': ['unesco-jericho', 'sd-jericho']}},
   {'ll': [35.976, 31.988], 'label': "'Ain Ghazal", 'date': 'statues c. 9,000 years ago', 'dy': -10, 'plate': {'kicker': '2.8 · villages', 'title': "'Ain Ghazal", 'sub': 'Amman, Jordan', 'text': "[[c-aingh]] [[c-megasite]]", 'sources': ['dsb-aingh', 'si-aingh', 'zielhofer2012', 'brit-aingh']}},
   {'ll': [32.828, 37.667], 'label': 'Çatalhöyük', 'date': 'c. 7100-5950 BCE', 'big': True, 'plate': {'kicker': '2.8 · towns', 'title': 'Çatalhöyük', 'sub': 'central Turkey, c. 7100 to 5950 BCE', 'text': "[[c-catal]] [[c-catal-houses]] [[c-catal-pop]] [[c-catal-equal]] [[c-catal-health]]", 'facts': [['area', '13.5 hectares'], ['entrance', 'through the roof'], ['burials', 'under the house floors']], 'sources': ['catal-guide', 'yuncu2025', 'osu-larsen']}},
   {'ll': [38.92, 37.22], 'label': 'Göbekli Tepe', 'date': 'see 2.6', 'dy': -8}]}]},
 'practice': [
  q("Which finding most weakens the idea that Çatalhöyük households were simply nuclear families?",
    ["Most of the dead were buried under house floors", "In later phases, many buried together were unrelated", "Around a tenth of adult teeth had cavities in them", "People entered their houses by ladder through the roof"], 1,
    "Ancient DNA published in 2025 shows that where people buried in the same house were related, the links ran mainly through mothers, and in later phases many were not related at all.",
    {0: "Floor burial shows where people were buried, not how they were related.", 2: "Cavities reflect diet and health, not household make-up.", 3: "Roof entry is a feature of the buildings with no bearing on kinship."}),
  q("What did Liran and Barkai (2011) argue about the Jericho tower?",
    ["A flood barrier protecting the village", "A granary for storing the village's grain", "A monument aligned with the solstice sunset", "A fortress added to the town in the Bronze Age"], 2,
    "They noted that the line of its staircase points to the midsummer sunset behind a nearby mountain, and read the tower as a monument that drew people into communal life.",
    {0: "Flood defence is one of the other readings of the tower; they stressed its alignment with the solstice sunset.", 1: "They did not propose a granary; they pointed to the alignment of its staircase with the solstice sunset.", 3: "The tower was built roughly 11,000 years ago, before pottery and before fully domesticated crops."})]}

P9 = {
 'title': "Was farming a good deal?", 'sub': "more people, harder lives",
 'lede': "Farming fed more people from the same land, and farming communities grew. But by many measures, early farmers were often shorter, sicker and harder-worked than the foragers before them.",
 'body': [
  "The clearest gain was in numbers. Cemeteries of the first farmers hold a much larger share of children than those of foragers, a sign that birth rates rose: the Neolithic Demographic Transition. [[c-ndt]] Settled women could have children more often, and grain could feed them.",
  "The costs show in bones and teeth. Most studies find that adult height fell as people came to rely on farming, [[c-stature]] and grain-rich diets brought tooth decay. Living close to herds and to each other brought new diseases: in ancient genomes, diseases caught from animals appear about 6,500 years ago and are widespread by 5,000. [[c-zoonoses]]",
  "In 1987 Jared Diamond called farming 'the worst mistake in the history of the human race'. [[c-diamond]] Few specialists put it so starkly. A 2023 study of 3,507 skeletons found that in most regions height had begun to fall before farming appeared, so farming was not the only cause. [[c-stock]]",
  {'table': {'head': ["Gains", "Costs"], 'rows': [
    ["more food from less land", "longer, harder work for many"],
    ["more children, faster growth", "shorter adults in most regions"],
    ["stored surplus", "tooth decay from grain"],
    ["settled villages", "crowding and infection"],
    ["animals for milk, wool, traction", "diseases caught from animals"]]}},
  "If it was such a mixed bargain, why did people farm? The answers are debated: a warmer and more stable climate after the Ice Age, growing populations, feasts that rewarded those who could produce a surplus, and new ideas of property. [[c-why-farm]] Perhaps the simplest answer is demographic: farmers had more children, and in time there were simply more of them."],
 'figure': {'kind': 'chart', 'chart': 'ledger', 'caption': "The farming bargain", 'title': "What farming brought, and what it cost",
  'left': {'h': 'Gains', 'items': [
   {'t': 'More people', 's': 'birth rates rose', 'tip': 'Cemeteries hold more children: the Neolithic Demographic Transition.'},
   {'t': 'Surplus and storage', 's': 'food for lean seasons, and for feasts'},
   {'t': 'Settled villages', 's': 'Jericho, Çatalhöyük (2.8)'},
   {'t': 'Animals', 's': 'milk, wool, hides, traction'}]},
  'right': {'h': 'Costs', 'items': [
   {'t': 'Shorter adults', 's': 'in most regions, though not only from farming', 'tip': 'Height began to fall before farming in many regions (Stock et al. 2023).'},
   {'t': 'Tooth decay', 's': '10-13% of adult teeth at Çatalhöyük'},
   {'t': 'Crowding and infection', 's': 'and more injuries in crowded towns'},
   {'t': 'Diseases from animals', 's': 'widespread by about 5,000 years ago'}]}},
 'practice': [
  q("Which observation best explains why farming spread despite its health costs?",
    ["Farmers were taller than the foragers around them", "Farming communities had more children and grew faster", "Farming removed the diseases people caught from animals", "Farming began at the coldest point of the Ice Age"], 1,
    "Higher birth rates meant farming populations outgrew and outnumbered foragers.",
    {0: "Most studies find that adult height fell as people came to rely on farming.", 2: "Diseases caught from animals increased with herding and crowding.", 3: "Farming began after the Ice Age; a warmer, more stable climate is one proposed reason."}),
  q("How does Stock and colleagues' 2023 study complicate the case that farming made people shorter?",
    ["Early farmers were usually the healthier group", "Height often began to fall before farming", "Early farmers showed no signs of tooth decay", "The sharpest fall in height came in the Levant"], 1,
    "In most regions, stature began to decline before the earliest signs of agriculture, so farming was not the only cause.",
    {0: "It did not find farmers healthier; height reached its lowest about 8,000-6,000 years ago.", 2: "Grain-rich diets brought tooth decay to early farmers.", 3: "It found the Levant relatively stable."})]}

P10 = {
 'title': "Farming spreads", 'sub': "people on the move",
 'lede': "Farming did not spread across Europe mainly as an idea. Ancient DNA shows it travelled with people: farmers whose ancestors came from Anatolia and the Aegean.",
 'body': [
  "Farmers reached Greece about 8,500 years ago, central Europe about 7,500 and Britain about 6,000. Their descendants carried the same ancestry, traceable back to the Aegean, all the way. [[c-europe-farmers]] Averaged over the continent, the frontier moved at roughly a kilometre a year. [[c-spread-rate]]",
  "They came by two routes. One followed the Danube into central Europe, where the Linear Pottery farmers built long timber houses on the fertile loess soils. [[c-lbk]] The other followed the Mediterranean coast to Italy, southern France and Iberia, and from there, eventually, to Britain. [[c-routes]]",
  {'table': {'head': ["Region", "Farming arrives", "Hunter-gatherer ancestry"], 'rows': [
    ["Greece", "c. 6500 BCE", "low"],
    ["Central Europe (LBK)", "c. 5500 BCE", "about 3%"],
    ["Southern France", "c. 5400 BCE", "about 31%"],
    ["Iberia", "after 5500 BCE", "about 13%"],
    ["Britain", "c. 4000 BCE", "small"]],
   'note': "[[c-routes]] [[c-replacement]]"}},
  "In much of western Europe the newcomers almost entirely replaced the earlier hunter-gatherer population, though the two mixed to different degrees along the way. [[c-replacement]]",
  "Farming spread with migrating farmers elsewhere too, later than this chapter: Bantu-speaking farmers across much of Africa, and Austronesian-speaking farmers from Taiwan out into the Pacific. [[c-bantu]]"],
 'figure': {'kind': 'map', 'view': {'lon': 11, 'lat': 46.5, 'zoom': 7}, 'caption': "Farmers enter Europe, c. 6500-4000 BCE (simplified)",
  'hint': "Click a site", 'legend': [['acc', 'route of farmers'], ['pt', 'site']], 'seas': False,
  'layers': [
   {'type': 'arrow', 'items': [
    {'path': [[29.5, 40.4], [22.265, 40.604], [22.5, 44.6], [19.0, 47.0], [16.4, 48.2], [8.3, 50.0], [5.5, 51.5]], 'label': 'Danube route', 'lab': [12, 50.5], 'ldy': -8},
    {'path': [[22.265, 40.604], [19.5, 39], [15.5, 41.5], [10.5, 43.5], [7.5, 43.79], [2.0, 41.4], [-2, 39]], 'label': 'Mediterranean route', 'lab': [8, 41], 'ldy': 18, 'delay': 0.4},
    {'path': [[2.0, 41.4], [0, 45], [-1.5, 48], [-1.93, 51.86]], 'delay': 0.9}]},
   {'type': 'points', 'items': [
    {'ll': [22.265, 40.604], 'label': 'Nea Nikomedeia', 'date': 'c. 6200 BCE', 'anchor': 'end', 'dy': 14},
    {'ll': [16.4, 48.2], 'label': 'Middle Danube', 'date': 'LBK, c. 5500 BCE', 'dy': -8, 'plate': {'kicker': '2.10 · farmers', 'title': 'The Linear Pottery farmers', 'sub': 'central Europe, from c. 5500 BCE', 'text': "[[c-lbk]] [[c-routes]]", 'sources': ['brit-lbk', 'rivollat2020']}},
    {'ll': [7.5, 43.79], 'label': 'Pendimoun', 'date': 'c. 5400 BCE', 'anchor': 'end', 'dy': 14, 'plate': {'kicker': '2.10 · farmers', 'title': 'Pendimoun', 'sub': 'Provence, c. 5480 to 5360 BCE', 'text': "[[c-routes]]", 'sources': ['rivollat2020']}},
    {'ll': [-1.93, 51.86], 'label': 'Britain', 'date': 'c. 4000 BCE', 'anchor': 'end', 'plate': {'kicker': '2.10 · farmers', 'title': 'Farmers reach Britain', 'sub': 'c. 4000 BCE', 'text': "[[c-europe-farmers]] [[c-replacement]]", 'sources': ['brace2019', 'allentoft2024']}}]}]},
 'practice': [
  q("What does ancient DNA show about how farming spread into Europe?",
    ["Local foragers took up farming without any migration", "Farmers of Anatolian and Aegean descent moved in", "Herders from the steppe first brought farming west", "Farmers from North Africa crossed into Iberia first"], 1,
    "Early European farmers' ancestry traces back to Anatolia and the Aegean; the newcomers mixed with local foragers to different degrees, and in much of the west almost entirely replaced them.",
    {0: "In much of western and central Europe the newcomers almost entirely replaced hunter-gatherer ancestry.", 2: "Early European farmers' ancestry traces back to Anatolia and the Aegean, not the steppe.", 3: "Farmers reached Greece first, about 8,500 years ago, and those who reached Iberia came along the Mediterranean coast."}),
  q("Why do early farmers of southern France carry more hunter-gatherer ancestry than those of central Europe?",
    ["Farming was invented separately in southern France", "Mediterranean-route farmers mixed more with foragers", "Central European farmers had no contact with foragers", "Foragers in France had migrated there from Anatolia"], 1,
    "About 31 percent hunter-gatherer ancestry in southern France against about 3 percent in central Europe reflects more mixing along the Mediterranean route.",
    {0: "Farming reached France with farmers who followed the Mediterranean coast.", 2: "Central European farmers did mix a little: about 3 percent of their ancestry is from hunter-gatherers.", 3: "Anatolian and Aegean ancestry is what the farmers carried; the extra ancestry in southern France came from local hunter-gatherers."})]}

P11 = {
 'title': "Copper, horses and the eve of cities", 'sub': "c. 5000 to 3500 BCE",
 'lede': "In the last two thousand years before writing, people learned to smelt metal, buried their chiefs in gold, and put wheels under carts. Then, in southern Mesopotamia, the first city rose.",
 'body': [
  "People had hammered native copper for thousands of years. Smelting it from ore was new: the earliest securely dated evidence comes from Belovode in Serbia, about 5000 BCE. [[c-belovode]] At Varna on the Black Sea, about 4500 BCE, a few graves held most of some 3,000 gold objects, the oldest worked-gold treasure known, and a sign that some people now held far more than others. [[c-varna]]",
  "Ötzi, the 'Iceman', died high in the Alps around 3250 BCE carrying a copper-bladed axe, a bow and a flint dagger; an arrow in his shoulder probably killed him. [[c-otzi]] His genome shows he descended mainly from Anatolian farmers, with no ancestry from the steppe. [[c-otzi-dna]]",
  "Wheels appear around 3500 BCE; where they were invented is uncertain. [[c-wheel]] People at Botai in Kazakhstan relied heavily on horses about 3500 BCE and may have tamed them, but those horses were not the ancestors of today's: modern domestic horses spread only after about 2200 BCE. [[c-horse]] On the steppe, the Yamnaya herders appeared about 3300 BCE, and their descendants changed the ancestry of most of Europe within a thousand years. [[c-yamnaya]] They may have spread the Indo-European languages; where those languages began is still argued. [[c-pie]]",
  {'table': {'head': ["", "Where", "When"], 'rows': [
    ["Copper smelted from ore", "Belovode, Serbia", "c. 5000 BCE"],
    ["Gold treasure", "Varna, Bulgaria", "c. 4500 BCE"],
    ["Wheel", "uncertain; oldest surviving in Slovenia", "c. 3500 BCE"],
    ["Ötzi", "Ötztal Alps", "c. 3250 BCE"],
    ["First city", "Uruk, Mesopotamia", "c. 3200 BCE"]]}},
  "Meanwhile, on the floodplain of southern Mesopotamia, Uruk was growing into the largest settlement in the region, perhaps in the world. [[c-uruk-eve]] There, around 3200 BCE, someone began to keep accounts on clay. History, in the narrow sense, was about to begin.",
  {'compare': "Chapter 3 begins here, at Uruk."}],
 'figure': {'kind': 'map', 'view': {'lon': 38, 'lat': 43, 'zoom': 4.2}, 'caption': "Metal, wheels and herders, c. 5000-3200 BCE",
  'hint': "Click a site", 'legend': [['pt', 'site'], ['dot', 'the first city']], 'seas': False,
  'layers': [
   {'type': 'zone', 'items': [{'ll': [40, 48], 'r': 6, 'label': 'YAMNAYA', 'lab': [40, 53]}]},
   {'type': 'points', 'items': [
    {'ll': [21.40, 44.32], 'label': 'Belovode', 'date': 'copper, c. 5000 BCE', 'dy': -10, 'plate': {'kicker': '2.11 · metal', 'title': 'Belovode', 'sub': 'Serbia, c. 5000 BCE', 'text': "[[c-belovode]]", 'sources': ['radivojevic2010']}},
    {'ll': [27.86, 43.21], 'label': 'Varna', 'date': 'gold, c. 4500 BCE', 'dy': 14, 'plate': {'kicker': '2.11 · metal', 'title': 'The Varna cemetery', 'sub': 'Bulgaria, c. 4560 to 4450 BCE', 'text': "[[c-varna]]", 'facts': [['graves', '294'], ['gold objects', 'about 3,000 (about 6 kg)']], 'sources': ['varna-city', 'higham2007']}},
    {'ll': [10.84, 46.78], 'label': 'Ötzi', 'date': 'c. 3250 BCE', 'anchor': 'end', 'dy': -10, 'plate': {'kicker': '2.11 · the Iceman', 'title': 'Ötzi', 'sub': 'Ötztal Alps, c. 3250 BCE', 'text': "[[c-otzi]] [[c-otzi-dna]]", 'facts': [['found', '1991, at about 3,200 m'], ['carried', 'copper axe, bow, arrows, flint dagger']], 'sources': ['penn-otzi', 'iceman', 'iceman-dna']}},
    {'ll': [14.36, 45.98], 'label': 'Ljubljana Marshes', 'date': 'wheel, c. 3200 BCE', 'anchor': 'end', 'dy': 18, 'plate': {'kicker': '2.11 · the wheel', 'title': 'The Ljubljana Marshes wheel', 'sub': 'Slovenia, about 5,200 years old', 'text': "[[c-wheel]]", 'sources': ['mgml-wheel', 'brit-wheel', 'gatech-wheel']}},
    {'ll': [67.645, 53.303], 'label': 'Botai', 'date': 'horses, c. 3500 BCE', 'anchor': 'end', 'plate': {'kicker': '2.11 · horses', 'title': 'Botai', 'sub': 'Kazakhstan, c. 3500 BCE', 'text': "[[c-horse]]", 'sources': ['cnrs-botai', 'librado2021', 'librado2024']}},
    {'ll': [45.64, 31.32], 'label': 'Uruk', 'date': 'c. 3200 BCE', 'acc': True, 'big': True, 'plate': {'kicker': '2.11 · the threshold', 'title': 'Uruk', 'sub': 'southern Mesopotamia, c. 3200 BCE', 'text': "[[c-uruk-eve]] Chapter 3 begins here.", 'sources': ['met-uruk2']}}]}]},
 'practice': [
  q("What did horse genomics (2021-2024) imply about the Yamnaya expansion around 3000 BCE?",
    ["It probably relied on the horses tamed at Botai", "It probably did not rely on modern domestic horses", "It carried horse-drawn chariots west into Europe", "It spread horses that were first domesticated in Iberia"], 1,
    "Modern domestic horses come from the lower Volga-Don and spread only after about 2200 BCE, centuries after the Yamnaya ranged from Hungary to Kazakhstan by 3000 BCE.",
    {0: "Botai horses were ancestors of Przewalski's horses, not of modern domestic horses.", 2: "Modern domestic horses spread only after about 2200 BCE, long after the expansion began.", 3: "Modern domestic horses come from the lower Volga-Don region."}),
  q("Why is Belovode in Serbia significant?",
    ["It holds the oldest worked-gold treasure known", "It has the earliest securely dated copper smelting", "The oldest surviving wheel and axle came from there", "It is where people first hammered native copper"], 1,
    "Smelting copper from ore, not just hammering native copper, began true metallurgy; Belovode, about 5000 BCE, has its earliest securely dated evidence. Its excavators argue metallurgy was invented independently in the Balkans.",
    {0: "The oldest worked-gold treasure is at Varna, about 4500 BCE.", 2: "The oldest surviving wheel with its axle is from the Ljubljana Marshes in Slovenia.", 3: "People had hammered native copper for thousands of years before; what was new at Belovode was smelting it from ore."})]}

PAGES = [P8, P9, P10, P11]
