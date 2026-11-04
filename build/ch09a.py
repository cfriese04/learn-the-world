# Chapter 9, pages 9.0 to 9.3. Coordinates are [longitude, latitude].
from common import c, q

S = {
 # 9.0
 'brit-simaqian': ("Encyclopaedia Britannica, \"Sima Qian\"", "https://www.britannica.com/biography/Sima-Qian"),
 'cdhk-shuihudi': ("China Daily Hong Kong, on the Shuihudi Qin slips (2024)", "https://chinadailyhk.com/article/581217"),
 'cd-liye2025': ("China Daily, \"Slips unearthed at Liye archaeological site dig into details of Qin life\" (6 November 2025)", "https://govt.chinadaily.com.cn/s/202511/06/WS690c0954498e36855033723b/slips-unearthed-at-liye-archaeological-site-dig-into-details-of-qin-life.html"),
 'ec-allan': ("Mark Edward Lewis, review of Sarah Allan, Buried Ideas: Legends of Abdication and Ideal Government in Early Chinese Bamboo-Slip Manuscripts, Early China", "https://www.cambridge.org/core/product/2594293007F2EF6F23C6F49758BB446A/core-reader"),
 'bmcr-stoneman': ("Giles Miles, review of Richard Stoneman, Megasthenes' Indica (2021), Bryn Mawr Classical Review 2022.10.08", "https://bmcr.brynmawr.edu/?p=67313"),
 'rbi-coins': ("Reserve Bank of India Monetary Museum, \"Ancient India\" coinage", "https://rbi.org.in/Scripts/mc_ancient.aspx"),
 'brit-prinsep': ("Encyclopaedia Britannica, \"James Prinsep\"", "https://www.britannica.com/biography/James-Prinsep"),
 'sciam-tsinghua': ("Scientific American, 'Ancient times table hidden in Chinese bamboo strips' (2014)", "https://www.scientificamerican.com/article/ancient-times-table-hidden-in-chinese-bamboo-strips"),
 # 9.1
 'sep-mohism': ("Chris Fraser, \"Mohism\", Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/mohism/"),
 'sep-mencius': ("Bryan Van Norden, \"Mencius\", Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/mencius/"),
 'sep-xunzi': ("Paul R. Goldin, \"Xunzi\", Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/xunzi/"),
 'sep-legalism': ("Yuri Pines, \"Legalism in Chinese philosophy\", Stanford Encyclopedia of Philosophy", "https://plato.stanford.edu/entries/chinese-legalism/"),
 'wagner-korean': ("Donald B. Wagner, on early iron in China and Korea", "https://donwagner.dk/KoreanFe/KoreanFe.html"),
 'uw-crossbow': ("University of Washington, A Visual Sourcebook of Chinese Civilization, \"The crossbow\"", "https://depts.washington.edu/chinaciv/miltech/crossbow.htm"),
 'li2014': ("Li, Bevan, Martinón-Torres et al., \"Crossbows and imperial craft organisation: the bronze triggers of China's Terracotta Army\", Antiquity 88 (2014)", "https://core-prod.cambridgecore.org/core/services/aop-cambridge-core/content/view/DB32EADD77493B84692756138D21D036/S0003598X00050262a.pdf/crossbows_and_imperial_craft_organisation_the_bronze_triggers_of_chinas_terracotta_army.pdf"),
 'sixthtone-changping': ("Sixth Tone, on bones found near the Changping battlefield (23 July 2020)", "https://sixthtone.com/news/1005971"),
 'kirkland-guodian': ("Russell Kirkland, on the Guodian Laozi (University of Georgia)", "https://reli.franklin.uga.edu/sites/default/files/inline-files/guodian.pdf"),
 'll-wangjiazui': ("Victor Mair, Language Log, on the Wangjiazui slips (May 2022)", "https://languagelog.ldc.upenn.edu/nll/?p=54780"),
 'cd-qinjiazui': ("China Daily, \"Bamboo slips reveal Warring States life\" (22 December 2023)", "https://govt.chinadaily.com.cn/s/202312/22/WS65ae0b2e498ed2d7b7ea601f/bamboo-slips-reveal-warring-states-life.html"),
 # 9.2
 'brit-qinshihuang': ("Encyclopaedia Britannica, \"Qin Shi Huang\"", "https://www.britannica.com/biography/Qin-Shi-Huang"),
 'met-qin': ("The Met, \"Qin dynasty (221-206 B.C.)\"", "https://www.metmuseum.org/toah/hd/qind/hd_qind.htm"),
 'neininger-keng': ("Ulrich Neininger, on the 'burying of the scholars'", "https://ulrichneininger.de/?p=461"),
 'unesco-qin': ("UNESCO World Heritage Centre, \"Mausoleum of the First Qin Emperor\"", "https://whc.unesco.org/en/list/441/"),
 'zhao2020': ("Zhao et al., mercury above the First Emperor's mound, Scientific Reports 10 (2020)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7319949"),
 'hubei-shuihudi': ("Hubei Provincial Museum, on the Shuihudi Qin slips", "https://www.hbww.org.cn/p/11501.html"),
 'korolkov-liye': ("Maxim Korolkov, \"Empire marches south\" (lecture, LMU Munich)", "https://www.sinologie.uni-muenchen.de/aktuelles/vortrag-korolkov/korolkov_empire-marches-south.pdf"),
 'pines-korolkov': ("Yuri Pines, review of Korolkov, The Imperial Network in Ancient China (2022), Journal of Chinese Studies 76 (2023)", "https://www.cuhk.edu.hk/ics/journal/articles/v76p221.pdf"),
 'korolkov-hein2021': ("Korolkov and Hein, on the Qin conquest of the south, Journal of Chinese History 5 (2021)", "https://www.cambridge.org/core/product/87D09AD61610E2E7ACC49405863893AB"),
 'scmp-gyaring': ("South China Morning Post, on the Qin inscription at Gyaring Lake (2025)", "https://www.scmp.com/news/china/science/article/3325766/chinas-first-emperor-really-did-send-quest-tibet-search-immortality-scientists"),
 'arkeo-gyaring': ("Arkeonews, \"Emperor's quest for immortality: Tibetan inscription confirmed authentic\" (September 2025)", "https://arkeonews.net/terracotta-army-emperors-quest-for-immortality-tibetan-inscription-confirmed-authentic/"),
 # 9.3
 'brit-gaozu': ("Encyclopaedia Britannica, \"Gaozu\" (emperor of the Han dynasty)", "https://www.britannica.com/biography/Gaozu-emperor-of-Han-dynasty"),
 'brit-handyn': ("Encyclopaedia Britannica, \"Han dynasty\"", "https://www.britannica.com/topic/Han-dynasty"),
 'met-han': ("The Met, \"Han dynasty (206 B.C.-220 A.D.)\"", "https://www.metmuseum.org/toah/hd/hand/hd_hand.htm"),
 'brit-dong': ("Encyclopaedia Britannica, \"Dong Zhongshu\"", "https://www.britannica.com/biography/Dong-Zhongshu"),
 'loewe2011': ("Michael Loewe, Dong Zhongshu, a 'Confucian' Heritage and the Chunqiu Fanlu (Brill, 2011)", "https://www.degruyterbrill.com/document/isbn/9789004214866/html"),
 'cai2014': ("Liang Cai, Witchcraft and the Rise of the First Confucian Empire (SUNY, 2014)", "https://www.degruyterbrill.com/document/doi/10.1515/9781438448510/html"),
 'cai2019': ("Liang Cai, \"Ru scholars, social networks, and bureaucracy: Donghai men and models for success in Western Han China\", Early China 42 (2019)", "https://www.cambridge.org/core/journals/early-china/article/abs/ru-scholars-social-networks-and-bureaucracy-donghai-men-and-models-for-success-in-western-han-china-206-bce9-ce/914C2482D9735A0AF09A32F569357957"),
 'brit-china-urban': ("Encyclopaedia Britannica, \"China: urban areas\" (on the census of 2 CE)", "https://www.britannica.com/place/China/Urban-areas"),
 'brit-wangmang': ("Encyclopaedia Britannica, \"Wang Mang\"", "https://www.britannica.com/biography/Wang-Mang"),
 'brit-yellowturbans': ("Encyclopaedia Britannica, \"Yellow Turbans\"", "https://www.britannica.com/topic/Yellow-Turbans"),
}

C = {
 # 9.0
 'c-simaqian': c("Sima Qian (about 145 to about 87 BCE), grand historian of the Han court, wrote the Shiji ('Records of the Historian'), a history from the legendary sage kings to his own day that became the model for all later Chinese dynastic histories. For defending a disgraced general he was condemned for 'defaming the emperor' and castrated instead of executed.", 'approx', ['brit-simaqian'], "His birth and death dates are approximate."),
 'c-slips-value': c("Excavated bamboo and wooden slips are working documents that can be checked against the histories: no Qin law code was known until the Shuihudi tomb gave one in 1975, and a well at Liye has yielded nearly 38,000 slips of a Qin county's records.", 'consensus', ['cdhk-shuihudi', 'cd-liye2025'], show=False),
 'c-looted-slips': c("The Shanghai Museum and Tsinghua University manuscripts were bought on the antiquities market, not excavated, so their authenticity has been questioned.", 'debated', ['ec-allan'], "Most specialists, including Sarah Allan, accept them as genuine because their script and contents match properly excavated texts; the doubt is their unknown origin."),
 'c-megasthenes-rel': c("How reliable Megasthenes was is disputed.", 'debated', ['bmcr-stoneman', 'brit-megasthenes'], "Strabo already accused him of inventing things; Richard Stoneman (2021) argues that even his 'fabulous races' faithfully pass on what Indian informants told him."),
 'c-punchmarked': c("India's first coins were silver 'punch-marked' pieces, issued first by merchant guilds and later by states including the Mauryas; the history of the Indo-Greek kings has been rebuilt almost entirely from their coins.", 'approx', ['rbi-coins'], "The Reserve Bank of India dates the first coins to the 7th-6th centuries BCE; many numismatists prefer a somewhat later start."),
 'c-prinsep-mint': c("James Prinsep, who first deciphered Ashoka's edicts, was the assay master of the Calcutta mint: a coin expert, not a professional linguist.", 'consensus', ['brit-prinsep'], show=False),
 # 9.1
 'c-mozi': c("Mozi (active about 430 BCE) taught impartial care for everyone, condemned wars of aggression and lavish funerals, and his followers formed bands that helped defend cities under attack.", 'approx', ['sep-mohism'], "His dates are approximate."),
 'c-mencius': c("Mencius (4th century BCE) taught that human nature is good, since everyone has innate 'sprouts' of virtue, and urged rulers to govern by benevolence rather than force.", 'consensus', ['sep-mencius'], show=False),
 'c-xunzi': c("Xunzi (born about 310 BCE) argued the opposite: human nature is bad, and goodness comes only from effort, education and ritual; his students included Han Fei and Li Si, the First Emperor's chief minister.", 'consensus', ['sep-xunzi'], show=False),
 'c-legalism-label': c("'Legalism' (fajia) is a label invented later by Han scholars; no early thinker saw himself as a member of such a school.", 'debated', ['sep-legalism'], "Yuri Pines calls the translation misleading; Arthur Waley preferred 'Realists'."),
 'c-shangyang': c("Shang Yang (died 338 BCE) reorganised Qin around 'agriculture and war': hereditary rank gave way to twenty ranks earned in battle or by producing grain, families were grouped to watch and inform on each other, and punishments were harsh.", 'consensus', ['sep-legalism'], show=False),
 'c-hanfei': c("Han Fei (died 233 BCE) combined impersonal law (fa), techniques for controlling officials (shu) and the ruler's positional power (shi) into a theory of the strong state.", 'consensus', ['sep-legalism'], show=False),
 'c-iron-ws': c("Smelted iron was in use in the south by the early 5th century BCE and in the north by the late 4th; by the early 3rd century it was the metal of choice for tools and weapons.", 'approx', ['wagner-korean'], "Donald Wagner notes that unpublished finds may push these dates earlier."),
 'c-crossbow': c("The trigger-fired crossbow, in use by the 5th century BCE, needed less skill and strength than a bow, which suited mass armies of conscripted farmers.", 'approx', ['uw-crossbow', 'li2014'], "Its exact origin is uncertain."),
 'c-changping': c("Tradition says that after the battle of Changping in about 260 BCE Qin killed more than 400,000 surrendered Zhao soldiers; in 2020 a long layer of bones was found near the battlefield.", 'debated', ['sixthtone-changping'], "The figure comes from Sima Qian; no count of the remains has been published, so the find cannot test it yet."),
 'c-guodian': c("A tomb at Guodian, sealed about 300 BCE and excavated in 1993, held some 800 bamboo slips, including the oldest known version of parts of the Laozi (see 7.10).", 'consensus', ['kirkland-guodian'], show=False),
 'c-abdication': c("Several excavated manuscripts discuss whether rulers should hand the throne to the most worthy man rather than to their sons, a debate the transmitted classics barely preserve.", 'debated', ['ec-allan'], "Sarah Allan reads them as evidence of a real Warring States debate; how widely they circulated is unknown."),
 'c-tsinghua': c("The Tsinghua slips, about 2,500 strips donated in 2008, carbon-date to about 305 BCE and include a lost chronicle and the world's oldest known decimal multiplication table.", 'approx', ['ec-allan', 'sciam-tsinghua'], "The radiocarbon date is a single sample; the slips' origin is unknown."),
 'c-newslips': c("Recent scientific excavations have found more: about 3,200 slips at Wangjiazui (2021-22), including parts of the Book of Songs and sayings of Confucius, and nearly 4,000 at Qinjiazui, from about 369-329 BCE.", 'approx', ['ll-wangjiazui', 'cd-qinjiazui'], "New. Unlike the Shanghai and Tsinghua slips, these come from known tombs; most are still being published."),
 # 9.2
 'c-qin-unify': c("Zheng became king of Qin in 246 BCE and conquered the last rival state, Qi, in 221 BCE, when he took the new title Qin Shi Huang, 'First Emperor of Qin'.", 'consensus', ['brit-qinshihuang'], show=False),
 'c-standard': c("The First Emperor divided the empire into 36 commanderies and standardised weights and measures, coinage, the length of cart axles, the script and the law.", 'consensus', ['brit-qinshihuang', 'met-qin'], show=False),
 'c-burning': c("According to Sima Qian, in 213 BCE the minister Li Si had books burned, sparing works on medicine, divination and farming, and in 212 more than 460 scholars were put to death at the capital.", 'tradition', ['brit-qinshihuang'], "The account was written about a century later, under the Han dynasty that replaced Qin."),
 'c-burning-debate': c("Many historians now doubt the 'burying of the scholars' as usually told.", 'debated', ['neininger-keng'], "Ulrich Neininger argues the victims were mostly magicians, that Sima Qian's word keng means 'killed', not 'buried alive', and that the story of Confucian martyrs grew up later; the earliest Han critics of Qin, Lu Jia and Jia Yi, do not mention the killings. Most accept that some book-burning took place."),
 'c-mausoleum': c("The First Emperor's tomb complex, found in 1974, covers 56 km², with nearly 200 pits and a mound 51 m high; the pits hold thousands of life-size terracotta soldiers.", 'approx', ['unesco-qin', 'met-qin'], "Estimates of the number of figures range from over 7,000 to about 8,000."),
 'c-mercury': c("Sima Qian says the tomb chamber held rivers of mercury; a 2016 survey found mercury in the air above the mound at roughly two to five times background levels.", 'debated', ['zhao2020', 'met-qin'], "The readings fit the story but do not prove it; the authors call their estimate 'extremely crude'. The burial chamber has never been opened."),
 'c-triggers': c("Crossbow triggers from the terracotta pits are so uniform that researchers think they were made in parallel workshops under central supervision.", 'approx', ['li2014'], "An inference from measurements of 216 triggers."),
 'c-shuihudi': c("The tomb of Xi, a minor Qin legal official, at Shuihudi (excavated 1975) held 1,155 slips: statutes on farming, markets and labour service, a ban on felling trees in spring, a rule that goods carry price labels, and Xi's own chronicle from 306 to 217 BCE.", 'consensus', ['cdhk-shuihudi', 'hubei-shuihudi'], show=False),
 'c-liye': c("The Liye slips, from a well in a Qin frontier county, record taxes, granaries, postal relays, medicine, even rat-catching, and include a multiplication table; about half of the inscribed slips had been published by 2025.", 'approx', ['cd-liye2025', 'korolkov-liye'], "Counts of inscribed slips run from about 17,000 to 18,000."),
 'c-liye-county': c("Liye shows a frontier county with 104 official posts, 86 of them filled, staffed partly by officials sent there as punishment and worked by convicts and conscripts.", 'debated', ['pines-korolkov'], "How many households the county governed is disputed: Maxim Korolkov estimates about 200; Yuri Pines thinks more."),
 'c-qin-fall': c("Why the Qin collapsed within four years of the First Emperor's death in 210 BCE is debated.", 'debated', ['brit-qinshihuang', 'korolkov-hein2021', 'pines-korolkov'], "The traditional answer blames tyranny and court intrigue. Maxim Korolkov (2022; see also Korolkov and Hein 2021) argues that the new documents show how precarious Qin's hold on its late conquests was, that its southern wars after 214 BCE 'may have diverted resources' needed to consolidate them, and that the real puzzle is 'how it managed to endure as long as it did'; Yuri Pines replies that Qin's hold on the borderlands was more robust than it first appears."),
 'c-gyaring': c("In 2025 China's heritage authorities declared genuine an inscription near Gyaring Lake in Qinghai, at 4,300 m, dated 210 BCE, recording an expedition sent by the First Emperor to collect yao, medicinal herbs or minerals, or perhaps the elixir of life.", 'debated', ['scmp-gyaring', 'arkeo-gyaring'], "New. Xin Deyong of Peking University and others have asked for the full scientific report; no peer-reviewed study has appeared."),
 # 9.3
 'c-liubang': c("Liu Bang, a man of humble birth who had served Qin as a minor official, defeated his rival Xiang Yu in 202 BCE and founded the Han dynasty, counting his reign from 206.", 'consensus', ['brit-gaozu'], show=False),
 'c-han-capitals': c("The Han kept Qin's centralised, salaried bureaucracy; its capital was Chang'an until 9 CE and Luoyang from 25 to 220 CE.", 'consensus', ['brit-handyn', 'met-han'], show=False),
 'c-confucian-trad': c("The traditional account says that Emperor Wu, advised by Dong Zhongshu, made Confucianism the state's official teaching from 136 BCE and founded an imperial academy to train officials in the classics.", 'tradition', ['brit-dong', 'met-han'], "This is how later Confucian historians told it."),
 'c-confucian-debate': c("Recent scholarship questions how Confucian Emperor Wu's government really was.", 'debated', ['loewe2011', 'cai2014'], "Michael Loewe doubts Dong Zhongshu's role and dates parts of the work credited to him much later; Liang Cai argues Confucian scholars were a powerless minority under Wu and rose only after a court witchcraft scandal of 91-87 BCE."),
 'c-yinwan': c("A register excavated at Yinwan lists about 2,200 officials in a single commandery, Donghai, late in the Western Han.", 'approx', ['cai2019'], "A rare check on the totals given in the histories."),
 'c-census-min': c("The census of 2 CE, China's oldest surviving count, was taken mainly for the poll tax; because people avoided registration, its total is a minimum.", 'approx', ['brit-china-urban', 'brit-han'], "Reported totals range from about 57.7 to 59.6 million."),
 'c-wangmang-fall': c("Wang Mang took the throne in 9 CE; the Yellow River shifted its course, peasant rebels called the Red Eyebrows rose, and he was killed in 23 CE.", 'consensus', ['brit-wangmang'], show=False),
 'c-eastern-han': c("Liu Xiu, Emperor Guangwu, restored the Han in 25 CE; the Yellow Turban rebellion of 184, led by a Daoist healer, and the armies raised against it hastened the dynasty's end in 220.", 'consensus', ['brit-yellowturbans', 'brit-handyn'], show=False),
}

# ---------------------------------------------------------------- 9.0
P0 = {
 'title': "India and China in the classical age", 'sub': "c. 500 BCE to 550 CE",
 'lede': "While Greeks, Persians and Romans fought over the Mediterranean, the two most populous regions on earth went through their own classical ages. China was unified for the first time and ruled by a bureaucracy whose model lasted two thousand years; India produced its first empire, its first royal inscriptions and the arithmetic the whole world now uses.",
 'body': [
  "In China, seven warring states became one in 221 BCE under Qin, [[c-qin-unify]] and the Han dynasty that followed ruled for four centuries. [[c-han-capitals]] In India, the Mauryas built an empire across most of the subcontinent, [[c-chandragupta]] and their emperor Ashoka turned his regret for a war into a public creed. [[c-re13]] After a long age of foreign and regional dynasties came the Gupta kings, from about 320 CE. [[c-gupta-era]]",
  "China has a historian to rival Herodotus: Sima Qian, whose Shiji became the model for every later dynastic history. [[c-simaqian]] But the most exciting evidence now comes out of the ground. Tombs and wells keep yielding bamboo and wooden slips: real laws, real accounts, lost books. [[c-slips-value]] Some of the most famous came from the antiquities market, which raises its own questions. [[c-looted-slips]]",
  "For early India there is no Sima Qian. Historians use a Greek ambassador's lost book, known only in quotations, [[c-megasthenes]] [[c-megasthenes-rel]] Ashoka's inscriptions, [[c-edict-sites]] deciphered by a mint official in the 1830s, [[c-prinsep]] [[c-prinsep-mint]] and coins, which are sometimes the only record that a king existed. [[c-punchmarked]]",
  {'table': {'head': ["Evidence", "China", "India"], 'rows': [
    ["Histories", "Sima Qian's Shiji (c. 100 BCE) and later dynastic histories", "no narrative histories; Puranic king lists, and Sri Lankan Buddhist chronicles of the 4th-6th centuries CE"],
    ["Documents", "bamboo and wooden slips from tombs and wells", "very few: most writing was on perishable leaves and bark"],
    ["Inscriptions", "on bronzes, steles and cliffs", "Ashoka's edicts; Gupta praise poems"],
    ["Foreign witnesses", "few before Buddhism", "Megasthenes; Chinese pilgrims such as Faxian"],
    ["Coins", "cast bronze, state-issued", "punch-marked silver; Indo-Greek and Kushan portrait coins"]], 'note': "[[c-simaqian]] [[c-slips-value]] [[c-edict-sites]] [[c-megasthenes]] [[c-punchmarked]]"}}],
 'figure': {'kind': 'map', 'view': {'lon': 94.0, 'lat': 30.0, 'zoom': 6.3}, 'caption': "Where the evidence comes from", 'hint': "Click a place",
  'legend': [['dot', 'texts excavated or inscribed'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [115.5, 27.0], 'label': 'CHINA', 'size': 13}, {'ll': [79.0, 22.0], 'label': 'INDIA', 'size': 13}, {'ll': [88.0, 33.0], 'label': 'TIBETAN PLATEAU', 'size': 9}, {'ll': [103.0, 44.5], 'label': 'STEPPE', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [110.429, 35.46], 'label': 'Hancheng', 'date': 'birthplace of Sima Qian', 'dy': -8, 'plate': {'kicker': '9.0 · how we know', 'title': 'Sima Qian', 'sub': 'c. 145 to c. 87 BCE', 'text': "[[c-simaqian]]", 'sources': ['brit-simaqian']}},
    {'ll': [109.21, 34.38], 'label': 'Lintong', 'date': "First Emperor's tomb", 'acc': True, 'dy': 16, 'plate': {'kicker': '9.2 · Qin', 'title': "The First Emperor's tomb", 'sub': 'found 1974', 'text': "[[c-mausoleum]] [[c-mercury]]", 'sources': ['unesco-qin', 'zhao2020']}},
    {'ll': [113.765, 31.063], 'label': 'Shuihudi', 'date': 'Qin laws, found 1975', 'acc': True, 'dy': -8, 'plate': {'kicker': '9.2 · Qin', 'title': 'Shuihudi', 'sub': 'Qin statutes', 'text': "[[c-shuihudi]] [[c-slips-value]]", 'sources': ['cdhk-shuihudi', 'hubei-shuihudi']}},
    {'ll': [112.19, 30.35], 'label': 'Jingzhou', 'date': 'Chu tomb slips', 'acc': True, 'anchor': 'end', 'dy': -6, 'plate': {'kicker': '9.1 · lost books', 'title': 'Slips from Chu tombs', 'sub': 'c. 300 BCE', 'text': "[[c-guodian]] [[c-newslips]]", 'sources': ['kirkland-guodian', 'll-wangjiazui', 'cd-qinjiazui']}},
    {'ll': [109.292, 28.789], 'label': 'Liye', 'date': 'Qin county archive', 'acc': True, 'dy': 16, 'plate': {'kicker': '9.2 · Qin', 'title': 'Liye', 'sub': 'found 2002', 'text': "[[c-liye]] [[c-liye-county]]", 'sources': ['cd-liye2025', 'pines-korolkov']}},
    {'ll': [94.683, 40.167], 'label': 'Dunhuang', 'date': 'Han slips', 'acc': True, 'dy': -10},
    {'ll': [85.189, 25.598], 'label': 'Pataliputra', 'date': 'described by Megasthenes', 'dy': 16, 'plate': {'kicker': '9.6 · Megasthenes', 'title': 'A Greek in India', 'sub': 'c. 300 BCE', 'text': "[[c-megasthenes]] [[c-megasthenes-rel]]", 'sources': ['brit-megasthenes', 'bmcr-stoneman']}},
    {'ll': [77.244, 28.636], 'label': 'Delhi', 'date': 'pillar read by Prinsep', 'acc': True, 'anchor': 'end', 'plate': {'kicker': '9.7 · Ashoka', 'title': 'Reading Ashoka', 'sub': '1837', 'text': "[[c-prinsep]] [[c-prinsep-mint]] [[c-edict-sites]]", 'sources': ['dhammika-prinsep', 'brit-prinsep', 'dhammika-edicts']}},
    {'ll': [65.717, 31.617], 'label': 'Kandahar', 'date': 'Greek edict', 'acc': True, 'dy': 16}]}]},
 'practice': [
  q("Why do the Shuihudi and Liye slips matter even though Sima Qian's history survives?",
    ["They are early Han copies of Sima Qian's Shiji", "They are Qin's own working records of law and government", "They were bought on the antiquities market, like Tsinghua's", "They are Han accounts written to blacken Qin's memory"], 1,
    "They are records, not narratives written by the dynasty that replaced Qin: Shuihudi gave the first known Qin law code, and Liye a Qin county's records, which can be checked against the histories.",
    {0: "They are Qin legal and administrative documents, not copies of a Han history.", 2: "Both were excavated, from a tomb at Shuihudi and a well at Liye; it was the Shanghai Museum and Tsinghua manuscripts that were bought.", 3: "They are Qin documents from a tomb and a Qin county's well, not Han writings about Qin."}),
  q("How does Megasthenes' Indica survive?",
    ["In a complete Greek manuscript copied in Byzantium", "As the Greek-language edicts carved at Kandahar", "As quotations in later Greek and Roman writers", "In a Sanskrit translation found at Pataliputra"], 2,
    "The four-book Indica is lost; it survives only in quotations, so every 'Megasthenes' passage reaches us through another author's choices.",
    {0: "The work is lost; no manuscript of it survives.", 1: "Those are Ashoka's own texts.", 3: "No Indian version is known; the Indica survives only in quotations by Greek and Roman writers."})]}

# ---------------------------------------------------------------- 9.1
P1 = {
 'title': "The Warring States", 'sub': "iron, mass armies and the Hundred Schools, c. 476-221 BCE",
 'lede': "For two and a half centuries a handful of Chinese kingdoms fought wars of a new scale and ferocity. The same pressure produced China's greatest age of philosophy, as thinkers competed to tell rulers how to survive, and lost books from that age keep coming out of the ground.",
 'body': [
  "War changed. Iron spread for tools and weapons, [[c-iron-ws]] the crossbow let peasant conscripts fight like professionals, [[c-crossbow]] and armies grew to hundreds of thousands. Tradition records slaughter on an enormous scale. [[c-changping]] The states that survived were those that could count, tax and mobilise their people best.",
  "Thinkers offered rival answers. Mozi preached impartial care for all and condemned aggressive war. [[c-mozi]] The Confucians split over human nature: Mencius thought it good, [[c-mencius]] Xunzi thought it bad and in need of shaping. [[c-xunzi]] Others, later lumped together as 'Legalists', [[c-legalism-label]] argued that only clear laws, rewards and punishments could make a state strong. Shang Yang put that into practice in Qin, [[c-shangyang]] and Han Fei turned it into theory. [[c-hanfei]] Qin's victory in 221 was, in part, a victory for their ideas.",
  "Archaeology has transformed this field. A tomb at Guodian held the oldest known Laozi, [[c-guodian]] and other manuscripts preserve debates the classics forgot, such as whether a king should pass the throne to the worthiest man. [[c-abdication]] Some of the most important, such as the Tsinghua slips, came from looters, [[c-tsinghua]] [[c-looted-slips]] but new scientific excavations keep adding more. [[c-newslips]]",
  {'table': {'head': ["Thinker", "Active", "Key idea"], 'rows': [
    ["Mozi", "c. 430 BCE", "impartial care; against aggressive war"],
    ["Shang Yang", "d. 338 BCE", "rank by merit in war and farming; harsh laws"],
    ["Mencius", "4th century BCE", "human nature is good; rule by benevolence"],
    ["Xunzi", "c. 310-after 238 BCE", "human nature is bad; ritual and learning shape it"],
    ["Han Fei", "d. 233 BCE", "law, technique and power: the strong state"]], 'note': "[[c-mozi]] [[c-shangyang]] [[c-mencius]] [[c-xunzi]] [[c-hanfei]]"}}],
 'figure': {'kind': 'chart', 'chart': 'bars', 'caption': "Lost books from the ground", 'title': "Slips in some major finds (log scale)",
  'scale': 'log', 'min': 100, 'max': 50000, 'ticks': [100, 1000, 10000], 'tickLabels': ['100', '1,000', '10,000'], 'axis': "number of slips, log scale", 'hint': "Hover a bar",
  'rows': [
   {'t': 'Guodian', 'sub': 'tomb, c. 300 BCE', 'v': 800, 'lab': 'c. 800', 'acc': True, 'tip': 'includes the oldest Laozi'},
   {'t': 'Shuihudi', 'sub': 'Qin tomb; excavated 1975', 'v': 1155, 'lab': '1,155', 'acc': True, 'tip': 'the first Qin laws ever found'},
   {'t': 'Shanghai Museum', 'sub': 'bought in Hong Kong', 'v': 1200, 'lab': 'c. 1,200', 'tip': 'origin unknown'},
   {'t': 'Tsinghua', 'sub': 'donated 2008', 'v': 2500, 'lab': 'c. 2,500', 'tip': 'origin unknown; c. 305 BCE'},
   {'t': 'Wangjiazui', 'sub': 'tomb; excavated 2021-22', 'v': 3200, 'lab': 'c. 3,200', 'acc': True, 'tip': 'Book of Songs; Confucius sayings'},
   {'t': 'Qinjiazui', 'sub': 'tomb, c. 369-329 BCE', 'v': 4000, 'lab': 'c. 4,000', 'acc': True, 'tip': 'includes multiplication tables'},
   {'t': 'Liye', 'sub': 'Qin county well; found 2002', 'v': 18000, 'lab': 'c. 18,000', 'acc': True, 'tip': 'out of nearly 38,000 slips', 'plate': {'kicker': '9.2 · Qin', 'title': 'Liye', 'sub': 'a Qin county archive', 'text': "[[c-liye]] [[c-liye-county]]", 'sources': ['cd-liye2025', 'pines-korolkov']}}],
  'notes': ["Coloured bars: excavated by archaeologists. Plain bars: bought or donated, origin unknown. Liye counts inscribed slips only."]},
 'practice': [
  q("Mencius and Xunzi, both Confucians, disagreed most sharply about what?",
    ["Whether Confucius deserved to be honoured as a sage", "Whether human nature is good or must be shaped by ritual", "Whether people owe impartial care to everyone alike", "Whether the throne should pass to the worthiest man"], 1,
    "Mencius thought human nature good, with innate 'sprouts' of virtue; Xunzi thought it bad, so that goodness comes only from effort, education and ritual.",
    {0: "Both were Confucians; the page sets them apart over human nature, not over Confucius.", 2: "Impartial care for everyone was Mozi's teaching, not the issue between the two Confucians.", 3: "That debate survives mainly in excavated manuscripts; it is not what divided Mencius from Xunzi."}),
  q("Why is 'the Legalist school' a problematic label?",
    ["Shang Yang and Han Fei wrote little about law itself", "Yuri Pines showed it was a formal school with members", "Han scholars invented it for men who never used it", "Arthur Waley coined it in place of the word 'Realists'"], 2,
    "'Legalism' (fajia) is a later Han label; no early thinker saw himself as a member of such a school.",
    {0: "Law (fa) was central to Han Fei, and Shang Yang put harsh laws into practice in Qin.", 1: "Pines calls the translation misleading; no early thinker saw himself as part of such a school.", 3: "Waley preferred 'Realists' as a better name; the label itself was invented by Han scholars."})]}

# ---------------------------------------------------------------- 9.2
P2 = {
 'title': "Qin: the first empire", 'sub': "221-207 BCE",
 'lede': "In 221 BCE the king of Qin finished conquering his rivals and called himself the First Emperor. His dynasty lasted only fifteen years, but the empire he built, with one script, one currency and one law, outlived him by two millennia.",
 'body': [
  "The Qin king Zheng took the last independent state in 221 BCE and invented a new title for himself. [[c-qin-unify]] He replaced the old kingdoms with commanderies run by appointed officials and imposed a single script, coinage, system of weights and even axle width. [[c-standard]] Sima Qian remembers him as a tyrant who burned books and killed scholars, [[c-burning]] though historians now doubt parts of that story. [[c-burning-debate]]",
  "His tomb is the most famous archaeological site in China: a buried city guarded by thousands of terracotta soldiers. [[c-mausoleum]] Their weapons were made to standard patterns by small workshops working in parallel under central supervision. [[c-triggers]] The emperor himself has not been disturbed, but mercury readings above the mound fit Sima Qian's story of a tomb with rivers of quicksilver. [[c-mercury]] In 2025 an inscription on the Tibetan plateau was claimed to record his search for the elixir of life. [[c-gyaring]]",
  "The slips show what the history books cannot: a state that ran on paperwork. The tomb of a minor official held Qin's laws, down to rules on price tags; [[c-shuihudi]] a well at Liye held a frontier county's daily records. [[c-liye]] They reveal a stretched administration, understaffed and run on forced labour. [[c-liye-county]]",
  "The First Emperor died in 210 BCE. Within four years rebels had destroyed his dynasty. Why it fell so fast is still argued over. [[c-qin-fall]]",
  {'table': {'head': ["Find", "Discovered", "What it shows"], 'rows': [
    ["Terracotta Army", "1974", "the scale and standardisation of the Qin state"],
    ["Shuihudi slips", "1975", "Qin statutes and an official's chronicle"],
    ["Liye well", "2002", "a frontier county's records"],
    ["Mercury survey", "2016", "readings above the mound fit Sima Qian's account"],
    ["Gyaring Lake inscription", "announced 2025", "an expedition to collect 'yao' (disputed)"]], 'note': "[[c-mausoleum]] [[c-shuihudi]] [[c-liye]] [[c-mercury]] [[c-gyaring]]"}},
  {'compare': "Rome and Qin both standardised to rule: Rome its coins and roads, Qin its axles, weights and script. But Rome left Greek as the language of its eastern half and let many cities keep their own laws, while Qin imposed one script on everyone. Over the following centuries spoken Latin split into the Romance languages and spoken Chinese into many mutually unintelligible varieties, but the Chinese world kept a single written standard that people of every dialect could read."}],
 'figure': {'kind': 'map', 'view': {'lon': 108.8, 'lat': 33.0, 'zoom': 14}, 'caption': "Qin China, 221-207 BCE", 'hint': "Click a place",
  'legend': [['dot', 'key place'], ['pt', 'other place']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [106.8, 36.3], 'label': 'QIN', 'size': 12}, {'ll': [112.8, 30.6], 'label': 'CHU', 'size': 11}, {'ll': [118.6, 36.3], 'label': 'QI', 'size': 11}, {'ll': [114.0, 37.9], 'label': 'ZHAO', 'size': 10}, {'ll': [116.4, 40.3], 'label': 'YAN', 'size': 10}]},
   {'type': 'points', 'items': [
    {'ll': [108.7, 34.34], 'label': 'Xianyang', 'date': 'Qin capital', 'acc': True, 'big': True, 'anchor': 'end', 'dy': -8, 'plate': {'kicker': '9.2 · Qin', 'title': 'The First Emperor', 'sub': 'king 246, emperor 221-210 BCE', 'text': "[[c-qin-unify]] [[c-standard]] [[c-burning]] [[c-burning-debate]]", 'sources': ['brit-qinshihuang', 'met-qin', 'neininger-keng']}},
    {'ll': [109.21, 34.38], 'label': 'Lintong', 'date': 'tomb and Terracotta Army', 'acc': True, 'big': True, 'dy': 16, 'plate': {'kicker': '9.2 · the tomb', 'title': 'The mausoleum', 'sub': 'found 1974', 'text': "[[c-mausoleum]] [[c-mercury]] [[c-triggers]]", 'sources': ['unesco-qin', 'zhao2020', 'li2014']}},
    {'ll': [118.3, 36.81], 'label': 'Linzi', 'date': 'Qi capital, falls 221', 'dy': 16},
    {'ll': [112.9, 35.81], 'label': 'Changping', 'date': 'c. 260 BCE', 'acc': True, 'dy': -8, 'plate': {'kicker': '9.1 · war', 'title': 'Changping', 'sub': 'c. 260 BCE', 'text': "[[c-changping]]", 'sources': ['sixthtone-changping']}},
    {'ll': [113.765, 31.063], 'label': 'Shuihudi', 'date': 'Qin laws', 'acc': True, 'dy': 16, 'plate': {'kicker': '9.2 · law', 'title': 'Shuihudi', 'sub': 'excavated 1975', 'text': "[[c-shuihudi]]", 'sources': ['cdhk-shuihudi', 'hubei-shuihudi']}},
    {'ll': [109.292, 28.789], 'label': 'Liye', 'date': 'county archive', 'acc': True, 'dy': 16, 'plate': {'kicker': '9.2 · administration', 'title': 'Liye', 'sub': 'found 2002', 'text': "[[c-liye]] [[c-liye-county]] [[c-qin-fall]]", 'sources': ['cd-liye2025', 'pines-korolkov', 'korolkov-hein2021']}},
    {'ll': [97.274, 34.918], 'label': 'Gyaring Lake', 'date': 'inscription, 210 BCE?', 'dy': 16, 'plate': {'kicker': '9.2 · new find', 'title': 'Gyaring Lake', 'sub': 'announced 2025', 'text': "[[c-gyaring]]", 'sources': ['scmp-gyaring', 'arkeo-gyaring']}}]}]},
 'practice': [
  q("What did the survey of mercury above the First Emperor's tomb show?",
    ["Rivers of mercury seen once the burial chamber was opened", "Raised readings that fit Sima Qian's story without proving it", "Background levels, which neither confirm nor refute the story", "Levels high enough to prove the rivers of mercury were real"], 1,
    "Mercury in the air above the mound ran at roughly two to five times background; the readings fit the story but do not prove it, and the authors call their estimate 'extremely crude'.",
    {0: "The burial chamber has never been opened.", 2: "The readings were roughly two to five times background, not at background.", 3: "The authors call their estimate 'extremely crude'; the readings fit the story but do not prove it."}),
  q("Which best reflects current scholarship on the 'burying of the scholars'?",
    ["Lu Jia and Jia Yi confirm Sima Qian's account in detail", "Historians now agree that no books were burned in 213 BCE", "Critics see magicians as the victims, and the martyr story as later", "Neininger confirms the victims were Confucians buried alive"], 2,
    "Ulrich Neininger argues the victims were mostly magicians, that keng means 'killed', and that the story of Confucian martyrs grew up later; the account itself comes from Sima Qian, about a century after the events.",
    {0: "The earliest Han critics of Qin, Lu Jia and Jia Yi, do not mention the killings.", 1: "Most historians accept that some book-burning took place.", 3: "Neininger argues the opposite: the victims were mostly magicians, and keng means 'killed', not 'buried alive'."})]}

# ---------------------------------------------------------------- 9.3
P3 = {
 'title': "The Han state", 'sub': "206 BCE to 220 CE",
 'lede': "The Han kept the Qin machine and gave it a softer face. For four centuries, with one interruption, it ruled through salaried officials who increasingly claimed to govern by Confucian principle, and the Chinese still call themselves 'the Han people'.",
 'body': [
  "Liu Bang, a commoner who had once been a minor Qin official, won the civil war that followed Qin's collapse. [[c-liubang]] His dynasty kept Qin's centralised, salaried bureaucracy, [[c-han-capitals]] and the numbers are impressive: one commandery alone had over two thousand officials on its books. [[c-yinwan]] [[c-han-officials]]",
  "Later Confucians told how Emperor Wu made their teaching the official ideology. [[c-confucian-trad]] Historians now think the change came more slowly and less cleanly. [[c-confucian-debate]] Wu's own reign is better remembered for war and monopolies (see 9.4 and 9.5), and for the historian Sima Qian, who was condemned for defending a disgraced general and castrated instead of being executed. [[c-simaqian]]",
  "In 2 CE the Han took China's oldest surviving census: almost 60 million registered people, and certainly more in reality. [[c-census-min]] [[c-census2]] A few years later the regent Wang Mang took the throne, tried to remake society, and was swept away by floods and rebellion. [[c-wangmang-fall]] [[c-wangmang]] The restored Eastern Han ruled from Luoyang, weakened by court factions and great landowners, until a religious rebellion and the warlords raised to fight it ended the dynasty in 220. [[c-eastern-han]]",
  {'table': {'head': ["Period", "Dates", "Capital", "Notes"], 'rows': [
    ["Western Han", "206 BCE-9 CE", "Chang'an", "Emperor Wu, 141-87 BCE"],
    ["Xin (Wang Mang)", "9-23 CE", "Chang'an", "land and coin reforms fail"],
    ["Eastern Han", "25-220 CE", "Luoyang", "Yellow Turbans, 184"]], 'note': "[[c-han-capitals]] [[c-wangmang-fall]] [[c-eastern-han]]"}}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "Four centuries of Han", 'title': "The Han dynasty and its interruption",
  'max': 230, 'min': -230, 'unit': 'ka', 'ticks': [200, 100, 0, -100, -200], 'tickLabels': ['200 BCE', '100 BCE', '1 CE', '100 CE', '200 CE'],
  'axis': "years BCE and CE", 'hint': "Hover or click a row",
  'marks': [{'ya': 136, 't': "Confucian turn (traditional date), 136 BCE"}, {'ya': -2, 't': 'census, 2 CE'}],
  'rows': [
   {'t': 'Western Han', 'sub': "capital Chang'an", 'from': 206, 'to': -9, 'lab': '206 BCE-9 CE', 'acc': True, 'plate': {'kicker': '9.3 · Han', 'title': 'The Western Han', 'sub': '206 BCE to 9 CE', 'text': "[[c-liubang]] [[c-han-capitals]] [[c-confucian-trad]] [[c-confucian-debate]]", 'sources': ['brit-gaozu', 'brit-handyn', 'cai2014']}},
   {'t': 'Emperor Wu', 'from': 141, 'to': 87, 'lab': '141-87 BCE', 'acc': True, 'plate': {'kicker': '9.5 · Emperor Wu', 'title': 'Emperor Wu', 'sub': '141-87 BCE', 'text': "[[c-wu-wars]] [[c-iron-monopoly]] [[c-confucian-debate]]", 'sources': ['brit-wudi', 'wagner-iron', 'cai2014']}},
   {'t': 'Sima Qian', 'sub': 'historian', 'from': 145, 'to': 87, 'lab': 'c. 145-87 BCE', 'open': True},
   {'t': 'Xin dynasty', 'sub': 'Wang Mang', 'from': -9, 'to': -23, 'lab': '9-23 CE', 'open': True, 'plate': {'kicker': '9.3 · Wang Mang', 'title': 'Wang Mang', 'sub': '9-23 CE', 'text': "[[c-wangmang]] [[c-wangmang-fall]]", 'sources': ['brit-wangmang', 'smith-wangmang']}},
   {'t': 'Eastern Han', 'sub': 'capital Luoyang', 'from': -25, 'to': -220, 'lab': '25-220 CE', 'acc': True, 'plate': {'kicker': '9.3 · Han', 'title': 'The Eastern Han', 'sub': '25-220 CE', 'text': "[[c-eastern-han]] [[c-great-families]]", 'sources': ['brit-yellowturbans', 'brit-han']}},
   {'t': 'Yellow Turbans', 'sub': 'rebellion', 'from': -184, 'to': -204, 'lab': '184-c. 204', 'open': True}]},
 'practice': [
  q("Liang Cai's Witchcraft and the Rise of the First Confucian Empire challenges which view?",
    ["That Dong Zhongshu really wrote the work credited to him", "That Confucians already ran the government under Wu", "That a witchcraft scandal helped the Confucians to rise", "That Wang Mang seized the Han throne in 9 CE"], 1,
    "She argues Confucian scholars were a powerless minority under Wu and rose only after a court witchcraft scandal of 91-87 BCE.",
    {0: "Doubts about Dong Zhongshu's authorship are Michael Loewe's argument, not Cai's.", 2: "That is Cai's own argument: the scandal of 91-87 BCE is when she says Confucians rose.", 3: "Her argument concerns Emperor Wu's reign and after; the page states plainly that Wang Mang took the throne in 9 CE."}),
  q("Why should the Han census total of 2 CE be read as a minimum?",
    ["It covered the capital region but not the provinces", "People avoided registering for the poll tax", "It left out the areas held by the Red Eyebrows", "It listed soldiers rather than farming households"], 1,
    "It was taken mainly for the poll tax, and people avoided registration, so the true population was larger.",
    {0: "It is described as China's oldest surviving count, with almost 60 million registered people, not a count of one region.", 2: "The Red Eyebrows rose against Wang Mang, who took the throne in 9 CE, years after the census.", 3: "It was a poll-tax count of almost 60 million registered people, not a muster of soldiers."})]}

PAGES = [P0, P1, P2, P3]
