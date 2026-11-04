# Chapter 6, pages 6.8 to 6.11. Coordinates are [longitude, latitude].
from common import c, q

S = {
 'brit-merneptah': ("Encyclopaedia Britannica, \"Merneptah\"", "https://www.britannica.com/biography/Merneptah"),
 'cojs-merneptah': ("Center for Online Judaic Studies, the Merneptah Stele", "https://cojs.org/stelae_and_reliefs_of_pharaoh_merneptah-_c-_1207_bce/"),
 'pulak2008': ("Cemal Pulak, \"The Uluburun shipwreck and Late Bronze Age trade\", in Beyond Babylon (Metropolitan Museum, 2008)", "https://cgs.la.psu.edu/wp-content/uploads/sites/27/2020/12/Pulak-2008-Reading.pdf"),
 'ina-gelidonya': ("Institute of Nautical Archaeology, \"Cape Gelidonya Late Bronze Age shipwreck\"", "https://nauticalarch.org/projects/cape-gelidonya-late-bronze-age-shipwreck-excavation/"),
 'sd-powell2022': ("ScienceDaily, on Powell et al., Science Advances (2022), the sources of Uluburun's tin", "https://www.sciencedaily.com/releases/2022/11/221130151458.htm"),
 'berger2023': ("Berger, Kaniuth, Brügmann and Pernicka, on the Uluburun tin, Frontiers in Earth Science 11 (2023)", "https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2023.1211478/full"),
 'toi-berger2019': ("Times of Israel, on Berger et al., PLOS ONE (2019): tin ingots found off Israel", "https://www.timesofisrael.com/groundbreaking-study-ancient-tin-ingots-found-in-israel-were-mined-in-england/"),
 'dartmouth-aegean': ("Dartmouth College, Aegean Prehistory, lesson 28: the end of the palaces", "https://sites.dartmouth.edu/aegean-prehistory/lessons/lesson-28-narrative"),
 'oeaw2022': ("Jung and Kardamaki (eds.), Synchronizing the Destructions of the Mycenaean Palaces (Austrian Academy of Sciences, 2022)", "https://verlag.oeaw.ac.at/en/product/synchronizing-the-destructions-of-the-mycenaean-palaces/99200522"),
 'bas-hazor': ("Bible History Daily, on the destruction of Canaanite Hazor", "https://www.biblicalarchaeology.org/daily/news/scorched-wheat-may-provide-answers-on-the-destruction-of-canaanite-tel-hazor/"),
 'ej-lachish': ("Encyclopaedia Judaica, \"Lachish\" (via encyclopedia.com)", "https://www.encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/lachish"),
 'whe-seapeoples': ("Joshua J. Mark, World History Encyclopedia, \"Sea Peoples\"", "https://www.worldhistory.org/Sea_Peoples/"),
 'grandet2014': ("Pierre Grandet, \"Early to mid-20th Dynasty\", UCLA Encyclopedia of Egyptology (2014)", "https://journalpub.escholarship.org/nelc_uee/article/4768/galley/2682/download"),
 'cline2015': ("Eric Cline, \"Raiders of the lost Bronze Age?\", MHQ (2015)", "https://ancientportsantiques.com/wp-content/uploads/Documents/AUTHORS/SeaPeoples/SeaPeoples-Cline2015.pdf"),
 'ucl-ramesses3': ("UCL Digital Egypt, \"Ramesses III\"", "https://www.ucl.ac.uk/museums-static/digitalegypt/chronology/ramsesiii.html"),
 'tau-langgut': ("Tel Aviv University, on Langgut, Finkelstein and Litt, Tel Aviv (2013): pollen and drought", "https://english.tau.ac.il/node/1346"),
 'kaniewski2013': ("Kaniewski et al., \"Environmental roots of the Late Bronze Age crisis\", PLOS ONE (2013)", "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0071004"),
 'archmag-power2026': ("Archaeology Magazine (Greece), on Power et al., Science Advances (2026): drought and the Bronze Age collapse", "https://archaeologymag.com/2026/07/severe-droughts-collapse-of-bronze-age-civilizations/"),
 'nur-cline2000': ("Nur and Cline, \"Poseidon's horses: plate tectonics and earthquake storms\", Journal of Archaeological Science 27 (2000)", "https://www.ancientportsantiques.com/wp-content/uploads/Documents/ETUDESarchivees/Tsunamis/Earthquakes-Nur&Cline2000.pdf"),
 'knapp-manning2016': ("Knapp and Manning, \"Crisis in context: the end of the Late Bronze Age in the eastern Mediterranean\", American Journal of Archaeology 120 (2016)", "https://ajaonline.org/wp-content/uploads/2015/12/1201_Knapp.pdf"),
 'pup-1177': ("Princeton University Press, Eric Cline, 1177 B.C.: The Year Civilization Collapsed (revised edition, 2021)", "https://press.princeton.edu/books/paperback/9780691208015/1177-bc"),
 'cline2024': ("Eric Cline, After 1177 B.C.: The Survival of Civilizations (Princeton, 2024), publisher's description", "https://betterread.com.au/book/after-1177-bc-the-survival-of-civilizations.do"),
 'brit-tiglath': ("Encyclopaedia Britannica, \"Tiglath-pileser I\"", "https://www.britannica.com/print/article/595525"),
 'erb-satullo2019': ("Nathaniel Erb-Satullo, \"The innovation and adoption of iron in the ancient Near East\", Journal of Archaeological Research (2019)", "https://link.springer.com/doi/10.1007/s10814-019-09129-6"),
 'mpg-ashkelon': ("Max Planck Institute, on Feldman et al., \"Ancient DNA sheds light on the genetic origins of early Iron Age Philistines\", Science Advances (2019)", "https://www.shh.mpg.de/1360247/sino-tibetan-origin"),
 'brit-philistines': ("Encyclopaedia Britannica, \"Philistine\"", "https://www.britannica.com/topic/Philistine-people"),
 'met-phoenicians': ("The Met, \"The Phoenicians (1500-300 B.C.)\" (2004)", "https://www.metmuseum.org/toah/hd/phoe/hd_phoe.htm"),
 'brit-phoen-alphabet': ("Encyclopaedia Britannica, \"Phoenician alphabet\"", "https://www.britannica.com/topic/Phoenician-alphabet"),
 'finkelstein2001': ("Finkelstein and Silberman, The Bible Unearthed (2001), chapter on the highland settlers (excerpt)", "https://courses.lsa.umich.edu/israel-palestine/wp-content/uploads/sites/142/2013/12/016.-I.Finkelstein_N.A-Silberman-105-120_01.pdf"),
 'dever-on-faust': ("William Dever, review of Avraham Faust, Israel's Ethnogenesis, Bible History Daily (2012)", "https://www.biblicalarchaeology.org/reviews/israels-ethnogenesis/"),
 'america-dever': ("Michael Coogan, review of William Dever, Who Were the Early Israelites?, America (2003)", "https://www.americamagazine.org/books/2003/06/09/emerging-confederation/"),
 'brit-neohittite': ("Encyclopaedia Britannica, \"Anatolia: the Neo-Hittite states\"", "https://www.britannica.com/place/Anatolia/The-neo-Hittite-states-from-c-1180-to-700-bce"),
}

C = {
 # 6.8
 'c-uluburun-find': c("The Uluburun wreck, off southern Turkey, was found by a sponge diver in 1982 and excavated in eleven seasons from 1984 to 1994, at depths of 42-61 metres.", 'consensus', ['pulak2008'], show=False),
 'c-uluburun-date': c("Tree rings and radiocarbon date the sinking to about 1300 BCE.", 'approx', ['pulak2008'], show=False),
 'c-copper': c("The ship carried about 10 tons of copper, in 354 slab ingots, most of them 'oxhide'-shaped, and lead isotopes link the copper to Cyprus.", 'approx', ['pulak2008'], show=False),
 'c-tin': c("It also carried about a ton of tin, enough with the copper to make about 11 tons of bronze in the usual proportion of ten parts copper to one of tin.", 'approx', ['pulak2008'], show=False),
 'c-cargo': c("Other cargo included about 175 ingots of glass, Canaanite jars of resin, ebony logs, elephant and hippopotamus ivory, and a gold scarab bearing the name of Nefertiti.", 'consensus', ['pulak2008'], show=False),
 'c-route': c("The ship probably sailed from the coast of Canaan and was heading west, perhaps to Mycenaean Greece.", 'debated', ['pulak2008'], "This is Cemal Pulak's reconstruction from the cargo; no text records its voyage."),
 'c-gelidonya': c("The smaller Cape Gelidonya wreck, about 1200 BCE, carried copper, tin and scrap bronze; excavated by George Bass in 1960, it was the first ancient wreck fully excavated on the seabed.", 'consensus', ['ina-gelidonya'], show=False),
 'c-tin-source': c("Where the tin came from is disputed: a 2022 study traced much of it to Anatolia and Central Asia; a 2023 reply rejected both proposed mines.", 'debated', ['sd-powell2022', 'berger2023'], "Powell and colleagues proposed Kestel in Anatolia and Mušiston in Central Asia; Berger and colleagues argue the chemistry does not match and suggest more distant sources, possibly south-west England."),
 'c-tin-cornwall': c("Tin ingots of the 13th-12th centuries found off Israel have been traced to Cornwall and Devon in Britain.", 'debated', ['toi-berger2019'], "The authors called England the most likely source; tin deposits are rare and scattered, which makes sourcing difficult."),
 'c-bronze-trade': c("Copper and tin rarely occur together, so making bronze depended on trade over long distances and across many borders.", 'consensus', ['pulak2008', 'sd-powell2022'], show=False),
 # 6.9
 'c-carchemish': c("Carchemish on the Euphrates was not destroyed; its ruler, a member of the Hittite royal family, took the title Great King.", 'consensus', ['demartino2018'], show=False),
 'c-tweini': c("At Tell Tweini near Ugarit, radiocarbon dates the destruction to about 1192-1190 BCE, at almost the same time as Ugarit.", 'approx', ['kaniewski2011'], "Some scholars think the precision of these dates is overstated."),
 'c-emar': c("Emar on the Euphrates fell about 1185 BCE or shortly after.", 'approx', ['demartino2018'], show=False),
 'c-aegean-fires': c("Fires ended the palaces of Mycenae, Tiryns, Pylos and Thebes around 1200 BCE; Pylos and Mycenae's palace were never rebuilt.", 'approx', ['dartmouth-aegean', 'oeaw2022'], "The destructions are dated by pottery phases, not calendar years, and may not have been simultaneous."),
 'c-hazor': c("The Canaanite city of Hazor burned in the 13th century BCE; who destroyed it, and exactly when, is disputed.", 'debated', ['bas-hazor'], "Amnon Ben-Tor links it to early Israel; Sharon Zuckerman argues for an internal revolt."),
 'c-lachish': c("Lachish was destroyed later, perhaps about 1130 BCE: an object bearing the name of Ramesses III shows it outlived his wars.", 'debated', ['ej-lachish'], "The attacker is unknown; Sea Peoples and Israelites have both been suggested."),
 'c-merneptah-sea': c("In about 1209 BCE, his fifth year, Merneptah defeated a Libyan invasion joined by groups including the Sherden, Shekelesh, Lukka, Teresh and Ekwesh.", 'approx', ['whe-seapeoples', 'grandet2014', 'brit-merneptah', 'cojs-merneptah'], "Britannica and the World History Encyclopedia give 1209 for the battle. The Merneptah Stele, which celebrates the victory in the same regnal year, is dated about 1208 in this book (4.9); some sources give c. 1207."),
 'c-medinet-habu': c("Ramesses III's inscription at Medinet Habu says that 'the foreign countries made a conspiracy in their islands' and that 'no land could stand before their arms', naming the Peleset, Tjekker, Shekelesh, Denyen and Weshesh.", 'consensus', ['cline2015', 'grandet2014'], show=False),
 'c-year8': c("Ramesses III records defeating them by land and sea in his 8th year, about 1177 BCE.", 'approx', ['cline2015', 'ucl-ramesses3', 'grandet2014'], "1177 follows the dates used in Chapter 4; other chronologies put it up to a decade earlier. The inscriptions are royal propaganda as well as record."),
 'c-sea-identity': c("The firmest identification of any 'Sea People' with a people known from later history is the Peleset, who are the Philistines.", 'debated', ['cline2015', 'ucl-ramesses3'], "Links of the Sherden to Sardinia and the Shekelesh to Sicily are guesses; Eric Cline suggests the Sea Peoples may have been 'as much the victims as the aggressors'."),
 # 6.10
 'c-langgut': c("Pollen from cores in the Sea of Galilee and the Dead Sea suggests repeated droughts in the southern Levant between about 1250 and 1100 BCE.", 'debated', ['tau-langgut'], "Critics say the dating of the cores is too loose to tie the drought to particular events."),
 'c-kaniewski-cyprus': c("Pollen from a salt lake in Cyprus has been read as the start of a long dry period about 1200 BCE.", 'debated', ['kaniewski2013'], "The authors argue the crisis, the Sea Peoples and the drought were 'the same event'; the evidence comes from one core."),
 'c-power2026': c("A 2026 climate-model study supports severe drought in the eastern Mediterranean about 3,200 years ago.", 'debated', ['archmag-power2026'], "Model results must be checked against physical records."),
 'c-quakes': c("Amos Nur and Eric Cline proposed an 'earthquake storm', a chain of earthquakes about 1225-1175 BCE that damaged many cities.", 'debated', ['nur-cline2000'], "They presented it as one factor among several; Knapp and Manning argue earthquake damage is hard to prove and would not by itself destroy societies."),
 'c-knapp': c("Bernard Knapp and Sturt Manning argued in 2016 that the climate records were too imprecise to name drought as the cause.", 'debated', ['knapp-manning2016'], "Manning later co-authored the precisely dated Gordion tree-ring study (6.1)."),
 'c-invasion': c("Destruction layers with arrowheads, and letters from Ugarit about enemy ships, fit seaborne raiding in the Levant.", 'debated', ['cline2015', 'kaniewski2011'], "There is no sound evidence that the Sea Peoples attacked the Aegean palaces."),
 'c-revolt': c("Other explanations stress internal weakness: peasant revolt, elite conflict, or a palace economy too specialised to survive shocks.", 'debated', ['dartmouth-aegean'], "These ideas are hard to test directly."),
 'c-systems': c("Eric Cline argues that drought, earthquakes, invasions, revolts and broken trade interacted, and that the powers' dependence on one another made the fall faster and wider.", 'debated', ['pup-1177'], "This 'systems collapse' view is widely cited, but its critics say it can explain almost anything."),
 'c-resilience': c("In a 2024 book Cline argues that some societies vanished while others, such as the Phoenicians, Philistines, Israelites and Assyria, adapted and built something new.", 'debated', ['cline2024'], "Whether 'collapse' is the right word depends on where one looks."),
 'c-assyria-survives': c("Assyria survived: Tiglath-pileser I (c. 1115-1077 BCE) campaigned to the Mediterranean coast and took tribute from Phoenician cities.", 'approx', ['brit-tiglath'], show=False),
 # 6.11
 'c-iron': c("Iron objects become more common from the 12th century BCE, first in Cyprus and the Levant; large-scale iron-working there came in the 10th-9th centuries.", 'approx', ['erb-satullo2019'], show=False),
 'c-iron-shortage': c("An old theory says iron spread because the collapse cut off supplies of tin; recent research finds little support for it.", 'debated', ['erb-satullo2019'], "Cypriot copper production continued, and bronzes show no clear fall in tin content."),
 'c-philistine-dna': c("DNA from Ashkelon shows that newcomers with European-related ancestry arrived at the start of the Iron Age and, within two centuries, mixed with the local population.", 'approx', ['mpg-ashkelon'], "The study sampled ten individuals; a southern European source is plausible but not confirmed."),
 'c-philistines': c("The Philistines settled the southern coast of Canaan in five cities, Gaza, Ashkelon, Ashdod, Gath and Ekron; their early pottery derives from Mycenaean styles.", 'consensus', ['brit-philistines'], show=False),
 'c-caphtor': c("The Bible says the Philistines came from Caphtor, usually taken to be Crete.", 'tradition', ['brit-philistines'], "Amos 9:7; Aegean-style pottery fits an origin in the Aegean world, but no find confirms Crete specifically."),
 'c-phoenicians': c("Freed from Egyptian control, the Phoenician cities of Tyre, Sidon, Byblos and Arwad grew rich on trade in cedar wood and purple dye.", 'consensus', ['met-phoenicians'], show=False),
 'c-phoen-alphabet': c("The Phoenician alphabet of 22 consonants, known from the 11th century BCE, is the ancestor of the Greek alphabet and so of the Latin one.", 'approx', ['brit-phoen-alphabet'], show=False),
 'c-highlands': c("From about 1200 BCE some 250 small villages appeared in the hill country of Canaan, rising to perhaps 45,000 people by about 1000.", 'approx', ['finkelstein2001'], "Population is estimated from the number and size of sites."),
 'c-highland-origins': c("Most archaeologists connect these villages with early Israel, but disagree about who the settlers were.", 'debated', ['finkelstein2001', 'dever-on-faust', 'america-dever'], "Israel Finkelstein sees mainly local pastoralists settling down; Avraham Faust sees a group marking its identity by avoiding pork and display; William Dever sees a mixed 'proto-Israelite' confederation. Some scholars doubt Israelite identity can be traced this early at all."),
 'c-no-pigs': c("The highland villages were small and unfortified, and their animal bones include almost no pig.", 'consensus', ['finkelstein2001'], show=False),
 'c-neohittite': c("In northern Syria and south-east Anatolia, Neo-Hittite kingdoms such as Carchemish kept Hittite traditions alive until Assyria absorbed them in the late 8th century BCE.", 'consensus', ['brit-neohittite', 'demartino2018'], show=False),
}

P8 = {
 'title': "The trade that bound them", 'sub': "the Uluburun ship, copper and tin",
 'lede': "Bronze is copper alloyed with a little tin, and the two metals are almost never found together. The great powers' armies, tools and temples therefore depended on long trade routes. A ship that sank about 1300 BCE shows what moved along them.",
 'body': [
  "In 1982 a sponge diver off southern Turkey reported strange metal objects on the sea floor. They were copper ingots from the Uluburun wreck, excavated over eleven seasons. [[c-uluburun-find]] Tree rings and radiocarbon date the sinking to about 1300 BCE. [[c-uluburun-date]]",
  "The ship carried about 10 tons of Cypriot copper [[c-copper]] and about a ton of tin, enough for some 11 tons of bronze. [[c-tin]] It also held glass ingots, jars of resin, African ebony, ivory, and a gold scarab with the name of Nefertiti. [[c-cargo]] It was probably sailing west from Canaan toward the Aegean. [[c-route]] A smaller wreck at Cape Gelidonya, about a century later, carried scrap bronze for recycling. [[c-gelidonya]]",
  "Copper came mainly from Cyprus, the Alashiya of the Amarna letters (6.0). Tin is harder. Recent studies trace Bronze Age tin to Anatolia, Central Asia or even Britain, and dispute each other's results. [[c-tin-source]] [[c-tin-cornwall]] Either way, tin came from a few scattered sources, and bronze tied the great powers to long and fragile supply lines. [[c-bronze-trade]]",
  {'table': {'head': ["Cargo", "Amount", "Origin"], 'rows': [
    ["copper", "c. 10 tons", "Cyprus"],
    ["tin", "c. 1 ton", "disputed"],
    ["glass ingots", "c. 175", "Egypt and the Near East"],
    ["resin in Canaanite jars", "c. 0.5 ton", "Canaan"],
    ["ebony; ivory", "logs; tusk, hippo teeth", "Africa; Africa or the Levant"]], 'note': "Pulak (2008). [[c-copper]] [[c-tin]] [[c-cargo]]"}},
  {'compare': "Compare the sea trade between the Indus, the Gulf and Mesopotamia (5.2), a thousand years earlier."}],
 'figure': {'kind': 'chart', 'chart': 'bars', 'caption': "What the Uluburun ship carried", 'title': "Main bulk cargoes, by weight (kg)",
  'max': 10500, 'ticks': [0, 2000, 4000, 6000, 8000, 10000], 'axis': "kilograms", 'hint': "Hover a bar",
  'rows': [
   {'t': 'Copper', 'sub': 'mostly oxhide ingots, Cyprus', 'v': 10000, 'lab': 'c. 10 tons', 'acc': True, 'plate': {'kicker': '6.8 · trade', 'title': 'The Uluburun ship', 'sub': 'sank c. 1300 BCE', 'text': "[[c-uluburun-find]] [[c-copper]] [[c-tin]] [[c-cargo]] [[c-route]]", 'sources': ['pulak2008']}},
   {'t': 'Tin', 'sub': 'source disputed', 'v': 1000, 'lab': 'c. 1 ton', 'acc': True, 'plate': {'kicker': '6.8 · trade', 'title': 'Where did the tin come from?', 'sub': 'a live debate', 'text': "[[c-tin-source]] [[c-tin-cornwall]]", 'sources': ['sd-powell2022', 'berger2023', 'toi-berger2019']}},
   {'t': 'Resin', 'sub': 'in Canaanite jars', 'v': 500, 'lab': 'c. 0.5 ton'},
   {'t': 'Glass ingots', 'sub': 'c. 175 ingots', 'v': 350, 'lab': 'c. 350 kg'}],
  'notes': ["Source: Pulak (2008). Tin decays in seawater; the original amount was probably larger."]},
 'practice': [
  q("Why do the 2022-2023 studies of the Uluburun tin matter for understanding the Late Bronze Age economy?",
    ["Tin came from a few scattered sources, still disputed today", "They traced the tin to Cyprus, the source of the ship's copper", "They redated the sinking of the ship to about 1000 BCE", "Both agreed on Central Asia but disputed how the tin travelled"], 0,
    "Proposed sources range from Anatolia to Central Asia and Britain. The disagreement itself shows how few and far-flung the sources were.",
    {1: "Cyprus supplied the copper, not the tin.", 2: "Tree rings and radiocarbon date the sinking to about 1300 BCE.", 3: "The 2023 reply rejected both the Central Asian and the Anatolian mines proposed in 2022."}),
  q("The Uluburun ship held about ten times as much copper as tin. What does that ratio suggest?",
    ["The metals were meant to be alloyed into bronze at ten to one", "The copper was meant for Cyprus and the tin for Canaan", "The ship had sailed from Mycenae with Greek copper for Egypt", "Tin was plentiful, so little of it needed to be carried"], 0,
    "Bronze was usually ten parts copper to one of tin; Pulak notes the cargo would make about 11 tons of bronze.",
    {1: "The copper itself came from Cyprus, and the ship was probably heading west.", 2: "Lead isotopes link the copper to Cyprus, and the ship probably sailed west from Canaan.", 3: "Tin came from a few scattered sources, which is why bronze depended on long-distance trade."})]}

P9 = {
 'title': "The collapse", 'sub': "c. 1200 to 1150 BCE",
 'lede': "Within about fifty years after 1200 BCE, the Hittite empire vanished, Ugarit was destroyed, the Mycenaean palaces burned, and Egypt fought off invaders by land and sea. Writing disappeared from Greece for four centuries.",
 'body': [
  "The Hittite court abandoned Hattusa early in the 12th century. [[c-hattusa-end]] Ugarit was destroyed soon after an eclipse of 1192 BCE, [[c-ugarit-end]] and nearby Tell Tweini at almost the same time. [[c-tweini]] Emar fell about 1185. [[c-emar]] But Carchemish survived, and its king called himself Great King. [[c-carchemish]] In Greece, fires ended the palaces of Mycenae, Tiryns, Pylos and Thebes around 1200. [[c-aegean-fires]] In Canaan, Hazor burned [[c-hazor]] and Lachish fell decades later. [[c-lachish]]",
  "Egypt left the most famous account. Merneptah had already fought a Libyan invasion joined by groups from the sea. [[c-merneptah-sea]] About 1177 BCE, in his 8th year, Ramesses III fought them again. [[c-year8]] His temple at Medinet Habu says 'the foreign countries made a conspiracy in their islands' and that 'no land could stand before their arms'. [[c-medinet-habu]] Modern historians call them the 'Sea Peoples'. The firmest identification is the Peleset, the Philistines. [[c-sea-identity]]",
  "The destructions were spread over decades, some cities survived, and some were abandoned rather than sacked. That is why most historians no longer think one wave of invaders destroyed the system.",
  {'table': {'head': ["Place", "What happened", "When (BCE)"], 'rows': [
    ["Hattusa", "abandoned", "early 12th century"],
    ["Ugarit", "destroyed", "soon after 1192"],
    ["Emar", "destroyed", "c. 1185"],
    ["Mycenae, Pylos", "palaces burned", "c. 1200"],
    ["Carchemish", "survived", "-"],
    ["Egypt", "repelled invaders", "c. 1177"]], 'note': "[[c-hattusa-end]] [[c-ugarit-end]] [[c-emar]] [[c-aegean-fires]] [[c-carchemish]] [[c-year8]]"}},
  {'compare': "Compare the end of Akkad and the crises around 2200 BCE (3.6, 4.6): another moment when several societies failed at once."}],
 'figure': {'kind': 'map', 'view': {'lon': 30.0, 'lat': 35.6, 'zoom': 21}, 'caption': "Destruction and survival, c. 1200-1130 BCE", 'hint': "Click a site",
  'legend': [['dot', 'destroyed or abandoned'], ['pt', 'survived']], 'seas': False,
  'layers': [
   {'type': 'region', 'items': [{'ll': [30.8, 30.4], 'label': 'EGYPT', 'size': 11}, {'ll': [33.5, 39.0], 'label': 'HATTI', 'size': 11}, {'ll': [26.0, 38.6], 'label': 'AEGEAN', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [34.6153, 40.0197], 'label': 'Hattusa', 'date': 'abandoned', 'acc': True, 'big': True, 'plate': {'kicker': '6.9 · collapse', 'title': 'Hattusa', 'sub': 'early 12th century BCE', 'text': "[[c-hattusa-end]] [[c-gordion-drought]]", 'sources': ['demartino2018', 'natgeo-hittite', 'manning2023']}},
    {'ll': [35.7854, 35.6019], 'label': 'Ugarit', 'date': 'soon after 1192', 'acc': True, 'big': True, 'dy': 14, 'plate': {'kicker': '6.9 · collapse', 'title': 'Ugarit', 'sub': 'destroyed soon after 1192 BCE', 'text': "[[c-ugarit-end]] [[c-tweini]] [[c-invasion]]", 'sources': ['kaniewski2011', 'met-ugarit']}},
    {'ll': [38.1114, 35.9868], 'label': 'Emar', 'date': 'c. 1185', 'acc': True, 'dy': -8},
    {'ll': [38.0164, 36.8294], 'label': 'Carchemish', 'date': 'survived', 'dy': -8, 'anchor': 'end', 'plate': {'kicker': '6.9 · collapse', 'title': 'Carchemish', 'sub': 'a survivor', 'text': "[[c-carchemish]] [[c-neohittite]]", 'sources': ['demartino2018', 'brit-neohittite']}},
    {'ll': [22.7561, 37.7306], 'label': 'Mycenae', 'acc': True, 'dy': -8, 'plate': {'kicker': '6.9 · collapse', 'title': 'The Mycenaean palaces', 'sub': 'burned c. 1200 BCE', 'text': "[[c-aegean-fires]] [[c-revolt]]", 'sources': ['dartmouth-aegean', 'oeaw2022']}},
    {'ll': [21.695, 37.0272], 'label': 'Pylos', 'acc': True, 'dy': 14},
    {'ll': [35.5668, 33.0192], 'label': 'Hazor', 'date': '13th century', 'acc': True, 'plate': {'kicker': '6.9 · collapse', 'title': 'Hazor', 'sub': 'burned in the 13th century BCE', 'text': "[[c-hazor]]", 'sources': ['bas-hazor']}},
    {'ll': [34.8489, 31.565], 'label': 'Lachish', 'date': 'c. 1130?', 'acc': True, 'anchor': 'end', 'plate': {'kicker': '6.9 · collapse', 'title': 'Lachish', 'sub': 'destroyed perhaps c. 1130 BCE', 'text': "[[c-lachish]]", 'sources': ['ej-lachish']}},
    {'ll': [33.8722, 35.166], 'label': 'Cyprus', 'date': 'copper trade went on', 'anchor': 'end', 'dy': 14}]}]},
 'practice': [
  q("Why do archaeologists doubt that a single army of 'Sea Peoples' destroyed the whole system in one campaign?",
    ["The destructions span decades, and Hattusa was abandoned", "Medinet Habu describes a raid on Egypt but names no groups", "Ugarit survived the raids and lasted into the Iron Age", "The Sea Peoples conquered Egypt before reaching Hattusa"], 0,
    "The destructions run from the 1190s to about 1130 BCE. Hattusa was abandoned rather than sacked, and Carchemish survived.",
    {1: "Medinet Habu names the Peleset, Tjekker, Shekelesh, Denyen and Weshesh.", 2: "Ugarit was destroyed soon after 1192 BCE.", 3: "Ramesses III records defeating them by land and sea, and Egypt survived."}),
  q("Which group of 'Sea Peoples' do scholars identify most firmly with a people of later history?",
    ["The Peleset, known later as the Philistines", "The Sherden, firmly linked to the Sardinians", "The Shekelesh, firmly linked with the Sicilians", "The Lukka, known later as the Philistines"], 0,
    "The Peleset are the Philistines. Links of the Sherden to Sardinia and the Shekelesh to Sicily are guesses.",
    {1: "The link with Sardinia is a guess.", 2: "The link with Sicily is a guess.", 3: "The Philistines are identified with the Peleset, not the Lukka."})]}

P10 = {
 'title': "Why did it collapse?", 'sub': "drought, earthquakes, raiders and a fragile system",
 'lede': "Few questions in ancient history have attracted so many answers. The evidence now points less to one cause than to several shocks hitting an interconnected world at once.",
 'body': [
  "Climate is the strongest new evidence. Pollen cores from the Sea of Galilee and the Dead Sea suggest repeated drought in the southern Levant, [[c-langgut]] and a core from Cyprus a long dry period beginning about 1200. [[c-kaniewski-cyprus]] Critics said such records were too loosely dated, [[c-knapp]] but in 2023 tree rings from Gordion pinned three years of severe drought to about 1198-1196 BCE, just before the Hittite collapse. [[c-gordion-drought]] A 2026 climate model points the same way. [[c-power2026]]",
  "Other factors were in play. Earthquakes may have damaged several cities, [[c-quakes]] and raiders struck the Levantine coast. [[c-invasion]] Inside the kingdoms, revolt, elite rivalry or brittle palace economies may have turned shocks into collapse. [[c-revolt]] Eric Cline argues that these causes interacted, and that the powers' dependence on one another let failure spread. [[c-systems]]",
  "Not everyone collapsed. Egypt survived, though weakened; Assyria recovered and marched to the Mediterranean; [[c-assyria-survives]] Carchemish and Cyprus carried on. In his 2024 sequel Cline asks why some societies adapted while others vanished. [[c-resilience]]",
  {'table': {'head': ["Explanation", "Main evidence", "Main objection"], 'rows': [
    ["drought", "pollen cores; Gordion tree rings", "timing in some records is loose"],
    ["earthquakes", "damaged walls and buildings", "hard to prove; cities recover from quakes"],
    ["invasion and raids", "Medinet Habu; Ugarit letters", "no evidence of raiders in the Aegean"],
    ["internal revolt", "fragile palace economies", "hard to test"],
    ["systems collapse", "everything above, interacting", "can explain almost anything"]], 'note': "[[c-langgut]] [[c-quakes]] [[c-invasion]] [[c-revolt]] [[c-systems]]"}},
  {'compare': "Compare the debate over the end of the Indus cities (5.3): there too, drought is now the leading suspect, but rarely the only one."}],
 'figure': {'kind': 'chart', 'chart': 'ranges', 'caption': "Evidence for drought and disaster", 'title': "Proposed windows, BCE",
  'max': 1300, 'min': 850, 'unit': 'ka', 'ticks': [1300, 1200, 1100, 1000, 900], 'tickLabels': ['1300 BCE', '1200', '1100', '1000', '900'],
  'axis': "years BCE", 'hint': "Hover or click a row",
  'rows': [
   {'t': 'Earthquake storm', 'sub': 'Nur and Cline', 'from': 1225, 'to': 1175, 'lab': 'c. 1225-1175', 'open': True, 'plate': {'kicker': '6.10 · causes', 'title': 'An earthquake storm?', 'sub': 'c. 1225 to 1175 BCE', 'text': "[[c-quakes]] [[c-knapp]]", 'sources': ['nur-cline2000', 'knapp-manning2016']}},
   {'t': 'Levant droughts', 'sub': 'pollen, Galilee and Dead Sea', 'from': 1250, 'to': 1100, 'lab': 'c. 1250-1100', 'open': True, 'plate': {'kicker': '6.10 · causes', 'title': 'Drought in the Levant', 'sub': 'pollen cores', 'text': "[[c-langgut]]", 'sources': ['tau-langgut']}},
   {'t': 'Cyprus dry period', 'sub': 'pollen, Larnaca salt lake', 'from': 1200, 'to': 850, 'lab': 'from c. 1200', 'open': True, 'plate': {'kicker': '6.10 · causes', 'title': 'A long dry period in Cyprus?', 'sub': 'from c. 1200 BCE', 'text': "[[c-kaniewski-cyprus]]", 'sources': ['kaniewski2013']}},
   {'t': 'Severe drought', 'sub': 'Gordion tree rings', 'from': 1199, 'to': 1195, 'lab': 'c. 1198-1196', 'acc': True, 'plate': {'kicker': '6.10 · causes', 'title': 'Three dry years', 'sub': 'c. 1198 to 1196 BCE', 'text': "[[c-gordion-drought]]", 'sources': ['manning2023']}},
   {'t': 'Ugarit destroyed', 'from': 1193, 'to': 1185, 'lab': 'soon after 1192', 'acc': True},
   {'t': 'Ramesses III fights the Sea Peoples', 'from': 1179, 'to': 1175, 'lab': 'c. 1177', 'acc': True}]},
 'practice': [
  q("Why did the 2023 Gordion tree-ring study strengthen the drought argument more than earlier pollen cores?",
    ["Tree rings date the drought to within a few years", "It showed drought caused each one of the destructions", "Its samples covered the whole eastern Mediterranean", "It showed the Sea Peoples played no part in the collapse"], 0,
    "The main objection to the climate case was loose dating. The Gordion rings pin three years of severe drought to about 1198-1196 BCE.",
    {1: "The authors present the drought as a possible tipping point, not the only cause.", 2: "It comes from a single site, Gordion.", 3: "It addresses climate only; the Egyptian records of the Sea Peoples still stand."}),
  q("Which statement best reflects Eric Cline's 2024 argument?",
    ["Some societies vanished while others adapted and rebuilt", "Little changed after 1177 BCE; the collapse was largely a myth", "Earthquakes, more than drought, ended the Bronze Age", "The Phoenicians and Philistines vanished; Egypt adapted"], 0,
    "His sequel asks why outcomes differed: the Phoenicians, Philistines, Israelites and Assyria adapted and built something new, while others vanished.",
    {1: "He describes societies that vanished as well as those that adapted.", 2: "Nur and Cline presented earthquakes as one factor among several.", 3: "Cline names the Phoenicians and Philistines among those that adapted and built something new."})]}

P11 = {
 'title': "After the collapse", 'sub': "iron, Philistines, Phoenicians and the first Israel",
 'lede': "Out of the ruins of the Bronze Age came a new world of smaller states: Philistine cities on the coast, Phoenician merchants in the north, Neo-Hittite kingdoms in Syria, and in the hills of Canaan a new people whom an Egyptian king had already called Israel.",
 'body': [
  "Iron objects became more common from the 12th century BCE, first in Cyprus and the Levant, [[c-iron]] though the old idea that a shortage of tin forced the change finds little support. [[c-iron-shortage]] The Peleset of Medinet Habu settled the southern coast as the Philistines, in five cities. [[c-philistines]] DNA from Ashkelon shows newcomers with European-related ancestry who soon mixed with locals; [[c-philistine-dna]] the Bible remembers them as coming from Caphtor. [[c-caphtor]] To the north, the Phoenician cities grew rich on trade, [[c-phoenicians]] and spread the alphabet that the Greeks would adopt. [[c-phoen-alphabet]] Neo-Hittite kingdoms kept Hittite traditions alive in Syria. [[c-neohittite]]",
  "In the hill country, about 250 small villages appeared from about 1200 BCE. [[c-highlands]] They were unfortified, simple, and nearly free of pig bones. [[c-no-pigs]] Most archaeologists connect them with the Israel named on the Merneptah Stele (4.9), but disagree about who the settlers were: mostly local pastoralists settling down, a group deliberately marking itself off from its neighbours, or a mixed confederation. [[c-highland-origins]]",
  "Chapter 7 takes up the story in the Iron Age, as Assyria rises again and the kingdoms of Israel and Judah take shape.",
  {'table': {'head': ["New player", "Where", "Known for"], 'rows': [
    ["Philistines", "southern coast of Canaan", "five cities; Aegean-style pottery"],
    ["Phoenicians", "Tyre, Sidon, Byblos", "trade, the alphabet"],
    ["Neo-Hittites", "northern Syria, south-east Anatolia", "Hittite traditions"],
    ["Highland villagers", "hill country of Canaan", "early Israel"]], 'note': "[[c-philistines]] [[c-phoenicians]] [[c-neohittite]] [[c-highland-origins]]"}},
  {'compare': "Compare the Bible's books of Joshua and Judges, which tell of conquest and of tribes living among Canaanites and Philistines. The archaeology of the highland villages shows no sign of a violent invasion; it fits better with gradual settlement."}],
 'figure': {'kind': 'map', 'view': {'lon': 36.4, 'lat': 34.6, 'zoom': 34}, 'caption': "The Levant in the early Iron Age, c. 1150-1000 BCE", 'hint': "Click a place",
  'legend': [['pt', 'city'], ['zone', 'region of new settlement']], 'seas': False,
  'layers': [
   {'type': 'zone', 'items': [
    {'ll': [35.25, 32.0], 'r': 0.45, 'label': 'HIGHLAND VILLAGES', 'lab': [37.2, 31.75]},
    {'ll': [34.6, 31.6], 'r': 0.3, 'label': 'PHILISTIA', 'lab': [33.6, 31.2]}]},
   {'type': 'region', 'items': [{'ll': [35.75, 33.6], 'label': 'PHOENICIA', 'size': 9}, {'ll': [37.6, 37.4], 'label': 'NEO-HITTITE STATES', 'size': 9}]},
   {'type': 'points', 'items': [
    {'ll': [34.5458, 31.6639], 'label': 'Ashkelon', 'date': 'Philistine DNA', 'anchor': 'end', 'plate': {'kicker': '6.11 · after the collapse', 'title': 'The Philistines', 'sub': 'from the 12th century BCE', 'text': "[[c-philistines]] [[c-philistine-dna]] [[c-caphtor]]", 'sources': ['brit-philistines', 'mpg-ashkelon']}},
    {'ll': [35.6519, 34.1236], 'label': 'Byblos', 'date': 'Phoenician city', 'anchor': 'end', 'plate': {'kicker': '6.11 · after the collapse', 'title': 'The Phoenicians', 'sub': 'from c. 1200 BCE', 'text': "[[c-phoenicians]] [[c-phoen-alphabet]]", 'sources': ['met-phoenicians', 'brit-phoen-alphabet']}},
    {'ll': [38.0164, 36.8294], 'label': 'Carchemish', 'acc': True, 'plate': {'kicker': '6.11 · after the collapse', 'title': 'The Neo-Hittite states', 'sub': 'c. 1180 to 700 BCE', 'text': "[[c-neohittite]] [[c-carchemish]]", 'sources': ['brit-neohittite', 'demartino2018']}},
    {'ll': [38.3611, 38.3819], 'label': 'Arslantepe (Milid)', 'acc': True},
    {'ll': [35.25, 32.0], 'label': 'hill country', 'plate': {'kicker': '6.11 · after the collapse', 'title': 'The highland villages', 'sub': 'c. 1200 to 1000 BCE', 'text': "[[c-highlands]] [[c-no-pigs]] [[c-highland-origins]]", 'sources': ['finkelstein2001', 'dever-on-faust', 'america-dever']}}]}]},
 'practice': [
  q("What does the DNA study from Ashkelon show?",
    ["Newcomers with European-related ancestry arrived and mixed in", "The Philistines came from Crete, as the Bible says of Caphtor", "The newcomers kept their ancestry distinct for centuries", "Hundreds of people were sampled across the Philistine cities"], 0,
    "Newcomers with European-related ancestry appear at the start of the Iron Age and mixed with the local population within two centuries.",
    {1: "A southern European source is plausible but not confirmed, and no find confirms Crete.", 2: "Within two centuries they had mixed with the local population.", 3: "The study sampled ten individuals."}),
  q("Why do archaeologists pay so much attention to the absence of pig bones in the highland villages?",
    ["It may mark a group identity, though scholars read it differently", "Faust sees herders settling down; Finkelstein, an identity marker", "It suggests the villages were wealthy towns with strong walls", "It shows the settlers were too poor to keep animals of any kind"], 0,
    "Finkelstein, Faust and Dever all connect the villages with early Israel, but disagree about who the settlers were.",
    {1: "It is the other way round: Finkelstein sees mainly local pastoralists settling down, and Faust a group marking its identity.", 2: "The villages were small and unfortified.", 3: "Animal bones are found there; what is almost missing is pig."})]}

PAGES = [P8, P9, P10, P11]
